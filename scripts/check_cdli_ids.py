#!/usr/bin/env python3
"""Compare catalogue id vs id_text against ATF P-number → designation."""

import csv
import random
import re
import sys
import unicodedata
from pathlib import Path

HEADER_RE = re.compile(r"^&P(\d+)\s*=\s*(.*)$")
APOSTROPHE_MAP = str.maketrans({
    "\u2019": "'",  # ’
    "\u2018": "'",  # ‘
    "\u02BC": "'",  # ʼ
    "\u00B4": "'",  # ´
    "`": "'",
})


def norm_exact(s: str) -> str:
    """Whitespace-normalised, case-insensitive (original T04 compare)."""
    return " ".join((s or "").casefold().split())


def norm_amended(s: str) -> str:
    """PI amendment normalisation for designation comparison."""
    s = unicodedata.normalize("NFKC", s or "")
    s = s.translate(APOSTROPHE_MAP)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,;:)])", r"\1", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\b0+(\d)", r"\1", s)
    return s.casefold().strip()


def parse_atf_designations(atf_path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    with atf_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            m = HEADER_RE.match(line.rstrip("\n"))
            if not m:
                continue
            pnum = f"P{int(m.group(1)):06d}"
            mapping[pnum] = m.group(2).strip()
    return mapping


def candidate_p(value: str):
    v = (value or "").strip()
    if not v:
        return None
    try:
        return f"P{int(v):06d}"
    except ValueError:
        return None


def evaluate(sample, atf_map, column: str):
    matched = []
    for row in sample:
        p = candidate_p(row.get(column, ""))
        if p is None or p not in atf_map:
            continue
        cat_des = row.get("designation") or ""
        atf_des = atf_map[p]
        matched.append(
            {
                "id": row.get("id", ""),
                "id_text": row.get("id_text", ""),
                "p": p,
                "catalogue": cat_des,
                "atf": atf_des,
                "equal_exact": norm_exact(cat_des) == norm_exact(atf_des),
                "equal_norm": norm_amended(cat_des) == norm_amended(atf_des),
            }
        )
    n = len(matched)
    agree_exact = sum(1 for m in matched if m["equal_exact"])
    agree_norm = sum(1 for m in matched if m["equal_norm"])
    share_exact = (agree_exact / n) if n else 0.0
    share_norm = (agree_norm / n) if n else 0.0
    return matched, agree_exact, share_exact, agree_norm, share_norm


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit(
            "usage: .venv/bin/python -I scripts/check_cdli_ids.py "
            "raw/cdli/data docs/data_notes/cdli_id_check.md"
        )
    data_dir = Path(argv[1])
    out_path = Path(argv[2])
    csv.field_size_limit(sys.maxsize)

    print("parsing ATF designations…", flush=True)
    atf_map = parse_atf_designations(data_dir / "cdliatf_unblocked.atf")
    print(f"ATF P-headers: {len(atf_map)}", flush=True)

    print("reading catalogue…", flush=True)
    with (data_dir / "cdli_cat.csv").open(
        encoding="utf-8", errors="replace", newline=""
    ) as f:
        rows = [
            row
            for row in csv.DictReader(f)
            if (row.get("designation") or "").strip()
        ]
    sample = random.Random(0).sample(rows, min(500, len(rows)))
    print(f"sampled {len(sample)} rows with non-empty designation", flush=True)

    results = {}
    for col in ("id_text", "id"):
        matched, ae, se, an, sn = evaluate(sample, atf_map, col)
        results[col] = (matched, ae, se, an, sn)
        print(
            f"{col}: matched={len(matched)} "
            f"exact={ae}/{len(matched)} ({se:.4f}) "
            f"normalised={an}/{len(matched)} ({sn:.4f})",
            flush=True,
        )

    id_text_matched, _, _, id_text_agree_n, id_text_share_n = results["id_text"]
    id_matched, _, _, id_agree_n, id_share_n = results["id"]

    # Decision: id_text wins if normalised ≥ 0.95 on ≥ 100 matched,
    # AND id stays below 0.05 (normalised).
    winner = None
    if (
        len(id_text_matched) >= 100
        and id_text_share_n >= 0.95
        and id_share_n < 0.05
    ):
        winner = "id_text"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    w = lines.append
    w("# CDLI ID convention check")
    w("")
    w(f"ATF P-number headers indexed: {len(atf_map)}")
    w(f"Sample size: {len(sample)} (seed 0, non-empty designation)")
    w("")
    w("## PI amendment to Part A normalisation")
    w("")
    w(
        "In addition to the original exact compare (whitespace-normalised, "
        "case-insensitive), designations are also compared after: Unicode NFKC; "
        "mapping ’ ‘ ʼ ´ ` to '; collapsing whitespace; removing spaces before "
        "`, ; : )` and after `(`; stripping leading zeros from digit runs "
        r"(`re.sub(r'\b0+(\d)', r'\1', s)`); casefold."
    )
    w("")
    for col in ("id_text", "id"):
        matched, ae, se, an, sn = results[col]
        w(f"## Convention `{col}`")
        w("")
        w(f"- Matched (candidate P in ATF): **{len(matched)}**")
        w(f"- Exact agreement: **{ae}/{len(matched)}** ({se:.4f})")
        w(f"- Normalised agreement: **{an}/{len(matched)}** ({sn:.4f})")
        w("")
        w("10 example rows (exact / normalised):")
        w("")
        w("| catalogue designation | ATF designation | exact? | normalised? |")
        w("| --- | --- | --- | --- |")
        for m in matched[:10]:
            cat = m["catalogue"].replace("|", "\\|")
            atf = m["atf"].replace("|", "\\|")
            w(
                f"| {cat} | {atf} | {m['equal_exact']} | {m['equal_norm']} |"
            )
        w("")

    mismatches = [m for m in id_text_matched if not m["equal_norm"]]
    w("## Remaining `id_text` mismatches after normalisation")
    w("")
    w(f"Count: **{len(mismatches)}**")
    w("")
    w("| catalogue designation | ATF designation |")
    w("| --- | --- |")
    for m in mismatches:
        cat = m["catalogue"].replace("|", "\\|")
        atf = m["atf"].replace("|", "\\|")
        w(f"| {cat} | {atf} |")
    w("")

    w("## Decision")
    w("")
    if winner:
        w(
            f"**Winning convention: `{winner}`** "
            f"(normalised agreement ≥ 0.95 on ≥ 100 matched rows, "
            f"and `id` normalised share < 0.05)."
        )
        w("")
        print(f"ID CONVENTION: {winner}", flush=True)
    else:
        w(
            "Decision rule not met "
            "(need `id_text` normalised ≥ 0.95 on ≥ 100 matched, "
            "and `id` normalised < 0.05). STOP after Part A."
        )
        w("")
        print("ID CONVENTION: none (stop after Part A)", flush=True)

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out_path}", flush=True)
    print(f"id_text remaining mismatches: {len(mismatches)}", flush=True)

    if winner is None:
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv)
