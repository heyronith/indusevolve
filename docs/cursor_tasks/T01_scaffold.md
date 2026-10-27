You are setting up the IndusEvolve repository(https://github.com/heyronith/indusevolve ): a research project testing whether the Indus script encodes language. Create exactly the files below, run the tests, write the report, then commit and push. Stop and report if anything fails; do not improvise beyond this spec.

## 1. Files to create

**`.gitignore`**, ignoring:
- `raw/`
- `data/restricted/`
- `__pycache__/` and `*.pyc`
- `.venv/`
- `.DS_Store`
- `.idea/` and `.vscode/`

**`README.md`** with these sections:
- **Title:** "IndusEvolve".
- **Purpose:** one paragraph. It is a pre-registered study using LLM-guided evolutionary program search (OpenEvolve) to (1) test whether the Indus script encodes language, judged on writing and symbol systems held out from the search, and (2) induce its sign-class structure.
- **Layout:** list the folders created in this task.
- **Running tests:** `python3 -m unittest discover -s tests -v`.
- **Workflow:** "Each task is specified in `docs/cursor_tasks/TNN_*.md` and reported in `docs/cursor_tasks/TNN_report.md`."

**`data/SOURCES.md`**:
- Title: "Source and licence register".
- One sentence: "Every corpus must have a row here before it is used."
- An empty table with columns: Key | System | What | Licence | Can release | Status | Notes.
- Under the table: "No sources yet."

**`src/indusevolve/__init__.py`**: empty.

**`src/indusevolve/schema.py`**, containing:

1. Constants:
   - `LABELS = {"language", "non-language", "unlabelled"}`
   - `DIRECTIONS = {"rtl", "ltr", "boustrophedon", "vertical", "unknown"}`
   - `GENRES = {"seal", "sealing", "tablet", "label", "docket", "graffito", "bulla", "coin", "inscription", "literary", "emblem", "mark", "other", "unknown"}`
   - `SIGN_TOKEN = re.compile(r"^[A-Z]{1,4}:\S+$")`. Sign tokens are namespaced, e.g. `IW:740`, `P:P324`, `CU:lugal`.

2. A dataclass `Inscription`, with fields in this order:

   | Field | Type | Default |
   | --- | --- | --- |
   | `system` | `str` | required |
   | `id` | `str` | required |
   | `signs` | `list[str]` | required |
   | `label` | `str` | required |
   | `genre` | `str` | `"unknown"` |
   | `direction` | `str` | `"unknown"` |
   | `object_type` | `str` | `""` |
   | `site` | `str` | `""` |
   | `complete` | `bool \| None` | `None` |
   | `source` | `str` | `""` |
   | `source_id` | `str` | `""` |
   | `meta` | `dict` | `field(default_factory=dict)` |

   - Docstring: "Signs are always stored in READING ORDER; `direction` records how the original was physically written."
   - Method `validate(self) -> list[str]` returns error strings, empty if valid. It checks:
     - `system` and `id` are non-empty;
     - `signs` is a non-empty list in which every item matches `SIGN_TOKEN`;
     - `label`, `direction` and `genre` are in their sets.

3. Function `write_jsonl(records, path) -> int`:
   - Creates parent folders as needed.
   - Validates every record and raises `ValueError` naming `system/id` and the errors on the first invalid one.
   - Raises `ValueError` on a duplicate `(system, id)`.
   - Writes one JSON object per line with `ensure_ascii=False`, using `dataclasses.asdict`.
   - Returns the number of lines written.

4. Function `read_jsonl(path)`: yields `Inscription` objects and skips blank lines.

**`tests/test_schema.py`**, using `unittest`. Put `sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))` at the top. Tests:
- A valid record (system `"indus"`, id `"T-1"`, signs `["IW:740", "IW:2"]`, label `"unlabelled"`) validates with no errors.
- A JSONL write and read round-trip, in a `tempfile.TemporaryDirectory()`, returns an identical record, including a non-ASCII `meta` value such as `{"site_note": "Mohenjo-daro, Śiva?"}`.
- A bad label is reported by `validate()`, and `write_jsonl` raises `ValueError`.
- Each of these signs fails validation: `[]`; `["740"]` (no namespace); `["IW:"]`; `["iw:740"]` (lowercase prefix).
- A duplicate `(system, id)` makes `write_jsonl` raise `ValueError`.

**`docs/cursor_tasks/T01_scaffold.md`**: this task text, saved verbatim.

## 2. Run the tests

`python3 -m unittest discover -s tests -v`. All tests must pass.

## 3. Write `docs/cursor_tasks/T01_report.md`

Include:
- your OS;
- the output of `python3 --version`;
- the full test output, verbatim;
- the output of `git status --short` before committing;
- any deviation from this spec, with the reason ("none" if none).

## 4. Commit and push

```
git add -A
git commit -m "T01: repository scaffold and record schema"
git push -u origin main
```

Reply with the commit hash and the final test line (e.g. "Ran 6 tests ... OK").
