"""CDLI cuneiform seal-legend loader.

Tokens are sign *readings* (prefix ``CU:``), not sign names.
Mapping readings to sign names via OGSL is a later task.
"""

import csv
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

from indusevolve.schema import Inscription

NORM_COLS = ("object_type", "genre", "subgenre", "language", "period")

OBJECT_TYPE_TO_GENRE = {
    "seal (not impression)": "seal",
    "seal": "seal",
    "sealing": "sealing",
    "bulla": "bulla",
    "tag": "label",
    "docket": "docket",
}

HEADER_RE = re.compile(r"^&P(\d+)\s*=\s*(.*)$")
SEAL_RE = re.compile(r"^@seal\s+(\S+)")
TEXT_LINE_RE = re.compile(r"^\s*[^\s.]+\.\s+(.*)$")
SKIP_PREFIXES = ("#", "$", "@", "&", ">>")
INLINE_COMMENT_RE = re.compile(r"\(\$.*?\$\)")
NUMERAL_RE = re.compile(r"^\d+\([^)]+\)")
SUBSCRIPT_MAP = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
APOSTROPHE_MAP = str.maketrans({
    "\u2019": "'",
    "\u2018": "'",
    "\u02BC": "'",
    "\u00B4": "'",
    "`": "'",
})

NON_LINGUISTIC_MARKERS = (
    "no linguistic content",
    "uninscribed",
    "undetermined",
    "uncertain",
    "unclear",
)


def norm_designation(s: str) -> str:
    """Part A amended normalisation for designation comparison."""
    s = unicodedata.normalize("NFKC", s or "")
    s = s.translate(APOSTROPHE_MAP)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,;:)])", r"\1", s)
    s = re.sub(r"\(\s+", "(", s)
    s = re.sub(r"\b0+(\d)", r"\1", s)
    return s.casefold().strip()


def load_catalogue(path, id_column: str) -> dict[str, dict]:
    csv.field_size_limit(sys.maxsize)
    out: dict[str, dict] = {}
    with Path(path).open(encoding="utf-8", errors="replace", newline="") as f:
        for row in csv.DictReader(f):
            raw = (row.get(id_column) or "").strip()
            if not raw:
                continue
            try:
                pnum = f"P{int(raw):06d}"
            except ValueError:
                continue
            normalised = dict(row)
            for col in NORM_COLS:
                normalised[col] = (normalised.get(col) or "").strip().lower()
            out[pnum] = normalised
    return out


def iter_atf(path):
    path = Path(path)
    current_p = None
    current_des = ""
    buf: list[str] = []
    with path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            raw = line.rstrip("\n")
            m = HEADER_RE.match(raw)
            if m:
                if current_p is not None:
                    yield current_p, current_des, buf
                current_p = f"P{int(m.group(1)):06d}"
                current_des = m.group(2).strip()
                buf = []
            elif current_p is not None:
                buf.append(raw)
        if current_p is not None:
            yield current_p, current_des, buf


def _exclusion_reason(row, lines: list[str]):
    if row is None:
        return "no_catalogue_row"
    period = row.get("period") or ""
    genre = row.get("genre") or ""
    language = row.get("language") or ""
    subgenre = row.get("subgenre") or ""
    if "fake" in period or "fake" in genre:
        return "fake"
    if any(ln.startswith("#atf: lang qpc") for ln in lines):
        return "proto_cuneiform"
    if (
        period.startswith("uruk")
        or period.startswith("pre-uruk")
        or period.startswith("proto-elamite")
    ):
        return "proto_cuneiform"
    if not language.strip():
        return "non_linguistic_or_unknown"
    low_lang = language
    if any(m in low_lang for m in NON_LINGUISTIC_MARKERS):
        return "non_linguistic_or_unknown"
    if "composite" in subgenre:
        return "composite"
    return None


def extract_text_bodies(lines: list[str]) -> tuple[list[str], int]:
    """Return transliteration bodies and count of unparsed lines."""
    bodies: list[str] = []
    unparsed = 0
    for line in lines:
        stripped = line.lstrip()
        if not stripped:
            continue
        if any(stripped.startswith(p) for p in SKIP_PREFIXES):
            continue
        m = TEXT_LINE_RE.match(line)
        if m:
            bodies.append(m.group(1))
        else:
            unparsed += 1
    return bodies, unparsed


def extract_seal_sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    """Return list of (seal_id_token, section_lines)."""
    sections: list[tuple[str, list[str]]] = []
    i = 0
    n = len(lines)
    while i < n:
        m = SEAL_RE.match(lines[i])
        if not m:
            i += 1
            continue
        seal_tok = m.group(1)
        i += 1
        section: list[str] = []
        while i < n:
            ln = lines[i]
            if SEAL_RE.match(ln):
                break
            if ln.startswith("@") and not ln.startswith("@seal"):
                break
            section.append(ln)
            i += 1
        sections.append((seal_tok, section))
    return sections


def _split_word(word: str) -> list[str]:
    tokens: list[str] = []
    i = 0
    n = len(word)
    while i < n:
        ch = word[i]
        if ch == "{":
            j = word.find("}", i)
            if j < 0:
                tokens.append(word[i + 1 :])
                break
            tokens.append(word[i + 1 : j])
            i = j + 1
        elif ch == "|":
            j = word.find("|", i + 1)
            if j < 0:
                tokens.append(word[i:])
                break
            tokens.append(word[i : j + 1])
            i = j + 1
        elif ch.isdigit():
            num = NUMERAL_RE.match(word, i)
            if num:
                tokens.append(num.group(0))
                i = num.end()
                continue
            j = i + 1
            while j < n and word[j].isdigit():
                j += 1
            # digits not forming a numeral compound; fall through as chunk start
            while j < n and word[j] not in "{|" and not (
                word[j].isdigit() and NUMERAL_RE.match(word, j)
            ):
                j += 1
            chunk = word[i:j]
            for part in chunk.replace(":", "-").replace(".", "-").replace("+", "-").split("-"):
                if part:
                    tokens.append(part)
            if j == i:
                i += 1
            else:
                i = j
        else:
            j = i
            while j < n and word[j] not in "{|" and not (
                word[j].isdigit() and NUMERAL_RE.match(word, j)
            ):
                j += 1
            chunk = word[i:j]
            # Split on - . : + without regex (avoids pathological cost).
            for part in chunk.replace(":", "-").replace(".", "-").replace("+", "-").split("-"):
                if part:
                    tokens.append(part)
            if j == i:
                # Stray character (e.g. lone '}') — skip to avoid infinite loop.
                i += 1
            else:
                i = j
    return tokens


def _norm_token(tok: str) -> str:
    tok = tok.translate(SUBSCRIPT_MAP)
    tok = tok.lower()
    tok = (
        tok.replace("sz", "š")
        .replace("s,", "ṣ")
        .replace("t,", "ṭ")
        .replace("h,", "ḫ")
    )
    return unicodedata.normalize("NFC", tok)


def tokenize(body: str) -> tuple[list[str], bool]:
    body = INLINE_COMMENT_RE.sub(" ", body or "")
    damaged = False
    if "[" in body or "]" in body or "..." in body:
        damaged = True
    if re.search(r"(?<!\w)[xX](?!\w)", body):
        damaged = True

    cleaned = re.sub(r"[\[\]⸢⸣#?!*<>]", "", body)
    words = cleaned.split()
    tokens: list[str] = []
    for w in words:
        if w in ("...", "x", "X"):
            continue
        for piece in _split_word(w):
            t = _norm_token(piece)
            if t and t not in ("x", "..."):
                tokens.append(t)
    return tokens, damaged


def _make_record(
    *,
    rec_id: str,
    p_number: str,
    signs: list[str],
    genre: str,
    object_type: str,
    site: str,
    complete: bool,
    period: str,
    language: str,
    designation: str,
    kind: str,
    designation_match: bool,
) -> Inscription:
    prefixed = [f"CU:{t}" for t in signs]
    seq_key = " ".join(prefixed)
    return Inscription(
        system="cuneiform-seal",
        id=rec_id,
        signs=prefixed,
        label="language",
        genre=genre,
        direction="ltr",
        object_type=object_type,
        site=site,
        complete=complete,
        source="cdli",
        source_id=p_number,
        meta={
            "period": period,
            "language": language,
            "designation": designation,
            "kind": kind,
            "seq_key": seq_key,
            "designation_match": designation_match,
        },
    )


def uniquify_ids(records: list[Inscription]) -> list[Inscription]:
    """Ensure record ids are unique (ATF can repeat &P / @seal labels)."""
    seen: Counter = Counter()
    for rec in records:
        base = rec.id
        seen[base] += 1
        if seen[base] > 1:
            rec.id = f"{base}#{seen[base]}"
    return records


def mark_duplicates(records: list[Inscription]) -> list[Inscription]:
    """Set meta['duplicate_of'] when seq_key appeared earlier. Do not drop."""
    first: dict[str, str] = {}
    for rec in records:
        key = rec.meta.get("seq_key", "")
        if not key:
            continue
        if key in first:
            rec.meta["duplicate_of"] = first[key]
        else:
            first[key] = rec.id
    return records


def build_records(
    atf_path,
    catalogue: dict[str, dict],
) -> tuple[list[Inscription], dict[str, int], int]:
    """Build seal-legend records.

    Returns (records, exclusion_counts, unparsed_lines).
    """
    exclusions: Counter = Counter()
    records: list[Inscription] = []
    unparsed_total = 0

    for p_number, atf_des, lines in iter_atf(atf_path):
        row = catalogue.get(p_number)
        reason = _exclusion_reason(row, lines)
        if reason:
            exclusions[reason] += 1
            continue

        assert row is not None
        cat_des = row.get("designation") or ""
        des_match = norm_designation(cat_des) == norm_designation(atf_des)
        object_type = row.get("object_type") or ""
        period = row.get("period") or ""
        language = row.get("language") or ""
        site = row.get("provenience") or ""
        # Use ATF designation in meta (as printed on the text); keep cat for match.
        designation = cat_des

        kind_a_genre = OBJECT_TYPE_TO_GENRE.get(object_type)

        # Kind A: whole-object transliteration for seal-type objects.
        if kind_a_genre is not None:
            bodies, unparsed = extract_text_bodies(lines)
            unparsed_total += unparsed
            all_tokens: list[str] = []
            damaged_any = False
            for body in bodies:
                toks, dam = tokenize(body)
                all_tokens.extend(toks)
                damaged_any = damaged_any or dam
            if all_tokens:
                records.append(
                    _make_record(
                        rec_id=p_number,
                        p_number=p_number,
                        signs=all_tokens,
                        genre=kind_a_genre,
                        object_type=object_type,
                        site=site,
                        complete=not damaged_any,
                        period=period,
                        language=language,
                        designation=designation,
                        kind="A",
                        designation_match=des_match,
                    )
                )

        # Kind B: @seal sections from every non-excluded text.
        for seal_tok, section_lines in extract_seal_sections(lines):
            bodies, unparsed = extract_text_bodies(section_lines)
            unparsed_total += unparsed
            all_tokens = []
            damaged_any = False
            for body in bodies:
                toks, dam = tokenize(body)
                all_tokens.extend(toks)
                damaged_any = damaged_any or dam
            if not all_tokens:
                continue
            rec_id = f"{p_number}-seal{seal_tok}"
            records.append(
                _make_record(
                    rec_id=rec_id,
                    p_number=p_number,
                    signs=all_tokens,
                    genre="sealing",
                    object_type=f"seal impression on {object_type}",
                    site=site,
                    complete=not damaged_any,
                    period=period,
                    language=language,
                    designation=designation,
                    kind="B",
                    designation_match=des_match,
                )
            )

    return records, dict(exclusions), unparsed_total
