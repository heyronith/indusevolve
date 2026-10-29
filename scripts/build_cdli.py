#!/usr/bin/env python3
"""Build the CDLI cuneiform seal-legend corpus."""

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from indusevolve.loaders.cdli import (
    build_records,
    load_catalogue,
    mark_duplicates,
    uniquify_ids,
)
from indusevolve.schema import write_jsonl
from indusevolve.stats import describe

ID_COLUMN = "id_text"


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit(
            "usage: .venv/bin/python -I scripts/build_cdli.py "
            "raw/cdli/data data/processed"
        )
    data_dir = Path(argv[1])
    out_dir = Path(argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"loading catalogue (id column={ID_COLUMN})…", flush=True)
    catalogue = load_catalogue(data_dir / "cdli_cat.csv", ID_COLUMN)
    print(f"catalogue entries: {len(catalogue)}", flush=True)

    print("building records from ATF…", flush=True)
    records, exclusions, unparsed = build_records(
        data_dir / "cdliatf_unblocked.atf", catalogue
    )
    records = uniquify_ids(records)
    records = mark_duplicates(records)

    n_dup = sum(1 for r in records if "duplicate_of" in r.meta)
    kind_counts = Counter(r.meta.get("kind") for r in records)
    genre_counts = Counter(r.genre for r in records)
    period_counts = Counter(r.meta.get("period", "") for r in records)
    language_counts = Counter(r.meta.get("language", "") for r in records)

    match_flags = [bool(r.meta.get("designation_match")) for r in records]
    overall_match = (sum(match_flags) / len(match_flags)) if match_flags else 0.0
    by_kind_match = {}
    for kind in ("A", "B"):
        subset = [r for r in records if r.meta.get("kind") == kind]
        if subset:
            by_kind_match[kind] = sum(
                1 for r in subset if r.meta.get("designation_match")
            ) / len(subset)
        else:
            by_kind_match[kind] = 0.0

    kind_a_mismatches = [
        {"id": r.id, "source_id": r.source_id, "designation": r.meta.get("designation")}
        for r in records
        if r.meta.get("kind") == "A" and not r.meta.get("designation_match")
    ][:30]

    clean = [
        r
        for r in records
        if r.complete
        and "duplicate_of" not in r.meta
        and len(r.signs) >= 2
    ]

    jsonl_path = out_dir / "cuneiform_seals.jsonl"
    n_written = write_jsonl(records, jsonl_path)

    stats = {
        "id_column": ID_COLUMN,
        "all": describe(records),
        "clean": describe(clean),
        "exclusions": exclusions,
        "unparsed_lines": unparsed,
        "counts_by_kind": dict(kind_counts),
        "counts_by_genre": dict(genre_counts),
        "period_top15": period_counts.most_common(15),
        "language_top10": language_counts.most_common(10),
        "duplicates": n_dup,
        "designation_match": {
            "overall": round(overall_match, 4),
            "by_kind": {k: round(v, 4) for k, v in by_kind_match.items()},
            "kind_a_mismatch_examples": kind_a_mismatches,
        },
    }
    stats_path = out_dir / "stats_cuneiform_seals.json"
    stats_path.write_text(
        json.dumps(stats, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(f"wrote {n_written} records → {jsonl_path}", flush=True)
    print(f"wrote stats → {stats_path}", flush=True)
    print(f"kind A: {kind_counts.get('A', 0)}  kind B: {kind_counts.get('B', 0)}")
    print(f"duplicates: {n_dup}")
    print(f"clean subset (complete, non-dup, len≥2): {len(clean)}")
    print(f"exclusions: {dict(exclusions)}")
    print(f"unparsed_lines: {unparsed}")
    print(
        f"designation_match overall={overall_match:.4f} "
        f"A={by_kind_match.get('A', 0):.4f} B={by_kind_match.get('B', 0):.4f}"
    )
    print(f"kind-A mismatch examples listed: {len(kind_a_mismatches)}")

    if overall_match < 0.80:
        print(
            "STOP: designation_match overall share "
            f"{overall_match:.4f} is below 0.80",
            flush=True,
        )
        sys.exit(3)


if __name__ == "__main__":
    main(sys.argv)
