#!/usr/bin/env python3
"""Build Indus pilot corpora, check reading order, write stats."""

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from indusevolve.loaders import cisi_mayig, indus_website
from indusevolve.schema import write_jsonl
from indusevolve.stats import describe


def order_check(records, label: str) -> None:
    counts = Counter()
    for r in records:
        counts.update(r.signs)
    if not counts:
        raise SystemExit(f"order check failed for {label}: empty corpus")
    top_sign, _ = counts.most_common(1)[0]
    initial = 0
    final = 0
    for r in records:
        if len(r.signs) < 2:
            continue
        if r.signs[0] == top_sign:
            initial += 1
        if r.signs[-1] == top_sign:
            final += 1
    threshold = 5 * max(1, initial)
    ok = final > threshold
    print(
        f"order check {label}: top={top_sign} final={final} initial={initial} "
        f"threshold={threshold} {'PASS' if ok else 'FAIL'}"
    )
    if not ok:
        raise SystemExit(f"order check failed for {label}")


def main(argv: list[str]) -> None:
    if len(argv) != 4:
        raise SystemExit(
            "usage: .venv/bin/python -I scripts/build_indus.py "
            "raw/indus data/processed data/restricted"
        )
    raw_indus = Path(argv[1])
    processed = Path(argv[2])
    restricted = Path(argv[3])
    processed.mkdir(parents=True, exist_ok=True)
    restricted.mkdir(parents=True, exist_ok=True)

    sql_path = raw_indus / "indus-website" / "population-script.sql"
    iw_db = indus_website.parse(sql_path)
    iw_records = indus_website.to_records(iw_db)
    order_check(iw_records, "indus-website")

    mayig_dir = raw_indus / "cisi-mayig" / "corpus"
    mayig_records = cisi_mayig.load_dir(mayig_dir)
    order_check(mayig_records, "cisi-mayig")

    write_jsonl(iw_records, restricted / "indus_website.jsonl")
    write_jsonl(mayig_records, processed / "indus_cisi_mayig.jsonl")

    stats = {
        "indus-website": describe(iw_records),
        "cisi-mayig": describe(mayig_records),
    }
    (processed / "stats_indus.json").write_text(
        json.dumps(stats, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(iw_records)} indus-website → {restricted / 'indus_website.jsonl'}")
    print(f"wrote {len(mayig_records)} cisi-mayig → {processed / 'indus_cisi_mayig.jsonl'}")
    print(f"wrote stats → {processed / 'stats_indus.json'}")


if __name__ == "__main__":
    main(sys.argv)
