# IndusEvolve

## Purpose

IndusEvolve is a pre-registered study using LLM-guided evolutionary program search (OpenEvolve) to (1) test whether the Indus script encodes language, judged on writing and symbol systems held out from the search, and (2) induce its sign-class structure.

## Layout

- `src/indusevolve/` — package source (schema and later search code)
- `data/` — corpus register and (later) corpora
- `tests/` — unit tests
- `docs/cursor_tasks/` — task specs and reports

## Running tests

```
python3 -m unittest discover -s tests -v
```

## Workflow

Each task is specified in `docs/cursor_tasks/TNN_*.md` and reported in `docs/cursor_tasks/TNN_report.md`.
