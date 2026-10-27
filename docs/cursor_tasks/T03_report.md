# T03 report

## Part C output (verbatim)

### `rm -rf raw/indus` then `bash scripts/fetch_sources.sh`

```
Cloning into 'raw/indus/indus-website'...
From https://github.com/yajnadevam/indus-website
 * branch            2434249618b1e74de3f26d28b90dfde093c3dd94 -> FETCH_HEAD
HEAD is now at 2434249 env
raw/indus/indus-website: 2434249618b1e74de3f26d28b90dfde093c3dd94 OK
Cloning into 'raw/indus/cisi-mayig'...
From https://github.com/mayig/indus-valley-script-corpus
 * branch            ad2f1e218a34b8c33c57de0d6cb8d99272765bbb -> FETCH_HEAD
HEAD is now at ad2f1e2 m184
raw/indus/cisi-mayig: ad2f1e218a34b8c33c57de0d6cb8d99272765bbb OK
Cloning into 'raw/cdli/data'...
From https://github.com/cdli-gh/data
 * branch            d66b12b065af39a57d640576b4c7e098db5dac7f -> FETCH_HEAD
HEAD is now at d66b12b Update README.md
raw/cdli/data: d66b12b065af39a57d640576b4c7e098db5dac7f OK
raw/cdli/data/cdliatf_unblocked.atf: 86897831 bytes
raw/cdli/data/cdli_cat.csv: 154768722 bytes
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
test_n_lines_ignores_leading_trailing_and_double_breaks (test_loaders.TestLoaders.test_n_lines_ignores_leading_trailing_and_double_breaks) ... ok
test_tuples_respects_commas_and_parens_in_quotes (test_loaders.TestLoaders.test_tuples_respects_commas_and_parens_in_quotes) ... ok
test_bad_label_reported_and_write_raises (test_schema.TestSchema.test_bad_label_reported_and_write_raises) ... ok
test_duplicate_system_id_raises (test_schema.TestSchema.test_duplicate_system_id_raises) ... ok
test_invalid_signs (test_schema.TestSchema.test_invalid_signs) ... ok
test_jsonl_round_trip_with_non_ascii_meta (test_schema.TestSchema.test_jsonl_round_trip_with_non_ascii_meta) ... ok
test_valid_record_has_no_errors (test_schema.TestSchema.test_valid_record_has_no_errors) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

### `git diff --stat data/processed`

```
(no output — no changes)
```

## `bash scripts/fetch_sources.sh` (re-run after pins present)

```
From https://github.com/yajnadevam/indus-website
 * branch            2434249618b1e74de3f26d28b90dfde093c3dd94 -> FETCH_HEAD
HEAD is now at 2434249 env
raw/indus/indus-website: 2434249618b1e74de3f26d28b90dfde093c3dd94 OK
From https://github.com/mayig/indus-valley-script-corpus
 * branch            ad2f1e218a34b8c33c57de0d6cb8d99272765bbb -> FETCH_HEAD
HEAD is now at ad2f1e2 m184
raw/indus/cisi-mayig: ad2f1e218a34b8c33c57de0d6cb8d99272765bbb OK
From https://github.com/cdli-gh/data
 * branch            d66b12b065af39a57d640576b4c7e098db5dac7f -> FETCH_HEAD
HEAD is now at d66b12b Update README.md
raw/cdli/data: d66b12b065af39a57d640576b4c7e098db5dac7f OK
raw/cdli/data/cdliatf_unblocked.atf: 86897831 bytes
raw/cdli/data/cdli_cat.csv: 154768722 bytes
```

## CDLI file sizes

- `raw/cdli/data/cdliatf_unblocked.atf`: 86897831 bytes (~83 MB)
- `raw/cdli/data/cdli_cat.csv`: 154768722 bytes (~148 MB)

## Inspection report path

`docs/data_notes/cdli_inspection.md`

Seal candidates total: **22691**

## Deviations

none
