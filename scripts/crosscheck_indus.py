#!/usr/bin/env python3
"""Cross-check CISI-mayig against indus-website by CISI number and jar sign."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from indusevolve.schema import Inscription, read_jsonl

CISI_RE = re.compile(r"^\s*([A-Za-z]+)\s*-?\s*0*(\d+)\s*([A-Za-z]?)")


def normalise_cisi(value: str):
    if not value:
        return None
    m = CISI_RE.match(value)
    if not m:
        return None
    prefix, num, suffix = m.group(1), m.group(2), m.group(3)
    return f"{prefix.upper()}-{int(num)}{suffix.upper()}"


def jar_positions(signs, jar: str):
    return [i for i, s in enumerate(signs) if s == jar]


def strip_side_letter(norm: str) -> str:
    if norm and norm[-1].isalpha() and "-" in norm:
        return norm[:-1]
    return norm


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit(
            "usage: .venv/bin/python -I scripts/crosscheck_indus.py "
            "data/processed data/restricted"
        )
    processed = Path(argv[1])
    restricted = Path(argv[2])

    mayig = list(read_jsonl(processed / "indus_cisi_mayig.jsonl"))
    website = list(read_jsonl(restricted / "indus_website.jsonl"))

    by_cisi: dict[str, Inscription] = {}
    for rec in website:
        norm = normalise_cisi(rec.source_id)
        if norm:
            by_cisi[norm] = rec

    overlaps = 0
    agree = 0
    disagreements = []

    for mrec in mayig:
        norm = normalise_cisi(mrec.source_id)
        if not norm:
            continue
        iw = by_cisi.get(norm)
        if iw is None:
            base = strip_side_letter(norm)
            if base != norm:
                iw = by_cisi.get(base)
        if iw is None:
            continue

        overlaps += 1
        len_m = len(mrec.signs)
        len_iw = len(iw.signs)
        jars_m = jar_positions(mrec.signs, "P:P324")
        jars_iw = jar_positions(iw.signs, "IW:740")
        if len_m == len_iw and jars_m == jars_iw:
            agree += 1
        else:
            disagreements.append(
                {
                    "cisi_id": mrec.id,
                    "iw_id": iw.id,
                    "cisi_source_id": mrec.source_id,
                    "iw_source_id": iw.source_id,
                    "length_cisi": len_m,
                    "length_iw": len_iw,
                    "jar_positions_cisi": jars_m,
                    "jar_positions_iw": jars_iw,
                }
            )

    pct = round(100.0 * agree / overlaps) if overlaps else 0
    # Prefer one-decimal display matching expected "91%"
    pct_display = round(100.0 * agree / overlaps) if overlaps else 0
    print(f"overlapping seals: {overlaps}")
    print(
        f"agreeing on length and jar positions: {agree} "
        f"({pct_display}%)"
    )

    out = {
        "overlapping": overlaps,
        "agreeing": agree,
        "agree_pct": pct_display,
        "disagreements": disagreements,
    }
    out_path = processed / "crosscheck_indus.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main(sys.argv)
