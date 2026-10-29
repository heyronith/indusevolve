# T04 report

## PI amendment to Part A

PI decision on T04 Part A (overrides the stop):

1. Create docs/data_notes/cdli_id_decision.md with this text:
   "Decision: id_text is the CDLI object key (P-number). Evidence: the id column matched 0/133 designations, exact or normalised. id_text matched 184/200 after normalisation. The PI hand-checked all 16 remaining mismatches: 12 are the same object under a different citation form (Š/S transliteration, an added or dropped museum number, a series alias); 4 cannot be resolved from the text alone; none is clearly a different object. Designation strings are citations that differ legitimately between the catalogue and ATF files, so exact-string agreement understates key correctness. The 0.95 rule is replaced by this manual audit plus the per-record check below."
   Below it, add the 16-row table with one extra column: the P-number of each row.

2. Continue T04 from Part B exactly as specified, using id_text, with ONE addition to Part C:
   - For every built record, set meta["designation_match"] = True or False, using the Part A normalised comparison between the catalogue and ATF designations.
   - In stats_cuneiform_seals.json and the report, give the designation_match share, overall and by kind (A or B).
   - List up to 30 kind-A mismatches with their P-numbers.
   - Do NOT filter on this field.
   - If the overall share is below 0.80, stop after writing the stats and report back.

### Agreement shares (exact and normalised)

| Convention | Exact | Normalised |
| --- | --- | --- |
| id_text | 169/200 = 0.8450 | 184/200 = 0.9200 |
| id | 0/133 = 0.0000 | 0/133 = 0.0000 |

Remaining `id_text` mismatches after normalisation: 16.

## Command output

### `.venv/bin/python -I scripts/check_cdli_ids.py raw/cdli/data docs/data_notes/cdli_id_check.md`

```
parsing ATF designations…
ATF P-headers: 135199
reading catalogue…
sampled 500 rows with non-empty designation
id_text: matched=200 exact=169/200 (0.8450) normalised=184/200 (0.9200)
id: matched=133 exact=0/133 (0.0000) normalised=0/133 (0.0000)
ID CONVENTION: id_text
  (PI override; formal 0.95 rule not met — see docs/data_notes/cdli_id_decision.md)
wrote docs/data_notes/cdli_id_check.md
id_text remaining mismatches: 16
```

### `.venv/bin/python -I scripts/build_cdli.py raw/cdli/data data/processed`

```
loading catalogue (id column=id_text)…
catalogue entries: 353283
building records from ATF…
wrote 26072 records → data/processed/cuneiform_seals.jsonl
wrote stats → data/processed/stats_cuneiform_seals.json
kind A: 2348  kind B: 23724
duplicates: 15496
clean subset (complete, non-dup, len≥2): 5354
exclusions: {'proto_cuneiform': 8818, 'composite': 8045, 'non_linguistic_or_unknown': 17790, 'no_catalogue_row': 15, 'fake': 20}
unparsed_lines: 16
designation_match overall=0.9422 A=0.9178 B=0.9446
kind-A mismatch examples listed: 30
```

### `.venv/bin/python -m unittest discover -s tests -v`

```
test_build_mini_corpus (test_cdli.TestCdli.test_build_mini_corpus) ... ok
test_tokeniser_specials (test_cdli.TestCdli.test_tokeniser_specials) ... ok
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
Ran 12 tests in 0.004s

OK
```

## designation_match

- overall: **0.9422**
- kind A: **0.9178**
- kind B: **0.9446**

(Above 0.80 — corpus retained. Up to 30 kind-A mismatches are listed in `data/processed/stats_cuneiform_seals.json`.)

## First 5 lines of `cuneiform_seals.jsonl`

```
{"system": "cuneiform-seal", "id": "P491234-seal1", "signs": ["CU:ia", "CU:ap", "CU:hu", "CU:ra", "CU:nu", "CU:um", "CU:_dumu_", "CU:a", "CU:bi", "CU:ra", "CU:ma", "CU:a", "CU:_arad2_", "CU:ša", "CU:d", "CU:suen"], "label": "language", "genre": "sealing", "direction": "ltr", "object_type": "seal impression on tablet", "site": "Me-Turan (mod. Tell Haddad)", "complete": true, "source": "cdli", "source_id": "P491234", "meta": {"period": "early old babylonian (ca. 2000-1900 bc)", "language": "akkadian", "designation": "É-dub-ba-a 01, 02", "kind": "B", "seq_key": "CU:ia CU:ap CU:hu CU:ra CU:nu CU:um CU:_dumu_ CU:a CU:bi CU:ra CU:ma CU:a CU:_arad2_ CU:ša CU:d CU:suen", "designation_match": true}}
{"system": "cuneiform-seal", "id": "P491234-seal2", "signs": ["CU:su", "CU:mu", "CU:ra", "CU:pi2", "CU:_dumu_", "CU:ia", "CU:šu", "CU:ub", "CU:dingir", "CU:_arad2_", "CU:ša", "CU:d", "CU:iškur"], "label": "language", "genre": "sealing", "direction": "ltr", "object_type": "seal impression on tablet", "site": "Me-Turan (mod. Tell Haddad)", "complete": false, "source": "cdli", "source_id": "P491234", "meta": {"period": "early old babylonian (ca. 2000-1900 bc)", "language": "akkadian", "designation": "É-dub-ba-a 01, 02", "kind": "B", "seq_key": "CU:su CU:mu CU:ra CU:pi2 CU:_dumu_ CU:ia CU:šu CU:ub CU:dingir CU:_arad2_ CU:ša CU:d CU:iškur", "designation_match": true}}
{"system": "cuneiform-seal", "id": "P491234-seal3", "signs": ["CU:u", "CU:bar", "CU:lu", "CU:lu", "CU:_dumu_", "CU:aq", "CU:bu", "CU:u2"], "label": "language", "genre": "sealing", "direction": "ltr", "object_type": "seal impression on tablet", "site": "Me-Turan (mod. Tell Haddad)", "complete": true, "source": "cdli", "source_id": "P491234", "meta": {"period": "early old babylonian (ca. 2000-1900 bc)", "language": "akkadian", "designation": "É-dub-ba-a 01, 02", "kind": "B", "seq_key": "CU:u CU:bar CU:lu CU:lu CU:_dumu_ CU:aq CU:bu CU:u2", "designation_match": true}}
{"system": "cuneiform-seal", "id": "P491234-seal4", "signs": ["CU:ku", "CU:uz", "CU:zi", "CU:_dumu_", "CU:nu", "CU:ri", "CU:_arad2_", "CU:ṣil2", "CU:li2", "CU:d", "CU:suen"], "label": "language", "genre": "sealing", "direction": "ltr", "object_type": "seal impression on tablet", "site": "Me-Turan (mod. Tell Haddad)", "complete": true, "source": "cdli", "source_id": "P491234", "meta": {"period": "early old babylonian (ca. 2000-1900 bc)", "language": "akkadian", "designation": "É-dub-ba-a 01, 02", "kind": "B", "seq_key": "CU:ku CU:uz CU:zi CU:_dumu_ CU:nu CU:ri CU:_arad2_ CU:ṣil2 CU:li2 CU:d CU:suen", "designation_match": true}}
{"system": "cuneiform-seal", "id": "P491234-seal5", "signs": ["CU:ia", "CU:am", "CU:ṣi2", "CU:at", "CU:nu", "CU:u2", "CU:_dumu_", "CU:a", "CU:li2", "CU:wa", "CU:aq", "CU:rum", "CU:_arad_", "CU:ša", "CU:d"], "label": "language", "genre": "sealing", "direction": "ltr", "object_type": "seal impression on tablet", "site": "Me-Turan (mod. Tell Haddad)", "complete": false, "source": "cdli", "source_id": "P491234", "meta": {"period": "early old babylonian (ca. 2000-1900 bc)", "language": "akkadian", "designation": "É-dub-ba-a 01, 02", "kind": "B", "seq_key": "CU:ia CU:am CU:ṣi2 CU:at CU:nu CU:u2 CU:_dumu_ CU:a CU:li2 CU:wa CU:aq CU:rum CU:_arad_ CU:ša CU:d", "designation_match": true}}
```

## Five random kind-B records (`random.Random(1)`) with ATF blocks

### P118877-seal1

```json
{
  "id": "P118877-seal1",
  "signs": [
    "CU:arad2",
    "CU:mu",
    "CU:dub",
    "CU:sar",
    "CU:dumu",
    "CU:d",
    "CU:šara2",
    "CU:za",
    "CU:me"
  ],
  "genre": "sealing",
  "object_type": "seal impression on tablet",
  "site": "Umma (mod. Tell Jokha)",
  "complete": true,
  "meta": {
    "period": "ur iii (ca. 2100-2000 bc)",
    "language": "sumerian",
    "designation": "MVN 16, 0829",
    "kind": "B",
    "seq_key": "CU:arad2 CU:mu CU:dub CU:sar CU:dumu CU:d CU:šara2 CU:za CU:me",
    "designation_match": true,
    "duplicate_of": "P106356-seal1"
  }
}
```

ATF block:

```
&P118877 = MVN 16, 0829
#atf: lang sux 
@tablet 
@obverse 
1. 1(u) {kusz}a2-ga2-la2 
2. 1(u) {kusz}du10-gan 2(disz) sila3-ta 
3. ki a-kal-la-ta 
4. kiszib3 ur-{d}nu-musz-da 
@reverse 
1. sza3 bala-a 
$ seal impression 
2. mu us2-sa {d}szu-{d}suen lugal-e bad3 mar#-tu mu-du3 
@seal 1 
1. ARAD2-mu# 
2. dub-sar 
3. dumu {d}szara2-za-me# 

```

### P454197-seal1

```json
{
  "id": "P454197-seal1",
  "signs": [
    "CU:šu",
    "CU:nu",
    "CU:a",
    "CU:dub",
    "CU:sar",
    "CU:dumu",
    "CU:e2",
    "CU:zi"
  ],
  "genre": "sealing",
  "object_type": "seal impression on tablet",
  "site": "Irisagrig (mod. uncertain) ?",
  "complete": true,
  "meta": {
    "period": "ur iii (ca. 2100-2000 bc) ?",
    "language": "sumerian",
    "designation": "Nisaba 15, 1045",
    "kind": "B",
    "seq_key": "CU:šu CU:nu CU:a CU:dub CU:sar CU:dumu CU:e2 CU:zi",
    "designation_match": true
  }
}
```

ATF block:

```
&P454197 = Nisaba 15, 1045
#atf: lang sux  
@tablet 
@obverse 
1. 3(asz) 1(barig) sze gur 
2. ki lu-lu-ta 
3. szu-nu-a 
@reverse 
1. szu ba-ti 
$ blank space 
# seal impression 
@seal 1 
1. szu-nu-a 
2. dub-sar 
3. dumu e2-zi 

```

### P109951-seal1

```json
{
  "id": "P109951-seal1",
  "signs": [
    "CU:ur",
    "CU:d",
    "CU:ba",
    "CU:ba6",
    "CU:dub",
    "CU:sar",
    "CU:dumu",
    "CU:ri2",
    "CU:ad"
  ],
  "genre": "sealing",
  "object_type": "seal impression on tablet & envelope",
  "site": "Girsu (mod. Tello)",
  "complete": true,
  "meta": {
    "period": "ur iii (ca. 2100-2000 bc)",
    "language": "sumerian",
    "designation": "HLC 073 (pl. 083)",
    "kind": "B",
    "seq_key": "CU:ur CU:d CU:ba CU:ba6 CU:dub CU:sar CU:dumu CU:ri2 CU:ad",
    "designation_match": true
  }
}
```

ATF block:

```
&P109951 = HLC 073 (pl. 083)
#atf: lang sux 
@tablet 
@obverse 
1. 5(u) 3(disz) amar ga 
2. ur-{d}nansze 
3. 1(u) 5(disz) elam 
4. 1(u) 2(disz) e2-ur2-bi 
5. 6(disz) ARAD2-dam 
6. 5(disz) hu-ru 
7. 4(disz) du11-ga 
8. 3(disz) lu2-{d}nin-gir2-su dumu nam-ha-ni 
9. 1(disz) ur-{d}hendur-sag 
10. 5(disz) lu2-uru11{ki} 
@reverse 
1. 1(u) la2 1(disz) na-a-na 
2. 3(disz) ur-an-ne2 
3. 1(u) 3(disz) amar a-ru-a 
4. 6(disz) amar ab2 tur3 
$ blank space 
5. szunigin 4(u) 2(disz) amar du3-a gub-ba 
6. szunigin 1(gesz2) 3(u) 3(disz) amar da-ba 
7. 4(barig) sze lugal-ta 
8. sze-bi 1(gesz2) 4(u) 8(asz) gur 
9. sze amar mu unu3-de3-sze3 
10. inim ur-sa6-ga-mu 
11. ur-{d}ba-ba6 szu ba-ti 
@left 
1. mu amar-{d}suen lugal 
@envelope 
$ blank space 
$ rest broken 
@reverse 
$ beginning broken 
1'. [...] gub-ba 4(barig) lugal-ta 
2'. 1(gesz2) 3(u) 3(disz) amar da-ba 
3'. sze-bi 1(gesz2) 4(u) 8(asz) gur 
$ blank space 
4'. sze amar-e gu7-a 
5'. mu unu3-de3-sze3 
6'. inim ur-sa6-ga-mu nam-[...] 
7'. kiszib3 ur-{d}ba-ba6# [dumu] ri2-ad 
$ blank space 
@seal 1 
1. ur-{d}ba-ba6 
2. dub-sar 
3. dumu ri2-ad 
 

```

### P131629-seal1

```json
{
  "id": "P131629-seal1",
  "signs": [
    "CU:nu",
    "CU:ur2",
    "CU:i3",
    "CU:li2",
    "CU:dumu",
    "CU:ib2",
    "CU:bi2",
    "CU:la"
  ],
  "genre": "sealing",
  "object_type": "seal impression on tablet",
  "site": "Puzriš-Dagan (mod. Drehem)",
  "complete": true,
  "meta": {
    "period": "ur iii (ca. 2100-2000 bc)",
    "language": "sumerian",
    "designation": "TCL 02, 5540",
    "kind": "B",
    "seq_key": "CU:nu CU:ur2 CU:i3 CU:li2 CU:dumu CU:ib2 CU:bi2 CU:la",
    "designation_match": true
  }
}
```

ATF block:

```
&P131629 = TCL 02, 5540
#atf: lang sux 
@tablet 
@obverse 
1. 1(asz) sze gur ur5-sze3 
2. masz2 1(asz) gur 1(barig) 4(ban2)-ta 
3. ki ur-du6-ku3-ta 
4. nu-ur2-i3-li2 
5. szu ba-ti 
6. kislah su-su-da 
@reverse 
1. tukum-bi 
2. nu-un-na-ag2 
3. tab-am3 tab-be2-da 
4. mu lugal-bi in-pa3 
5. 1(disz) e2-ki-bi 
6. 1(disz) lu2-{d}iszkur dub-sar 
7. lu2-inim-ma-bi-me 
$ 1 line blank 
8. iti sze-sag11-ku5 
9. mu {d}i-bi2-{d}suen lugal 
@seal 1 
1. nu-ur2-i3-li2 
2. dumu ib2-bi2-la 

```

### P117631-seal1

```json
{
  "id": "P117631-seal1",
  "signs": [
    "CU:lu2",
    "CU:d",
    "CU:nin",
    "CU:šubur",
    "CU:dumu",
    "CU:lugal",
    "CU:iri"
  ],
  "genre": "sealing",
  "object_type": "seal impression on tablet",
  "site": "Girsu (mod. Tello)",
  "complete": false,
  "meta": {
    "period": "ur iii (ca. 2100-2000 bc)",
    "language": "sumerian",
    "designation": "MVN 13, 859",
    "kind": "B",
    "seq_key": "CU:lu2 CU:d CU:nin CU:šubur CU:dumu CU:lugal CU:iri",
    "designation_match": true
  }
}
```

ATF block:

```
&P117631 = MVN 13, 859
#atf: lang sux 
@tablet 
@obverse 
1. 1(disz) i3-gesz 
2. elam lu2-ha-zi 
3. szu ba-ab-ti 
4. ki ur?-ab-ba-ta 
@reverse 
1. kiszib3 lu2-{d}nin#-[szubur e2? x] 
2. giri3 {d}ba-ba6-nin-am3 
3. iti diri sze-sag11-ku5 
4. mu si#-mu-ru-um#{ki#} ba#-hul 
@seal 1 
1. lu2-{d}nin-[szubur] 
2. dumu lugal-iri [...] 

```

## `ls -lh data/processed`

```
total 32648
-rw-r--r--@ 1 ronny  staff   6.3K Oct 27 13:27 crosscheck_indus.json
-rw-r--r--@ 1 ronny  staff    16M Oct 28 19:20 cuneiform_seals.jsonl
-rw-r--r--@ 1 ronny  staff    53K Oct 27 13:27 indus_cisi_mayig.jsonl
-rw-r--r--@ 1 ronny  staff    11K Oct 28 19:20 stats_cuneiform_seals.json
-rw-r--r--@ 1 ronny  staff   2.8K Oct 27 13:27 stats_indus.json
```

## Deviations

- `uniquify_ids`: a few ATF blocks / `@seal` labels repeat the same id; second+ copies get a `#N` suffix so JSONL ids stay unique.
- Tokeniser: stray `}` / malformed determinatives like `ur-(d}szara2` no longer infinite-loop (skip stuck characters; avoid regex split in the hot path).
- Part A formal 0.95 rule still fails (0.9200); corpus build proceeds under the PI override in `docs/data_notes/cdli_id_decision.md`.
