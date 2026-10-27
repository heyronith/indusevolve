from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Iterator

LABELS = {"language", "non-language", "unlabelled"}
DIRECTIONS = {"rtl", "ltr", "boustrophedon", "vertical", "unknown"}
GENRES = {
    "seal",
    "sealing",
    "tablet",
    "label",
    "docket",
    "graffito",
    "bulla",
    "coin",
    "inscription",
    "literary",
    "emblem",
    "mark",
    "other",
    "unknown",
}
SIGN_TOKEN = re.compile(r"^[A-Z]{1,4}:\S+$")


@dataclass
class Inscription:
    """Signs are always stored in READING ORDER; `direction` records how the original was physically written."""

    system: str
    id: str
    signs: list[str]
    label: str
    genre: str = "unknown"
    direction: str = "unknown"
    object_type: str = ""
    site: str = ""
    complete: bool | None = None
    source: str = ""
    source_id: str = ""
    meta: dict = field(default_factory=dict)

    def validate(self) -> list[str]:
        errors: list[str] = []
        if not self.system:
            errors.append("system must be non-empty")
        if not self.id:
            errors.append("id must be non-empty")
        if not self.signs:
            errors.append("signs must be a non-empty list")
        else:
            for i, sign in enumerate(self.signs):
                if not isinstance(sign, str) or not SIGN_TOKEN.match(sign):
                    errors.append(f"signs[{i}] does not match SIGN_TOKEN: {sign!r}")
        if self.label not in LABELS:
            errors.append(f"label must be one of {sorted(LABELS)}; got {self.label!r}")
        if self.direction not in DIRECTIONS:
            errors.append(
                f"direction must be one of {sorted(DIRECTIONS)}; got {self.direction!r}"
            )
        if self.genre not in GENRES:
            errors.append(f"genre must be one of {sorted(GENRES)}; got {self.genre!r}")
        return errors


def write_jsonl(records: Iterable[Inscription], path) -> int:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    seen: set[tuple[str, str]] = set()
    lines: list[str] = []
    for record in records:
        errors = record.validate()
        if errors:
            raise ValueError(
                f"invalid record {record.system}/{record.id}: {'; '.join(errors)}"
            )
        key = (record.system, record.id)
        if key in seen:
            raise ValueError(f"duplicate (system, id): {record.system}/{record.id}")
        seen.add(key)
        lines.append(json.dumps(asdict(record), ensure_ascii=False))

    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return len(lines)


def read_jsonl(path) -> Iterator[Inscription]:
    path = Path(path)
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            yield Inscription(**data)
