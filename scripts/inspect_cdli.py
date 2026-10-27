#!/usr/bin/env python3
"""Inspect CDLI ATF + catalogue; write a Markdown report (no corpus build)."""

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

KEY_SUBSTR = ("object", "genre", "language", "period", "provenience", "material", "id_")


def key_columns(fieldnames):
    return [c for c in fieldnames if any(s in c.lower() for s in KEY_SUBSTR)]


def p_candidates_from_id(raw: str) -> list[tuple[str, str]]:
    """Return (p_number, convention) pairs to try against ATF keys."""
    v = (raw or "").strip()
    out: list[tuple[str, str]] = []
    if not v:
        return out
    # as-is (with P prefix if missing)
    as_is = v if v.upper().startswith("P") else f"P{v}"
    out.append((as_is, "as-is"))
    # zero-padded to 6 digits with a P prefix
    digits = v[1:] if v.upper().startswith("P") else v
    if digits.isdigit():
        padded = f"P{int(digits):06d}"
        if padded != as_is:
            out.append((padded, "zero-padded-6"))
    return out


def index_atf(atf_path: Path):
    """Map P-number → (start_line_idx, lines) for each &P block (0-based)."""
    blocks: dict[str, list[str]] = {}
    order: list[str] = []
    current: str | None = None
    buf: list[str] = []
    n_lines = 0
    n_p = 0
    with atf_path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            n_lines += 1
            if line.startswith("&P"):
                n_p += 1
                if current is not None:
                    blocks[current] = buf
                pnum = line[1:].split()[0]
                current = pnum
                order.append(pnum)
                buf = [line.rstrip("\n")]
            elif current is not None:
                buf.append(line.rstrip("\n"))
        if current is not None:
            blocks[current] = buf
    return blocks, n_lines, n_p


def is_seal_candidate(row, cols) -> bool:
    for c in cols:
        val = (row.get(c) or "").lower()
        if "seal" in val or "bulla" in val:
            return True
    return False


def match_atf(row_id: str, blocks: dict) -> tuple[str | None, str | None]:
    """Return (matched_pnum, convention) or (None, None)."""
    seen = set()
    for pnum, conv in p_candidates_from_id(row_id):
        if pnum in seen:
            continue
        seen.add(pnum)
        if pnum in blocks:
            return pnum, conv
    return None, None


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit(
            "usage: .venv/bin/python -I scripts/inspect_cdli.py "
            "raw/cdli/data docs/data_notes/cdli_inspection.md"
        )
    data_dir = Path(argv[1])
    out_path = Path(argv[2])
    atf_path = data_dir / "cdliatf_unblocked.atf"
    cat_path = data_dir / "cdli_cat.csv"

    csv.field_size_limit(sys.maxsize)

    atf_size = atf_path.stat().st_size
    cat_size = cat_path.stat().st_size

    print("indexing ATF…", flush=True)
    blocks, atf_lines, n_p = index_atf(atf_path)

    print("reading ATF sample…", flush=True)
    with atf_path.open(encoding="utf-8", errors="replace") as f:
        atf_sample = [next(f).rstrip("\n") for _ in range(60)]

    print("scanning catalogue…", flush=True)
    with cat_path.open(encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        kcols = key_columns(fieldnames)
        value_counters = {c: Counter() for c in kcols}
        seal_by_col_val: Counter = Counter()
        seal_rows: list[dict] = []
        n_data = 0
        for row in reader:
            n_data += 1
            for c in kcols:
                value_counters[c][(row.get(c) or "")] += 1
            if is_seal_candidate(row, kcols):
                seal_rows.append(row)
                for c in kcols:
                    val = row.get(c) or ""
                    low = val.lower()
                    if "seal" in low or "bulla" in low:
                        seal_by_col_val[(c, val)] += 1

    cat_lines = n_data + 1  # header + data

    print(f"seal candidates: {len(seal_rows)}", flush=True)

    # Seal examples: first 8 with ATF match
    examples = []
    conventions_used = Counter()
    unmatched = 0
    for row in seal_rows:
        pnum, conv = match_atf(row.get("id", ""), blocks)
        if pnum is None:
            unmatched += 1
            continue
        conventions_used[conv] += 1
        if len(examples) < 8:
            examples.append((row, pnum, conv))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    w = lines.append

    w("# CDLI inspection")
    w("")
    w("## Header")
    w("")
    w(
        "Source: Cuneiform Digital Library Initiative (CDLI), "
        "github.com/cdli-gh/data at commit d66b12b, licence CC BY-NC-SA. "
        "Short excerpts reproduced for research documentation."
    )
    w("")
    w("## Files")
    w("")
    w(f"- `cdliatf_unblocked.atf`: {atf_size} bytes, {atf_lines} lines; "
      f"{n_p} lines starting with `&P`.")
    w(f"- `cdli_cat.csv`: {cat_size} bytes, {cat_lines} lines "
      f"({n_data} data rows + 1 header).")
    w("")
    w("## ATF sample")
    w("")
    w("First 60 lines of `cdliatf_unblocked.atf`:")
    w("")
    w("```")
    for line in atf_sample:
        w(line)
    w("```")
    w("")
    w("## Catalogue overview")
    w("")
    w(f"Data rows: {n_data}")
    w("")
    w("Columns (in order):")
    w("")
    for i, name in enumerate(fieldnames, start=1):
        w(f"{i}. `{name}`")
    w("")
    w("## Key columns")
    w("")
    w(
        "Columns whose lowercased name contains any of "
        "`object`, `genre`, `language`, `period`, `provenience`, "
        "`material`, `id_`:"
    )
    w("")
    for c in kcols:
        w(f"### `{c}`")
        w("")
        w("```")
        for val, cnt in value_counters[c].most_common(40):
            shown = repr(val) if val == "" else val
            w(f"{cnt}\t{shown}")
        w("```")
        w("")
    w("## Seal candidates")
    w("")
    w(
        f"Catalogue rows where any Key column value contains "
        f"`seal` or `bulla` (case-insensitive): **{len(seal_rows)}**"
    )
    w("")
    w("Breakdown by (column, value), sorted by count:")
    w("")
    w("```")
    for (col, val), cnt in sorted(
        seal_by_col_val.items(), key=lambda x: (-x[1], x[0][0], x[0][1])
    ):
        w(f"{cnt}\t{col}\t{val}")
    w("```")
    w("")
    w("## Seal examples")
    w("")
    w(
        "First 8 seal-candidate rows that also have a matching `&P` entry "
        "in the ATF. Matching tried on catalogue `id` as-is (with `P` "
        "prefix if missing) and zero-padded to 6 digits with a `P` prefix."
    )
    w("")
    w(f"Convention counts among matched seal candidates: {dict(conventions_used)}")
    w("")
    for i, (row, pnum, conv) in enumerate(examples, start=1):
        w(f"### Example {i}: catalogue id=`{row.get('id','')}` → ATF `{pnum}` "
          f"(matched via **{conv}**)")
        w("")
        w("Key columns:")
        w("")
        w("```")
        for c in kcols:
            w(f"{c}: {row.get(c, '')}")
        w("```")
        w("")
        block = blocks[pnum][:40]
        w("ATF block (max 40 lines):")
        w("")
        w("```")
        for line in block:
            w(line)
        w("```")
        w("")
    w("## Unmatched")
    w("")
    w(
        f"Of {len(seal_rows)} seal-candidate rows, "
        f"**{unmatched}** have no matching ATF entry "
        f"(no transliteration available under catalogue `id`)."
    )
    w("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out_path}", flush=True)
    print(f"seal candidates total: {len(seal_rows)}", flush=True)
    print(f"unmatched: {unmatched}", flush=True)


if __name__ == "__main__":
    main(sys.argv)
