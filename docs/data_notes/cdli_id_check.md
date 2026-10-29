# CDLI ID convention check

ATF P-number headers indexed: 135199
Sample size: 500 (seed 0, non-empty designation)

## PI amendment to Part A normalisation

In addition to the original exact compare (whitespace-normalised, case-insensitive), designations are also compared after: Unicode NFKC; mapping ’ ‘ ʼ ´ ` to '; collapsing whitespace; removing spaces before `, ; : )` and after `(`; stripping leading zeros from digit runs (`re.sub(r'\b0+(\d)', r'\1', s)`); casefold.

## Convention `id_text`

- Matched (candidate P in ATF): **200**
- Exact agreement: **169/200** (0.8450)
- Normalised agreement: **184/200** (0.9200)

10 example rows (exact / normalised):

| catalogue designation | ATF designation | exact? | normalised? |
| --- | --- | --- | --- |
| L'uomo 73 | L’uomo 73 | False | True |
| UET 5, 0792 | UET 5, 0792 | True | True |
| CDLI Seals 007946 (physical) | CDLI Seals 007946 (physical) | True | True |
| RIME 3/2.01.02.047 composite | RIME 3/2.01.02.47 composite | False | True |
| UTI 5, 3352 | UTI 5, 3352 | True | True |
| KKBullae 321 kt b/k 711 | KKBullae 321 kt b/k 711 | True | True |
| UM 29-16-552 | UM 29-16-552 | True | True |
| CUSAS 19, 031 | CUSAS 19, 031 | True | True |
| SAT 2, 0795 | SAT 2, 0795 | True | True |
| SNAT 370 | SNAT 370 | True | True |

## Convention `id`

- Matched (candidate P in ATF): **133**
- Exact agreement: **0/133** (0.0000)
- Normalised agreement: **0/133** (0.0000)

10 example rows (exact / normalised):

| catalogue designation | ATF designation | exact? | normalised? |
| --- | --- | --- | --- |
| NBC 04312 | TUT 190 | False | False |
| BM 111087 | CDLJ 2002/1 §09 | False | False |
| CDLI Seals 007946 (physical) | YOS 05, 070 | False | False |
| CBS 10726 | MVN 06, 027 | False | False |
| NBC 10110 | SAT 1, 266 | False | False |
| AO 19836 | CUSAS 03, 0453 | False | False |
| CDLB 2014/002 | FAOS 09/1, Lagash 04 | False | False |
| BE 06/1, 023 | BM Messenger 328 | False | False |
| K 08071 | RIME 3/1.01.06.04, ex. 330 | False | False |
| GCCI 1, 415  | UET 3, 0292 | False | False |

## Remaining `id_text` mismatches after normalisation

Count: **16**

| catalogue designation | ATF designation |
| --- | --- |
| CDLB 2014/002 | CDLJ 2014/003 |
| NTSŠ 0157 | NTSS 157 |
| AMT pl. 029 09 | AMT 29, 9 (Sm. 380) |
| AMT pl. 055 04 | AMT 55, 4 (K 13423) |
| CT 03, pl. 18, BM 014602 | CT 03, pl. 12, BM 014602 |
| STTI 1, 101 | STTI 101 |
| EEN 331, CBS 10767 | CBS 10767 |
| Anonymous 145434 | www ebay 023 |
| RINAP 3/2 Sennacherib 174, ex. 004 ? | RINAP 3/2 Sennacherib 174, ex. 01* |
| AMT pl. 002 06 | AMT pl. 002 06 (K 07744) |
| TSŠ 0619 | TSS 0619 |
| TCBI 2/1, 16 | Banca d'Italia 2/1, 16 |
| TCTI 3, 04929 | ITT 3, 04929 |
| Fs Cagni 1107-1109 01 | De Marcellis |
| EEN 329, HS 1662 | HS 1662 |
| HSS 68, 193 | SM 1911.10.048 |

## Decision

Formal 0.95 rule not met (`id_text` normalised=0.9200). **PI override:** `id_text` is the CDLI object key — see `docs/data_notes/cdli_id_decision.md`.
