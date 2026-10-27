# T01 report

## OS

Darwin 25.5.0 arm64 (macOS)

## python3 --version

```
Python 3.9.6
```

## Test output

```
test_bad_label_reported_and_write_raises (test_schema.TestSchema) ... ok
test_duplicate_system_id_raises (test_schema.TestSchema) ... ok
test_invalid_signs (test_schema.TestSchema) ... ok
test_jsonl_round_trip_with_non_ascii_meta (test_schema.TestSchema) ... ok
test_valid_record_has_no_errors (test_schema.TestSchema) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.005s

OK
```

## git status --short (before committing)

```
?? .gitignore
?? README.md
?? data/
?? docs/
?? src/
?? tests/
```

## Deviations

- Added `from __future__ import annotations` in `src/indusevolve/schema.py` so `bool | None` and `list[str]` type hints work on Python 3.9.6.
- Initialized a local git repository (`git init -b main`) and set `origin` to `https://github.com/heyronith/indusevolve.git` because the workspace had no git history yet (remote repo was empty).
