"""Loader for the indus-website MySQL dump (population-script.sql)."""

import re
from collections import defaultdict
from pathlib import Path

from indusevolve.schema import Inscription

_INSERT_RE = re.compile(
    r"INSERT INTO\s+(\w+)\s*\(([^)]+)\)\s*VALUES\s*",
    re.IGNORECASE,
)


def _tuples(body: str) -> list[list[str]]:
    """Parse a MySQL VALUES body `(...),(...)` into rows of string fields."""
    rows: list[list[str]] = []
    row: list[str] = []
    i = 0
    n = len(body)
    in_row = False
    field_chars: list[str] = []
    quote: str | None = None
    escape = False

    def flush_field() -> None:
        nonlocal field_chars
        value = "".join(field_chars).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        row.append(value)
        field_chars = []

    while i < n:
        ch = body[i]
        if not in_row:
            if ch == "(":
                in_row = True
                row = []
                field_chars = []
                quote = None
                escape = False
            i += 1
            continue

        if quote is not None:
            if escape:
                field_chars.append(ch)
                escape = False
            elif ch == "\\":
                field_chars.append(ch)
                escape = True
            elif ch == quote:
                field_chars.append(ch)
                quote = None
            else:
                field_chars.append(ch)
            i += 1
            continue

        if ch in "'\"":
            field_chars.append(ch)
            quote = ch
            i += 1
            continue

        if ch == ",":
            flush_field()
            i += 1
            continue

        if ch == ")":
            flush_field()
            rows.append(row)
            in_row = False
            i += 1
            continue

        field_chars.append(ch)
        i += 1

    return rows


def _extract_insert_body(sql: str, table: str) -> str:
    for match in _INSERT_RE.finditer(sql):
        if match.group(1).upper() != table.upper():
            continue
        start = match.end()
        # Find the terminating semicolon that ends this INSERT, respecting quotes.
        i = start
        n = len(sql)
        quote: str | None = None
        escape = False
        while i < n:
            ch = sql[i]
            if quote is not None:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == quote:
                    quote = None
            else:
                if ch in "'\"":
                    quote = ch
                elif ch == ";":
                    return sql[start:i]
            i += 1
        raise ValueError(f"unterminated INSERT for {table}")
    raise ValueError(f"INSERT INTO {table} not found")


def parse(sql_path) -> dict:
    sql = Path(sql_path).read_text(encoding="utf-8", errors="replace")
    db: dict = {}

    site_rows = _tuples(_extract_insert_body(sql, "SITE"))
    db["SITE"] = {r[0]: r[1] for r in site_rows}

    glyph_rows = _tuples(_extract_insert_body(sql, "GLYPH"))
    db["GLYPH"] = {r[0]: r[1] for r in glyph_rows}

    seal_cols = ["SEALID", "SITEID", "MATERIAL", "CISI", "MUSEUM", "WIDTH", "HEIGHT", "THICKNESS"]
    seal_rows = _tuples(_extract_insert_body(sql, "SEAL"))
    db["SEAL"] = {r[0]: dict(zip(seal_cols, r)) for r in seal_rows}

    insc_cols = ["SEALID", "ISCOMPLETE", "DIRECTION"]
    insc_rows = _tuples(_extract_insert_body(sql, "INSCRIPTION"))
    db["INSCRIPTION"] = {r[0]: dict(zip(insc_cols, r)) for r in insc_rows}

    icon_rows = _tuples(_extract_insert_body(sql, "ICONOGRAPHY"))
    db["ICONOGRAPHY"] = {r[0]: r[1] for r in icon_rows}

    seq_rows = _tuples(_extract_insert_body(sql, "GLYPHSEQUENCE"))
    by_seal: dict[str, list[tuple[int, str]]] = defaultdict(list)
    for sealid, glyphid, idx in seq_rows:
        by_seal[sealid].append((int(idx), glyphid))
    db["GLYPHSEQUENCE"] = {
        sealid: [g for _, g in sorted(items, key=lambda t: t[0])]
        for sealid, items in by_seal.items()
    }
    return db


def _is_null_or_empty(value: str | None) -> bool:
    if value is None:
        return True
    v = value.strip()
    return v == "" or v.upper() == "NULL"


def to_records(db: dict) -> list[Inscription]:
    sites = db["SITE"]
    seals = db["SEAL"]
    inscriptions = db.get("INSCRIPTION", {})
    iconography = db.get("ICONOGRAPHY", {})
    sequences = db["GLYPHSEQUENCE"]

    records: list[Inscription] = []
    for sealid, glyphs in sequences.items():
        signs_stored = [g for g in glyphs if g != "0"]
        if not signs_stored:
            continue
        # Dump stores reverse reading order; reverse to reading order.
        signs = [f"IW:{g}" for g in reversed(signs_stored)]
        # Split on line-break marker "0"; n_lines = non-empty segments.
        segments: list[list[str]] = [[]]
        for g in glyphs:
            if g == "0":
                segments.append([])
            else:
                segments[-1].append(g)
        n_lines = sum(1 for seg in segments if seg)

        seal = seals.get(sealid, {})
        siteid = seal.get("SITEID", "")
        site_name = sites.get(siteid, siteid)

        material = seal.get("MATERIAL", "")
        if _is_null_or_empty(material):
            material = ""

        cisi = seal.get("CISI", "")
        if _is_null_or_empty(cisi):
            cisi = ""

        insc = inscriptions.get(sealid, {})
        iscomplete = insc.get("ISCOMPLETE", "")
        if iscomplete == "Y":
            complete: bool | None = True
        elif iscomplete == "N":
            complete = False
        else:
            complete = None

        stored_direction = insc.get("DIRECTION", "")
        if _is_null_or_empty(stored_direction):
            stored_direction = ""

        motif = iconography.get(sealid, "")
        if _is_null_or_empty(motif):
            motif = ""

        records.append(
            Inscription(
                system="indus",
                id=f"IW-{sealid}",
                signs=signs,
                label="unlabelled",
                genre="unknown",
                direction="unknown",
                object_type=material,
                site=site_name,
                complete=complete,
                source="indus-website",
                source_id=cisi,
                meta={
                    "material": material,
                    "motif": motif,
                    "stored_direction": stored_direction,
                    "n_lines": n_lines,
                },
            )
        )
    return records
