You are working in the IndusEvolve repo (https://github.com/heyronith/indusevolve). Do the parts in order. Stop and report if anything fails or a check does not match; do not change the spec to make a check pass.

## Part A: Python 3.12 environment

The system Python is 3.9.6. OpenEvolve, which we use later, requires 3.10 or newer.

1. Install Python 3.12 with `brew install python@3.12`. Skip this if `python3.12 --version` already works.
2. Create a virtual environment: `python3.12 -m venv .venv`. It is already gitignored.
3. From now on, run every Python command with `.venv/bin/python`.
4. Create `pyproject.toml`:
   ```toml
   [project]
   name = "indusevolve"
   version = "0.1.0"
   requires-python = ">=3.10"
   dependencies = []

   [build-system]
   requires = ["setuptools>=68"]
   build-backend = "setuptools.build_meta"

   [tool.setuptools.packages.find]
   where = ["src"]
   ```
5. Remove the line `from __future__ import annotations` from `src/indusevolve/schema.py`; it is no longer needed.
6. In `README.md`, under "Running tests":
   - Add the setup steps (`brew install python@3.12`, then `python3.12 -m venv .venv`).
   - Change the test command to `.venv/bin/python -m unittest discover -s tests -v`.
7. Run the tests and confirm all 5 existing tests pass on 3.12.

## Part B: fetch script

Create `scripts/fetch_sources.sh` (bash, `set -euo pipefail`, run from the repo root):
- Create `raw/indus/`.
- Shallow-clone (`--depth 1`) into it, skipping any clone that already exists:
  - `https://github.com/yajnadevam/indus-website.git` → `raw/indus/indus-website`
  - `https://github.com/mayig/indus-valley-script-corpus.git` → `raw/indus/cisi-mayig`
- Print each source's latest commit hash, e.g. `git -C raw/indus/indus-website rev-parse HEAD`.

Run it. Record both commit hashes; they pin the exact versions of our data.

## Part C: loaders (in `src/indusevolve/loaders/`, with an empty `__init__.py`)

Use the standard library only.

### `loaders/indus_website.py`

Reads `population-script.sql` from `raw/indus/indus-website/`. It is a MySQL dump. The tables we need appear as `INSERT INTO <TABLE> (<cols>) VALUES (...),(...);` blocks:

| Table | Columns |
| --- | --- |
| SITE | SITEID, NAME |
| GLYPH | GLYPHID, UNICODE |
| SEAL | SEALID, SITEID, MATERIAL, CISI, MUSEUM, WIDTH, HEIGHT, THICKNESS |
| INSCRIPTION | SEALID, ISCOMPLETE, DIRECTION |
| ICONOGRAPHY | SEALID, DESCRIPTION |
| GLYPHSEQUENCE | SEALID, GLYPHID, IDX |

Write it as follows:

- **`_tuples(body) -> list[list[str]]`:** a character-level parser for the `(...),(...)` list. It must respect single and double quotes, backslash escapes, and commas or parentheses inside quoted strings, and strip the quotes from values. Do not use a simple regex split; values contain commas and parentheses.
- **`parse(sql_path) -> dict`:** returns the tables above as Python structures. Group GLYPHSEQUENCE rows by SEALID and sort them by IDX.
- **`to_records(db) -> list[Inscription]`**, one per SEALID with a glyph sequence:
  - GLYPHID `0` is a line break (`<br>`). Drop it from `signs`, but count lines into `meta["n_lines"]`.
  - **Reverse the order.** The dump stores signs in reverse reading order; we verified this from the "jar" sign (glyph 740), and Part E checks it.
  - Skip sequences that are empty after removing line breaks.
  - Field mapping:
    - `system="indus"`, `id=f"IW-{SEALID}"`, `signs=[f"IW:{g}" ...]`, `label="unlabelled"`
    - `genre="unknown"`, `direction="unknown"`
    - `object_type=MATERIAL`, `site=` the site NAME from SITE (fall back to the code)
    - `complete`: `True` for "Y", `False` for "N", otherwise `None`
    - `source="indus-website"`, `source_id=CISI` (`""` if NULL or empty)
    - `meta={"material", "motif" (ICONOGRAPHY description or ""), "stored_direction" (INSCRIPTION.DIRECTION), "n_lines"}`

### `loaders/cisi_mayig.py`

Reads every `*.json` under `raw/indus/cisi-mayig/corpus/`, recursively. Each file is a JSON list of artefact sides, each `{"id": "M-174A", "description": "...", "graphemes": [{"id": "P324", ...}, ...]}`. The README of that repo says graphemes are recorded left to right as seen on the sealing, and the script reads right to left. So:

- **Reverse the grapheme order** to get reading order. Part E checks this.
- Skip sides with no graphemes.
- Field mapping:
  - `system="indus"`, `id=f"CISI-{side id}"`, `signs=[f"P:{g}" ...]`, `label="unlabelled"`
  - `genre="seal"` if "seal" is in the description (lowercased), else `"unknown"`
  - `direction="rtl"`, `object_type=` the description, `site="Mohenjo-daro"`
  - `source="cisi-mayig"`, `source_id=` the side id

## Part D: statistics and build scripts

**`src/indusevolve/stats.py`**: `describe(records) -> dict` returns:
- `texts`, `tokens`, `sign_types`, `hapax_types` (sign types occurring once)
- `mean_length` (3 decimals), `max_length`, `length_hist` (length → count)
- `unigram_entropy_bits` (3 decimals)
- `top_signs` (10 most common)
- `top_initial` and `top_final` (5 most common first and last signs, over texts of length ≥ 2)

**`scripts/build_indus.py`**: usage `.venv/bin/python -I scripts/build_indus.py raw/indus data/processed data/restricted`. It:
1. Builds both corpora.
2. For each corpus, runs an **order check**. Take the most frequent sign; count how often it is the final sign and how often the first sign (texts of length ≥ 2). Pass if final > 5 × max(1, initial). Print the result. Exit with an error if it fails.
3. Writes `data/restricted/indus_website.jsonl`. This file is gitignored because its provenance is unconfirmed.
4. Writes `data/processed/indus_cisi_mayig.jsonl` (MIT licence, committed).
5. Writes `data/processed/stats_indus.json` with `describe()` for both.

**`scripts/crosscheck_indus.py`**: usage `.venv/bin/python -I scripts/crosscheck_indus.py data/processed data/restricted`.
- Matches CISI-mayig records to indus-website records by CISI number. Normalise both IDs with `^\s*([A-Za-z]+)\s*-?\s*0*(\d+)\s*([A-Za-z]?)` → `f"{prefix.upper()}-{int(num)}{suffix.upper()}"`. If there is no exact match, try without the trailing side letter.
- For each overlapping seal, compare:
  - (a) text length;
  - (b) the positions of the jar sign, which is `IW:740` in one source and `P:P324` in the other.
- Print the number of overlapping seals and the percentage agreeing on both checks.
- Write `data/processed/crosscheck_indus.json`: counts, plus a list of disagreements (CISI id, IW id, both lengths, both jar positions).

## Part E: tests (`tests/test_loaders.py`, unittest)

Use tiny inline fixtures written to a temp folder; do not touch `raw/`.

- **`_tuples`** parses `("SI1","Kot Diji (site)"),("SI2","a, b")` into `[["SI1","Kot Diji (site)"],["SI2","a, b"]]`.
- **indus-website**, using a mini SQL dump with 3 seals:
  - seal 1: IDX 0→740, 1→17, 2→5. Reading order must come out as `["IW:5","IW:17","IW:740"]`.
  - seal 2: contains a GLYPHID 0 line break. The break is dropped and `n_lines == 2`.
  - seal 3: only a line break. It is skipped.
- **cisi-mayig**, using one JSON file with a side whose graphemes are P324, P175, P050. Signs come out as `["P:P050","P:P175","P:P324"]`.
- **The `describe()` hapax count** is correct on a 3-record toy corpus.

## Part F: run and check

```
bash scripts/fetch_sources.sh
.venv/bin/python -I scripts/build_indus.py raw/indus data/processed data/restricted
.venv/bin/python -I scripts/crosscheck_indus.py data/processed data/restricted
.venv/bin/python -m unittest discover -s tests -v
```

**Expected values.** These are from an independent run on the same source versions. Report any mismatch; do not adjust code to force them.

| Corpus | Texts | Tokens | Sign types | Top sign |
| --- | --- | --- | --- | --- |
| indus-website | 2,536 | 11,135 | 591 | IW:740, final 868 times, initial 0 |
| cisi-mayig | 179 | 1,003 | 182 | P:P324, final 77 times, initial 0 |

The cross-check should give 161 overlapping seals, with 146 (91%) agreeing on both checks.

## Part G: register, report, commit

1. Add two rows to `data/SOURCES.md` (and remove "No sources yet."):
   - **indus-website** | Indus | 2,536 inscriptions, ~700 sign codes, 52 sites, motifs, CISI numbers; MySQL dump, commit <hash> | GPL-3.0 (repository); transcription provenance undocumented | No (until provenance confirmed) | Built (pilot) | Stored in reverse reading order; flipped and verified by jar-sign position. Output kept in `data/restricted/`.
   - **cisi-mayig** | Indus | 179 Mohenjo-daro seals in Parpola (CISI) numbering; JSON, commit <hash> | MIT | Yes | Built | Work in progress digitisation of CISI vol. 1.
2. Save this task text as `docs/cursor_tasks/T02_python_and_indus_pilot.md`.
3. Write `docs/cursor_tasks/T02_report.md` containing:
   - the output of `.venv/bin/python --version`;
   - both source commit hashes;
   - the full output of the four commands in Part F, verbatim;
   - a table of expected vs actual values;
   - `git status --short`;
   - deviations ("none" if none).
4. Commit and push:
   ```
   git add -A
   git commit -m "T02: Python 3.12 env, Indus pilot loaders, build and cross-check"
   git push
   ```
   Check that `git status` shows nothing from `raw/` or `data/restricted/` staged.

Reply with the commit hash and the expected-vs-actual table.
