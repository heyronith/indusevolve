You are working in the IndusEvolve repo (https://github.com/heyronith/indusevolve). Use `.venv/bin/python` for all Python. Do the parts in order. Stop and report if anything fails; do not change the spec to make a check pass.

This task does NOT build a CDLI corpus. It only downloads CDLI and records what the files actually contain, so the loader in the next task is written against the real format rather than guesses.

## Part A: pin every source to an exact commit

Rewrite `scripts/fetch_sources.sh` (bash, `set -euo pipefail`, run from repo root):

1. Define the pins at the top:
   ```
   INDUS_WEBSITE_COMMIT=2434249618b1e74de3f26d28b90dfde093c3dd94
   CISI_MAYIG_COMMIT=ad2f1e218a34b8c33c57de0d6cb8d99272765bbb
   CDLI_COMMIT=d66b12b065af39a57d640576b4c7e098db5dac7f
   ```
2. Write a function `fetch_pinned URL DIR COMMIT`:
   - If DIR does not exist: `GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 URL DIR`.
   - Then: `git -C DIR fetch --depth 1 origin COMMIT` and `GIT_LFS_SKIP_SMUDGE=1 git -C DIR checkout --detach COMMIT`.
   - Check: if `git -C DIR rev-parse HEAD` does not equal COMMIT, print an error and exit 1.
   - Print `<dir>: <commit> OK`.
3. Call it three times:
   - `https://github.com/yajnadevam/indus-website.git` → `raw/indus/indus-website`
   - `https://github.com/mayig/indus-valley-script-corpus.git` → `raw/indus/cisi-mayig`
   - `https://github.com/cdli-gh/data.git` → `raw/cdli/data`
4. For CDLI only, then run `git -C raw/cdli/data lfs pull`, which downloads about 240 MB. Fail with a clear message if `git lfs version` does not work.
5. Check that both `raw/cdli/data/cdliatf_unblocked.atf` and `raw/cdli/data/cdli_cat.csv` are larger than 1 MB. Smaller means they are still Git LFS pointer stubs; exit 1.

Expected sizes: about 83 MB for the `.atf` file and about 148 MB for the `.csv` file.

## Part B: fix the line count in the indus-website loader

In `src/indusevolve/loaders/indus_website.py`:
- **The bug:** `n_lines = n_breaks + 1` over-counts when a sequence starts or ends with a line break (GLYPHID `0`), or has two breaks in a row. This happens in about 60 real texts.
- **The fix:** split the stored sequence on `"0"` and count the non-empty segments. `n_lines` is that count.
- **Add a test** in `tests/test_loaders.py`: a seal whose stored sequence is `0, 5, 0, 0, 7, 0` must give `n_lines == 2`, and signs `["IW:7", "IW:5"]` (reversed reading order).

## Part C: rebuild and confirm nothing else changed

```
rm -rf raw/indus
bash scripts/fetch_sources.sh
.venv/bin/python -I scripts/build_indus.py raw/indus data/processed data/restricted
.venv/bin/python -I scripts/crosscheck_indus.py data/processed data/restricted
.venv/bin/python -m unittest discover -s tests -v
git diff --stat data/processed
```

- `git diff --stat data/processed` must show **no changes**. The line-count fix only touches `meta.n_lines` in the restricted file.
- The results must still read: 2536 / 179 texts, order checks PASS, 161 overlapping, 137 (85%) agreeing.

## Part D: CDLI inspection script (no loader yet)

Create `scripts/inspect_cdli.py`, usage `.venv/bin/python -I scripts/inspect_cdli.py raw/cdli/data docs/data_notes/cdli_inspection.md`.

Standard library only. Read files with `encoding="utf-8", errors="replace"`, and call `csv.field_size_limit(sys.maxsize)`.

The script writes a Markdown report with these sections, using code blocks for raw text:

1. **Header.** "Source: Cuneiform Digital Library Initiative (CDLI), github.com/cdli-gh/data at commit d66b12b, licence CC BY-NC-SA. Short excerpts reproduced for research documentation."
2. **Files.** For each file: size in bytes and line count. Also the number of lines in the ATF starting with `&P`.
3. **ATF sample.** The first 60 lines of `cdliatf_unblocked.atf`, verbatim.
4. **Catalogue overview.** Number of data rows, and the full list of column names in order, numbered.
5. **Key columns.** For every column whose lowercased name contains any of `object`, `genre`, `language`, `period`, `provenience`, `material`, `id_`: its 40 most common values with counts, including the empty value.
6. **Seal candidates.**
   - Count the catalogue rows where any of the Key columns from section 5 has a lowercased value containing `seal` or `bulla`.
   - Break the count down by (column, value), sorted by count.
7. **Seal examples.**
   - Take the first 8 seal-candidate rows that also have a matching `&P` entry in the ATF.
   - For each, print its values in the Key columns, then its full ATF block from the `&P` line up to the next `&P` line, verbatim (max 40 lines).
   - The P-number in the ATF looks like `&P000123`. Try matching on the catalogue's id column both as-is and zero-padded to 6 digits with a `P` prefix. Report which convention matched.
8. **Unmatched.** Of all seal-candidate rows, how many have no matching ATF entry (no transliteration available)?

Run it.

## Part E: register, report, commit

1. In `data/SOURCES.md`, update the Notes of both Indus rows to say "pinned in `scripts/fetch_sources.sh`". Add a row:
   - **cdli** | Cuneiform | CDLI bulk dump: ATF transliterations + catalogue, commit d66b12b (data last updated Aug 2022) | CC BY-NC-SA | Yes, same licence, non-commercial only | Inspected (T03) | Loader to be written in T04 from `docs/data_notes/cdli_inspection.md`.
2. Save this task text as `docs/cursor_tasks/T03_pin_sources_and_inspect_cdli.md`.
3. Write `docs/cursor_tasks/T03_report.md` containing:
   - the full output of Part C, verbatim;
   - the output of `bash scripts/fetch_sources.sh`;
   - the CDLI file sizes;
   - the path of the inspection report;
   - deviations ("none" if none).
4. Commit and push:
   ```
   git add -A
   git commit -m "T03: pin source commits, fix n_lines, CDLI download + inspection report"
   git push
   ```
   Do not stage anything under `raw/` or `data/restricted/`.

Reply with the commit hash and the "Seal candidates" total from the inspection report.
