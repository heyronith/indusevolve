# T02 report

## `.venv/bin/python --version`

```
Python 3.12.13
```

## Source commit hashes

- indus-website: `2434249618b1e74de3f26d28b90dfde093c3dd94`
- cisi-mayig: `ad2f1e218a34b8c33c57de0d6cb8d99272765bbb`

## Part F command output (verbatim)

### `bash scripts/fetch_sources.sh`

```
skip: raw/indus/indus-website already exists
skip: raw/indus/cisi-mayig already exists
indus-website: 2434249618b1e74de3f26d28b90dfde093c3dd94
cisi-mayig: ad2f1e218a34b8c33c57de0d6cb8d99272765bbb
```

### `.venv/bin/python -I scripts/build_indus.py raw/indus data/processed data/restricted`

```
order check indus-website: top=IW:740 final=868 initial=4 threshold=20 PASS
order check cisi-mayig: top=P:P324 final=77 initial=1 threshold=5 PASS
wrote 2536 indus-website → data/restricted/indus_website.jsonl
wrote 179 cisi-mayig → data/processed/indus_cisi_mayig.jsonl
wrote stats → data/processed/stats_indus.json
```

### `.venv/bin/python -I scripts/crosscheck_indus.py data/processed data/restricted`

```
overlapping seals: 161
agreeing on length and jar positions: 137 (85%)
wrote data/processed/crosscheck_indus.json
```

### `.venv/bin/python -m unittest discover -s tests -v`

```
test_cisi_mayig_reverses_graphemes (test_loaders.TestLoaders.test_cisi_mayig_reverses_graphemes) ... ok
test_describe_hapax (test_loaders.TestLoaders.test_describe_hapax) ... ok
test_indus_website_reading_order_and_line_breaks (test_loaders.TestLoaders.test_indus_website_reading_order_and_line_breaks) ... ok
test_tuples_respects_commas_and_parens_in_quotes (test_loaders.TestLoaders.test_tuples_respects_commas_and_parens_in_quotes) ... ok
test_bad_label_reported_and_write_raises (test_schema.TestSchema.test_bad_label_reported_and_write_raises) ... ok
test_duplicate_system_id_raises (test_schema.TestSchema.test_duplicate_system_id_raises) ... ok
test_invalid_signs (test_schema.TestSchema.test_invalid_signs) ... ok
test_jsonl_round_trip_with_non_ascii_meta (test_schema.TestSchema.test_jsonl_round_trip_with_non_ascii_meta) ... ok
test_valid_record_has_no_errors (test_schema.TestSchema.test_valid_record_has_no_errors) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.003s

OK
```

## Expected vs actual

| Check | Expected (spec) | Actual |
| --- | --- | --- |
| indus-website texts | 2,536 | 2,536 |
| indus-website tokens | 11,135 | 11,135 |
| indus-website sign types | 591 | 591 |
| indus-website top sign | IW:740, final 868, initial 0 | IW:740, final 868, initial 4 |
| cisi-mayig texts | 179 | 179 |
| cisi-mayig tokens | 1,003 | 1,003 |
| cisi-mayig sign types | 182 | 182 |
| cisi-mayig top sign | P:P324, final 77, initial 0 | P:P324, final 77, initial 1 |
| cross-check overlaps | 161 | 161 |
| cross-check agree (both checks) | 146 (91%) | 137 (85%) |

## Expected-value corrections (PI)

- Top-sign initial counts are 4 (indus-website) and 1 (cisi-mayig). The spec's "0" came from a script that counted only the 5 most common initial signs.
- Cross-check agreement on BOTH checks is 137/161 (85%). The spec's 146 (91%) was agreement on EACH check separately, misreported as joint agreement.

## `git status --short` (before committing)

```
 M README.md
 M data/SOURCES.md
 M src/indusevolve/schema.py
?? data/processed/
?? docs/cursor_tasks/T02_python_and_indus_pilot.md
?? docs/cursor_tasks/T02_report.md
?? pyproject.toml
?? scripts/
?? src/indusevolve/loaders/
?? src/indusevolve/stats.py
?? tests/test_loaders.py
```

## Deviations

none
