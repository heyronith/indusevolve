"""Loader for the CISI-mayig JSON corpus."""

import json
from pathlib import Path

from indusevolve.schema import Inscription


def load_dir(corpus_dir) -> list[Inscription]:
    root = Path(corpus_dir)
    records: list[Inscription] = []
    for path in sorted(root.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue
        for side in data:
            graphemes = side.get("graphemes") or []
            if not graphemes:
                continue
            # Recorded L→R as seen on sealing; script reads R→L → reverse.
            signs = [f"P:{g['id']}" for g in reversed(graphemes)]
            side_id = side["id"]
            description = side.get("description") or ""
            genre = "seal" if "seal" in description.lower() else "unknown"
            records.append(
                Inscription(
                    system="indus",
                    id=f"CISI-{side_id}",
                    signs=signs,
                    label="unlabelled",
                    genre=genre,
                    direction="rtl",
                    object_type=description,
                    site="Mohenjo-daro",
                    source="cisi-mayig",
                    source_id=side_id,
                )
            )
    return records
