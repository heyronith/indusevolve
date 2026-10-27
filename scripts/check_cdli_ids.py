#!/usr/bin/env python3
"""Compare catalogue id vs id_text against ATF P-number → designation."""

import csv
import random
import re
import sys
from pathlib import Path

HEADER_RE = re.compile(r"^&P(\d+)\s*=\s*(.*)$")


def norm(s: str) -> str:
    return " ".join((s or "").casefold().split())


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
        equal = norm(cat_des) == norm(atf_des)
        matched.append(
            {
                "id": row.get("id", ""),
                "id_text": row.get("id_text", ""),
                "p": p,
                "catalogue": cat_des,
                "atf": atf_des,
                "equal": equal,
            }
        )
    agree = sum(1 for m in matched if m["equal"])
    share = (agree / len(matched)) if matched else 0.0
    return matched, agree, share


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
        matched, agree, share = evaluate(sample, atf_map, col)
        results[col] = (matched, agree, share)
        print(
            f"{col}: matched={len(matched)} agree={agree} share={share:.4f}",
            flush=True,
        )

    # Prefer id_text if both qualify.
    winner = None
    for col in ("id_text", "id"):
        matched, agree, share = results[col]
        if len(matched) >= 100 and share >= 0.95:
            winner = col
            break

    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    w = lines.append
    w("# CDLI ID convention check")
    w("")
    w(f"ATF P-number headers indexed: {len(atf_map)}")
    w(f"Sample size: {len(sample)} (seed 0, non-empty designation)")
    w("")
    for col in ("id_text", "id"):
        matched, agree, share = results[col]
        w(f"## Convention `{col}`")
        w("")
        w(f"- Matched (candidate P in ATF): **{len(matched)}**")
        w(f"- Designation agreement: **{agree}/{len(matched)}** "
          f"({share:.4f})")
        w("")
        w("10 example rows:")
        w("")
        w("| catalogue designation | ATF designation | equal? |")
        w("| --- | --- | --- |")
        for m in matched[:10]:
            cat = m["catalogue"].replace("|", "\\|")
            atf = m["atf"].replace("|", "\\|")
            w(f"| {cat} | {atf} | {m['equal']} |")
        w("")

    if winner:
        w(f"## Decision")
        w("")
        w(f"**Winning convention: `{winner}`** "
          f"(agreement ≥ 0.95 on ≥ 100 matched rows).")
        w("")
        print(f"ID CONVENTION: {winner}", flush=True)
    else:
        w("## Decision")
        w("")
        w("Neither convention reached agreement ≥ 0.95 on ≥ 100 matched rows. "
          "STOP after Part A.")
        w("")
        print("ID CONVENTION: none (stop after Part A)", flush=True)
        for col in ("id_text", "id"):
            _, _, share = results[col]
            print(f"  {col} agreement share: {share:.4f}", flush=True)

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out_path}", flush=True)

    if winner is None:
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv)
