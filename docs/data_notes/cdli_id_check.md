# CDLI ID convention check

ATF P-number headers indexed: 135199
Sample size: 500 (seed 0, non-empty designation)

## Convention `id_text`

- Matched (candidate P in ATF): **200**
- Designation agreement: **169/200** (0.8450)

10 example rows:

| catalogue designation | ATF designation | equal? |
| --- | --- | --- |
| L'uomo 73 | L’uomo 73 | False |
| UET 5, 0792 | UET 5, 0792 | True |
| CDLI Seals 007946 (physical) | CDLI Seals 007946 (physical) | True |
| RIME 3/2.01.02.047 composite | RIME 3/2.01.02.47 composite | False |
| UTI 5, 3352 | UTI 5, 3352 | True |
| KKBullae 321 kt b/k 711 | KKBullae 321 kt b/k 711 | True |
| UM 29-16-552 | UM 29-16-552 | True |
| CUSAS 19, 031 | CUSAS 19, 031 | True |
| SAT 2, 0795 | SAT 2, 0795 | True |
| SNAT 370 | SNAT 370 | True |

## Convention `id`

- Matched (candidate P in ATF): **133**
- Designation agreement: **0/133** (0.0000)

10 example rows:

| catalogue designation | ATF designation | equal? |
| --- | --- | --- |
| NBC 04312 | TUT 190 | False |
| BM 111087 | CDLJ 2002/1 §09 | False |
| CDLI Seals 007946 (physical) | YOS 05, 070 | False |
| CBS 10726 | MVN 06, 027 | False |
| NBC 10110 | SAT 1, 266 | False |
| AO 19836 | CUSAS 03, 0453 | False |
| CDLB 2014/002 | FAOS 09/1, Lagash 04 | False |
| BE 06/1, 023 | BM Messenger 328 | False |
| K 08071 | RIME 3/1.01.06.04, ex. 330 | False |
| GCCI 1, 415  | UET 3, 0292 | False |

## Decision

Neither convention reached agreement ≥ 0.95 on ≥ 100 matched rows. STOP after Part A.
