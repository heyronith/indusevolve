# CDLI inspection

## Header

Source: Cuneiform Digital Library Initiative (CDLI), github.com/cdli-gh/data at commit d66b12b, licence CC BY-NC-SA. Short excerpts reproduced for research documentation.

## Files

- `cdliatf_unblocked.atf`: 86897831 bytes, 3559111 lines; 135254 lines starting with `&P`.
- `cdli_cat.csv`: 154768722 bytes, 353284 lines (353283 data rows + 1 header).

## ATF sample

First 60 lines of `cdliatf_unblocked.atf`:

```
&P000001 = CDLI Lexical 000002, ex. 065
#atf: lang qpc
@tablet
@obverse
@column 1
$ beginning broken
1'. 1(N01) , [...]
>>Q000002 014
2'. 1(N01) , TIM ABGAL#
>>Q000002 015
3'. 1(N01) , KINGAL#
>>Q000002 016
@column 2
$ beginning broken
1'. 1(N01) , [...]
>>Q000002 030
2'. 1(N01) , GAL~a# UMUN2#
>>Q000002 031
3'. 1(N01) , GAL~a UMUN2 KU3~a
>>Q000002 032
@column 3
$ beginning broken
1'. 1(N01) , DUB~a SANGA~a#
>>Q000002 048
2'. 1(N01) , SUG5# SAG#
>>Q000002 049
3'. 1(N01) , UB SAG#
>>Q000002 050
@reverse
1. [N] , [...]
>>Q000002 colophon

&P000002 = CDLI Lexical 000002, ex. 066
#atf: lang qpc 
@tablet 
@obverse 
@column 1 
$ beginning broken 
1'. [1(N01)] , [...] 
>>Q000002 013 
2'. [1(N01)] , GAL~a# SZITA~a1 
>>Q000002 014 
3'. [1(N01)] , ABGAL# 
>>Q000002 015 
$ rest broken 
@column 2 
$ beginning broken 
1'. [1(N01)] , [...] NIM~a#? 
>>Q000002 023 
2'. 1(N01) , GAL~a SILA4~b 
>>Q000002 024 
3'. 1(N01) , GAL~a SZAB~a 
>>Q000002 025 
$ rest broken 
@column 3 
$ beginning broken 
1'. [1(N01)] , [...] 
>>Q000002 n 
$ rest broken 
@reverse 
```

## Catalogue overview

Data rows: 353283

Columns (in order):

1. `accession_no`
2. `accounting_period`
3. `acquisition_history`
4. `alternative_years`
5. `ark_number`
6. `atf_source`
7. `atf_up`
8. `author`
9. `author_remarks`
10. `cdli_collation`
11. `cdli_comments`
12. `citation`
13. `collection`
14. `composite_id`
15. `condition_description`
16. `date_entered`
17. `date_of_origin`
18. `date_remarks`
19. `date_updated`
20. `dates_referenced`
21. `db_source`
22. `designation`
23. `dumb`
24. `dumb2`
25. `electronic_publication`
26. `elevation`
27. `excavation_no`
28. `external_id`
29. `findspot_remarks`
30. `findspot_square`
31. `genre`
32. `google_earth_collection`
33. `google_earth_provenience`
34. `height`
35. `id`
36. `id_text2`
37. `id_text`
38. `join_information`
39. `language`
40. `lineart_up`
41. `material`
42. `museum_no`
43. `object_preservation`
44. `object_type`
45. `period`
46. `period_remarks`
47. `photo_up`
48. `primary_publication`
49. `provenience`
50. `provenience_remarks`
51. `publication_date`
52. `publication_history`
53. `published_collation`
54. `seal_id`
55. `seal_information`
56. `stratigraphic_level`
57. `subgenre`
58. `subgenre_remarks`
59. `surface_preservation`
60. `text_remarks`
61. `thickness`
62. `translation_source`
63. `width`
64. `object_remarks`

## Key columns

Columns whose lowercased name contains any of `object`, `genre`, `language`, `period`, `provenience`, `material`, `id_`:

### `accounting_period`

```
348815	''
20	Amar-Suen.07.00.00 to Amar-Suen.08.00.00
19	Šū-Suen.02.01.00 to Šū-Suen.02.12.00
19	Amar-Suen.05.01.00 to Amar-Suen.05.12.00
16	Amar-Suen.05.00.00 to Amar-Suen.06.00.00
13	--.--.01.00 to --.--.12.00
12	Šulgi.45.00.00 to Šulgi.46.00.00
12	Šū-Suen.04.01.00 to Šū-Suen.04.12.00
12	Ibbi-Suen.02.01.00 to Ibbi-Suen.02.12.00
12	00.00.11 to 00.00.01.00
11	Amar-Suen.04.00.00 to Amar-Suen.05.00.00
11	Amar-Suen.07.00.00 to Amar-Suen.09.00.00
10	Šulgi.48.00.00 to Amar-Suen.01.00.00
10	Šū-Suen.07.01.00 to Šū-Suen.07.12.00
10	Šū-Suen.09.00.00 to Ibbi-Suen.01.00.00
10	Šū-Suen.07.02.00 to Šū-Suen.07.12.00
10	Šū-Suen.03.01.00 to Šū-Suen.03.13.00 (intercalated)
9	Šulgi.42.00.00 to Šulgi.43.00.00
9	Amar-Suen.08.01.00 to Amar-Suen.08.12.00
9	Šū-Suen.01.01.00 to Šū-Suen.01.13.00 (intercalated)
9	Amar-Suen.07.01.00 to Amar-Suen.07.12.00
8	Amar-Suen.06.01.00 to Amar-Suen.06.12.00
8	Amar-Suen.01.01.00 to Amar-Suen.01.12.00
8	Šulgi.48.11.00 to Šulgi.48.12.00
8	Šū-Suen.03.00.00 to Šū-Suen.04.00.00
8	Amar-Suen.02.00.00 to Amar-Suen.03.00.00
8	00.00.04.00 to 00.00.06.00
7	Šū-Suen.06.01.00 to Šū-Suen.07.01.00
7	Amar-Suen.02.01.00 to Amar-Suen.02.12.00
7	Šū-Suen.06.01.00 to Šū-Suen.06.13.00
6	Šulgi.45.00.00 to Šulgi.47.00.00 (us2 year)
6	Amar-Suen.06.00.00 to Amar-Suen.07.00.00
6	Amar-Suen.01.02.00 to Amar-Suen.01.03.00
6	Šulgi.36.01.00 to Šulgi.36.12.00
6	Šū-Suen.03.01.00 to Šū-Suen.03.11d.00 (intercalated)
6	Šū-Suen.06.01.00 to Šū-Suen.06.12d.00 (intercalated)
6	Amar-Suen.01.01.00 to Amar-Suen.01.08.00
6	Ibbi-Suen.01.00.00 to Ibbi-Suen.02.00.00
6	Šū-Suen.04.00.00 to Šū-Suen.05.00.00 (us2 year)
6	Šū-Suen.09.00.00 to Ibbi-Suen.02.00.00
```

### `genre`

```
194555	Administrative
64520	''
22278	Royal/Monumental
16571	Legal
15846	Letter
9662	Literary
8149	Lexical
3988	Administrative ?
3896	School
3042	Omen
2793	uncertain
1947	Mathematical
1628	Astronomical
972	Prayer/Incantation
763	Scientific
725	administrative
420	Ritual
287	Lexical ?
230	fake (modern)
98	Literary ?
97	Letter ?
97	legal
87	Legal ?
78	Lexical; Mathematical
69	Lexical; Literary
63	School ?
55	Historical
54	Private/Votive
50	Literary; Mathematical
39	Other (see subgenre)
36	Mathematical ?
36	Royal/Monumental ?
36	letter
16	fake (modern) ?
14	Royal/Votive
12	Ritual ?
11	Votive
10	Uncertain
6	lexical
5	Lexical; School
```

### `google_earth_provenience`

```
353282	''
1	33.18870244 N  44.07743502 E
```

### `id_text2`

```
353283	0
```

### `id_text`

```
1	1
1	2
1	3
1	4
1	5
1	6
1	7
1	8
1	9
1	10
1	11
1	12
1	13
1	14
1	15
1	19
1	20
1	21
1	22
1	23
1	24
1	25
1	30
1	31
1	33
1	34
1	35
1	36
1	37
1	38
1	39
1	40
1	41
1	42
1	43
1	45
1	46
1	47
1	48
1	50
```

### `language`

```
139961	Sumerian
90176	''
84732	Akkadian
14669	Hittite
8493	undetermined
6871	Eblaite
2844	Sumerian; Akkadian
2702	Elamite
1107	Ugaritic
550	Sumerian ?
186	Egyptian ?
157	Akkadian ?
151	no linguistic content
138	Akkadian; Persian; Elamite
125	Persian
111	uncertain
85	Akkadian, Aramaic
55	Aramaic
25	Akkadian; Aramaic
15	Akkadian; Persian; Elamite; Egyptian 
11	Qatabanian
9	Greek
9	clay
8	Akkadian; Elamite
8	Akkadian; Elamite; Persian
7	Hebrew
5	Hurrian
4	Sumerian; Akkadian (pseudo)
4	Mandaic
3	Aramaic ?
3	Akkadian; Elamite; Persian; Egyptian
3	Akkadian; Persian
3	Egyptian
3	Luwian
3	Persian; Elamite; Akkadian
3	Persian, Babylonian
3	unclear
2	Akkadian; Egyptian
2	Hittite; Hurrian
2	uninscribed
```

### `material`

```
323306	clay
7909	stone
6608	stone ?
4734	''
3598	composite
1266	Clay
1063	stone: limestone
269	stone: lapis lazuli
253	metal: bronze
249	stone: alabaster
245	stone: diorite
234	stone: serpentine
228	stone: steatite
221	stone: calcite
196	stone: hematite
186	bone: ivory ?
179	soapstone
146	stone: marble
140	serpentine
125	stone: chlorite
125	gypsum: plaster
123	stone: haematite
82	chalcedony
73	Stone
69	limestone
69	hematite
65	stone: agate
62	shell
55	metal: copper
46	stone: basalt
46	faience
44	stone: chalcedony
44	glass
41	stone: jasper
41	marble
41	carnelian
40	jasper
37	bronze
34	stone: rock crystal
34	stone; soapstone
```

### `object_preservation`

```
327098	''
16458	fragment
5055	complete
2092	50%
1398	75%
518	nearly complete
264	--
162	incomplete
138	25%
48	fragmentary
32	pastiche
8	complete?
2	pastiche?
2	75 %
2	rim fragment
1	complete ?
1	Complete
1	tablet complete, case complete
1	.5
1	.75
1	2 rim+2 base fragments
```

### `object_type`

```
296949	tablet
15524	seal (not impression)
10519	other (see object remarks)
7194	tablet & envelope
5855	cone
4249	brick
3890	''
2290	tag
1884	bulla
1279	prism
1057	Tablet
1037	seal
673	cylinder
453	sealing
255	barrel
44	Cone
36	Tag
25	envelope
19	Brick
14	vessel
10	Seal (not impression)
7	prismatic cylinder
5	Bulla
5	vase
3	docket
2	Prism
1	block
1	tablet 
1	tablet in envelope
1	other
1	lentil
```

### `period`

```
110984	Ur III (ca. 2100-2000 BC)
66236	Old Babylonian (ca. 1900-1600 BC)
35478	Neo-Assyrian (ca. 911-612 BC)
22110	''
15633	Neo-Babylonian (ca. 626-539 BC)
14692	Middle Hittite (ca. 1500-1100 BC)
12704	Middle Babylonian (ca. 1400-1100 BC)
9974	Old Akkadian (ca. 2340-2200 BC)
8597	Early Old Babylonian (ca. 2000-1900 BC)
7111	Ebla (ca. 2350-2250 BC)
6452	Old Assyrian (ca. 1950-1850 BC)
5746	Achaemenid (547-331 BC)
4899	Uruk III (ca. 3200-3000 BC)
4646	Lagash II (ca. 2200-2100 BC)
4579	ED IIIb (ca. 2500-2340 BC)
4558	Middle Assyrian (ca. 1400-1000 BC)
3351	Hellenistic (323-63 BC)
1868	Neo-Babylonian (ca. 626-539 BC) ?
1867	ED IIIa (ca. 2600-2500 BC)
1848	Uruk IV (ca. 3350-3200 BC)
1729	Proto-Elamite (ca. 3100-2900 BC)
1164	ED I-II (ca. 2900-2700 BC)
1033	Neo-Elamite (ca. 770-539 BC)
847	uncertain
837	Middle Elamite (ca. 1300-1000 BC)
591	Old Babylonian (ca. 1900-1600 BC) ?
508	ED IIIb (ca. 2500-2340 BC) ?
298	Ur III (ca. 2100-2000 BC) ?
258	Neo-Babylonian (626-539 BC)
231	Early Neo-Babylonian (ca. 1150-730 BC)
224	Uruk V (ca. 3500-3350 BC) ?
219	Pre-Uruk V (ca. 8500-3500 BC)
217	Achaemenid (547-331 BC) ?
211	Old Akkadian (ca. 2340-2200 BC) ?
211	Middle Babylonian (ca. 1400-1100 BC) ?
194	Uruk V (ca. 3500-3350 BC)
186	Egyptian 0 (ca. 3300-3000 BC)
183	Neo-Assyrian (ca. 911-612 BC) ?
168	Old Assyrian (ca. 1950-1850 BC) ?
114	fake (modern)
```

### `period_remarks`

```
348237	''
1327	Classical Sargonic
553	Middle Elamite I
469	Sealand Dynasty
325	Mari period (Yasmah-Addu and Zimri-Lim)
277	Pre-Classical Sargonic
162	Pre-Sargonic 
153	Kadashman-Turgu
132	Diyala region
120	*before 2000 B.C.
113	check period!
92	period uncertain
73	Shagarakti-Shuriash
59	change to Uruk V ?, numerical tablet
58	Pre-Sargonic - Sargonic
51	shakkanakku period
43	Kudur-Enlil
42	Period uncertain.
40	loose token(s)
37	uncertain
37	Nazi-Maruttash
32	Sargonic
31	14th century
25	c. 1800
22	Diyala region ?
22	Middle Babylonian ?
21	Old Babylonian (late)
19	Alter Or 75, 93 n. 2: Ur III
19	--
19	Period uncertain
18	KISZ series
16	numerical tablet
15	Late MAss
13	?
13	from OB tablet
12	Not dated.
11	uncertain, dated to IV due to use of stylus shank divider in W 10613,f
11	changed from ED IIIb based on use of szunigin ligature
11	library of Tiglatpileser I
11	Ishme-Dagan
```

### `provenience`

```
54354	''
37045	Girsu (mod. Tello)
35342	Umma (mod. Tell Jokha)
27112	Nippur (mod. Nuffar)
26187	Nineveh (mod. Kuyunjik)
19703	uncertain (mod. uncertain)
16848	Puzriš-Dagan (mod. Drehem)
14519	Ḫattusa (mod. Boğazkale)
13422	Uruk (mod. Warka)
11023	Ur (mod. Tell Muqayyar)
9758	Mari (mod. Tell Hariri)
6893	Ebla (mod. Tell Mardikh)
6406	Assur (mod. Qalat Sherqat)
6025	Kanesh (mod. Kültepe)
4434	Sippar-Yahrurum (mod. Tell Abu Habbah)
4215	Susa (mod. Shush)
3577	Bābili (mod. Babylon)
2821	Adab (mod. Bismaya)
2683	Gasur/Nuzi (mod. Yorgan Tepe)
2583	Irisagrig (mod. uncertain)
2570	Kalhu (mod. Nimrud)
2245	Pārśa (mod. Persepolis)
2244	Sippar-Yahrurum (mod. Tell Abu Habbah) ?
2214	Ugarit (mod. Ras Shamra)
2018	Kish (mod. Tell Uhaimir)
1961	uncertain (mod. Babylonia)
1812	Larsa (mod. Tell as-Senkereh)
1750	Garšana (mod. uncertain)
1620	Umma (mod. Tell Jokha) ?
1314	Emar (mod. Tell Meskene)
1194	Isin (mod. Bahriyat) ?
1112	Ešnunna (mod. Tell Asmar)
1108	Girsu (mod. Tello) ?
1066	Isin (mod. Bahriyat)
954	Uruk (mod. Warka) ?
947	Šaduppum (mod. Tell Harmal)
883	Nerebtum (mod. Iščali)
883	uncertain (mod. northern Babylonia)
816	Šuruppak (mod. Fara)
757	Larsa (mod. Tell as-Senkereh) ?
```

### `provenience_remarks`

```
347161	''
482	Sin-kashid palace
479	Sealand
436	Selim
300	"Textes administratifs de la salle 5"
288	antiquities market
279	"Textes administratifs de la salle 110"
231	Ezida
203	Eanna
199	mu-iti
166	20111230 corrected firth
145	"du6-{d}en-lil2-la2", accd. to Allred and Owen near Nippur (mod. Nuffar)
141	Uncertain provenance.
139	modern Wilayah ?
133	Weitemeyer: "Sippar region"
122	Shu-ilisu archive
113	Syria
110	Luristan
88	CUSAS 35: Umma region
78	Adab
67	Aradmu
60	Umma archive.
57	Mesopotamia
50	was listed as Lagash; corrected R. Firth feedback 20111002
47	Larsa ?
40	Iran
40	Syria/Palestine
37	Umma region
35	ancient Tushan
35	Turkey
32	G--neydogu Anadolu B--lgesi, Turkey
31	Ninurta-MU-MU
31	Palace
30	purchased
30	Nabu Temple
27	was listed as Lagash
27	Shu-ilisu
23	Shulgisimtum archive
22	Shu-ilisu archive?
21	Nippur region
```

### `subgenre`

```
281454	''
18263	witness
8758	composite
7969	physical cylinder seal
4458	messenger text
1359	textiles
1040	medical
915	composite seal, royal
873	contract
809	pisan-dub-ba
773	gaba-ri
712	loan
588	diary
555	metal
541	extispicy
452	physical seal
315	sale
282	liturgy
260	animal tag
222	Liturgy
206	commentaries
193	Archaic Lu2 A (witness)
177	ETCSL 7.99 Unidentified texts (witness) (CHECK)
172	Obv: Syllabary B; Rev: Syllabary B
169	exercise
163	ETCSL 6.01.02 Proverbs Collection 02 (witness)
160	messenger
160	ETCSL 1.06.02 Ninurta’s Exploits (witness)
160	receipt
148	ledger
139	tabular account
139	incantation
139	bit asiri  flour
138	Obv: Model contract
136	physical seal, royal
127	Archaic Unidentified (witness)
123	problem text
122	field plan (drawing)
120	almanac
119	liturgy?
```

### `subgenre_remarks`

```
300576	''
632	letter (to the king)
480	votive inscription
353	astr omens
353	Messenger text (CBT 2)
334	Astronomical diary.
313	Messenger tablet
282	unclear
207	?
202	---
188	3 lines.
186	4 lines.
178	list
176	report astr 
172	oracle enquiry
161	barley
156	letter;
138	report astr
134	Astronomical diary
130	5 lines.
124	Messenger tablet.
120	metal
112	.
100	receipt
98	SM catalogue: messenger text--distribution of beer, bread etc
92	(UD.GAL.NUN).
90	6 lines.
89	2 lines.
88	3 lines
83	letter
83	2 lines
79	rit inc
78	barley.
76	rel
66	Written off
64	liver omens
63	SM catalogue: messenger text--distribution of beer, bread etc. 
63	loan of barley
62	4 lines
62	promissory note
```

### `object_remarks`

```
324243	''
7220	physical
6272	composite
3895	composite text
1839	unopened envelope
986	Object
709	lentil
640	slab, relief
409	vase
334	pierced for suspension
304	bowl
258	slab, unscupltured
239	stamp seal
237	door socket
212	vessel
174	block
165	stele
132	with token(s)
132	round tablet
113	envelope
109	statue
104	foundation tablet
104	mace head
95	jar stopper
81	jar
80	bead
79	kudurru
78	stone slab
73	brick stamp
64	paving stone
56	unclear
56	statuette
51	plaque
51	foundation canephor
51	disk
47	slab
46	arrowhead
45	Single-column
43	hand
42	ovoid-shaped
```

## Seal candidates

Catalogue rows where any Key column value contains `seal` or `bulla` (case-insensitive): **22691**

Breakdown by (column, value), sorted by count:

```
15524	object_type	seal (not impression)
7969	subgenre	physical cylinder seal
1884	object_type	bulla
1037	object_type	seal
915	subgenre	composite seal, royal
479	provenience_remarks	Sealand
469	period_remarks	Sealand Dynasty
453	object_type	sealing
452	subgenre	physical seal
239	object_remarks	stamp seal
136	subgenre	physical seal, royal
87	subgenre	physical stamp seal
50	subgenre_remarks	W/seal impressions;
38	subgenre_remarks	W/stamp seal impression
33	subgenre_remarks	W/seal impression
32	subgenre_remarks	W/seal impressions
28	object_remarks	triangular bulla
19	subgenre_remarks	Seal
19	subgenre_remarks	Seals
18	object_remarks	oval bulla
17	object_remarks	stamp seal (material from Ashmolean catalog: --)
14	subgenre_remarks	W/seal impressions; traces of strings inside
13	subgenre	physical  seal, royal
11	object_remarks	stamp seal (material from Ashmolean catalog: bronze)
11	subgenre_remarks	Uninscribed; seals
10	object_remarks	physical seal
10	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: steatite)
10	object_type	Seal (not impression)
9	object_remarks	cylindrical bulla
9	subgenre	physical seal, stamp
9	subgenre	sealing
8	object_remarks	stamp seal (Gable) (material from Ashmolean catalog: steatite)
7	object_remarks	physical cylinder seal
7	object_remarks	stamp seal (cowroid) (material from Ashmolean catalog: steatite)
7	object_remarks	stamp seal (material from Ashmolean catalog: steatite)
6	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: bluish chalcedony)
6	object_remarks	stamp seal (material from Ashmolean catalog: cornelian)
6	subgenre	bulla
5	object_remarks	cylinder seal
5	object_remarks	rounded bulla
5	object_remarks	stamp seal ( Carnelian seal (ring bezel) and impression (material from Ashmolean catalog: carnelian)
5	object_remarks	stamp seal ( Carnelian stamp seal (material from Ashmolean catalog: carnelian)
5	object_remarks	stamp seal (Low back gable) (material from Ashmolean catalog: steatite)
5	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: faience)
5	object_type	Bulla
5	subgenre	physical stamp seal ; figurine
5	subgenre_remarks	Administrative; seals; 3 lines
5	subgenre_remarks	Contract.  Seal impressions.
5	subgenre_remarks	Receipt; seals; 4 lines
5	subgenre_remarks	Seal impression
5	subgenre_remarks	Seal impression: a crescent & a horse
5	subgenre_remarks	W/seal impressions; linear inscription??
5	subgenre_remarks	sealed bulla
4	object_remarks	stamp seal (Carinated hemispheroid) (material from Ashmolean catalog: steatite)
4	object_remarks	stamp seal (Hemispheroid rosette) (material from Ashmolean catalog: faience)
4	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: green jasper)
4	object_remarks	stamp seal (garnet) (ring bezel) and impression (material from Ashmolean catalog: garnet)
4	object_remarks	stamp seal (material from Ashmolean catalog: chalcedony)
4	object_remarks	stamp seal (material from Ashmolean catalog: serpentine/steatite)
4	period_remarks	"Sealand Dynasty"
4	subgenre	physical cylinder seal, royal
4	subgenre_remarks	Administrative; seals; 2 lines
4	subgenre_remarks	Bulla for wool baskets.
4	subgenre_remarks	W/stamp seal impressions
4	subgenre_remarks	seal
4	subgenre_remarks	with seal impression
3	object_remarks	modern cast of a cylinder seal
3	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: steatite)
3	object_remarks	stamp seal (High hemispheroid) (material from Ashmolean catalog: steatite)
3	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: black serpentine)
3	object_remarks	stamp seal (scaraboid  (material from Ashmolean catalog: Egyptian blue' frit)
3	period_remarks	Ur III seal
3	subgenre	seal
3	subgenre_remarks	Administrative; seals; 2x3 lines
3	subgenre_remarks	Administrative; seals; 4 lines
3	subgenre_remarks	Business document.  Seal impressions.
3	subgenre_remarks	Business; seals; 2 lines
3	subgenre_remarks	Inscribed.  Seal impressions.
3	subgenre_remarks	Seal impression.
3	subgenre_remarks	Seals; 1 sign
3	subgenre_remarks	w/seal impression
2	object_remarks	stamp Seal (Scarab) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal ( Carnelian seal (rounded-face ring bezel) and impression (material from Ashmolean catalog: carnelian)
2	object_remarks	stamp seal (Ceramic stamp cone shaped (material from Ashmolean catalog: ceramic, part- or unglazed)
2	object_remarks	stamp seal (Conoid; eagle (material from Ashmolean catalog: amber glass)
2	object_remarks	stamp seal (Crystal seal (ring bezel) and impression (material from Ashmolean catalog: crystal)
2	object_remarks	stamp seal (Gable) (material from Ashmolean catalog: dark brown mica-schist)
2	object_remarks	stamp seal (Gable; and impression) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal (Hare) (material from Ashmolean catalog: faience)
2	object_remarks	stamp seal (Jasper stamp seal (material from Ashmolean catalog: jasper)
2	object_remarks	stamp seal (Loaf-shaped) (material from Ashmolean catalog: brownish green granular calcite)
2	object_remarks	stamp seal (Low ridge) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal (Metal Finger Ring) (material from Ashmolean catalog: bronze alloy)
2	object_remarks	stamp seal (Metal Finger Ring) (material from Ashmolean catalog: bronze)
2	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: milky chalcedony, brown-tinged)
2	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: streaked milky chalcedony)
2	object_remarks	stamp seal (Ovoid) with goat design (material from Ashmolean catalog: dark-grey serpentine)
2	object_remarks	stamp seal (Rolled stud) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: carnelian)
2	object_remarks	stamp seal (Scaraboid) impression (material from Ashmolean catalog: plaster)
2	object_remarks	stamp seal (Spherical Hittite) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: grey marble)
2	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal (Tubular loop) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal (material from Ashmolean catalog: stone)
2	object_remarks	stamp seal (scaraboid) (material from Ashmolean catalog: steatite)
2	object_remarks	stamp seal in the form of a double birds' head (material from Ashmolean catalog: copper alloy, cast)
2	object_remarks	stamp seal ring (material from Ashmolean catalog: bronze alloy)
2	object_remarks	stamp seal with linear design (material from Ashmolean catalog: metal)
2	provenience_remarks	Umma seal
2	provenience_remarks	based on seal
2	subgenre	ETCSL 5.07.a Public Announcement of Lost of Seal (witness)
2	subgenre	stringed bulla
2	subgenre_remarks	2 lines. Seal impression.
2	subgenre_remarks	3 lines. Seal impression.
2	subgenre_remarks	A stamp seal impression (potter's stamp?)
2	subgenre_remarks	Barley for sheep from Lu-Ningirsu to Íakuge; seal: Íà-kù-ge dubsar dumu Lú-kal-la (CBT 2)
2	subgenre_remarks	Barley from Lu-melam to Lu-Baba; seal: Lú-dBa-ba6 ds d. []
2	subgenre_remarks	Barley from Lugina; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
2	subgenre_remarks	Business; seal
2	subgenre_remarks	Business; seal; 3 lines
2	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.  Seal impressions only
2	subgenre_remarks	Contract.  The outer case of an inscribed clay.  Seal impressions. 1 line
2	subgenre_remarks	Contract.  The outer inscribed case of an inscribed clay.  Seal impressions only
2	subgenre_remarks	Date only; seals; 3 lines
2	subgenre_remarks	Date only; seals; 4 lines
2	subgenre_remarks	Forgery, cast from a mould of an Ur III tablet with seal impressions.
2	subgenre_remarks	Memorandum.  Seal impressions.
2	subgenre_remarks	Receipt of dead sheeps. Seal: Lu2-kal-la ds d. Ur-e11-e kuå7.
2	subgenre_remarks	Receipt of flour from temple of Enlil; seal; 5x8 lines; 4.1x3.4
2	subgenre_remarks	Receipt of various flours; seal
2	subgenre_remarks	Receipt; seal
2	subgenre_remarks	Receipt; seals
2	subgenre_remarks	Receipt; seals; 2 lines
2	subgenre_remarks	Receipt; seals; 3 lines
2	subgenre_remarks	Receipt; seals; 3x3 lines
2	subgenre_remarks	Remainder of an account of barley, transfered from Ur-dBa-ba6 to Ur-dEn-líl-lá; seal: Ur-dEn-líl-lá; ds d. Inim-sha6 kurushda
2	subgenre_remarks	SM catalogue: sealed tablet: expenditure of sheep
2	subgenre_remarks	SM catalogue: sealed tablet: receipt of sheep
2	subgenre_remarks	Sale of a slave girl Ša-at-d.Zikum-ma daughter of Na-na-a-tum for 12 shekel of silver from Du-da-nu-um and Na-a-na-tum by Sin-re-me-ni; giš.gan-na íb-ta-bal; Ninurta and Itur-Šamaš oath; sealed
2	subgenre_remarks	Seal impression only
2	subgenre_remarks	Seal impressions
2	subgenre_remarks	Seal impressions only;
2	subgenre_remarks	Seal impressions.
2	subgenre_remarks	Seal impressions;
2	subgenre_remarks	Sealed tablet.#
2	subgenre_remarks	Tag with seal
2	subgenre_remarks	Tag with uninscribed seal
2	subgenre_remarks	W/seal impression (pseudo-Kassite)
2	subgenre_remarks	W/seal impression;
2	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)8x(Rev)1 lines
2	subgenre_remarks	W/seal impressions; (Obv)3x(Rev)1 lines
2	subgenre_remarks	W/seal impressions; 4 lines
2	subgenre_remarks	W/seal impressions; cloth impression on Rev.
2	subgenre_remarks	With seal impressions;
2	subgenre_remarks	sealed account
2	subgenre_remarks	sealing on flat clay strip
2	subgenre_remarks	seals
1	genre	Pottery (seal)
1	object_remarks	Associated with bulla NCTU 18
1	object_remarks	Bulla associated with NCTU 19
1	object_remarks	Cappadocian Tablet with Seal Impression, clay 
1	object_remarks	Clay bulla with two stamp seals, of which one contains Aramaic writing
1	object_remarks	Five thumbmarks on L.E.; 3 seal impressions on U.E., one on L.E. and Lo. E.
1	object_remarks	Stamp Seal (Blunt-ended ovoid) (material from Ashmolean catalog: brown mottled, white marble)
1	object_remarks	Stamp Seal (Carinated hemispheroid) (material from Ashmolean catalog: brownish mica-schist)
1	object_remarks	Stamp Seal (Cone) (material from Ashmolean catalog: fired clay)
1	object_remarks	Stamp Seal (Gabled lentoid) (material from Ashmolean catalog: steatite)
1	object_remarks	Stamp Seal (Half-cylinder) (material from Ashmolean catalog: shell)
1	object_remarks	Stamp Seal (Hammer) (material from Ashmolean catalog: grey-streaked light-brown marble)
1	object_remarks	Stamp Seal (Oval conoid) (material from Ashmolean catalog: clouded dark-brown agate)
1	object_remarks	Stamp Seal (Ovoid) (material from Ashmolean catalog: brownish volcanic stone)
1	object_remarks	Stamp Seal (Scarab) (material from Ashmolean catalog: pale-green jasper)
1	object_remarks	Stamp Seal (Sliced 'conoid') (material from Ashmolean catalog: chalcedony)
1	object_remarks	The date was written first. Then the tablet was sealed. The rest of the text was written after that.
1	object_remarks	Two seal impressions on Lo.E. and one on L.E.; seal ring impression on U.E.
1	object_remarks	ancient clay cast of cylinder seal
1	object_remarks	bead, shape of seal
1	object_remarks	bulla ?
1	object_remarks	cast of a cylinder seal
1	object_remarks	conical seal or bead
1	object_remarks	cylinder seal (material from Ashmolean catalog: stone)
1	object_remarks	cylinder seal (row of three animals, apparently in linear outline, each perhaps having two heads on a common body) (material from Ashmolean catalog: steatite-type stone, with perforated knob on top)
1	object_remarks	cylinder seal depicting framed criss-cross, squatting figure above seated one, eight seated figures in offset arrangement and two eyes (material from Ashmolean catalog: brown, glazed clay)
1	object_remarks	cylinder seal with hero, goat, lion and seated figure on face and eagle above the bull on base (material from Ashmolean catalog: black serpentine)
1	object_remarks	cylinder seal with sidewise lion (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	cylinder seal, circle motifs (material from Ashmolean catalog: light grey-green calcite, slightly decomposed)
1	object_remarks	door sealing
1	object_remarks	drawing and seal impression at left side of lower reverse/upper edge
1	object_remarks	jar sealing
1	object_remarks	not sealed
1	object_remarks	physical; so-called "Adam and Eve" seal
1	object_remarks	round tablet (bulla ?)
1	object_remarks	seal impression only
1	object_remarks	seal impressions on upper reverse and on top edge; the latter is rolled upside down in relation to the writing
1	object_remarks	sealed at centre of lower obverse; for drawing see Baker, Nappahu no. 72
1	object_remarks	sealed on both left and right edges, with fingernail-marks on both upper and lower edges
1	object_remarks	sealed on left and right edges, with fingernail impressions on upper and lower edges; another set of fingernail impressions on lower left and lower right edges has been partially erased
1	object_remarks	sealed on left edge, with a marking next to the seal impression
1	object_remarks	sealed on left, upper, and right edges; lower edge is not preserved
1	object_remarks	sealed on lower obverse
1	object_remarks	sealed on lower reverse
1	object_remarks	sealed on lower reverse; for drawing see Baker, Nappahu no. 73
1	object_remarks	sealed on lower reverse; the join is indirect
1	object_remarks	sealed on middle of  left edge
1	object_remarks	sealed on the bottom of the obverse; for drawing see Baker, Nappahu no. 66b
1	object_remarks	sealed on the centre of the lower edge, with a drawing to the left of the sealing
1	object_remarks	sealed on upper obverse/top edge
1	object_remarks	sealed on upper obverse/upper edge
1	object_remarks	six-sided bulla
1	object_remarks	stamp Seal (Gable) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp Seal (High, thick, oval conoid) (material from Ashmolean catalog: bituminous shale)
1	object_remarks	stamp Seal (Looped conoid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal  (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal ( Calcite seal in the form of a reclining bull (material from Ashmolean catalog: calcite)
1	object_remarks	stamp seal ( Conoid shape stamp seal depicting a stylised tree (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal ( Duck shaped stamp seal depicting single-tasselled crescent-standard on a podium (material from Ashmolean catalog: brownish-red jasper-agate)
1	object_remarks	stamp seal ( Gable stamp seal with sheep between two gazelles (material from Ashmolean catalog: brownish black schist)
1	object_remarks	stamp seal ( High handle stamp seal with incised chevron design (material from Ashmolean catalog: brown-flecked, light steatite-type stone)
1	object_remarks	stamp seal ( Octagonal pyramid stamp seal (material from Ashmolean catalog: brownish chalcedony)
1	object_remarks	stamp seal ( Ovoid stamp seal depicting an antelope (material from Ashmolean catalog: brownish steatite-type stone)
1	object_remarks	stamp seal ( Ovoid stamp seal depicting man wielding 'daggers' above goats on either side (material from Ashmolean catalog: black stone, carved)
1	object_remarks	stamp seal ( Ovoid stamp seal with horned animal above a lion (material from Ashmolean catalog: brownish chloritic schist)
1	object_remarks	stamp seal ( Ring-seal with cruciform design of Bactrian monarch? (material from Ashmolean catalog: brown chalcedony)
1	object_remarks	stamp seal ( Sassanian stamp seal (material from Ashmolean catalog: bronwn stone)
1	object_remarks	stamp seal ( and impression) (material from Ashmolean catalog: stone (brown-mottled, smoky chalcedony))
1	object_remarks	stamp seal ('Neo-Assyria' seal, Scaraboid) (material from Ashmolean catalog: lapis lazuli)
1	object_remarks	stamp seal ('Neo-Assyria' seal, Scaraboid) (material from Ashmolean catalog: pink-and-brown mottled agate)
1	object_remarks	stamp seal ('Neo-Assyria' seal, Tabloid) (material from Ashmolean catalog: mottled dark-grey stone)
1	object_remarks	stamp seal ('Neo-Babylonian' seal, Oval concoid; star above symbols (material from Ashmolean catalog: bluish chalcedony; stone)
1	object_remarks	stamp seal ('Neo-Imperial' style seals (material from Ashmolean catalog: cement/plaster; soft stone)
1	object_remarks	stamp seal ('Scaraboid') (material from Ashmolean catalog: black limestone)
1	object_remarks	stamp seal ('Scaraboid') (material from Ashmolean catalog: black-and-white mottled marble)
1	object_remarks	stamp seal ('Scaraboid') (material from Ashmolean catalog: drab limestone)
1	object_remarks	stamp seal (Agate ring seal (material from Ashmolean catalog: agate (dark green)
1	object_remarks	stamp seal (Anthropomorphic back) (material from Ashmolean catalog: burnt steatite)
1	object_remarks	stamp seal (Back loop) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Back loop; and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Bead seal (material from Ashmolean catalog: black marble)
1	object_remarks	stamp seal (Bead seal (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (Bead seal (material from Ashmolean catalog: onyx)
1	object_remarks	stamp seal (Bearded male head shape) depicting kneeling male, one arm over outstretched wing (material from Ashmolean catalog: bronze)
1	object_remarks	stamp seal (Bezel) (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (Bezel; frieze of men, lions and goats (material from Ashmolean catalog: --)
1	object_remarks	stamp seal (Bezel; male and ram) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (Bezel; procession (material from Ashmolean catalog: limestone)
1	object_remarks	stamp seal (Bird) (material from Ashmolean catalog: faience, once glazed
1	object_remarks	stamp seal (Blunt-ended ovoid) (material from Ashmolean catalog: white marble)
1	object_remarks	stamp seal (Boot- or foot-shaped) and impression (material from Ashmolean catalog: light green talc-like stone)
1	object_remarks	stamp seal (Bronze pendant seal with warrior motif (material from Ashmolean catalog: copper alloy)
1	object_remarks	stamp seal (Bullock's(?) head with eye cavities; and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Button-shaped; and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Carinated hemispheroid) (material from Ashmolean catalog: dark brownish mica-schist)
1	object_remarks	stamp seal (Carinated hemispheroid) (material from Ashmolean catalog: pale yellow calcite, light streaked)
1	object_remarks	stamp seal (Carinated hemispheroid) (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Carinated lentoid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Carinated oval hemispheroid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Carinated oval lentoid stamp seal (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Carnelian seal (flat ring bezel) and impression (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (Carnelian seal ring and impression (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (Ceramic stamp (material from Ashmolean catalog: pottery)
1	object_remarks	stamp seal (Chalcedony seal (Dome, slightly oval) and impression (material from Ashmolean catalog: chalcedony (brown streaked light yellow)
1	object_remarks	stamp seal (Chalcedony seal (Dome, slightly oval) and impression (material from Ashmolean catalog: chalcedony (milky white streaked)
1	object_remarks	stamp seal (Chalcedony seal (dome) and impression (material from Ashmolean catalog: chalcedony (pale brown light streaked)
1	object_remarks	stamp seal (Chalcedony seal (rounded-face ring bezel) and impression)
1	object_remarks	stamp seal (Circular 'scaraboid'; horseback rider, arms lifted on either side, with rein on right, part of harness (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (Circular 'scaraboid'; worshipper before fish-tailed man, who holds a vase at his waist (material from Ashmolean catalog: blue chalcedony)
1	object_remarks	stamp seal (Circular boss) (material from Ashmolean catalog: glazed steatite)
1	object_remarks	stamp seal (Circular scaraboid) (material from Ashmolean catalog: pink and white marble)
1	object_remarks	stamp seal (Circular stalk on ovoid base; cross in linear border on top.  Design description: animal with long tail) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Circular; crescent-standard with single tassels between symbols (material from Ashmolean catalog: brown jasper)
1	object_remarks	stamp seal (Collared hemispheroid) (material from Ashmolean catalog: pale brown marble, dark speckled)
1	object_remarks	stamp seal (Collared hemispheroid; and impression) (material from Ashmolean catalog: red-brown marble)
1	object_remarks	stamp seal (Collared ovoid) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Concoid) (material from Ashmolean catalog: faience; bluish-green glaze)
1	object_remarks	stamp seal (Concoid) (material from Ashmolean catalog: faience; faded blue glaze)
1	object_remarks	stamp seal (Concoid) (material from Ashmolean catalog: faience; light-blue glaze)
1	object_remarks	stamp seal (Concoid) (material from Ashmolean catalog: faience; worn green glaze)
1	object_remarks	stamp seal (Concoid) (material from Ashmolean catalog: faience; worn light-green glaze)
1	object_remarks	stamp seal (Concoid) (material from Ashmolean catalog: green glass)
1	object_remarks	stamp seal (Conical plummet; antelope design) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Conoid seal with star, standing priest and altar (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Conoid stamp seal depicting standing antelope, line under mouth, irregular lines elsewhere in field (material from Ashmolean catalog: greenish steatite-type stone)
1	object_remarks	stamp seal (Conoid) (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Conoid) (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Conoid) (material from Ashmolean catalog: dark-brown marbly limestone)
1	object_remarks	stamp seal (Conoid) (material from Ashmolean catalog: green glass)
1	object_remarks	stamp seal (Conoid) (material from Ashmolean catalog: light greenish yellow limestone)
1	object_remarks	stamp seal (Conoid) (material from Ashmolean catalog: milky-brown chalcedony)
1	object_remarks	stamp seal (Conoid) with lion attacking rear of a boar, over two lines, star and crescent above (material from Ashmolean catalog: green glass; copper or bronze wire suspension loop)
1	object_remarks	stamp seal (Conoid; antelope with young beneath it, scorpion above, plant in front (material from Ashmolean catalog: dark brown composition)
1	object_remarks	stamp seal (Conoid; bull with head turned back, bird above it, plant in front) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Conoid; cross-hatched spade and stylus (material from Ashmolean catalog: baked clay)
1	object_remarks	stamp seal (Conoid; eagle (material from Ashmolean catalog: pale green glass)
1	object_remarks	stamp seal (Conoid; facing scorpion-man and scorpion-woman on line, lozenge-shape between them, crescent above (material from Ashmolean catalog: brown chalcedony)
1	object_remarks	stamp seal (Conoid; four globes separated by four dividers, fifth globe in centre (material from Ashmolean catalog: compact green serpentine with steatite-type inclusion
1	object_remarks	stamp seal (Conoid; hero between rampant animals with heads turned outwards; they look rather like lions (material from Ashmolean catalog: dark-blue glass)
1	object_remarks	stamp seal (Conoid; hero with sword or dagger stepping on rear and grasping horn base of winged ibex) (material from Ashmolean catalog: white limestone)
1	object_remarks	stamp seal (Conoid; man confronting lion (material from Ashmolean catalog: blue frit)
1	object_remarks	stamp seal (Conoid; recumbent antelope, head turned back, animal above (material from Ashmolean catalog: faience)
1	object_remarks	stamp seal (Conoid; roaring lions on either side of a tree (material from Ashmolean catalog: brownish-green faience)
1	object_remarks	stamp seal (Conoid; squatting Bes-figure (material from Ashmolean catalog: pale blue-green faience)
1	object_remarks	stamp seal (Conoid; uraei on either side of a tree (material from Ashmolean catalog: green faience)
1	object_remarks	stamp seal (Conoid; winged lion or lion-sphinx squatting (material from Ashmolean catalog: blue glass)
1	object_remarks	stamp seal (Conoidal 'pebble'; one animal above another, one side- wise (material from Ashmolean catalog: grey steatite-type stone)
1	object_remarks	stamp seal (Conoidal base) (material from Ashmolean catalog: grey limestone)
1	object_remarks	stamp seal (Conoidal) (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Crude loop handle; antelope motif) (material from Ashmolean catalog: speckled brownish steatite-type stone)
1	object_remarks	stamp seal (Cube) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Cubical seal or bead, jackal-headed figure) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Disk) (material from Ashmolean catalog: bituminous shale)
1	object_remarks	stamp seal (Disk) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Disk) (material from Ashmolean catalog: grey-brown limestone)
1	object_remarks	stamp seal (Disk; pierced by a piece of bronze wire ending in a loop;  (a) bull, spray before and above it; (b) bull above animal; spray before and above it (material from Ashmolean catalog: steatite-type stone; stone (worked rock)
1	object_remarks	stamp seal (Dome, slightly oval; and impression) (material from Ashmolean catalog: stone, chalcedony (brown))
1	object_remarks	stamp seal (Double axe pendant) (material from Ashmolean catalog: dark serpentine)
1	object_remarks	stamp seal (Double axe pendant) (material from Ashmolean catalog: pink limestone)
1	object_remarks	stamp seal (Dragon head bead) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Duck backed seal (material from Ashmolean catalog: glazed steatite)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting a fish (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting a goat (material from Ashmolean catalog: light-grey chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting a prancing gazelle over two lines (material from Ashmolean catalog: grey-banded milky agate)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting a tree (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting a tree (material from Ashmolean catalog: lapis lazuli)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting a worshipper between symbols (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting an oryx (material from Ashmolean catalog: light grey chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting bearded god in long open robe with six-pointed star behind (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting crescent above eight stars (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting crescent, cross of five drillings, reversed crescent, rudely carved (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting crescent-standard, with single tassels rendered by drill holes, on a podium (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting crescent-standard, with single tassels, on a podium (material from Ashmolean catalog: light-grey chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting crescent-standard, with single tassels, on a podium (material from Ashmolean catalog: mottled quartz)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting four-winged goddess on line (material from Ashmolean catalog: flecked white siliceous limestone)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting star-shaped device on a shaft (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting stylized winged creature set sideways (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Duck shaped stamp seal depicting two-winged deity in long open robe (material from Ashmolean catalog: light-yellow translucent chalcedony)
1	object_remarks	stamp seal (Electrotype of silver plating seal Tarkondemos seal) (material from Ashmolean catalog: silver plate, plaster)
1	object_remarks	stamp seal (Engraved pendant) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Eye of Horus seal
1	object_remarks	stamp seal (Fish-backed seal (material from Ashmolean catalog: glazed steatite)
1	object_remarks	stamp seal (Fist shape) depicting a seated winged sphinx, its tail held by standing man (material from Ashmolean catalog: light-green faience)
1	object_remarks	stamp seal (Fist shape) depicting male on one knee, on either side wings, perhaps fused with arms (material from Ashmolean catalog: bronze)
1	object_remarks	stamp seal (Fist) depicting a winged-lion (material from Ashmolean catalog: light blue-green jasper)
1	object_remarks	stamp seal (Fist) depicting two rampant, winged lions, grasping 'tree' between them (material from Ashmolean catalog: ivory, carved
1	object_remarks	stamp seal (Fist; depicting two ibexes with tree between them) (material from Ashmolean catalog: stained bone or ivory)
1	object_remarks	stamp seal (Flat-sided conoid) (material from Ashmolean catalog: glazed steatite, now yellow brown)
1	object_remarks	stamp seal (Flattened hemispheroid) (material from Ashmolean catalog: green-grey chlorite-schist)
1	object_remarks	stamp seal (Four-sided prism) (material from Ashmolean catalog: grey marble, light brown mottled at ends)
1	object_remarks	stamp seal (Fragment of a cowroid lower half of a standing figure?) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Fragment of ridged rectangle with thick base) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Gable stamp seal with a bird (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Gable stamp seal with antelope (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Gable stamp seal with crouching boar (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Gable stamp seal with lentoid profile and low carinated back (material from Ashmolean catalog: dark brown mica-schist)
1	object_remarks	stamp seal (Gable stamp seal, cross with thick centre; angled strokes in quadrangles (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Gable) (material from Ashmolean catalog: black schist)
1	object_remarks	stamp seal (Gable) (material from Ashmolean catalog: bronze (fine cast of a genuine gable seal?)
1	object_remarks	stamp seal (Gable; antelope, one or more strokes before it (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Gable; cross made up of four ibex heads, four gouges in field (material from Ashmolean catalog: brownish steatite-type stone)
1	object_remarks	stamp seal (Gable; horned animal with a second head springing from its chest (material from Ashmolean catalog: light steatite-type stone)
1	object_remarks	stamp seal (Gable; stag or possibly two schematic animals back to back) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Gable; two figures with forearm in common, one to left has stroke at waist, horned animal head between them (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Gabled lentoid) (material from Ashmolean catalog: dark brownish schist)
1	object_remarks	stamp seal (Half a reel-shaped stamp seal and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Half a scarab; half a bowman moving to right; hatched encircling border (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (Half-almond) (material from Ashmolean catalog: red veined, buff limestone)
1	object_remarks	stamp seal (Half-disk) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Hammer) (material from Ashmolean catalog: dark-brownish mica schist)
1	object_remarks	stamp seal (Hammer) (material from Ashmolean catalog: dark-grey marble)
1	object_remarks	stamp seal (Hammer-shape) with central skirted figure holding unidentified objects (material from Ashmolean catalog: grey-brown marble)
1	object_remarks	stamp seal (Hammer; spread-winged eagle and lion above crouching horned animal with branch before it) (material from Ashmolean catalog: red streaked, pale-brown marble)
1	object_remarks	stamp seal (Hammer; two spread-winged eagles above and behind crouching lion (material from Ashmolean catalog: marbled limestone)
1	object_remarks	stamp seal (Hare) (material from Ashmolean catalog: faience, once glazed)
1	object_remarks	stamp seal (Hedgehog ?) (material from Ashmolean catalog: dark grey serpentine)
1	object_remarks	stamp seal (Hedgehog-shape) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Hemispheroid rosette) (material from Ashmolean catalog: faience with traces of blue-green glaze)
1	object_remarks	stamp seal (Hemispheroid rosette) (material from Ashmolean catalog: faience; traces of pale greenish blue glaze)
1	object_remarks	stamp seal (Hemispheroid rosette) (material from Ashmolean catalog: white steatite-style
1	object_remarks	stamp seal (Hemispheroid stamp seal; possibly with two figures and a tree) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: dark grey limestone)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: dark veined, pale brown marble
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: pale brown limestone)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: pale brown marble)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: purplish brown serpentine)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: red flecked, light brown marble)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: speckled grey serpentine)
1	object_remarks	stamp seal (Hemispheroid) (material from Ashmolean catalog: speckled grey talc-schist)
1	object_remarks	stamp seal (Hemispheroid, gabled; profile mouflon and antelope heads, scorpion (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Hemispheroid; bull attacked from above and behind by lion; scorpion, crescent above; tree in front (material from Ashmolean catalog: light-mottled dark-brown limestone)
1	object_remarks	stamp seal (High back gable) (material from Ashmolean catalog: dark red serpentine)
1	object_remarks	stamp seal (High back gable) (material from Ashmolean catalog: light grey mica-schist)
1	object_remarks	stamp seal (High back gable) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (High back gable; with three gazelles) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (High conoidal base) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (High hemispheroid) (material from Ashmolean catalog: banded brown calcite)
1	object_remarks	stamp seal (High hemispheroid) (material from Ashmolean catalog: dark brown mica-schist)
1	object_remarks	stamp seal (High hemispheroid) (material from Ashmolean catalog: grey-brown mica-schist)
1	object_remarks	stamp seal (High oblong stem) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (High oval hemispheroid) (material from Ashmolean catalog: greyish mica-schist)
1	object_remarks	stamp seal (High oval hemispheroid; two horned animal heads on one side of common body (material from Ashmolean catalog: dark mottled, red-brown serpentine)
1	object_remarks	stamp seal (High ovoid; lion above antelope, scorpions in field (material from Ashmolean catalog: greyish-brown stone)
1	object_remarks	stamp seal (High scarab; quadruped, passant, with straight wing above and one more curved below, scorpion above (material from Ashmolean catalog: light-gray alabaster)
1	object_remarks	stamp seal (High scaraboid) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (High scaraboid) (material from Ashmolean catalog: pink-tinged limestone)
1	object_remarks	stamp seal (High scaraboid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (High scaraboid; goat passant (material from Ashmolean catalog: grey limestone, dark-streaked)
1	object_remarks	stamp seal (High scaraboid; horse passant, bird above (material from Ashmolean catalog: banded brown calcite)
1	object_remarks	stamp seal (High scaraboid; horse, scorpion above it, plant (material from Ashmolean catalog: light steatite-style stone)
1	object_remarks	stamp seal (High scaraboid; winged lion (material from Ashmolean catalog: burnt steatite)
1	object_remarks	stamp seal (Hittite hammer seal (material from Ashmolean catalog: haematite stone)
1	object_remarks	stamp seal (Hittite seal; and impressions) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Hittite stamp seal, priest at fire-altar (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Hittite; and impression) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (Human head shape) without design (material from Ashmolean catalog: bronze)
1	object_remarks	stamp seal (Human head; figure, galloping horse, plant and scorpion) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Human head; human figure in linear-marked robe; galloping quadruped, possibly horned or with filling motif above, plant and scorpion) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Irregular disk) (material from Ashmolean catalog: light brown alabaster)
1	object_remarks	stamp seal (Irregular disk; horned animal with head turned back) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Jasper seal (material from Ashmolean catalog: jasper (dark brown)
1	object_remarks	stamp seal (Joined foreparts of two birds) (material from Ashmolean catalog: bone)
1	object_remarks	stamp seal (Kidney-shaped hemispheroid) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Kidney-shaped hemispheroid) (material from Ashmolean catalog: yellow limestone)
1	object_remarks	stamp seal (Kidney-shaped hemispheroid; seated monkey-like animal with long tail holding vessel (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Knobbed conoid) (material from Ashmolean catalog: brown limestone)
1	object_remarks	stamp seal (Lentoid profile gable; face rounded parallel to perforation.  Design description: antelope; young below it, three strokes in field (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Loaf shape; central man with reversed animals on either side of him, three scorpions below (material from Ashmolean catalog: light-brown limestone)
1	object_remarks	stamp seal (Loaf-shaped ovoid) (material from Ashmolean catalog: faience or fired clay)
1	object_remarks	stamp seal (Loaf-shaped) (material from Ashmolean catalog: light brown limestone; dark-tinged)
1	object_remarks	stamp seal (Loaf-shaped; hero on one knee with a bow (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (Local Syrian Style stamp seal and impression (material from Ashmolean catalog: dark-grey serpentine)
1	object_remarks	stamp seal (Loop on crescent-shaped base) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Loop on three-lobed base; lion and two other animals (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Loop on truncated conoid; and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Loop-handled stamp seal (material from Ashmolean catalog: milky quartz)
1	object_remarks	stamp seal (Loop-handled) and impression (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Loop-topped conoid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low back gable stamp seal with three figures (material from Ashmolean catalog: dark grey-brown mica-schist
1	object_remarks	stamp seal (Low back gable stamp seal, possibly with a bird or bird above animal with head down (material from Ashmolean catalog: brownish steatite-type stone)
1	object_remarks	stamp seal (Low back gable) (material from Ashmolean catalog: brownish mica-schist)
1	object_remarks	stamp seal (Low back gable) (material from Ashmolean catalog: dark brown mica-schist)
1	object_remarks	stamp seal (Low back gable) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (Low back gable) and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low back gable: and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low back gable; and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low back gable; with antelope) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low conoid; horned animal, scorpion above it, plant in front (material from Ashmolean catalog: dark steatite-style stone)
1	object_remarks	stamp seal (Low conoidal) (material from Ashmolean catalog: dark green serpentine)
1	object_remarks	stamp seal (Low flat scaraboid stamp seal depicting horned animal followed by man with right arm raised (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (Low gabled hemispheroid) (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Low gabled hemispheroid) (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Low gabled hemispheroid; spiral in relief (material from Ashmolean catalog: light steatite-type stone)
1	object_remarks	stamp seal (Low hemispheroid) (material from Ashmolean catalog: brownish grey chert)
1	object_remarks	stamp seal (Low hemispheroid; an angle-filled cross (material from Ashmolean catalog: light flecked, brownish steatite-type stone)
1	object_remarks	stamp seal (Low oval conoid; human figure, stag, tree (material from Ashmolean catalog: dark-brownish schist)
1	object_remarks	stamp seal (Low oval hemispheroid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low ridge handle) and impression (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Low round sloping ridge) (material from Ashmolean catalog: glass, stone, composition)
1	object_remarks	stamp seal (Low truncated conoid; animal above scorpion and quadruped) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low truncated oval conoid; horse, scorpion above, plant in front, bird below) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low truncated pyramid; horned animal, scorpion above it, spray in front) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Low, roughly circular boss) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Lying bovid) (material from Ashmolean catalog: brown mottled, white marble)
1	object_remarks	stamp seal (Lying bovid) (material from Ashmolean catalog: green-black serpentine)
1	object_remarks	stamp seal (Lying bovid) (material from Ashmolean catalog: white limestone)
1	object_remarks	stamp seal (Metal Finger Ring) (material from Ashmolean catalog: gold)
1	object_remarks	stamp seal (Metal Finger Ring) (material from Ashmolean catalog: silver)
1	object_remarks	stamp seal (Middle Bronze Age 'Old Hittite' and impression) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Middle Bronze Age 'Old Hittite' stamp seal and impression (material from Ashmolean catalog: cement/plaster; soft stone)
1	object_remarks	stamp seal (Middle Bronze Age 'Old Hittite'; and impression) (material from Ashmolean catalog: silver)
1	object_remarks	stamp seal (Neo Hittite stamp seal, sphinx, dot below; inscription around it (material from Ashmolean catalog: brown and red mottled jasper-agate)
1	object_remarks	stamp seal (Oblong base topped by fist; depicting human figure in long robe, holding a scimitar) (material from Ashmolean catalog: white marble)
1	object_remarks	stamp seal (Oblong loop handle) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Octagonal pyramid stamp seal with symbols set on the back of a dragon recumbent on an altar, crescent above, standing worshipper (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: bluish chalcedony, streaked)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: brownish chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: brownish chalcedony, white-flecked)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: light-brown limestone)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: light-brown marbly limestone)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: mottled green serpentine)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: streaked bluish chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid) (material from Ashmolean catalog: yellowish chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid), worshipper;crescent above two symbols) (material from Ashmolean catalog: yellowish chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid;  'god in winged disk', with male head set on each end, held up by two bull-men, plant (sacred tree) between them (material from Ashmolean catalog: brownish chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid; 'tree' rendered in drilled blobs before rampant bull on line; crescent, radiate disk, and lozenge in field (material from Ashmolean catalog: blue chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid; bearded worshipper before spade and stylus on podium overlying recumbent animal; spray to left, crescent and star above (material from Ashmolean catalog: light-brown marble
1	object_remarks	stamp seal (Octagonal pyramid; between two stars, spade and stylus on podium; set over a dragon passant between two sprays (material from Ashmolean catalog: light-brown limestone)
1	object_remarks	stamp seal (Octagonal pyramid; hawk-headed men, walking one behind the other, line between them (material from Ashmolean catalog: green faience)
1	object_remarks	stamp seal (Octagonal pyramid; royal hero with dagger in combat with rampant lion (material from Ashmolean catalog: mottled white jasper)
1	object_remarks	stamp seal (Octagonal pyramid; royal hero with dagger in combat with rampant winged lion (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid; spade and stylus between two worshippers, winged-disk (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid; vertical stroke on three horizontals, human figure on either side, crescent above (material from Ashmolean catalog: brown-tinged, milky chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid; winged 'goat' passant, left front leg raised (material from Ashmolean catalog: milky-blue chalcedony)
1	object_remarks	stamp seal (Octagonal pyramid; winged hero in tunic wearing a helmet with curled back-piece, lifting two inverted animals, perhaps goats (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Originally hemispheroid) (material from Ashmolean catalog: dark brownish mica-schist)
1	object_remarks	stamp seal (Oval bezel) (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (Oval conoid) (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (Oval conoid) (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (Oval conoid) (material from Ashmolean catalog: milky chalcedony, brown-tinged)
1	object_remarks	stamp seal (Oval conoid) (material from Ashmolean catalog: milky yellowish chalcedony)
1	object_remarks	stamp seal (Oval conoid) (material from Ashmolean catalog: mottled greenish quartz)
1	object_remarks	stamp seal (Oval conoid) (material from Ashmolean catalog: pink-flecked creamy agate)
1	object_remarks	stamp seal (Oval conoid; crescent above star and plant) (material from Ashmolean catalog: yellowish chalcedony with brown flaw)
1	object_remarks	stamp seal (Oval conoid; inverted goat with hind leg held by royal hero, crescent above; four 'signs' set vertically between hero and beast (material from Ashmolean catalog: orange carnelian, white-and-red-banded) 
1	object_remarks	stamp seal (Oval conoid; rampant ibex looking back, its horn held by royal hero grasping dagger (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Oval conoid; royal hero lifting an inverted lion by the hind leg on either side of him) (material from Ashmolean catalog: rock crystal)
1	object_remarks	stamp seal (Oval conoid; royal hero lifting an inverted lion by the hind leg on either side of him) (material from Ashmolean catalog: streaked carnelian)
1	object_remarks	stamp seal (Oval conoid; two confronted monsters (head and feet of lion-griffin, human body) in kilts holding weapons (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Oval conoid; two crossed bulls, winged disk above, with inverted crescent over it) (material from Ashmolean catalog: yellowish chalcedony)
1	object_remarks	stamp seal (Oval conoid; worshipper. symbol on altar (material from Ashmolean catalog: banded agate, creamy blue to light brown)
1	object_remarks	stamp seal (Oval disk) (material from Ashmolean catalog: mottled green glass)
1	object_remarks	stamp seal (Oval disk) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Oval disk; (a) seated dog, crescent; (b) star, fish (material from Ashmolean catalog: black jasper)
1	object_remarks	stamp seal (Oval hemispheroid) (material from Ashmolean catalog: dark grey steatite-type stone)
1	object_remarks	stamp seal (Oval hemispheroid) (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Oval hemispheroid; animal above stag, angle, and two sprays in field (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Oval hemispheroid; scorpion design (material from Ashmolean catalog: light steatite-type stone)
1	object_remarks	stamp seal (Oval loop) (material from Ashmolean catalog: agate breccia)
1	object_remarks	stamp seal (Oval stamp seal depicting stag and spray (material from Ashmolean catalog: dark steatite-style stone)
1	object_remarks	stamp seal (Ovoid bevel; and impression) (material from Ashmolean catalog: stone, carnelian)
1	object_remarks	stamp seal (Ovoid pendant) (material from Ashmolean catalog: grey limestone)
1	object_remarks	stamp seal (Ovoid stamp seal (material from Ashmolean catalog: brown limestone, mottled light and red)
1	object_remarks	stamp seal (Ovoid stamp seal with two encircled dot eyes (material from Ashmolean catalog: grey limestone)
1	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: black and white mottled marble)
1	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: blue glass)
1	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: dark mica-schist)
1	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: light brown limestone; dark-tinged)
1	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ovoid) (material from Ashmolean catalog: yellow-brown serpentine)
1	object_remarks	stamp seal (Ovoid) with goat design (material from Ashmolean catalog: dark steatite)
1	object_remarks	stamp seal (Ovoid) with stag design (material from Ashmolean catalog: light-brown marble)
1	object_remarks	stamp seal (Ovoid; animal above bull, device below, stroke in field) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ovoid; central human figure, but with outspread chevron-decorated arms, small animal on either side (material from Ashmolean catalog: dark-grey serpentine)
1	object_remarks	stamp seal (Ovoid; cicada or similar insect) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (Ovoid; cross, scorpion and lion) (material from Ashmolean catalog: steatite-style stone, burnt)
1	object_remarks	stamp seal (Ovoid; gazelle with head turned back above reversed gazelle, spray between (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Ovoid; lion with head turned back above stag, (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Ovoid; male figure, one arm up and one down, sideways ibex on (material from Ashmolean catalog: dark-grey serpentine)
1	object_remarks	stamp seal (Ovoid; seated man, arms bent at elbows, hands raised; long curving line in front (material from Ashmolean catalog: brown-streaked white marble)
1	object_remarks	stamp seal (Ovoid; stag and scorpion motif (material from Ashmolean catalog: brownish steatite-type stone)
1	object_remarks	stamp seal (Ovoid; two stick-like human figures with tree between them) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ovoid; two twisted 'animals' over running antelope) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ovoid; with horse and ibex design) (material from Ashmolean catalog: steatite stone)
1	object_remarks	stamp seal (Pendant) (material from Ashmolean catalog: red limestone)
1	object_remarks	stamp seal (Plaster cast of stamp seal (material from Ashmolean catalog: plaster)
1	object_remarks	stamp seal (Pointed conoid) (material from Ashmolean catalog: faience)
1	object_remarks	stamp seal (Pointed conoid; man facing woman sitting on stool) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Pointed ovoid; snake above quadruped, confonted lions on other face) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ptah-Seker on a rectangular base cut with a seal design;  standing man with arms raised (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (Pyramidal back) and impression (material from Ashmolean catalog: dark green serpentine)
1	object_remarks	stamp seal (Ram's head) (material from Ashmolean catalog: shell)
1	object_remarks	stamp seal (Reclining animal) (material from Ashmolean catalog: bone)
1	object_remarks	stamp seal (Reclining animal) and impression (material from Ashmolean catalog: pink mottled, light brown marble)
1	object_remarks	stamp seal (Reclining boar) (material from Ashmolean catalog: white marble)
1	object_remarks	stamp seal (Reclining bovid(?)) (material from Ashmolean catalog: light green calcite)
1	object_remarks	stamp seal (Reclining bovid) (material from Ashmolean catalog: brownish yellow marble)
1	object_remarks	stamp seal (Reclining bovid) and impression (material from Ashmolean catalog: brown banded, greenish calcite)
1	object_remarks	stamp seal (Reclining dog) (material from Ashmolean catalog: faience, once glazed)
1	object_remarks	stamp seal (Reclining lion) (material from Ashmolean catalog: bone)
1	object_remarks	stamp seal (Reclining sheep(?)) (material from Ashmolean catalog: grey brown marble)
1	object_remarks	stamp seal (Rectangular;  (a) worshipper before a crescent over symbols; stylus and spade on podium; (b) bull over hatched area (c) lightning symbol on podium; (d) dot in crescent (material from Ashmolean catalog: grey-brown limestone)
1	object_remarks	stamp seal (Recumbent animal) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Recumbent bull) (material from Ashmolean catalog: banded agate, pale translucent and orange)
1	object_remarks	stamp seal (Reel-shaped) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Rib-handled ovoid) (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Rib-handled ovoid; star over winged disk with tail (material from Ashmolean catalog: milky chalcedony, brown-tinged)
1	object_remarks	stamp seal (Ridge handle (broken)) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ridge handle) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Ring seal with beaded head flanked by stars (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Ring-seal with bearded head wearing cap (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Ring-seal) (material from Ashmolean catalog: rock crystal)
1	object_remarks	stamp seal (RoIled stud; with a goat (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Rock crystal scaraboid; depicting youth with Corinthian helmet, lyre and cockerel) (material from Ashmolean catalog: rock crystal, gold)
1	object_remarks	stamp seal (Rolled stud; horse, bird above it, shrub (material from Ashmolean catalog: light steatite-style stone)
1	object_remarks	stamp seal (Round button of unbaked clay with low perforated loop and convex face) (material from Ashmolean catalog: unfired clay)
1	object_remarks	stamp seal (Round flat-topped stem) (material from Ashmolean catalog: buff fired clay)
1	object_remarks	stamp seal (Round stamp seal (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (Rounded back gable stamp seal with antelope (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Rounded back gable stamp seal with antelope (material from Ashmolean catalog: light steatite-type stone)
1	object_remarks	stamp seal (Rounded back gable) (material from Ashmolean catalog: dark grey mica-schist)
1	object_remarks	stamp seal (Rounded back gable) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Rounded pyramid) (material from Ashmolean catalog: mottled green and black serpentine)
1	object_remarks	stamp seal (Rounded tabloid; archer and antelope (material from Ashmolean catalog: brownish steatite-type stone)
1	object_remarks	stamp seal (Scarab backed) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Scarab seal, Harpocrates seated on a lotus plant, with flail and sceptre, flanked by standing protective goddesses (material from Ashmolean catalog: chalcedony; plaster)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: deep blue-green faience)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: faded blue glazed faience)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: greenish-blue glazed steatite)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: limestone)
1	object_remarks	stamp seal (Scarab) (material from Ashmolean catalog: pale-blue faience)
1	object_remarks	stamp seal (Scarab-backed seal (material from Ashmolean catalog: glazed steatite)
1	object_remarks	stamp seal (Scarabiod stamp seal, seated jackal (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (Scaraboid of blue-grey chalcedony depicting a seated Persian man (with Persian cap) approached by a woman (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Scaraboid sealstone with a cow suckling a calf (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: banded agate)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: branded agate, dark-brown with milky streak)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: brown ironstone)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: brown-flecked green serpentine)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: buff marble)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: clear bluish chalcedony)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: cloudy chalcedony)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: dark, streaked yellowish-green faience)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: dark-grey serpentine, mottled brown)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: faience; bronze loop attachment)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: greenish-blue faience)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: grey limestone)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: lapis lazuli, traces of bitumen
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: light chalcedony)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: mottled red jasper)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: orange-red limestone)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: pale greenish-blue faience)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: pink-tinged chalcedony)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: red limestone)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: red-brown limestone)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: stone: brown-and-yellow mottled agate)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: translucent yellowish chalcedony)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: yellow-brown limestone)
1	object_remarks	stamp seal (Scaraboid) (material from Ashmolean catalog: yellowish-green faience; bronze mounting wire)
1	object_remarks	stamp seal (Scaraboid; African face on back (material from Ashmolean catalog: light-green faience)
1	object_remarks	stamp seal (Scaraboid; a squatting baboon with disk head-dress on either side of elaborate altar, hatched segment below (material from Ashmolean catalog: amber glass)
1	object_remarks	stamp seal (Scaraboid; a uraeus-snake on either side of elaborate altar, linear border (material from Ashmolean catalog: blue glass)
1	object_remarks	stamp seal (Scaraboid; antelope speared by mounted horseman, linear border (material from Ashmolean catalog: green glass)
1	object_remarks	stamp seal (Scaraboid; archer, shooting from chariot drawn by horses, diminutive male in rear of chariot (material from Ashmolean catalog: milky-blue chalcedony)
1	object_remarks	stamp seal (Scaraboid; kneeling bull, linear border (material from Ashmolean catalog: pale green glass)
1	object_remarks	stamp seal (Scaraboid; kneeling man holding shield; linear border (material from Ashmolean catalog: bluish-green glass)
1	object_remarks	stamp seal (Scaraboid; recumbent lion (material from Ashmolean catalog: black serpentine; mottled green)
1	object_remarks	stamp seal (Scaraboid; stag passant (material from Ashmolean catalog: red serpentine with light mottling)
1	object_remarks	stamp seal (Scraboid; with mouflon and star design) (material from Ashmolean catalog: red-veined quartz)
1	object_remarks	stamp seal (Seal from Warren collection (material from Ashmolean catalog: metal)
1	object_remarks	stamp seal (Seal ring depicting a god flanked by lions and signs for --great-- and --prince-- in Hittite (material from Ashmolean catalog: gold)
1	object_remarks	stamp seal (Seal stamp, seated figure on stamp, swastikas (material from Ashmolean catalog: copper alloy)
1	object_remarks	stamp seal (Seal with Hebrew inscription, and impression, mounted on wood (material from Ashmolean catalog: cornelian)
1	object_remarks	stamp seal (Seal with loop shaped ring handle (material from Ashmolean catalog: iron)
1	object_remarks	stamp seal (Sealstone depicting a wild sow (material from Ashmolean catalog: porphyry)
1	object_remarks	stamp seal (Short cylinder handle stamp seal with linear design (material from Ashmolean catalog: metal)
1	object_remarks	stamp seal (Short, low ridge handle) (material from Ashmolean catalog: dark grey serpentine)
1	object_remarks	stamp seal (Single stone amulet) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (Single stone scrab amulet) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (Sitting dog; symbol on line, trace of worshipper's hand (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Sliced barrel; lion head) (material from Ashmolean catalog: red-veined, milky quartz)
1	object_remarks	stamp seal (Sliced barrel; star over winged disk with tail (material from Ashmolean catalog: banded quartz)
1	object_remarks	stamp seal (Sliced truncated 'conoid') (material from Ashmolean catalog: smoky chalcedony)
1	object_remarks	stamp seal (Slightly rounded conoid) (material from Ashmolean catalog: mottled green and black serpentine)
1	object_remarks	stamp seal (Sloping cylindrical Stud) (material from Ashmolean catalog: grey-flecked green serpentine)
1	object_remarks	stamp seal (Sloping cylindrical Stud) (material from Ashmolean catalog: light steatite)
1	object_remarks	stamp seal (Sloping cylindrical Stud) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Sloping ridge handle) (material from Ashmolean catalog: mica-schist)
1	object_remarks	stamp seal (Sloping ridge handle) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Small blunt-ended ovoid) (material from Ashmolean catalog: light brown limestone; dark-tinged
1	object_remarks	stamp seal (Small stone object with incised pattern) (material from Ashmolean catalog: stone, incised)
1	object_remarks	stamp seal (Square-based loop seal in duck shape depicting a winged bull) (material from Ashmolean catalog: yellowish-brown marbly limestone)
1	object_remarks	stamp seal (Squat oval conoid) (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (Stalk on oblong base; antelope) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Stalk) (material from Ashmolean catalog: burnt steatite)
1	object_remarks	stamp seal (Stalk; two seated human figures, table with loaves between them (material from Ashmolean catalog: brown-flecked steatite-style stone)
1	object_remarks	stamp seal (Stamp with handle (material from Ashmolean catalog: ceramic, part- or unglazed)
1	object_remarks	stamp seal (Stamp-cylinder seal with dancing figure on the face and bird with a crescent on the base (material from Ashmolean catalog: dark green steatite-type stone)
1	object_remarks	stamp seal (Stamp-seal depicting a winged horse (material from Ashmolean catalog: cornelian)
1	object_remarks	stamp seal (Steatite stamp seal (material from Ashmolean catalog: --)
1	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: black soapstone)
1	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: dark-brown ironstone)
1	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: light-brown limestone)
1	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: light-brown marble)
1	object_remarks	stamp seal (Stud) (material from Ashmolean catalog: light-yellow granular limestone)
1	object_remarks	stamp seal (Stud; antelope and sideways animal) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Stud; goat passant within a frame; two blobs and a star in the field (material from Ashmolean catalog: black stone)
1	object_remarks	stamp seal (Stud; griffin rampant (material from Ashmolean catalog: glazed frit)
1	object_remarks	stamp seal (Stud; horse with spray above it, scorpion in front, unidentified animal below) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Stud; human-headed male sphinx passant (material from Ashmolean catalog: burnt limestone)
1	object_remarks	stamp seal (Stud; lion above antelope) (material from Ashmolean catalog: steatite-type stone, with perforated knob on top)
1	object_remarks	stamp seal (Stud; two animals (material from Ashmolean catalog: brown-stained steatite-type stone)
1	object_remarks	stamp seal (Stud; winged creature above stag (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (Tabloid stamp seal, (A) bearded worshipper, arm raised, palm open facing single tasselled crescent- standard on podium; (B) radiate disk with central dot, bearded sphinx chouchant (material from Ashmolean catalog: limestone
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: bituminous shale)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: brown limestone)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: brownish-green steatite)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: dark grey serpentine)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: green-grey schist)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: light brown marble)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: orange-red limestone)
1	object_remarks	stamp seal (Tabloid) (material from Ashmolean catalog: speckled light grey talc)
1	object_remarks	stamp seal (Tabloid; enthroned figure before a table with offerings; figure squatting in front with its back to him (material from Ashmolean catalog: light-brown marble, dark mottling)
1	object_remarks	stamp seal (Tabloid; galloping bearded sphinx, wide-spread rear wing, front wing erect, creature (material from Ashmolean catalog: cuprous sulphide)
1	object_remarks	stamp seal (Tabloid; hero scene (material from Ashmolean catalog: grey-brown stone)
1	object_remarks	stamp seal (Tabloid; mouflons (material from Ashmolean catalog: glazed steatite)
1	object_remarks	stamp seal (Tabloid?) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (Tall conoid) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (Tall pyramid; lion, one foreleg raised) (material from Ashmolean catalog: reddish-brown limestone)
1	object_remarks	stamp seal (Tall sloping cylindrical stud; roaring 'lion', spray above and below (material from Ashmolean catalog: dark-brown steatite-type stone)
1	object_remarks	stamp seal (Thin ovoid) (material from Ashmolean catalog: dark grey steatite-type stone)
1	object_remarks	stamp seal (Thin, carinated rhomboid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Triangular, two faced seal with snake and letters) (material from Ashmolean catalog: terracotta)
1	object_remarks	stamp seal (Truncated conoid) (material from Ashmolean catalog: grey limestone)
1	object_remarks	stamp seal (Truncated conoid; horse with bird above it, plant in front, blob below) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Truncated oblong pyramid) (material from Ashmolean catalog: brown limestone)
1	object_remarks	stamp seal (Truncated oval conoid; floral motif (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (Truncated pyramid; lion, scorpion above, human figure in front) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (Truncated pyramidal 'pebble') (material from Ashmolean catalog: mottled pink and brown marble)
1	object_remarks	stamp seal (Truncated-conoidal oval base) (material from Ashmolean catalog: brownish-grey stone)
1	object_remarks	stamp seal (Vertically grooved oval base) depicting a gazelle (material from Ashmolean catalog: milky light-brown agate)
1	object_remarks	stamp seal (Vertically grooved oval base) depicting a goat in front of a tree (material from Ashmolean catalog: grey-brown marble)
1	object_remarks	stamp seal (Worn hammer; recut with bull passant on line, plant before it, crescent above. lozenge behind (material from Ashmolean catalog: dark-grey serpentine)
1	object_remarks	stamp seal (Worn scaraboid) with incised hieroglyphs (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (Zoomorphic back) (material from Ashmolean catalog: burnt steatite)
1	object_remarks	stamp seal (and impression) (material from Ashmolean catalog: stone, plaster)
1	object_remarks	stamp seal (bead) (material from Ashmolean catalog: stone: hard - part or un-glazed ceramic)
1	object_remarks	stamp seal (bronze) (material from Ashmolean catalog: copper alloy)
1	object_remarks	stamp seal (concoid shape) with antelopes (material from Ashmolean catalog: green glass; copper or bronze wire suspension loop)
1	object_remarks	stamp seal (conoid (material from Ashmolean catalog: green glass)
1	object_remarks	stamp seal (conoid depicting a bull (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (conoid depicting standing antelope (material from Ashmolean catalog: dark-grey schist)
1	object_remarks	stamp seal (conoid with crude interlocked lines (material from Ashmolean catalog: fired clay)
1	object_remarks	stamp seal (conoid with depiction of two gazelles with forefeet on either side of tree) (material from Ashmolean catalog: streaked brown-and-green faience)
1	object_remarks	stamp seal (cowroid (material from Ashmolean catalog: green glass)
1	object_remarks	stamp seal (cowroid (material from Ashmolean catalog: quartz)
1	object_remarks	stamp seal (depiction of antelope with crescent above) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (discoid; with crude mouflon) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (disk) (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (finger-ring; with Hittite inscription) (material from Ashmolean catalog: silver)
1	object_remarks	stamp seal (finger-ring; with lion) (material from Ashmolean catalog: silver)
1	object_remarks	stamp seal (finger-ring; with winged horse) (material from Ashmolean catalog: silver)
1	object_remarks	stamp seal (gable) (material from Ashmolean catalog: brownish grey steatite-type stone)
1	object_remarks	stamp seal (gable) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (gable; tethered antelop design) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (gabled lentoid) (material from Ashmolean catalog: pale green, brown bottled marble)
1	object_remarks	stamp seal (garnet) (ring bezel) and impression)
1	object_remarks	stamp seal (hedgehog) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (hemispheroid) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (hemispheroid; with a swirl of three pair of strokes) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (imperial Hittite and Impression) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (imperial Hittite and impression (material from Ashmolean catalog: cement/plaster; soft stone)
1	object_remarks	stamp seal (imperial Hittite and impression (material from Ashmolean catalog: metal, plaster)
1	object_remarks	stamp seal (imperial Hittite and impression) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (imperial Hittite and impression) (material from Ashmolean catalog: stone; plaster)
1	object_remarks	stamp seal (imperial Hittite; and Impression) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (imperial Hittites and Impressions (material from Ashmolean catalog: cement/plaster; soft stone)
1	object_remarks	stamp seal (imperial Hittites and Impressions) (material from Ashmolean catalog: steatite, plaster)
1	object_remarks	stamp seal (imperial Hittites and Impressions) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (imperial Hittites and Impressions) (material from Ashmolean catalog: stone; plaster)
1	object_remarks	stamp seal (imperial Hittites; and Impressions) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (linear design of ibex reclining with snake beneath) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (loop-topped conoid) (material from Ashmolean catalog: reddish brown serpentine-chipped)
1	object_remarks	stamp seal (material from Ashmolean catalog: baked clay)
1	object_remarks	stamp seal (material from Ashmolean catalog: bone)
1	object_remarks	stamp seal (material from Ashmolean catalog: ceramic)
1	object_remarks	stamp seal (material from Ashmolean catalog: copper alloy)
1	object_remarks	stamp seal (material from Ashmolean catalog: copper alloy, cast)
1	object_remarks	stamp seal (material from Ashmolean catalog: garnet)
1	object_remarks	stamp seal (material from Ashmolean catalog: garnet?)
1	object_remarks	stamp seal (material from Ashmolean catalog: glass)
1	object_remarks	stamp seal (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (material from Ashmolean catalog: metal, silver?)
1	object_remarks	stamp seal (material from Ashmolean catalog: red stone)
1	object_remarks	stamp seal (material from Ashmolean catalog: serpentine stone)
1	object_remarks	stamp seal (material from Ashmolean catalog: steatite stone)
1	object_remarks	stamp seal (material from Ashmolean catalog: stone, steatite)
1	object_remarks	stamp seal (material from Ashmolean catalog: white marble, worn; traces of green stain)
1	object_remarks	stamp seal (material from Ashmolean catalog: white quartz)
1	object_remarks	stamp seal (oblong) (material from Ashmolean catalog: dark steatite-type stone)
1	object_remarks	stamp seal (oval conoid stamp seal depicting antelope and spray (material from Ashmolean catalog: dark steatite-style stone)
1	object_remarks	stamp seal (oval conoid stamp seal depicting man holding a scorpion (material from Ashmolean catalog: red limestone)
1	object_remarks	stamp seal (oval conoid stamp seal depicting man set horizontally over back of bull (material from Ashmolean catalog: dull green stone)
1	object_remarks	stamp seal (oval conoid stamp seal depicting recumbant winged bull looking back, crescent above) (material from Ashmolean catalog: yellowish calcite)
1	object_remarks	stamp seal (oval conoid; depicting frontal bull head with bird) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (oval conoid; depicting tree with scorpion on either side) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (oval ring bezel; and impression) (material from Ashmolean catalog: stone, onyx (nicolo))
1	object_remarks	stamp seal (oval vonoid; spread-winged eagle above two feeding bulls) (material from Ashmolean catalog: rock crystal)
1	object_remarks	stamp seal (ovoid) (material from Ashmolean catalog: grey-brown limestone)
1	object_remarks	stamp seal (ovoid; with bearded god on throne with studded back, touching tree held by worshipper) (material from Ashmolean catalog: white glazed steatite-type stone)
1	object_remarks	stamp seal (ovoid; with snake above saluki?; above antelope with head turned back) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (pendant stamp seal depicting vulture attacking a recumbent horned animal (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (pendant; foot incised with two facing goats) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (reclining calf) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (ring  with stag, crescent and star (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (ring , hump-back bull in dotted border (material from Ashmolean catalog: --)
1	object_remarks	stamp seal (ring , hump-back bull surrounded by wreath (material from Ashmolean catalog: brown chalcedony)
1	object_remarks	stamp seal (ring) (material from Ashmolean catalog: stone, jasper (dark brown)
1	object_remarks	stamp seal (ring; human figure with diadem) (material from Ashmolean catalog: white chalcedony)
1	object_remarks	stamp seal (scarab) (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (scaraboid  (material from Ashmolean catalog: green glass)
1	object_remarks	stamp seal (scaraboid  (material from Ashmolean catalog: grey limestone)
1	object_remarks	stamp seal (scaraboid  depicting a fish hanging vertically and held by standing man, linear border (material from Ashmolean catalog: chalcedony)
1	object_remarks	stamp seal (scaraboid  depicting a horned animal (material from Ashmolean catalog: pink limestone)
1	object_remarks	stamp seal (scaraboid  depicting a human figure (material from Ashmolean catalog: mottled quartz and jasper)
1	object_remarks	stamp seal (scaraboid  depicting a man and bird above a quadruped (material from Ashmolean catalog: black-grey limestone)
1	object_remarks	stamp seal (scaraboid  depicting a running deer (material from Ashmolean catalog: blue to dark-green jasper)
1	object_remarks	stamp seal (scaraboid  depicting a squatting male figure with shield (material from Ashmolean catalog: brownish-yellow glass)
1	object_remarks	stamp seal (scaraboid  depicting a standing pharaoh in crown of Upper Egypt, moving to right, with shield and sword held across his head (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (scaraboid  depicting a winged griffin in apron with falcon head wearing Egyptian double crown (material from Ashmolean catalog: brown chalcedony)
1	object_remarks	stamp seal (scaraboid  depicting an ibex passant with crescent above (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (scaraboid  depicting belted hero, dot for back curl, skin over right shoulder, wielding club bow in left hand, skin under arm, linear border (material from Ashmolean catalog: pale brownish chalcedony) 
1	object_remarks	stamp seal (scaraboid  depicting bird, fan-like device above rear of bird, standing man in front facing bird, linear border (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (scaraboid  depicting bird, goat and archer (material from Ashmolean catalog: black jasper)
1	object_remarks	stamp seal (scaraboid  depicting bird, standing archer, disk in crescent above, linear border (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (scaraboid  depicting bull and snake (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (scaraboid  depicting curvilinear bulls tete-beche, head of one turned back, linear border (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (scaraboid  depicting driver in chariot with back-board, over heavy line (material from Ashmolean catalog: blue glass)
1	object_remarks	stamp seal (scaraboid  depicting four birds in a row followed by an ankh-sign; winged disk of unusual form above (material from Ashmolean catalog: red serpentine)
1	object_remarks	stamp seal (scaraboid  depicting four registers, alternate hatching, crosses in squares, chevrons, alternate hatching (material from Ashmolean catalog: green serpentine)
1	object_remarks	stamp seal (scaraboid  depicting four-winged scarab-beetle with hawk's head wearing Egyptian crown and with raised human arms, holding sun-disk in lower legs (material from Ashmolean catalog: chalcedony, tinged light bluish-buff
1	object_remarks	stamp seal (scaraboid  depicting four-winged scarab-beetle, star above, sun-disk below; offering stand and inscription (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid  depicting four-winged uraeus-snake with Egyptian crown with inscription (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid  depicting galloping horse with scorpion below; bird and floral device above (material from Ashmolean catalog: dark-grey schist)
1	object_remarks	stamp seal (scaraboid  depicting horse, bird above it, shrub on either side, scorpion below,  linear border (material from Ashmolean catalog: brownish steatite-type stone)
1	object_remarks	stamp seal (scaraboid  depicting horse, scorpion above, plant in front, bird below) (material from Ashmolean catalog: steatite-type stone)
1	object_remarks	stamp seal (scaraboid  depicting in registers ankh-sign, uraeus-snake with double lines above and below and two rows of inscription (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid  depicting lion walking beneath a crescent (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (scaraboid  depicting male worshipper, arm raised with palm open facing double tasselled crescent-standard set on podium (material from Ashmolean catalog: burnt pink limestone)
1	object_remarks	stamp seal (scaraboid  depicting man between two ostriches (material from Ashmolean catalog: dark grey stone)
1	object_remarks	stamp seal (scaraboid  depicting man with weapon, quadruped above) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid  depicting mirror, crescent, bisected lozenge, star and seven dots (material from Ashmolean catalog: haematite stone)
1	object_remarks	stamp seal (scaraboid  depicting ornamental tree between two kneeling human figures, each holding the adjacent volute on the tree; winged disk above (material from Ashmolean catalog: black serpentine) 
1	object_remarks	stamp seal (scaraboid  depicting radiate disk over eye lozenge, in front of a bearded worshipper with his arm raised, palm open (material from Ashmolean catalog: buff marble)
1	object_remarks	stamp seal (scaraboid  depicting reclining antlered deer, linear border) (material from Ashmolean catalog: amber glass)
1	object_remarks	stamp seal (scaraboid  depicting reversed-wing scarab, double horizontals, roaring lion walking to right (material from Ashmolean catalog: orange-red carnelian)
1	object_remarks	stamp seal (scaraboid  depicting seven-part rosette between triangular segments divided by double-lined compartments and two griffins (material from Ashmolean catalog: dark grey-green limestone)
1	object_remarks	stamp seal (scaraboid  depicting skirted lion passant, dot before it, bird above, double chevron behind, linear border (material from Ashmolean catalog: green serpentine)
1	object_remarks	stamp seal (scaraboid  depicting spread-winged bird below winged disk dividing face into two, above, a reversed design 'signs' in three vertical panels (material from Ashmolean catalog: blue glass)
1	object_remarks	stamp seal (scaraboid  depicting standing Isis offering breast to small standing Horus in the double crown of Egypt, with flail on shoulder, kilted male facing them (material from Ashmolean catalog: dark-green jasper
1	object_remarks	stamp seal (scaraboid  depicting standing male figure facing his right with pair of wings turned down, set on incised double lines (material from Ashmolean catalog: quartz)
1	object_remarks	stamp seal (scaraboid  depicting standing man in profile, arms raised above a floral motif on one side, scorpion on the other (material from Ashmolean catalog: pink-tinged, creamy yellow limestone)
1	object_remarks	stamp seal (scaraboid  depicting standing man, arms raised with a dagger in left hand; branch on one side, in profile possibly a scorpion on the other (material from Ashmolean catalog: red serpentine) 
1	object_remarks	stamp seal (scaraboid  depicting standing pharaoh in Red Crown, moving to left, holding a sceptre and stepping on uraeus (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid  depicting superimposed registers, bird on either side of life-sign over spread wings, man, on one knee, looking to his left, touching offering stand on either side (material from Ashmolean catalog: milky quartz; yellow- and brown-ti
1	object_remarks	stamp seal (scaraboid  depicting two hawks flanking a gazelle) (material from Ashmolean catalog: yellow limestone)
1	object_remarks	stamp seal (scaraboid  depicting two hawks, their double wings held forward, flanking ornamental tree, set on thick hatched line, two winged uraei (material from Ashmolean catalog: milky chalcedony)
1	object_remarks	stamp seal (scaraboid  depicting two men, heads in profile, wearing helmets (material from Ashmolean catalog: pink limestone)
1	object_remarks	stamp seal (scaraboid  depicting two monkeys climbing tree between them, linear border (material from Ashmolean catalog: obsidian)
1	object_remarks	stamp seal (scaraboid  depicting two opposed winged uraeus-snakes; inner wings raised, outer lowered, tails doubled over, encircling linear border (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid  depicting two seated double-winged lion sphinxes with human foreparts (material from Ashmolean catalog: glazed steatite, now white)
1	object_remarks	stamp seal (scaraboid  depicting two squatting monkeys with a tree between them (material from Ashmolean catalog: glazed steatite, now buff)
1	object_remarks	stamp seal (scaraboid  depicting winged and skirted sphinx moving to right, ankh-sign behind, star above altar in front (material from Ashmolean catalog: black and white banded stone)
1	object_remarks	stamp seal (scaraboid  depicting winged disk and Moabite inscription (material from Ashmolean catalog: milky quartz)
1	object_remarks	stamp seal (scaraboid  depicting winged sphinx moving to left, floral motif on front, life-sign under tail (material from Ashmolean catalog: mottled brownish chalcedony)
1	object_remarks	stamp seal (scaraboid  depicting winged sphinx with frontal apron moving to right, standing figure, body to front, head in profile (material from Ashmolean catalog: pink limestone)
1	object_remarks	stamp seal (scaraboid  in registers depicting two uraeus-snakes flanking an ankh-sign, spread-winged disk, scarab-beetle with upturned wings (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid  with Hebrew inscription (material from Ashmolean catalog: red jasper-agate)
1	object_remarks	stamp seal (scaraboid  with crude; ibex, open curve below (material from Ashmolean catalog: fired clay)
1	object_remarks	stamp seal (scaraboid  with depiction of horse (material from Ashmolean catalog: dark-grey serpentine)
1	object_remarks	stamp seal (scaraboid  with depiction of man with 'sceptre' in right hand, V-shaped object in left (material from Ashmolean catalog: banded onyx)
1	object_remarks	stamp seal (scaraboid  with depiction of passant goat (material from Ashmolean catalog: black steatite)
1	object_remarks	stamp seal (scaraboid  with inscription (material from Ashmolean catalog: bronze )
1	object_remarks	stamp seal (scaraboid  with inscription (material from Ashmolean catalog: mottled red jasper)
1	object_remarks	stamp seal (scaraboid  with recumbent goat (material from Ashmolean catalog: dark-brownish serpentine)
1	object_remarks	stamp seal (scaraboid  with winged griffin passant (material from Ashmolean catalog: brown limestone)
1	object_remarks	stamp seal (scaraboid  with winged sphinx passant) (material from Ashmolean catalog: yellowish chalcedony)
1	object_remarks	stamp seal (scaraboid 'Mouse-headed'; bird on post) (material from Ashmolean catalog: stone)
1	object_remarks	stamp seal (scaraboid ,  (a) two facing bearded men with daggers at waists, each raising cup, plant between them; (b) antelope with straight wing above and below (material from Ashmolean catalog: dark-green serpentine, mottled brown
1	object_remarks	stamp seal (scaraboid , a griffin, disk on head, on either side of a stylized tree) (material from Ashmolean catalog: altered limestone (now buff to dark-brown)
1	object_remarks	stamp seal (scaraboid , a kilted man in pointed head-dress on either side of a tall stand; cross above (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (scaraboid , archer on line; in front, goat with head turned back (material from Ashmolean catalog: olive-grey schist)
1	object_remarks	stamp seal (scaraboid , bearded male head, perhaps with helmet, in profile; Bes-head behind it; two lions' foreparts set back to back below (material from Ashmolean catalog: light blue-green jasper)
1	object_remarks	stamp seal (scaraboid , bearded man wearing dot-tipped sword and bow-case, holding a dotted ring (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid , bird (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid , bird of prey with serpent) (material from Ashmolean catalog: yellow-green chalcedony)
1	object_remarks	stamp seal (scaraboid , bull passant, bull's head in front of it, disk above (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (scaraboid , bull passant, reversed bird over back (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (scaraboid , central standing goddess with sun-disk head-dress, horizontally outspread wings holding lotus blossom on either side; uraeus on either side below wings (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , disk with drooping wings above urael, one on either side of a cartouche, topped by two feathers (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , enthroned goddess with disk head-dress, right hand held before face, left holding spear or sceptre, incense stand (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , falcon with disk head-dress, flail at shoulder (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (scaraboid , goat passant with triangular-shaped hatched tree above; ankh-sign in front (material from Ashmolean catalog: green serpentine)
1	object_remarks	stamp seal (scaraboid , hawk- (or falcon-)headed god, facing goddess wearing head-dress with disk between horns (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (scaraboid , hawk-headed figure (Horus) with sun-disk headdress facing two-winged protective deit, perhaps Isis, holding feathers; one wing up, one down, winged disk above (material from Ashmolean catalog: dark-green jasper
1	object_remarks	stamp seal (scaraboid , hero in long robe, left leg free, and conical head-dress, grasping rampant lion (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , hero with club in right hand, reversed lion in left, dog behind him (material from Ashmolean catalog: dark blue-black glass)
1	object_remarks	stamp seal (scaraboid , horizontal lines dividing face into four panels filled with 'chip' designs) (material from Ashmolean catalog: white marble)
1	object_remarks	stamp seal (scaraboid , ibex passant (material from Ashmolean catalog: red limestone)
1	object_remarks	stamp seal (scaraboid , ibex with head turned back, lion to rear, over circle, S-curve behind (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (scaraboid , janiform heads back to back;  African and bearded man, above them two rams' heads set back to back (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (scaraboid , kneeling nude female with long hair over shoulder, holding flower or bird (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (scaraboid , kneeling nude man, with long trident held behind him in right hand (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , lion passant (material from Ashmolean catalog: black glass)
1	object_remarks	stamp seal (scaraboid , lion, hatched double linear border (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , lioness mounting front of goring bull, snake over bull's tail, detached bull's head under belly (material from Ashmolean catalog: haematite)
1	object_remarks	stamp seal (scaraboid , merman, profile bearded head; frontal torso; arms upraised, lower body and tail of a fish with forked tail (material from Ashmolean catalog: light-green jasper)
1	object_remarks	stamp seal (scaraboid , nude hero with lion skin hanging down from right shoulder, club in left hand, reversed lion in right, star above (material from Ashmolean catalog: green jasper)
1	object_remarks	stamp seal (scaraboid , possibe traces of cartouches (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (scaraboid , prancing antelope or goat, peculiar head due partly to wear, partly to bad engraving, between two sprays (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (scaraboid , quadruped passant with drilled devices (material from Ashmolean catalog: faience or glass)
1	object_remarks	stamp seal (scaraboid , reclining antlered deer, linear border (material from Ashmolean catalog: glass)
1	object_remarks	stamp seal (scaraboid , recumbent lion, linear devices (material from Ashmolean catalog: pale-brown marble)
1	object_remarks	stamp seal (scaraboid , recumbent stag, fish or three interlocking wedges and 'eye' lozenge above animal (material from Ashmolean catalog: olive-grey limestone)
1	object_remarks	stamp seal (scaraboid , seated figure (material from Ashmolean catalog: carnelian)
1	object_remarks	stamp seal (scaraboid , small male in kilt (Horus; hair or wig in chignon(?). standing between protective goddesses, Isis and Nepphthys (material from Ashmolean catalog: dark-green jasper)
1	object_remarks	stamp seal (scaraboid , squatting female figure holding a lotus, probably Isis; standing kilted man with crooked sceptre on his shoulder (material from Ashmolean catalog: olive-green jasper)
1	object_remarks	stamp seal (scaraboid , squatting full-frontal Bes-figure holding an inverted scorpion on either side (material from Ashmolean catalog: brownish-green jasper)
1	object_remarks	stamp seal (scaraboid , squatting leonine creature with a Bes-head and outstretched wings, each terminating in the head of a bird of prey with horns; uraeus in front (material from Ashmolean catalog: brown-tinged, blue chalcedony)
1	object_remarks	stamp seal (scaraboid , stand or table over lap of a seated figure (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (scaraboid , stand or table, very stylized seated figure (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal (scaraboid , standing 'Egyptian' figure with Red Crown, arms raised, triangle in crescent above, on either side a spray above cartouche with garbled hieroglyphs (material from Ashmolean catalog: brown limestone;) 
1	object_remarks	stamp seal (scaraboid , standing goddess with palm frond before a vertical cartouche (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (scaraboid , standing worshipper, facing left, in 'Syrian' costume (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (scaraboid , vertical goat on either side of a tree, set on crudely hatched segment (material from Ashmolean catalog: dark-streaked, light-flecked, green serpentine)
1	object_remarks	stamp seal (scaraboid , winged lion, one foreleg raised; linear border (material from Ashmolean catalog: green glazed faience)
1	object_remarks	stamp seal (scaraboid , worshipper, symbols on altar (material from Ashmolean catalog: fired clay)
1	object_remarks	stamp seal (scaraboid , worshipper. in front of him a crescent over a star over a plant; behind him a squatting monkey facing away (material from Ashmolean catalog: mottled grey quartz)
1	object_remarks	stamp seal (scaraboid sealstone, galloping bull) (material from Ashmolean catalog: yellow smoky chalcedony)
1	object_remarks	stamp seal (scaraboid stamp seal, gazelle passant) (material from Ashmolean catalog: translucent bluish chalcedony)
1	object_remarks	stamp seal (scaraboid stamp seal, winged griffin passant (material from Ashmolean catalog: brown limestone)
1	object_remarks	stamp seal (scaraboid) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (scaraboid; depicting a quadaped animal) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; depicting bull, scorpion and branch) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; depicting cow with calf, spray in front) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; depicting four-winged male figure, arms extended behind wings, standing on double line) (material from Ashmolean catalog: rock crystal)
1	object_remarks	stamp seal (scaraboid; depicting lion in the centre facing left, quadruped set sideways, star and crescent in the field) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (scaraboid; depicting prancing goat with star above) (material from Ashmolean catalog: speckled grey serpentine)
1	object_remarks	stamp seal (scaraboid; depicting right-facing human-headed lion sphinx couchant over a spread-winged scarab-beetle) (material from Ashmolean catalog: sardonyx)
1	object_remarks	stamp seal (scaraboid; depicting semi-recumbent falcon-headed sphinx facing left, disk on head, skirted, standing on uraeus-snake) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; depicting semi-recumbent griffin facing right, wearing Red Crown and apron, life-sign before it) (material from Ashmolean catalog: sard)
1	object_remarks	stamp seal (scaraboid; depicting standing 'Egyptian' figure holding sceptre; ankh-sign in front, linear border, fan-shaped motif below figure) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; depicting two standing men grasping central stylized tree on double lines; spread-winged eagle or vulture; encircling linear border) (material from Ashmolean catalog: rock crystal) 
1	object_remarks	stamp seal (scaraboid; depicting upright bird, possibly an owl, flanked by row of chevron gouges on one side, spear on the other) (material from Ashmolean catalog: serpentine or steatite stone)
1	object_remarks	stamp seal (scaraboid; depiction of galloping horse, bird above it) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; lion couchant with bird above) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (scaraboid; man with bow above quadruped) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; two men, right arms raised, sideways horse) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (scaraboid; winged 'hero' holding inverted lion, standing on a ground line. Quiver visible between wings) (material from Ashmolean catalog: sard)
1	object_remarks	stamp seal (scaraboid; with depiction of goat) (material from Ashmolean catalog: yellow glass)
1	object_remarks	stamp seal (scaraboid; with lion motif and Ammonite inscription) (material from Ashmolean catalog: red-tinged, milky chalcedony)
1	object_remarks	stamp seal (sliced barrel; deer with head turned back) (material from Ashmolean catalog: veined, brownish chalcedony)
1	object_remarks	stamp seal (stud shaped stamp seal with depiction of antelope (material from Ashmolean catalog: black serpentine)
1	object_remarks	stamp seal (stud shaped; with stag motif) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (stud with recumbent stag) (material from Ashmolean catalog: white steatite)
1	object_remarks	stamp seal (stud with three unidentifiable animals) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (stud with winged creature) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (stud with winged sphinx wearing a flat cap (material from Ashmolean catalog: dark-grey serpentine)
1	object_remarks	stamp seal (tabloid shape; with depiction of winged lion) (material from Ashmolean catalog: steatite)
1	object_remarks	stamp seal (two crossed fish-tailed men) (material from Ashmolean catalog: red-brown serpentine)
1	object_remarks	stamp seal (winged horse (material from Ashmolean catalog: green stone)
1	object_remarks	stamp seal (winged, seated griffin with head turned back, one foreleg raised (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal (with )irregular criss-cross design) (material from Ashmolean catalog: serpentine)
1	object_remarks	stamp seal (with hero fighting rampant lion above recumbent lion (material from Ashmolean catalog: translucent light-green glass)
1	object_remarks	stamp seal (with straight-winged horned animal passant with head turned back) (material from Ashmolean catalog: white marble)
1	object_remarks	stamp seal (with winged roaring lion looking back, its young below) (material from Ashmolean catalog: white marble)
1	object_remarks	stamp seal (worshipper, symbols and lamp on altar, crescent above (material from Ashmolean catalog: bluish chalcedony)
1	object_remarks	stamp seal and impression (material from Ashmolean catalog: mica-schist stone)
1	object_remarks	stamp seal and impression, dancing figure (material from Ashmolean catalog: black limestone, plaster)
1	object_remarks	stamp seal depicting a reclining pig (material from Ashmolean catalog: dark mottled, pale brown marble)
1	object_remarks	stamp seal depicting lion with bird of prey above (material from Ashmolean catalog: dark brownish-red steatite-style stone)
1	object_remarks	stamp seal in the form of a bull lying upon its side (material from Ashmolean catalog: marble)
1	object_remarks	stamp seal in the form of a ram (material from Ashmolean catalog: brown-mottled, grey marble)
1	object_remarks	stamp seal in the form of debased Maltese cross (material from Ashmolean catalog: metal)
1	object_remarks	stamp seal in the form of reclining lion (material from Ashmolean catalog: bone)
1	object_remarks	stamp seal in the shape of a lion's head) (material from Ashmolean catalog: red streaked, pale brown marble)
1	object_remarks	stamp seal set in finger-ring with depiction of standing warrior with bow on back and spear in hands (material from Ashmolean catalog: bronze)
1	object_remarks	stamp seal with displayed eagle (material from Ashmolean catalog: amber glass)
1	object_remarks	stamp seal with linear with linear design (material from Ashmolean catalog: metal)
1	object_remarks	stamp seal with ridge handle (material from Ashmolean catalog: faience)
1	object_remarks	stamp seal with tre-foil volute (material from Ashmolean catalog: metal)
1	object_remarks	stamp seal with tree, hero grasping tail of lion rampant over goat (material from Ashmolean catalog: fired clay)
1	object_remarks	stamp seal with whirl design (material from Ashmolean catalog: metal)
1	object_remarks	stamp seal, hammar back pierced for suspension, circular with central quadrant design (material from Ashmolean catalog: bronze)
1	object_remarks	stamp seal, ibex passant; plant in front, possibly a uraeus (material from Ashmolean catalog: Egyptian blue' frit)
1	object_remarks	stamp seal, lion passant with crescent above (material from Ashmolean catalog: bronze)
1	object_remarks	stamp seals (Turkey, Early Bronze Age (material from Ashmolean catalog: cement/plaster - copper, silver and gold and alloys)
1	object_remarks	stamp seals-Turkey, Early Bronze Age (material from Ashmolean catalog: metal)
1	object_remarks	stamp-seal (material from Ashmolean catalog: serpentine)
1	object_remarks	two seal impressions and a drawing on the lower obverse and another drawing on the left edge
1	object_remarks	uncertain if seal
1	object_remarks	very large seal
1	period_remarks	"Sealand dynasty"
1	period_remarks	bulla
1	provenience_remarks	Drehem seal; Nippur calendar
1	provenience_remarks	Nippur month name, Umma seal
1	provenience_remarks	Ozaki: Garszana text according to its seal inscription
1	provenience_remarks	Umma seal, Drehem calendar; 01m = iti masz2-ku3-gu7 min, unique instance so declared school
1	provenience_remarks	cf. P291177 etc. naming ugula da-du-mu and sealed by lugal-e2-mah-e dumu lugal-ku3-ga-ni
1	provenience_remarks	given as Umma in catalogue, but seal suggests Girsu
1	provenience_remarks	legend, not seal (Zs. Földi)
1	provenience_remarks	mn Girsu form, but seal said to be Umma
1	provenience_remarks	the legend,  not the seal itself (Zs. Földi)
1	subgenre	"physical stamp seal ; zegelring"
1	subgenre	ETCSL 5.07.a Public Announcement of Lost of Seal (composite)
1	subgenre	ETCSL 5.07.a Public Announcement of Lost of Seal (witness) ?
1	subgenre	ETCSL 5.07.a Public Announcement of Lost of Seal (witness); model contract
1	subgenre	Pottery (seal)
1	subgenre	Seal impression
1	subgenre	Sealing
1	subgenre	cylinder seal
1	subgenre	land sale; seals
1	subgenre	physical stamp seal ; sieraard ; ketting
1	subgenre	physical stamp seal ?
1	subgenre_remarks	(Obv)10x(Rev)7 lines, seal impressions, nail mark, inked Aramaic docket on Rev?, 5.5x6.8x2.6
1	subgenre_remarks	(Obv)10x(Rev)8 lines, seal & nail impressions, 4.81x5.78x2.2
1	subgenre_remarks	(Obv)11x(Rev)6 lines, seal impressions on edges, * pub.-/-/acc.
1	subgenre_remarks	(Obv)11x(Rev)7 lines, seal & nail impressions & signatures, 6.15x7.45x2.65
1	subgenre_remarks	(Obv)12x(LoE)2x(Rev)10 lines, seal impressions on UE.& RE., nail impression on LoE., 5.9x7.6x3
1	subgenre_remarks	(Obv)13x(Rev)6 lines, labels on edges, seal & nail impressions, 8.1x6.85.2.8
1	subgenre_remarks	(Obv)14x(Rev)16x(UE)2 lines. Seal impressions on all the surfaces.
1	subgenre_remarks	(Obv)15x(Rev)15 lines, labels on edges, seal impressions, 7.65x7.45x3.2
1	subgenre_remarks	(Obv)17x(Rev)18x(UE)1 lines; w/seal impressions
1	subgenre_remarks	(Obv)19x(Rev)17 lines, seal impressions on Obv,Rev,UE & LE.
1	subgenre_remarks	(Obv)7x(Rev)6 lines, seal impressions, label on UE.
1	subgenre_remarks	(Obv)9x(LoE)2x(Rev)7x(UE)1x(LE)2 lines; faint seal impression on Obv.Lo.part.
1	subgenre_remarks	(Obv)9x(Rev)6 lines, seal impressions, nail impression, signatures on edges, 5.6x7.1x2.85
1	subgenre_remarks	(Obv)seal(?) impression; Cf. Peters Cat. 595.
1	subgenre_remarks	* of quartz, for the use of cylinder seal
1	subgenre_remarks	*16293 to 16291: cylinder seal
1	subgenre_remarks	*16859 to 16868: cylinder seals without inscription
1	subgenre_remarks	*16875 to 16904:cylinder seal, without inscription
1	subgenre_remarks	*17722 to 17747: cylinder seals without inscription
1	subgenre_remarks	*17749 to 17752: cylinder seal without inscription
1	subgenre_remarks	*17760 to 17786: cylinder seals without inscription
1	subgenre_remarks	*19246 to 19428: cylinder seals without inscription
1	subgenre_remarks	*19421 to 19424: cylinder seals without inscription
1	subgenre_remarks	*19514 to 19517: cylinder seals without inscription
1	subgenre_remarks	*19519 to 19529: cylinder seals without inscription
1	subgenre_remarks	*19534 to 19536: cylinder seals without inscription
1	subgenre_remarks	, from A-gu, kiszib lugal-e-ba-an-sza6 sza3 bala seal: lugal-e2-ba-an-sza6
1	subgenre_remarks	0;2.0. nì-àr-ra lugal má-ú-da ki Lú-dNin-shubur-ta kishib Ur-dIg-alim; seal: Ur-dIg-alim ds d. Lú-dNin-gír-su.
1	subgenre_remarks	1 amar-giå kù transferred from Lu-Utu to Ur-Baba (CBT 2). A: Case of 18211; seal: Ur-∂Ba-ba6 dubsar dumu ∂Utu-mu sa12-du5 urub.ki-ka (CBT 2)
1	subgenre_remarks	1 goat taken in charge; seals; 5x6 lines
1	subgenre_remarks	1 gú ú-sa sig5 from Ur-Hendursag to Anana; seal: Ir3-ra-ba-ni ir11 Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	1 line; seal impr.
1	subgenre_remarks	1 line; seals
1	subgenre_remarks	1 ma-na sù-gan ki Nì-ga-ta Ur-dNin-gis-zi-da shu-ba-ti; seal: Ur-dNin-gis-zi-da simug d. A2-zi-da; metal
1	subgenre_remarks	1 ring(?) seal impr of god in crescent & 2 horses or 2-headed horse; traces of cord; sm holes on r. & l. sides
1	subgenre_remarks	1 seal impr; trace of cord; small holes on u. & lo. sides
1	subgenre_remarks	1 seal impr; traces of cord; sm. holes on 2 sides
1	subgenre_remarks	1 sign; w/seal impression
1	subgenre_remarks	1 stamp seal impr of 3 winged animals around a center circle; holes on 2 sides
1	subgenre_remarks	1 stamp seal impr of hero holding 2 antelopes; traces of cord; sm holes on u. & lo. ends
1	subgenre_remarks	1 stamp seal impr of horse & crescent (= CBS 4013); traces of cord; sm holes on r. & l. ends
1	subgenre_remarks	1 stamp seal impr of horse & crescent; trace of cord; holes on r. & l. sides
1	subgenre_remarks	1 stamp seal impr of quadruped; trace of cord; sm holes on r. & l. ends
1	subgenre_remarks	1 stamp seal impr, almond shaped, completely effaced; holes on r. & l. ends
1	subgenre_remarks	1 stamp seal impr; small holes on r. & l. sides
1	subgenre_remarks	1 stamp seal impr; traces of cords; small holes on u. & lo. sides
1	subgenre_remarks	1.0.0 brooms, nì-ki-luh from Ur-ab-ba to Ur-èsh-kù-ga; seal: Ur-èsh-kù-ga ds d. Ab-ba-gi-na
1	subgenre_remarks	10 gur of barley from Bazi to the é-duru5 dInanna; seal: Lugal-síg-sud4 ds d. Ur-dLama.
1	subgenre_remarks	10 gurush for irrigation work; kun dNa-rú-a-igi-du mu SHà-lá-súd-shè; seal: Lú-dNa-rú-a d. SHà-lá-súd
1	subgenre_remarks	10 gín of silver for the bala received by Ur-sha6-ga from A-gi4; seal: Ur-sha6-ga d. ›-ki dam-gàr
1	subgenre_remarks	10 lá 1 pisan im-sar im a-shà-ge lugal-ta búr-da gá-gá-dè ki Lú-dNin-gír-su dumu Ba-zi-ta mu sa12-du5-shè kishib Lú-dNin-gír-su dumu Ur-dBa-ba6 dumu Igi-ziseal: Lú-dNin-gír-su ds dumu Ur-dBa-ba6
1	subgenre_remarks	1050 gur of old barley from Bazi to Lu-Ningirsu for the use of Ur-Nanshe; seal: Lú-dNin-gír-su ds d. Ur-dNanshe.
1	subgenre_remarks	11 gín of silver for the bala received by Nì-ga from Ir11; [seal]
1	subgenre_remarks	12 ashgab-du10 0;1. dabin-lugal-ta ki sukkal-mah gìr dNanna-ì-gi sukkal; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	13x3x15x3(u.e.) lines; 9.55x5.7x2.8 cm (Case= seals; s; 9.95x6.6x3.1 cm)
1	subgenre_remarks	16;1.0. gur má Nì-ú-rum-ta kiåib Ma-an-né; seal: Ma-ni sagi ∂Gù-dé-a dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	17x22x5(u.e.) lines; 11.8x6.5x4.6 cms; seals
1	subgenre_remarks	1800 ùkush 5 dusu geshtin duru5 10 sìla-ta gìr Ur-mes; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	1912 7-6 30 4 col. mu ma2 ∂Enki. seal: Lugal-ni3-lagar-e. dub-sar. dumu Da-da. rations of some kind for a number of persons
1	subgenre_remarks	1912 7-6 55 4 col. guruå for field work. mu Haråi§, seal: E2-agl-e-si. dub-sar dumu Lu2-d[...]
1	subgenre_remarks	1913 4-16 911 4 col.. seal: Nimgir-an-ne2. dub-sar dumu Inim-d.[  ]  mu a-ra2 2-kam Åa-aå-ru-um§. Work in fieldub-sar
1	subgenre_remarks	1913 4-16 913 4 col. seal: Åa3-nin-ga2. dub-sar. dumu Lugal-nanaga. travail des champs
1	subgenre_remarks	2 goats al-dar á-giå-gar-ra muåen-dù; seal: Ka-làl dubsar dumu Lugal-[] (CBT 2)
1	subgenre_remarks	2 lines.  Seal impression.
1	subgenre_remarks	2 lines; seal impr.
1	subgenre_remarks	2 lines; seals
1	subgenre_remarks	2 same seal impressions w/inscription (5 lines)
1	subgenre_remarks	2 same stamp seal impressions on rev.; (Obv)13x(Rev)5 lines.
1	subgenre_remarks	2 seal impr; sm holes on 2 sides
1	subgenre_remarks	2 seal impressions of a same cylinder seal impressed like a stamp seal
1	subgenre_remarks	2 seal imprs
1	subgenre_remarks	200 gur of barley loaden on boats for Nippur, from Bazi to Bur-Mama; seal: Bur-Ma-ma d. Pàd-da-a sanga []
1	subgenre_remarks	2x2 lines; seal
1	subgenre_remarks	2x4 lines; two diff. periods;" seal impr."
1	subgenre_remarks	3 impr from same seal; inside traces of cords
1	subgenre_remarks	3 lines.  Seal impressions (inscription only).
1	subgenre_remarks	3 lines.  Seal impressions on 2 sides.
1	subgenre_remarks	3 lines. A seal impression.
1	subgenre_remarks	3 lines. Kassite seal impression
1	subgenre_remarks	3 lines; seals
1	subgenre_remarks	3 same stamp seal impressions (potter's stamp?)
1	subgenre_remarks	3 urudu si-im-da ki sha13-dub-ba-ta Ur-dLama d U2-du-lu shu-ba-ti; seal: Ur-dLama ds d. Gish-sha6-mu ú-du-lu
1	subgenre_remarks	30 kuå.gu4 giå.åubur-a ba-a-lá from Urguenna, received by Ahua the son of Luduga; seal: Lugal-[] dubsar dumu Lú-du10-ga (CBT 2)
1	subgenre_remarks	3x2(rev) lines; faint seal impressions
1	subgenre_remarks	4 1/2 sìla li from the merchant Urguenna; seal: Lú-dNin-gír-su ds d. Ir11-mu.
1	subgenre_remarks	4 lines, seal impressions.
1	subgenre_remarks	4 lines.  Seal impression.
1	subgenre_remarks	4 lines.  Seal impressions.
1	subgenre_remarks	4 lines. Seal impression.
1	subgenre_remarks	4 lines; psbly.Kassite stamp seal impression
1	subgenre_remarks	4 lines; seal
1	subgenre_remarks	4 lines; seals
1	subgenre_remarks	4 seal impr from same cyl seal; inside traces of cords & cloth(?)
1	subgenre_remarks	49 about woodub-sar, eroded, sealed
1	subgenre_remarks	4x2(rev) lines; seal impr.
1	subgenre_remarks	4x3x2(u.e.) lines; seal impr.
1	subgenre_remarks	5 lines.  Seal impression.
1	subgenre_remarks	5 lines. Seal impression.
1	subgenre_remarks	5-year hire of a flock of sheep and goats; seal impr. on le.e.; 9x2x8x2 lines
1	subgenre_remarks	5x1(lo.e.) lines; writing nearly effaced; seal impr.
1	subgenre_remarks	6 gur of flour loaden on a boat, from Namhani to Ur-Nanshe son of Baa; seal: Ur-dNanshe ds d. Ur-sukkal.
1	subgenre_remarks	6 lines. A seal impression?
1	subgenre_remarks	6 lines. Seal impression on the LE.
1	subgenre_remarks	600 gur of barley loaden on boats for Ur, from Bazi to Kaamu for Ur-ur; seal: Ka5-a-mu ds d. Hé-ti.
1	subgenre_remarks	6x2x6x3(l.e.2); seals with labels;
1	subgenre_remarks	8x2(u.e.) lines; 5.3x7.1x2.9 cm; rev (shown in PBS 2) is completely gone; faint seal impr
1	subgenre_remarks	<Silver> deficit of the plowmen and nu-bànda gu4, passing from the sanga of Dumuzi to Lu-Ninshubur; seal: Lú-dNin-shubur ds d. Lú-dBa-ba6
1	subgenre_remarks	A partial sign. Seal impression.
1	subgenre_remarks	A seal impression
1	subgenre_remarks	A seal impression (lion & bull-man?), Cf. CBS6994
1	subgenre_remarks	A seal impression only.
1	subgenre_remarks	A solid bulla recording field rent.
1	subgenre_remarks	A stamp seal impressions (potter's stamp?)
1	subgenre_remarks	About barley to Ur-dIg-alim; seal: Ur-dIg-alim ds d. Lú-[dNin-gír-su]
1	subgenre_remarks	About barley, tablet eroded; seal illegible
1	subgenre_remarks	About barley: 2 she gur Ab-bu-na késh-da gur7 Ad-da sanga dInanna Èe-na nu-bàn-da-gu4-ke4 íb-su-su, gìr Na-bí-dEn-líl; seal: Èe-na nu-bànda-gu4 d. U-bar.
1	subgenre_remarks	About barley; seal: Ir3-ra-nu-id ds d. Ur-sha6-ga
1	subgenre_remarks	About barley; seal: Lú-[] ds d Lú-[]
1	subgenre_remarks	About barley; seal: dIshkur-[] d. Lú-[].
1	subgenre_remarks	About barley; she nì-gál-la ki I3-kal-la-ta kishib Ki-lu5-la ki Lugal-u5-a-ta; seal: Ur-sukkal ds d. Da-a-ga
1	subgenre_remarks	About dates; [ seal].
1	subgenre_remarks	About reed mats for Ur-shugalamma; seal: Ur-shu-ga-lam-ma ds d. []
1	subgenre_remarks	About wood, a-tir-du8; frgt of case; seal: Ur-shu-ga-lam-ma ds d. Nam-mah shabra
1	subgenre_remarks	Accession to govern; 5 lines; excavated by Haynes; faint seal impr.; tire tracks" in rev"
1	subgenre_remarks	Account garments expended; seal; 5x7 lines
1	subgenre_remarks	Account list; w/seal impression
1	subgenre_remarks	Account list; w/seal impression.
1	subgenre_remarks	Account list; w/seal impression;
1	subgenre_remarks	Account list; w/seal impressions; from Box 3; (Obv)15 lines, Rev.illegible
1	subgenre_remarks	Account of 1 goat taken in charge; seals; 4x4 lines
1	subgenre_remarks	Account of 26 []; Sippar; seals; 9x1x9x1 line
1	subgenre_remarks	Account of barley rations expended; seals. 7x2x4 UE 1 lines
1	subgenre_remarks	Account of barley rations for workers; seal 13x13 lines
1	subgenre_remarks	Account of barley receipts (ì-dab5); case unopened; seal: Gù-dé-a (CBT 2)
1	subgenre_remarks	Account of barley; sealed uninscribed tablet, ì-dub érin-e åu-ti-a (CBT 2)
1	subgenre_remarks	Account of barley; seals; tablet: 3 lines; envelope: 5 lines
1	subgenre_remarks	Account of barley; she zi-ga lá-ni nì-ka9-ak Nam-zi-tar-ra; seal: Nam-zi-tar-ra ds d. Ba-zi
1	subgenre_remarks	Account of calves consigned to a herdsman who has received silver for chopped straw for 2 months.  Seal impressions. 12X2X8
1	subgenre_remarks	Account of cattle; w/seal impressions & nail mark; (Obv)4x(Rev)4 lines
1	subgenre_remarks	Account of delivery of cloth; seal; 5x3 lines
1	subgenre_remarks	Account of delivery of cloth; seals; 5x3 lines
1	subgenre_remarks	Account of destruction of sprouted malt; seals; 4x2 lines
1	subgenre_remarks	Account of expenditure; Babili; seal of Enlil-nadin-ahe; cf. 29-15-778; 6 lines
1	subgenre_remarks	Account of expenditures from 4th day of V to the 18th day of 3rd year of KE; seal; 5x5 lines
1	subgenre_remarks	Account of fields; seal; 3x1 line
1	subgenre_remarks	Account of flour of Íeåkalla, kiåib Bù-du-núm; case unopened; seal: Íu-∂Utu ugula []-ru-um Bù-du-nu-um ugula kikken ir11-zu (CBT 2)
1	subgenre_remarks	Account of flour rations for days 7-23; seals; 5 lines
1	subgenre_remarks	Account of gold/stars transfered; seal; 3x1x2x1 lines; 4.5x1.7x1.5cm
1	subgenre_remarks	Account of gold/statues wieghed received and transfered; seals; 3x2x3 lines; 5.6x2.0x1.3
1	subgenre_remarks	Account of gold; seal; 3x1x3 lines; 4.6x1.7x1.5cm
1	subgenre_remarks	Account of gold; seals; 3x1x1 lines; 4.9c1.6 cms
1	subgenre_remarks	Account of gold; seals; 4 lines; 4.5x2.8x1.7
1	subgenre_remarks	Account of géme work; seal: Lú-hé-gál ds d. Ur-dingir-ra
1	subgenre_remarks	Account of issues (zi-ga) of barley fodder for livestock; åà NE.RU.ÛI.ÛI˚-ka; åà I7-sal4-la˚; åà Uru-gibil˚; åà Uru-x-kix; åà kar?-lugal-ka; åà Nibru˚; Gír-su˚-ta Nibru˚ ir-ra; udu kaå-dé-a é kú-a; seal: Ur-∂En-líl-lá dubsar dumu Inim-åa6 kuruåda (CBT 2)
1	subgenre_remarks	Account of issues of barley under the seals (kiåib) of various officials; zi-ga-àm gur7 ∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Account of oil; seals; 2x3 lines
1	subgenre_remarks	Account of one goat taken in charge; seal; 4x3 lines
1	subgenre_remarks	Account of payment due with penalty clause; seals; 8x4 lines
1	subgenre_remarks	Account of rations of barley; seals. 8x7 lines
1	subgenre_remarks	Account of silver; seals; 3 lines; 4.9x1.6 cms
1	subgenre_remarks	Account of transfer of gold for beams; Anzan; seals; 3x2x2 lines; 5.0x1.8x2.1cm
1	subgenre_remarks	Account of transport of 7 slaves; seal; 9x9 lines
1	subgenre_remarks	Account rations expended for days 5-16; Dur-Enlil; seal?; 6x6 lines
1	subgenre_remarks	Account: cereals for persons; seals; 5x2x4 lines
1	subgenre_remarks	Account; seal impressions on all over the surfaces, (Obv)27x(Rev)29x(UE)3 lines
1	subgenre_remarks	Account; seal; 5x4 lines
1	subgenre_remarks	Account; seals; 2x2 lines
1	subgenre_remarks	Account; seals; 3x2 lines
1	subgenre_remarks	Account; seals; 3x3 lines
1	subgenre_remarks	Account; seals; 5 lines
1	subgenre_remarks	Account; seals; 5x1x5 lines
1	subgenre_remarks	Account; w/seal impression; (Obv)6x(Rev)5 lines
1	subgenre_remarks	Accounts; W/seal impressions; (Obv)5x(Rev)1 lines
1	subgenre_remarks	Accounts; W/seal impressions; (Obv)8x(LoE)3x(Rev)6 lines
1	subgenre_remarks	Accounts; seals; 13x13x2(u.e.)x2(le.e.) lines
1	subgenre_remarks	Accounts; w/seal impression; (Obv)3x(LoE)3(Rev)3 lines
1	subgenre_remarks	Accounts; w/seal impressions all over the surfaces; (Obv)4x(Rev)3 lines; *or earlier
1	subgenre_remarks	Accounts; w/seal impressions; case:3 lines
1	subgenre_remarks	Adad-illat received hides from Awilumma.  The tablet was probably originally enclosed in a case sealed by Adad-illat.  Tablets with similar contents are all copies (98-06-38; 99-15-512; 99-15-513; 99-15-532).#
1	subgenre_remarks	Adalal received barley from Adad-illat, using the seal of his wife.
1	subgenre_remarks	Adjustement (lá-ni su-ga) of the barley account of Kuli, received by Nanshe-kam; seal: Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	Administrative text concerning silver for sheep for regular offering; seal. 7x1x5 UE1 lines
1	subgenre_remarks	Administrative text; badly defaced; case unopened; seal: Lugal-zag-ge-si dubsar dumu Ur-∂[Ig-alim] (CBT 2)
1	subgenre_remarks	Administrative; barley for åim, ki-ne, munus.mar-tu, kaå4 ki Lugal-inim-gi-na sukkal; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Administrative; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe kuruåda (CBT 2)
1	subgenre_remarks	Administrative; date only; seals; 3 lines
1	subgenre_remarks	Administrative; seals;  3 lines
1	subgenre_remarks	Administrative; seals; 1 line
1	subgenre_remarks	Administrative; seals; 1 sign
1	subgenre_remarks	Administrative; seals; 3 lines; cf. UM 29-16-162
1	subgenre_remarks	Administrative; seals; 3x1 line
1	subgenre_remarks	Administrative; seals; 3x3 lines
1	subgenre_remarks	Administrative; seals; 5 lines
1	subgenre_remarks	Administrative; seals; 5x1 lines
1	subgenre_remarks	Administrative; seals; 5x2 lines
1	subgenre_remarks	Administrative; seals; 5x3 lines
1	subgenre_remarks	Administrative; seals; 6 lines
1	subgenre_remarks	Administrative; seals; 7 lines
1	subgenre_remarks	Administrative; seals; Drehem calendar; 4 lines
1	subgenre_remarks	Adoption contract; PN1 adopts PN2 and makes him co-heir with PN3; bur-gul seal of 2 heirs; clauses with tukum-bi; 17x21 lines; 10.3x5.7
1	subgenre_remarks	Adoption; seal impressions; (Obv)13x(Rev)14x(UE)2 lines
1	subgenre_remarks	Allocation of a number of hé-dab5 workers for 1 day; case unopened; seal: Nam-uru-na dubsar dumu Ur-gar (CBT 2)
1	subgenre_remarks	Allocation of a number of hé-dab5 workers for 1 day; case unopened; sealed (CBT 2)
1	subgenre_remarks	Allocation of temple offices witnesses; 2 offices divided between three men;  witnesses; bur-gul seal; 13x15 lines; 6.7x4.9
1	subgenre_remarks	Amount of barley loaden on 2 boats, Mansum bur-sag, sá-du11 dNin-gír-su; seal: Ma-an-sum d. Ur-dUr-dEN.ZU àr-àr dNin-gír-su
1	subgenre_remarks	Amounts of barley to be returned; from SHS 8 xi 5 to IS 1 iv 19; 2 seals: Lú-dNin-mar-ki ds d. Ku5-da-dBa-ba6 ugula ush-bar; .Ku5-da-dBa-ba6 ds d. Ur-dNun-gal ugula ush-bar
1	subgenre_remarks	Amounts of flour recorded on several tablets are handed over to Lugal-an-na-ab-túm from the boat of Gisgal-di; seal: Lugal-an-na-ab-túm ds d. Na-di-lí
1	subgenre_remarks	An item Nam-mah shesh Pú-ta shu-ba-ti; seal illegible
1	subgenre_remarks	An ox (covered with) silver from Ur-Nanshe to Ur-Baba; seal: Ur-dBa-ba6 ds d. dUtu-mu sa12-du5-ka.
1	subgenre_remarks	Aram. inscription incised on Rev. Hilprecht?, (Obv)8x(Rev)3 lines, labels (UE)2x(LE)2 lines, seal impressions on UE.& LE.
1	subgenre_remarks	Areas of the fields sig7-tur and gishma-nu to be harrowed, zar3-tab-ba; seal: Lugal-é-mah-e ds d. [].
1	subgenre_remarks	Arzana to be brought back by Ur-ni9-gar; seal illegible
1	subgenre_remarks	Asses taken in charge; seals; 8x6 lines
1	subgenre_remarks	Axes taken in account by Ur-dNin-gis-zi-da; obv. broken; 4 seals: Ur-ni9-gar ds; Ur-shu-ga-lam-ma ds d. Ur-dNin-gis-zi-da ugula; Ba-zi ds d. SHesh-shesh; Ur-dDumu-zi d d. Ur-d[]
1	subgenre_remarks	Barley (174 gur) for seed and for wages in the storehouse; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ba-a-da sa12-du5 (CBT 2)
1	subgenre_remarks	Barley (18 gur) åe-ba un-íl for 6 months é ∂Nin-gis-zi-da from Guzani; case unopened; seal: Nì-ú-rum dumu Gìr-ni (CBT 2)
1	subgenre_remarks	Barley (26 gur) åe-ur5-ra zì-ka-åè from Urdam; case unopened; seal: Ku-li dubsar dumu Ki-ág-mu (CBT 2)
1	subgenre_remarks	Barley (90 gur) åu-im ba-ka; case unopened; seal: Ur-∂Nanåe dubsar dumu Ur-é-an-na (CBT 2)
1	subgenre_remarks	Barley (92 gur) transferred from Ur-Igalim to Lugal-lú-åa6-åa6; case unopened; seal: Lugal-lú-åa6-åa6 dubsar dumu Nimgir-åà-kúå-an-na (CBT 2)
1	subgenre_remarks	Barley (a-åà ki-BAD-a-gug4) transferred from Bazi to Utu-åaga (CBT 2). A: Case of 18773; seal: ∂Utu-åa6-ga dumu Al-la (CBT 2)
1	subgenre_remarks	Barley (nì-gál-la zì-ka-åè) transferred from Lumarsa to Ur-Baba; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ur-∂[] (CBT 2)
1	subgenre_remarks	Barley (nì-gál-la) from Dada son of Urgula to Ur-Nanåe the storekeeper; case unopened; seal: Ur-∂Nanåe dubsar dumu Lú-du10-ga ka-gur7-ka (CBT 2)
1	subgenre_remarks	Barley (nì-gál-la) transferred from Lu-Baba to Lu-Ningirsu (CBT 2). A: Case of 18208; seal: Lú-∂Nin-gír-su dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Barley (she dab5-ba) received by various persons; seals: Lugal-lú-sha6-sha6 ds d. Nim-shà-kúsh-an-na; Ur-Ig-alim ds d. La-la []
1	subgenre_remarks	Barley (she nì-gál-la) and flour received by Urgar, ugula sanga dNin-dar-a; seal: Ur-gar ds d. Lugal-gaba.
1	subgenre_remarks	Barley (zì-ka) transferred from Abbamu to Ía6-åa6-ga, gìr Abba ab-ba uru; case unopened; seal: Ur-∂Nanåe dubsar dumu Ur-sukkal (CBT 2)
1	subgenre_remarks	Barley (åe gur zabar Lú-∂Nin-sún-zi) for guruå and érin at the bala duty received by Ur-ni9-gar; case unopened; seal: Ur-ni9-gar dumu Ur-sukkal (CBT 2)
1	subgenre_remarks	Barley (åe åà-gal udu kaskal) from Lu-Utu to Lu-Magan; seal: Lugal-engar-du10 dumu Nì-kal-la sipa udu niga (CBT 2)
1	subgenre_remarks	Barley (åe-ba a-bal) from Itini to Ur-Íulpae; case unopened; seal: Ur-∂Íul-pa-è [ds] [d.   ] (CBT 2)
1	subgenre_remarks	Barley (ì-dub kar-du6-èå-sá) transferred from Bazi to Lugalmelam (CBT 2). A: Case of 18771; seal: Íà-ba-na-sig dumu Ib2-ta-è má-lah4 (CBT 2)
1	subgenre_remarks	Barley account of Lú-kiri4-zal; seal: Lú-kiri4-zal d Lú-dBa-ba6
1	subgenre_remarks	Barley account; nì-ka9-ak she Ur-d.Ba-ba6 gudu4 d.Mes-lam-ta-è-a;seal: Ur-d.Ba-ba6 dumu Ur-dNanshe gudu4
1	subgenre_remarks	Barley account; nì-ka9-ak she Ur-dNanshe-dNin-a-su; seal Lugal-gú-tuk d. Ur-dNanshe
1	subgenre_remarks	Barley allotment (åe åuku-ra) for the érin in the household of Namhani, received by Lugaldaga from Lugal-annabtum; case unopened; seal: Lugal-da-ga dubsar dumu Ur-[∂Nanåe] (CBT 2)
1	subgenre_remarks	Barley and emmer as regular deliveries for Iåhara; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu; months xi to xi-2 (CBT 2)
1	subgenre_remarks	Barley and emmer from Bazi to Mani, sá-du11 she-ba-shè; seal: Ma-ni sagi dGù-dé-a d. Ur-dLama
1	subgenre_remarks	Barley and emmer from Inim-Baba-idab to Ur-SHulpae the overseer of the mill; seal: Géme-dLama nin-dingir-dBa-ba6 Ur-dSHul-pa-è ugula àr-àr dumu [] ir11-zu
1	subgenre_remarks	Barley and flour from Lugula; seal: Ur-dIg-alim ds d. Ur-ni9-gar.
1	subgenre_remarks	Barley and flour rations for guruå åeå-tab-ba má-lah4, from Urmes to Hetae; case unopened; seal: Hé-ta-è má-lah4 [] (CBT 2)
1	subgenre_remarks	Barley and seed transferred from Ur-Nanåe to Ur-∂Lamma; a-åà sahar-sur-ra; case unopened; seal: Ur-∂Lamma dubsar dumu Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Barley and wheat from Ur-èsh-kù-ga to Katar-Baba; seal: Ka-tar-dBa-ba6 d. Eren-da gu-za-lá
1	subgenre_remarks	Barley as fodder for cattle from Ur-Baba to Ir3-ra-nu-id; seal: Ir3-ra-nu-id dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Barley as fodder for the dumu-dab5-ba; seal: Lú-dIgi-ma-shè ds d. Da-da
1	subgenre_remarks	Barley as food for the erin of the fattener, from Ur-badtibirra to Ur-Ningirsu; seal: Ur-dNin-gír-su ds d. Ur-gishgigir.
1	subgenre_remarks	Barley as food for the oxen of Sabum; kiåib Íu-Enlil lú giå.gigir; seal: Íu-∂En-líl-lá lú giå.tukul, dumu Gu-[]-lu (CBT 2)
1	subgenre_remarks	Barley as food for the plowmen taken in account by Ur-Lama; seal: Ur-dLama ds d. Nam-mah
1	subgenre_remarks	Barley as food for the érin of Ebih given by Ur-Enlil to Urmes; case unopened; seal: Ur-mes dubsar dumu Lú-Nina.ki (CBT 2)
1	subgenre_remarks	Barley as food for the érin of Madga, from Ur-sag-ku5 to Guzana the ploughman; case unopened; seal: Gu-za-na dumu Ía6-mu nagar (CBT 2)
1	subgenre_remarks	Barley as food for women; kiåib Ur-Igalim; seal: Ur-∂Ig-alim dumu Nam-mu (CBT 2)
1	subgenre_remarks	Barley as food for åarabdu received by Ilum-bani from Lugina; seal: Ilum-ba-ni x-da dumu [] (CBT 2)
1	subgenre_remarks	Barley as food for érin bala gub-ba; seal: Nimgir-åà-kúå dubsar dumu Má-gur8-re (CBT 2)
1	subgenre_remarks	Barley as food for érin from Ur-Enlilla to Ahua (CBT 2). A: Case of 18881; seal: Ur-∂Nanåe dubsar dumu Lú-du10-ga ka-gur7-ka (CBT 2)
1	subgenre_remarks	Barley as food for érin going to Madga received by Eå3-àm; case unopened; seal: Ur-∂Ig-alim dubsar dumu A-tu (CBT 2)
1	subgenre_remarks	Barley as food for érin received by Abbamu from Ur-ni9-gar; seal: Ab-ba-mu [  ] (CBT 2)
1	subgenre_remarks	Barley as food transferred from Zazi to Urgar; case unopened; seal: Ur-gar dubsar dumu A-tu dubsar hé-dab5 (CBT 2)
1	subgenre_remarks	Barley as loan for hired men from Lugirnun for Urgar; seal: Ur-gar dubsar dumu Lú-kal-la; Shulgi 46/Amar-Suen 3 (CBT 2)
1	subgenre_remarks	Barley as regular delivery for wages transferred from Bazi to Lu-Ningirsu; case unopened; seal: Lú-∂Nin-gír-su dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Barley as shà-gal for hé-dab5 from Ur-bad3-tibir-ra; seal: Ur-dNanshe ds [?]
1	subgenre_remarks	Barley as shà-gal érin-na from Ur-Enlilla to Lu-Ninshubur; nu-bànda Ur-sha6-ga gu-za-lá; seal Lú-dNin-shubur dumu Lú-dUtu
1	subgenre_remarks	Barley as wages for hired érin received by Lugal-zaggesi from Guzani; case unopened; seal: Lugal-zag-ge-si dubsar dumu Ur-∂[Ig-alim] (CBT 2)
1	subgenre_remarks	Barley as wages for women from A-gi4 to Ur-ni9-gar; seal: Ur-ni9-gar ds d. Lú-dNin-shubur.
1	subgenre_remarks	Barley delivered by Lú-∂Nin-åubur son of I-ta-è; seal: Íeå-kal-la dubsar dumu An-né nu-[bànda] (CBT 2)
1	subgenre_remarks	Barley distributed over several months to the érin bala tush-a and the érin é-sukkal; seal: Ur-gishgigir dumu É-d.Anzu
1	subgenre_remarks	Barley distribution; seal: Lú-dNin-[] ds d. Na-ba-sha6
1	subgenre_remarks	Barley flour for the temple of Amar-Sin delivered by Guzani; case unopened; seal: Ma-an-sì-na dubsar dumu Lú-kir4-zal (CBT 2)
1	subgenre_remarks	Barley flour issued to Ur-ni9-gar for the boats of Urdun and Ur-Sin; seal: Ur-ni9-gar dubsar dumu Lú-∂Nin-[ ] (CBT 2)
1	subgenre_remarks	Barley flour transferred from Íeåkalla to Ur-Igalim; seal: Ur-∂Ig-alim dumu Ur-∂[] lú-kaå (CBT 2)
1	subgenre_remarks	Barley food for the érin at the bala duty from Bazi to Ur-Baba; case unopened; seal: Ur-∂Ba-ba6 [ ] (CBT 2)
1	subgenre_remarks	Barley for 4 persons from Íakuge to Lu-melam; seal: Lú-me-lám dubsar dumu [] (CBT 2)
1	subgenre_remarks	Barley for Inim-Nanshe from Urbadtibirra to Ur-Nanshe; seal: []-dNin-gír-su []-an-na []-ad-[] ki-ág-dNanshe Ur-dBa-ba6 ds d. Lugal-[] ir11-zu.
1	subgenre_remarks	Barley for Lú-ba-a; seal: SHà-kù-ge ds d. Lú-kal-la
1	subgenre_remarks	Barley for Nippur loaded on boats, má-a GAR-na; seal: Ka-tar-dBa-ba6 d. Eren-da gu-za-lá.
1	subgenre_remarks	Barley for Nippur; 600 she gur lugal ì-dub sha6-ga-tur-ta ki Ba-zi-ta má-a si-ga Nibruki-shè kishib U2-ú d. Ur-ab-ba; seal: U2-ú d. Ur-ab-ba
1	subgenre_remarks	Barley for Pù-ta-pàd a-igi-du8; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Barley for Ur-Lamma and Lugal-inimgina transferred from Ur-Hendursag to Ur-Nanåe; case unopened; seal: Ur-∂Nanåe dubsar dumu Lú-du10-ga ka-gur7-ka (CBT 2)
1	subgenre_remarks	Barley for Ur-ki-gu-la; seal: Ur-ki-gu-la d. Kù-[] [] nin-dingir-[].
1	subgenre_remarks	Barley for Urkalla; seal: Lú-kal-la ds d. Ur-é-an-na.
1	subgenre_remarks	Barley for Urmes, from Íakuge to Ur-dingirsianna; seal: Ur-dingir-si4-an-na dumu [Nì]-åa6-[ga] (CBT 2)
1	subgenre_remarks	Barley for abba-uru and Ur-Baba to Ur-badtibirra and Ur-Baba; seal: Ur-dBa-ba6 d. Ur-dLama.
1	subgenre_remarks	Barley for all kind of field workers received by Bazi; case unopened; seal: Ba-zi dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Barley for anshe-baran, shà-gal ú-íl, from Ur-SHulpae to Ur-sag-ùbaki; seal: Géme-dBa-ba6 nin-dingir dBa-ba6 Ur-sag-ùbaki sipa anshe
1	subgenre_remarks	Barley for bala workers coming from Nana to Lugal-maå-su; seal: Lugal-maå-su dumu Ur-kù-nun-na (CBT 2)
1	subgenre_remarks	Barley for craftmen (gaåam) åe é-kin-gá-x˚; seal: Lú-∂Nin-gír-su dubsar dumu Lú-du10-ga?; mu en [] itu ezem-[] (CBT 2)
1	subgenre_remarks	Barley for dSHul-gi-ur-shu-ru-uq from dSHul-gi-kalam-ma-me-te-bi; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley for donkeys from Inim-Baba-idab to Ur-sag-ùbaki; seal: Géme-dLama nin-dingir-dBa-ba6 Ur-sag-ùbaki sipa anshe-[baran]
1	subgenre_remarks	Barley for engar and shà-gu4; case + tablet inside; seal: Lú-dGish-pa-è d. Ur-dNanshe
1	subgenre_remarks	Barley for erin from Ur-badtibirra to Ur-Ningirsu; seal: Ur-dNin-gír-su ds d. Ur-gishgigir.
1	subgenre_remarks	Barley for fat sheep (shà-gal udu-niga) from Ur-Lama to Lú-kal-la; seal: Ur-é-ninnu ds d. Lú-du10-ga sanga dNin-gír-su
1	subgenre_remarks	Barley for fat sheep, from the house of Ki-tush-lú for Lú-Lagash; seal: Lú-Lagashki ds d. Ur-dNanshe nu-bànda kurushda
1	subgenre_remarks	Barley for flour from Ahua; case unopened; seal: A-tu dubsar dumu Lú-∂Nanåe dubsar hé-dab5 (CBT 2)
1	subgenre_remarks	Barley for flour from Bazi to Guzani; seal: Gu-za-ni ds d. Lú-dingir-ra sha13-dub-ba.
1	subgenre_remarks	Barley for flour from En-e-ki-ág; seal: Lú-∂Nin-åubur dubsar dumu Ur-∂[...] (CBT 2)
1	subgenre_remarks	Barley for flour, ì-dub á-gúl, from Bazi to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Ur-dNanshe.
1	subgenre_remarks	Barley for flour; only obverse legible; seal: Ur-dNin-gis-zi-da ds d. Ur-sha6-ga
1	subgenre_remarks	Barley for garden workers (a-bal, dù-a-ku5); case unopened; seal: Ur-dun dumu Lugal-GIÍ.gigir (CBT 2)
1	subgenre_remarks	Barley for gudu4 mí-[gil?]-sa received by Ur-Enzu; case unopened; seal: Ur-∂EN.ZU dumu Lú-du10-ga (CBT 2)
1	subgenre_remarks	Barley for gudu4-bala from the sanga dNin-mar-ki received by ›-e-ba-ab-du7; seal: ›-e-ba-ab-du7 d. Du10-ga
1	subgenre_remarks	Barley for gurush dumu-dab5-ba, kishib Ka-a-bi; seal: Géme-sha6-ga dam Ka-bi.
1	subgenre_remarks	Barley for gurush from Ur-Nanshe to Namhani; seal: Nam-ha-ni ds []
1	subgenre_remarks	Barley for gurush rations; seal: SHu-ì-lí d. Ba-zi
1	subgenre_remarks	Barley for gurush é-kurushda-me, from Dudu; seal: Ur-sha6-ga ds d. Ur-dKal-kal
1	subgenre_remarks	Barley for gurush-gudu4 from Bazi to Lu-Baba; seal: A-tu gu-za-lá d. Ur-èsh
1	subgenre_remarks	Barley for guruå (guruå nu-dab5-me, gán-dab5-ba é kuruåda lugal) from the egula received by Ur-Nungal; seal: Ur-∂Nun-gal dubsar dumu NI-NI muhaldim kuruåda (CBT 2)
1	subgenre_remarks	Barley for guruå (åe-zì-ka-ta) transferred from Mani to Ur-Baba ugula é gu-za-lá; case unopened; seal: Ur-∂Ba-ba6 [?] (CBT 2)
1	subgenre_remarks	Barley for guruå and hired workers transferred from Lubimu to Ur-Numuåda; case unopened; seal: Ur-∂Nu-muå-da dubsar dumu Du-du sanga Urub.ki (CBT 2)
1	subgenre_remarks	Barley for guruå and érin from Ur-ni9-gar to Lu-Íara; case unopened; seal: Ur-∂Íára dubsar dumu Ur-∂[] []-∂Nanåe (CBT 2)
1	subgenre_remarks	Barley for guruå and érin received by Lu-Dumuzi ugula; case unopened; seal: Lú-∂Dumu-zi dumu Ur-[] (CBT 2)
1	subgenre_remarks	Barley for guruå transferred from Bazi to the érin on bala duty; case unopened; seal: Ur-∂Lamma dubsar dumu Ur-nu (CBT 2)
1	subgenre_remarks	Barley for guruå, hé-dab5, tu-ra; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu ∂Utu-mu sa12-du5 urub˚-ka (CBT 2)
1	subgenre_remarks	Barley for géme and dumu; seal: Géme-dLama nin-dingir dBa-ba6 Ur-dDa-mu ds d. Ur-sha6-ga ir11-zu
1	subgenre_remarks	Barley for géme and nu-bànda; seal: Géme-dLama nin-dingir dBa-ba6 Ur-dDa-mu ds d. Ur-sha6-ga ir11-zu
1	subgenre_remarks	Barley for géme nu-gishkiri6 and un-íl in the girsiga of the gods; seal: Ur-mes ds d. Gù-dé-a
1	subgenre_remarks	Barley for hired men from Ur-Igalim to Lu-Urub; case unopened; seal: Lú-Urub˚ dubsar dumu Ur-∂Iåkur (CBT 2)
1	subgenre_remarks	Barley for hired men received by Lu-Inanna from Nabaåa; case unopened; seal: Lú-∂Inanna nu-bànda-gu4 dumu Ir11-mu (CBT 2)
1	subgenre_remarks	Barley for hired men working at the canal which the sanga has received from Mani; seal: sanga a-igi-du8 dumu Ha-sum-ma (CBT 2)
1	subgenre_remarks	Barley for hired oxen from Ur-gú-en-na to Zalag-ga-íl; seal: Lugal-[] ir11 Ur-.
1	subgenre_remarks	Barley for hé-dab5 and un-íl received by Urmes; case unopened; seal: Ur-mes dubsar dumu Ur-gar nu-bànda (CBT 2)
1	subgenre_remarks	Barley for kin-gi4-a, kash-dé-a lugal, from Dada to Ur-Baba; seal: Ur-dBa-ba6 ds d. Si-dù kurushda
1	subgenre_remarks	Barley for loan, åe ur5-ra àga-uå énsi ki Bazi. Seal: Ir11-∂Nanåe dumu Ba-zi-ge (CBT 3)
1	subgenre_remarks	Barley for lú-suhur-lá and lam-gaz?; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley for nu-bànda-gu4, engar, dumu-da-ba, dumu gu4-gur, from Ur-ni9-gar; seal: Lú-é-sukud-rá ds d. Lugal-gistukul sa12-du5 dNin-dar-a
1	subgenre_remarks	Barley for oxen and sheep, from Sidu to Lugal-gú-gal; seal: Lú-gú-gal ds d. Lú-dBa-ba6.
1	subgenre_remarks	Barley for oxen and érin; seal: Lú-du10-ga ds d. Gú-ku
1	subgenre_remarks	Barley for seed from Ur-dNanshe to Inim-Inanna; seal:  [] ds d. Inim-d[Inanna]
1	subgenre_remarks	Barley for seed from dUtu-mu from ì-dub elam-e-ne-ta; seal: dUtu-mu nu-bànda gu4 d. Ur-dun
1	subgenre_remarks	Barley for seeding a-shà pú-shu-i-ne, from A-tu-kal-la kishib Du11-ga-dBa-ba6 shesh A-kal-la shabra; seal: Du11-ga-dBa-ba6 ds d. []
1	subgenre_remarks	Barley for seeding fields, for the oxen and the workers; ì-dub érin-e shu-ti-a, kishib Lugal-sukkal; ugula Bù-zi, nu-bànda Lugal-kù-zu; Umma month name; seal: Lugal-sukkal d. Lugal-an-né
1	subgenre_remarks	Barley for seeding for the field gishdúsu, from Lú-dNin-shubur to Ur-èsh-kù-ga; seal: Ur-èsh-kù-ga ds d. [].
1	subgenre_remarks	Barley for seeding from Ku5-da to Ur-dNin-mar-ki; seal: Ur-dNin-mar-ki ds d. Nam-ha-ni
1	subgenre_remarks	Barley for seeding from Ur-Nanshe to Lu-Narua; seal: Lú-dNa-rú-a ds d. Ur-dBa-ba6.
1	subgenre_remarks	Barley for seeding in the field Lugal-nam-rí-na-shè; ì-dub íd-tir-nin; from Ur-dNanshe; ugula ›-URUxKAR2ki; gìr Ab-ba-mu d. Ba-a; seal: Ur-dLama ds d. dUtu-mu
1	subgenre_remarks	Barley for seeding in the ì-dub dEn-ki-ta kishib Ur-gu-la d. Ga-ni gìr SHa6-sha6-ga d. Ba-a; seal Ur-gu-la ds d. Ga-ni
1	subgenre_remarks	Barley for seeding the field Lugal-nam-URUxKAR2ki she dUtu-bar-ra dumu A-mu ì-dub íd tir-sikil ki Ur-dNanshe-ta kishib Ur-dBa-ba6 d. Ha-lí-lí ugula sanga-dNanshe; seal: Ur-dBa-ba6 d. Ha-lí-lí
1	subgenre_remarks	Barley for seeding the field a-geshtin-dDumu-zi and pirig-tur-gim; from Ur-dNanshe; seal: Ur-é-ninnu ds d. Al-la-mu shabra
1	subgenre_remarks	Barley for seeding, a-shà na-kab-tum-shè ki Ur-dNanshe ka-gur7-ta ì-dub a-shà mah-ta kishib Ur-dNin-gis-zi-da a-rá 2-kam; seal: Ur-dNin-gis-zi-da ds d. Ur-[]
1	subgenre_remarks	Barley for seeding, from Bazi; seal: Lú-kiri4-zal ds d. Ur-dBa-ba6
1	subgenre_remarks	Barley for seeding, ì-dub é-duru5 Ab-ba-kal-la-ta ki Ba-zi-ta ugula Ur-dNin-mar-ki; seal: Ur-Ma-ma d. Nam-ha-ni
1	subgenre_remarks	Barley for several persons, ì-dub hé-gál, given by Ur-ISH-Baba; seal: Lú-kiri4-zal d. Lugal-má-gur8-re lú-kash.
1	subgenre_remarks	Barley for several persons; seal illegible
1	subgenre_remarks	Barley for several types of field workers from Ur-GIÍ.gigir to Íu-Iåtar; mu ka-a-bi-åè íb-ra; case unopened; seal: Íu-Eå4-tár dumu Bur-Ωé-Ωé (CBT 2)
1	subgenre_remarks	Barley for sheep from Id-ni-lí to Lu-melam; seal: Lú-me-lám ds d. Lú-kal-la.
1	subgenre_remarks	Barley for sheep from Lukalla for Íakuge; seal: Íà-kù-ge dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Barley for sheep from Ur-Baba to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Nì-dBa-ba6
1	subgenre_remarks	Barley for sheep from Ur-ba-gár to Lú-me-lám; seal: Lú-me-lám ds d. Lú-kal-la
1	subgenre_remarks	Barley for sheep received by Lubaa from Lu-melam; seal: Lú-ba-a dubsar dumu Lú-[] (CBT 2)
1	subgenre_remarks	Barley for sheep, from Lú-kal-la to SHà-kù-ge; seal : [] [] d. Lugal-[]
1	subgenre_remarks	Barley for sheep, má Ur-ti-ra-ásh-ta gá-nun gish-ta; seal: Lugal-gú-gal ds d. Lú-dBa-ba6.
1	subgenre_remarks	Barley for shà-gu4 from the sanga of Ninmarki to Lu-Baba; seal Lú-dBa-ba6 d. A-tu gu-za-lá.
1	subgenre_remarks	Barley for sowing from Lú-dIgi-ma-shè to Lugal-DU; seal: Lugal-DU d. Da-gi
1	subgenre_remarks	Barley for sowing from Na-ba-sha6 to A-al-la; seal: A-a-kal-la ds d. Ab-ba-gi-na
1	subgenre_remarks	Barley for sowing, from Lú-dingir-ra to Ur-ki-sal4-la; seal: Â-zi-da d. Ma-an-sum?
1	subgenre_remarks	Barley for the bala; seal: Ur-dNanshe d. Ur-sha6-ga gu-za-lá, written in the inverse sequence
1	subgenre_remarks	Barley for the field Igi-dIshkur given to several persons; seal: Ur-dLama ds d. Nam-mah ugula
1	subgenre_remarks	Barley for the gishgab-tab work delivered by Ur-gú-en-na; seal: Ur-dLama [] [].
1	subgenre_remarks	Barley for the hired workers in the palmtree plantation of Qarshum, from Lugal-amaru to Dudu the hazanum of Bír-bírki; seal: Du-du dumu Lú-[].
1	subgenre_remarks	Barley for the kash4 from Ur-ni9-gar to Lu-Baba; seal: Lú-dBa-ba6 ds d. []
1	subgenre_remarks	Barley for the kitchen from the shabra Ur-Baba; seal: Ur-shu-ga-lam-ma d. Ur-dUtu-du10-ga nu-bànda-gu4
1	subgenre_remarks	Barley for the marsa men; seal: Gu-za-na dumu Ía6-mu nagar (CBT 2)
1	subgenre_remarks	Barley for the oxen and sheep of the bala from Lú-uruxkár the merchant to Lugal-sha6-ga; seal: Ur-dIg-alim d. Lugal-sha6-ga dub-sar sic!
1	subgenre_remarks	Barley for the temple of Amar-Sin; 652 gur she gish è-a kishib Du11-ga-dBa-ba6 ugula SHesh-kal-la é-dAmar-dEN.ZU; seal: Du11-ga-dBa-ba6 ds d. Ab-ba-gi-na
1	subgenre_remarks	Barley for the temple of Íara; kiåib Lú-mar-sa; case unopened; seal: Ur-∂Ig-alim dubsar dumu Na-ba-åa6 (CBT 2)
1	subgenre_remarks	Barley for the temples of SHulgi and Ningiszida; DLama-uru-na-ra Ka5-a-mu tùm-dam; seal: Lú-dDumu-zi ds d. Ur5-bi-shè
1	subgenre_remarks	Barley for the women of the mill from Bazi to Mansi; case unopened; seal: Ma-an-sì dubsar dumu Eren-da gu-za-lá (CBT 2)
1	subgenre_remarks	Barley for the érin (bala gub-ba gu-za-lá-åè), received by Ur-Lamma; case unopened; seal: Ur-∂Lamma dubsar dumu Ur-∂Nun-gal (CBT 2)
1	subgenre_remarks	Barley for the érin (åe érin-e kú-a) transferred from Ur-Enlilla to Ur-GIÍ.gigir in months xi-2 and xii; seal: Ur-GIÍ.gigir dumu É-Anzu (CBT 2)
1	subgenre_remarks	Barley for the érin ì-dub tranfered from Ur-Lama the shabra to Ka-gu; seal: Ab-ba-du10-ga ds d. Ab-ba-mu
1	subgenre_remarks	Barley for un-íl (zì-íl) on the tablet of Lu-URUxKAR2; seal: Géme-dLama nin-dingir-dBa-ba6 Lú-URUxKAR2ki ir11-zu.
1	subgenre_remarks	Barley for un-íl from Ur-Igizibarra to Ur-Nanshe.; seal: Géme-dLama nin-dingir dBa-ba6 Inim-dBa-ba6-ì-dab5 rá-gaba ir11-zu.
1	subgenre_remarks	Barley for un-íl; seal: Lugal-uru-da nu-bànda gu4 nin-dingir d[]
1	subgenre_remarks	Barley for various farmers; ì-dub TE? Lú-pàd-da; seal: Ur-dNin-zu engar dIg-alim d. nu-bàn-da
1	subgenre_remarks	Barley for wages (á hun-gá-shè), kishib Ur-sag-ùbaki; seal: Ur-sag-ùbaki d. NI.NI a-igi-du8 [gal].
1	subgenre_remarks	Barley for young cattle from Gir-Baba-idab to Unil; seal: Nin-dingir-dBa-ba6 Un-íl.
1	subgenre_remarks	Barley for young cattle from Utu-a received by Ir11-dam; case unopened; seal: dumu ∂Dumu-zi-kam / Ir11-dam ùnu (sic!) (CBT 2)
1	subgenre_remarks	Barley for àga-ush, bala Ur-dLama énsi Gír-suki; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley for á hun-gá, gishgaba-tab, from Bazi to Dingir-sha6-ga; seal: Dingir-sha6-ga d. Lú-nimgir gu-za-lá
1	subgenre_remarks	Barley for érin at the bala, from Bazi to []; seal illegible
1	subgenre_remarks	Barley for érin at the bala; [seal].
1	subgenre_remarks	Barley for érin coming from the ì-dub dSHul-gi-zi-kalam-ma; from Ur-Baba to Lugal-dumu-gi7; seal: Lugal-dumu-gi7 ds d. Lú-[]
1	subgenre_remarks	Barley for érin from Alla to Ur-Lama; seal: Ur-dLama d. dNin-marki.
1	subgenre_remarks	Barley for érin from Bazi to Ur-Hendursag; case unopened; seal: Ur-∂Hendur-sag dubsar dumu Lugal-åa6-ga (CBT 2)
1	subgenre_remarks	Barley for érin from Bazi to Ur-Nanshe; [seal].
1	subgenre_remarks	Barley for érin from Ku5-da to Ur-Nanåe; case unopened; seal Ur-∂Nanåe dubsar dumu Lú-du10-ga ka-gur7-ka (CBT 2)
1	subgenre_remarks	Barley for érin from Ur-Enlil to Ahua; seal: Ur-dNanshe ds d. Lú-du10-ga.
1	subgenre_remarks	Barley for érin from Ur-Enlil to Lu-dingirra; seal: Lú-dingir-ra ugula ds d. Ur-gishgigir un-gal pro un-íl?
1	subgenre_remarks	Barley for érin from Ur-Enlila to Ur-Nanshe; seal: Ur-dNanshe ds d. Al-la.
1	subgenre_remarks	Barley for érin from Ur-Gilgames to Ur-Lama; seal: Ur-dLama d. dNin-marki-ka.
1	subgenre_remarks	Barley for érin from Ur-dEn-líl-lá; months viii-xii; seal: Gù-dé-a ds d. Ur-dUtu nu-bànda
1	subgenre_remarks	Barley for érin from Ur-dLama to Ku5-da; seal: Ku5-da ds d. Du11-ga-zi-da
1	subgenre_remarks	Barley for érin from Ur-ni9-gar to Igiannakezu; seal: Igi-an-na-ke4-zu dubsar dumu Zi-mu (CBT 2)
1	subgenre_remarks	Barley for érin gi-gibil-lá-me and nu-bànda from Ur-èsh-kù-ga to Lú-bala-sha6-ga; seal: Lú-bala-sha6-ga ds d. Ur-dNin-[]
1	subgenre_remarks	Barley for érin gi-zi from Lu-Nindara; case unopened; seal: Ur-∂An-ta-sur-ra dumu Lugal-åa6-ga (CBT 2)
1	subgenre_remarks	Barley for érin gi-zi from Ur-Ninpirig to Ur-Hendursag; case unopened; seal: Ur-∂Hendur-sag dubsar dumu Lugal-åa6-ga (CBT 2)
1	subgenre_remarks	Barley for érin on bala duty from Lukalla to Lugal-Eridu-åe; seal: Lugal-Eridu˚-åè dumu A-tu gudu4 ∂Mes-lam-ta-è-a (CBT 2)
1	subgenre_remarks	Barley for érin workers which Lugal-imrua received from Guzani (CBT 2). A: Case of 15922; seal: Ur-∂Nanåe dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Barley for érin íd-da gub-ba; seal: Nimgir-shà-kúsh ds d. Má-gur8-re.
1	subgenre_remarks	Barley for érin, from Guzani to Lamlammaseal: Lam-lam-ma d. Ha-ti.
1	subgenre_remarks	Barley for érin, from Ur-Enlilla to Dagu ugula; seal: dUtu-bar-ra d. Lú-dBa-ba6.
1	subgenre_remarks	Barley for érin, from the é-udu-gibil, from Lú-kalla; tablet in case; seal: Lú-åa6-ga dumu [] (CBT 2)
1	subgenre_remarks	Barley for érin, kishib Inim-kù; seal illegible.
1	subgenre_remarks	Barley for érin, returned by Bazi to Ur-idda; seal: Ur-íd-da d. Ur-dBa-ba6 [].
1	subgenre_remarks	Barley for érin; seal: Lú-gishgigir ds d. []
1	subgenre_remarks	Barley for érin; seal: Nam-lugal-ì-[du10] ds d. Ur-tur-tur []
1	subgenre_remarks	Barley from A-li-ih to Ba-da-rí for seeding the field en-nu-lum-ma; seal: Ba-da-rí ugula dumu-dab5-ba dumu Gu-za-ni
1	subgenre_remarks	Barley from Ahua to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Barley from Alla received by Ludingirra; case unopened; seal: Lú-dingir-ra dubsar dumu Ga-a-ni (CBT 2)
1	subgenre_remarks	Barley from Alla to Ur-Enlilla; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Barley from Ba-zi to Ur-Baba; seal: Ur-dBa-ba6 d. Ur-li lú-shim
1	subgenre_remarks	Barley from Bazi to Mani; seal: Ma-ni sagi dGù-dé-a d. Ur-dLama
1	subgenre_remarks	Barley from Bazi to Ur-Baba; seal: Ur-dBa-ba6 d. Na-di lú-shim
1	subgenre_remarks	Barley from Bazi to Ur-é-mush; seal: Lú-d[] ds d. Ur?-[]
1	subgenre_remarks	Barley from Bazi to Urshugalamma; seal: Ur-shu-ga-lam=-ma ds d. Nam-zi-tar-ra? shabra
1	subgenre_remarks	Barley from Eå3-àm to Guzana for the men going to Madga; case unopened; seal: Gu-za-na dumu Ía6-mu nagar (CBT 2)
1	subgenre_remarks	Barley from Ga-a to Ur-Nanshe; seal eroded [Ur-dNanshe ds d. Na-ba-sha6]
1	subgenre_remarks	Barley from Gudea for the weaver women; seal: Lú-dingir-ra ds d. Lú-dUtu.
1	subgenre_remarks	Barley from Gudea; kishib Lú-dNa-rú-a ugula Lú-eba; seal: Lú-dNa-rú-a ds d. KA-KA nu-bànda
1	subgenre_remarks	Barley from Guzani to Ur-dKal-kal; seal: Ur-dKal-kal d. Bur-la?
1	subgenre_remarks	Barley from I3-kal-la to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Barley from Ikalla; kiåib Ur-[ ] dumu Ur-sur!; case unopened; seal: Ur-[] dubsar dumu Ur-[] (CBT 2)
1	subgenre_remarks	Barley from Ka5-a-mu; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Barley from Kù-dInanna and dEn-líl-ra-bi; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Barley from Lu-Baba to Ur-Enlilla; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Barley from Lu-Baba to be returned by Lugal-uåumgal; seal: Lugal-uåumgal dubsar dumu Ur-ni9 (CBT 2)
1	subgenre_remarks	Barley from Lu-Baba; seal: [] ds d. Ur-dNun-gal
1	subgenre_remarks	Barley from Lu-Dumuzi to Lugal-ezem; seal: Lugal-ezem d. SHa6-ga sagi.
1	subgenre_remarks	Barley from Lu-Igimaåe to Itaea; seal: I3-ta-è-a dubsar dumu Lú-du10-ga sanga ∂Nin-gír-su-ka (CBT 2)
1	subgenre_remarks	Barley from Lu-Ningirsu to Lu-Baba; seal: Lú-dBa-ba6 ds d. Lú-kal-la.
1	subgenre_remarks	Barley from Lu-Ningirsu to Lugal-Eriduki-shè; seal: Lú-d[] ds d. Ur-dLama sanga dNin-shubur.
1	subgenre_remarks	Barley from Lu-Ninshubur to Lu-Baba son of Lu-kalla; seal Lú-dBa-ba6 ds d. Lú-kal-la
1	subgenre_remarks	Barley from Lu-igimaåe to Lu-melam; seal: Lú-me-lám dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Barley from Lu-melam to Ur-Igalim; seal: Ur-dIg-alim ds d. Ur-ni9-gar
1	subgenre_remarks	Barley from Lu-melam to Ur-du10-ùr-ra su-su-dam; seal Gù-dé-a énsi Lagashki Ur-d.Du10-ùr-ra d. Ur-dEN.ZU rá-gaba ir11-zu
1	subgenre_remarks	Barley from Lu-melam; seal illegible (CBT 2)
1	subgenre_remarks	Barley from Ludingirra to Isnati; case unopened; seal: Lú-∂Nin-[] dubsar dumu Lú-∂Nin-na-[] (CBT 2)
1	subgenre_remarks	Barley from Lugal-SHulgi to Lu-Baba; seal: Lú-dBa-ba6 ds d. Lú-kal-la
1	subgenre_remarks	Barley from Lugal-an-na-túm to Ur-dBa-ba; seal: Ur-dBa-ba6 ds d. Lú-du10-ga sanga dNin-gír-su
1	subgenre_remarks	Barley from Lugal-tuå-du10 to Ur-IÍ-Baba; seal: Ur-∂IÍ-∂Ba-ba6 dubsar dumu[] (CBT 2)
1	subgenre_remarks	Barley from Lugal-íd-ru, she-ba géme ì-sur kishib SHesh-kal-la; seal: SHesh-kal-la ds d. Ur-ab-ba
1	subgenre_remarks	Barley from Lugalmagan to Íakuge; seal: Íà-kù-ge dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Barley from Lugina to Lu-Baba; seal: Lú-∂Ba-ba6 dubsar dumu [] (CBT 2)
1	subgenre_remarks	Barley from Lugina to Ur-Igalim; seal: Ur-dIg-alim ds d. Lú-dNin-gír-su.
1	subgenre_remarks	Barley from Lukalla to Lumelam, gìr Ur-∂Ig-alim; seal: Lú-me-lám dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Barley from Lukalla to Lumelam; seal: Lú-me-lám dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Barley from Lukalla to Luåagamu; seal: Lú-åa6-ga-mu dubsar dumu Lugal-á-zi-da (CBT 2)
1	subgenre_remarks	Barley from Lú-Igimashe to Ur-Ninmarki; seal: Ur-èsh-kù-ga ds d. Ab-ba-gi-na.
1	subgenre_remarks	Barley from Lú-ba-a; gìr SHà-kù-ge; seal: Ur-dNin-mug en-zi-an-na en-ki-ág-dNanshe Nimgir-di-ne ds X-na ir11-zu
1	subgenre_remarks	Barley from Lú-bi-mu to Ab-ba-mu; seal: Ab-ba-mu ds d. Na-ba-sha6.
1	subgenre_remarks	Barley from Lú-dNin-shubur to Lugal-ezem; seal: Lugal-ezem ds d. Da-da
1	subgenre_remarks	Barley from Lú-dingir-ra to Ur-dDa-mu; seal: Ur-dDa-mu ds d. Lú-[]
1	subgenre_remarks	Barley from Lú-du10-ga to Lú-ush-gi-na; seal: Lú-ush-gi-na ds
1	subgenre_remarks	Barley from Lú-gi-na for 2 persons: dSHul-gi-ur-shu-ru-uq, dSHul-gi-kalam-ma-me-te-bi; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley from Lú-gi-na for mur-gu4; seal: A-tu d. Lú-dNin-gír-su lú-shim
1	subgenre_remarks	Barley from Lú-gu-la to Ur-dIshtaran; seal: Ur-dIshtaran ds d. Na-ba-sha6.
1	subgenre_remarks	Barley from Lú-kal-la to Ur-SHulpae; seal: Ur-dSHul-pa-è d. []
1	subgenre_remarks	Barley from Lú-me-lám kishib Lú-dBa-ba6 gìr Ur-dIg-alim má Ur-dBa-ba6; seal: Lú-dBa-ba6 ds d. Lú-[]
1	subgenre_remarks	Barley from Lú-∂Nin-åubur to Urmes. Seal dedicated to Åulgi, Ur-mes dub-sar dumu [...] ir11-zu (CBT 3)
1	subgenre_remarks	Barley from Mani to Ur-ni9-gar; case unopened; seal: Ur-ni9-gar dumu Ur-sukkal (CBT 2)
1	subgenre_remarks	Barley from Mansi to Ur-Igalim; seal: Ur-∂Ig-alim àr-àr ∂Nin-gír-su dumu Lugal-[] (CBT 2)
1	subgenre_remarks	Barley from Mansum to Lugal-kiag; seal: Lugal-ki-ág dubsar dumu Ur-[dun] (CBT 2)
1	subgenre_remarks	Barley from Namhani to Lú-dingir-ra; seal: Lúd-dingir-ra d. NI-NI-mu lú-ùr
1	subgenre_remarks	Barley from Namzitarra to Luågina; seal: Lú-uå-gi-na (only) (CBT 2)
1	subgenre_remarks	Barley from Nana for the brewer Lu-Baba in Egibille; seal: Lú-∂Ba-ba6 dumu ∂Nanåe-kam lú-åim (CBT 2)
1	subgenre_remarks	Barley from Nì-ú-rum to Ur-dNanshe; seal: Ur-dNin-gír-su ds d. Ur-dNanshe
1	subgenre_remarks	Barley from SHu-Esh4-tár to Ur-ni9-gar; seal: Ur-ni9-gar ds d. Ba-a shabra.
1	subgenre_remarks	Barley from SHà-kù-ge and Lú-dNin-gír-su; seal: Lú-me-lám ds d. Lú-kal-la
1	subgenre_remarks	Barley from SHà-kù-ge to Ur-SHulpae; seal: Ur-an-si4-an-na-tum d. Hé-sha6
1	subgenre_remarks	Barley from SHà-kù-ge to Ur-bàd-tibir-ra in the field shàr-ra-mu-gi4; seal: Ur-bàd-tibir-ra ds d. Ur-[]
1	subgenre_remarks	Barley from SHà-kù-ge; kishib Lú-sha6-ga; seal: Lugal-ti-ra-ásh-e ds d. Na-mu
1	subgenre_remarks	Barley from Ur-Baba to A-igi-du8-a; seal: Lú-dNin-gír-su d. Ab-ba-kal-la nu-bànda-gu4.
1	subgenre_remarks	Barley from Ur-Baba to Mansina; seal: Ma-an-sì-na ds d. Lú-kiri4-zal.
1	subgenre_remarks	Barley from Ur-Baba to Ur-sha6-ga; seal: Ir3-ra-nu-id ds d. Ur-sha6-ga
1	subgenre_remarks	Barley from Ur-Enlilla to Lu-dingirra; seal: Lú-dingir-ra d. Amar-gul.
1	subgenre_remarks	Barley from Ur-Enlilla to Ludingirra gu-za-lá; seal: Lú-dingir-ra dumu Amar-gul (CBT 2)
1	subgenre_remarks	Barley from Ur-Enlilla to Mani the ka-gur7; seal: Ma-ni sagi dGù-dé-a d. Ur-dLama.
1	subgenre_remarks	Barley from Ur-Enlilla to Ur-gar; seal: Ur-gar ds d. A-tu ds hé-dab5
1	subgenre_remarks	Barley from Ur-Enlilla to Ur-ki-síg-ka; seal: Ur-ki-síg-ka ds d. dNanshe-kam ugula
1	subgenre_remarks	Barley from Ur-Nanshe to Ur-Baba; seal: Ur-dNanshe ds d. Ur-dLama sanga dNin-shubur
1	subgenre_remarks	Barley from Ur-Nungal to Duduni; case adhering to the tablet; seal: Du-du-ni []
1	subgenre_remarks	Barley from Ur-Sin to Ur-SHulpae, lú shim; seal: Ur-dSHul-pa-è d d.[] lú-shim
1	subgenre_remarks	Barley from Ur-ab-ba to Ur-dNanshe; seal: Ur-dNanshe ds d. Nam-mah
1	subgenre_remarks	Barley from Ur-abba to Ur-Lamma; seal: Ur-∂Lamma dubsar dumu Ur-[] (CBT 2)
1	subgenre_remarks	Barley from Ur-badtibira to Kaamu; seal: Ka5-a-mu ds d. Lugal-bára-ge-si.
1	subgenre_remarks	Barley from Ur-badtibira to Lushaga, to be returned; seal: Nam-zi-tar-ra ds d. Ba-zi.
1	subgenre_remarks	Barley from Ur-badtibira to Ur-kigula, to be returned; seal: Ur-ki-gu-la d. Ush-mu nu-bànda-gu4.
1	subgenre_remarks	Barley from Ur-badtibirra to Abba-kalla; seal: Ab-ba-kal-la d. dUtu-bar-ra.
1	subgenre_remarks	Barley from Ur-badtibirra to Belimu, to be returned; seal: Lú-dIgi-ma-shè ds d. Lú-dNin-[].
1	subgenre_remarks	Barley from Ur-badtibirra to Belimu; seal: Lú-dIgi-ma-shè ds d. Lú-dNin-[] [].
1	subgenre_remarks	Barley from Ur-badtibirra to Lu-Baba; seal dedicated to [Ibbi-Sin], Lú-dBa-ba6 ds d. Al-la-mu.
1	subgenre_remarks	Barley from Ur-badtibirra to Lu-dingirra son of A-li-ih; seal illegible.
1	subgenre_remarks	Barley from Ur-badtibirra to Lu-dingirra; seal: Lú-dingir-ra ds d. []
1	subgenre_remarks	Barley from Ur-badtibirra to Lu-igimashe; seal: Lú-dIgi-ma-shè ds d. Ur-[] ú-du-lu.
1	subgenre_remarks	Barley from Ur-badtibirra to Lugal-gú-gal; seal: Lugal-gú-gal ds d. Lú-dBa-ba6.
1	subgenre_remarks	Barley from Ur-badtibirra to Lugal-nirgal; seal: Lugal-nir-gál d. Ur-dun gudu4 dLama-ka.
1	subgenre_remarks	Barley from Ur-badtibirra to Lugal-siggid, to be returned; seal: Lugal-síg-sud4 ds d. Ur-dLama énsi Lagashki.
1	subgenre_remarks	Barley from Ur-badtibirra to Lugal-síg-sud4; seal: Nin-agrig-zi dam Lugal-síg-sud4 dub-sar.
1	subgenre_remarks	Barley from Ur-badtibirra to Lugalezem; seal: Lugal-ezem d. Ur-dIshkur sagi.
1	subgenre_remarks	Barley from Ur-badtibirra to Lú-sha6-ga, to be returned a-ma-nu-ta; seal: Lú-sha6-ga ds d. Ur-dLama.
1	subgenre_remarks	Barley from Ur-badtibirra to Nabasha; seal: Na-ba-sha6 [].
1	subgenre_remarks	Barley from Ur-badtibirra to Namzitarra; seal: Lú-dNin-gír-su ds d. Ur-dBa-ba6.
1	subgenre_remarks	Barley from Ur-badtibirra to Namzitarra; seal: Lú-dNin-shubur ds d. Ur-dBa-ba6.
1	subgenre_remarks	Barley from Ur-badtibirra to Ur-Alla to be returned; seal: Ur-dAl-la d. Ur-dIg-alim.
1	subgenre_remarks	Barley from Ur-badtibirra to Ur-Ishkur, to be returned; seal: Ur-dIshkur d. E-a [].
1	subgenre_remarks	Barley from Ur-badtibirra to Ur-Lama, to be returned; seal: Ur-dLama d. Ur-dIshkur sagi.
1	subgenre_remarks	Barley from Ur-badtibirra to Ur-Ningirsu; seal: Ur-dNin-gír-su ds d. Ur-dBa-ba6.
1	subgenre_remarks	Barley from Ur-badtibirra; seal: Ur-sha6-sha6-[] sagi d. E2-bur-ba-X]
1	subgenre_remarks	Barley from Ur-badtibirra; to be returned; seal: Bur-sag-ki-du10 àr-àr-d[] d. Lú-d[]
1	subgenre_remarks	Barley from Ur-bàd-tibir-ra to Ur-dLama; seal: Ur-dLama ds d. Ir11-mu
1	subgenre_remarks	Barley from Ur-bàd-tibir-ra to Ur-dNin-mar.ki; seal: Ur-dNin-mar-ki ds d. Lú-ushumgal
1	subgenre_remarks	Barley from Ur-bàd-tibir-ra, Gishgal-di d. Mu-ni su-su-dam; seal: Gishgal-di d. Mu-ni []
1	subgenre_remarks	Barley from Ur-bàd-tibir-ra, kishib Ku5-da-mu dumu sanga [] gìr Ka5-a-mu ì-dub []; seal: Lú-dBa-ba6 ds d. Du-du? sanga []
1	subgenre_remarks	Barley from Ur-bàd-tibir-ra; seal: Ur-dNanshe ds d. Al-la
1	subgenre_remarks	Barley from Ur-bàd-tibira to Lú-sha6-ga; seal: Lú-sha6-ga ds d. Lú-dgis.gibil-ga-mes nu-bànda
1	subgenre_remarks	Barley from Ur-dIg-alim kishib Lú-dNa-rú-a d. Na-ba-sha6 gìr Lú-kal-la; seal: Lú-dNa-rú-a ds d. Na-ba-sha6
1	subgenre_remarks	Barley from Ur-dNanshe to Ur-dNanshe son of Na-ba-sha6; seal: Ur-dNanshe ds d. Na-ba-sha6
1	subgenre_remarks	Barley from Ur-sha6-ga the cook to Lugal-inimgina; seal: Ur-dBa-ba6 ds d. Ha-ba-zi-zi.
1	subgenre_remarks	Barley from Ur-sha6-ga to dUtu-mu; seal: dUtu-mu ds d. dNanshe-kam
1	subgenre_remarks	Barley from Ur-èsh-kù-ga to Ur-dBa-ba6; seal: Ur-dBa-ba6 ds d []
1	subgenre_remarks	Barley from Urbadtibira to Urbagar, to be returned; seal: Ur-ba-gár ds d. Ur-dBa-ba6
1	subgenre_remarks	Barley from Urbadtibirra to Abbakalla in the temple of Gishbare; seal: Ab-ba-kal-la (ds?) d. Ur-dam.
1	subgenre_remarks	Barley from Urbadtibirra to Lu-Dumuzi; seal: Lú-dDumu-zi ds d. Ur-dBa-ba6
1	subgenre_remarks	Barley from Urbadtibirra to SHa6-ga, to be returned; [seal].
1	subgenre_remarks	Barley from Urgar to Ur-dIgi-ma-shè; seal: Ur-dIgi-ma-shè ds d. Ur-dNin-gír-su
1	subgenre_remarks	Barley from Uru-sag-rig7ki as fodder for sheep; seal: SHà-kù-ge ds d. Lú-kal-la
1	subgenre_remarks	Barley from dUtu-a received by Ur-dNanshe; seal: Ur-dNanshe ds d. Na-ba-sha6
1	subgenre_remarks	Barley from several persons; seal: Ur-ki-sal4-la d. Lugal-pa-è
1	subgenre_remarks	Barley from the  sanga of dNin-mar-ki to Sag-du; seal: Ur-dub-shen d. Ha-zi sipa anshe
1	subgenre_remarks	Barley from the boat of Lú-GIÍ.gigir; kiåib Lú-me-lám; seal illegible (CBT 2)
1	subgenre_remarks	Barley from the field za-ha-tin; she bala-a-shè from Lú-dingir-ra to Ur-dEn-líl-lá; seal: Ur-dEn-líl-lá ds d. Ka-sha6 kurushda
1	subgenre_remarks	Barley from the garden of Ninlilgal (giå.kiri6 ∂Nin-líl-gal); seal: Ur-ni9-gar dubsar dumu Lú-∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Barley from the sanga of Nin-MAR.KI to Utubarra; case unopened; seal: ∂Utu-bar-ra dumu A-tu àga-uå (CBT 2)
1	subgenre_remarks	Barley from the sanga of Ninmarki to Ur-Lama; seal Ur-dLama ds d. Na-ba-sha6.
1	subgenre_remarks	Barley from the storehouse of Urub transferred to Urgar; case unopened; seal: Ur-gar dubsar dumu Lugal-gaba (CBT 2)
1	subgenre_remarks	Barley from å-da-da to Atu; case unopened; seal: A-tu dubsar dumu Na-di-lí (CBT 2)
1	subgenre_remarks	Barley from é-shu-sum-ma from Lú-me-lám; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Barley fron Bazi to Sì-du, she a-shà Du11-ga-ni-zi; seal: A-hu-ma d. Dingir-a-mu sipa-udu-niga
1	subgenre_remarks	Barley given by ·z-ú-ú to 3 persons; seal: Ur-dIg-alim d. Lú-[gar?] àr-àr dNin-gír-su
1	subgenre_remarks	Barley in the control of the fattener Lú-me-lám; seal: Lú-me-lám d. Ur-Ma-ma kurushda.
1	subgenre_remarks	Barley issued as fodder for sheep by single days; seal: Ur-∂EN.ZU dumu Ur-[gú-en-na rá-gaba] (CBT 2)
1	subgenre_remarks	Barley issued by Lú-gi-na to Hu-ba-gi, U3-bi, Gu-ba-nu-um máå-åu-gíd-gíd; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Barley kusha-lá má-ad-ma-gaki, from Nabasha to Kaamu; seal: Ka5-a-mu ds d. Hé-ti.
1	subgenre_remarks	Barley lent for engar and nu-bànda by the sanga of Nin-MAR.KI to Ir11-mu; case unopened; seal: Lú-∂Giå-bar-è dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Barley loaded on a boat from Gudea to Atu; case unopened; seal: A-tu dubsar dumu Lú-∂[Nanåe] dub-sar hé-dab5 (CBT 2)
1	subgenre_remarks	Barley loaden on a boat from dUtu-bar to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ur-dNanshe shabra-[].
1	subgenre_remarks	Barley loaden on a boat, from Bazi to Ur-Hendursag; seal: Lú-gi-na ds d. Ur-ba-gár.
1	subgenre_remarks	Barley loaden on a boat, from sanga dNanshe to Ma-an-sì-na; seal: Ma-an-sì-na ds d. Lú-kiri4-zal
1	subgenre_remarks	Barley loaden on a boat; from Ur-Baba to Mansum; case + tablet inside; seal Ma-an-sì-na ds d Lú-kiri4-zal
1	subgenre_remarks	Barley loaden on boats for Nippur, from Bazi to Dada; seal: Da-da ds d. Ur-dBa-ba6.
1	subgenre_remarks	Barley loan for plowmen from Bazi to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ur-dLama
1	subgenre_remarks	Barley loan for the érin from Ur-Nanshe to Lugal-inim-gi-na; seal: Lugal-inim-gi-na ds d. A-tu.
1	subgenre_remarks	Barley loan for érin from Bazi to Unil; case unopened; seal: Un-íl dumu Ur-∂EN.ZU (CBT 2)
1	subgenre_remarks	Barley loan for érin from Lú-dDumu-zi to Lú-dingir-ra; seal: Lú-dingir-ra ds d. Ur-sha6-ga
1	subgenre_remarks	Barley loan from Bazi to Urbagar; case unopened; seal: Ur-ba-gár dubsar dumu [] (CBT 2)
1	subgenre_remarks	Barley loan received by Nammah, for the girsiga of the household of Nindara; seal: Nam-mah-∂Ba-ba6 dumu Ku-li muhaldim sagi ∂Nin-dar-a (CBT 2)
1	subgenre_remarks	Barley loan to érin from Ur-Baba to Lu-Ningirsu (CBT 2). A: Case of 19948; seal: Lú-∂Nin-gír-su dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Barley loaned by Bazi to Mansi; case unopened; seal: Ma-an-sì dumu Lú-∂[] (CBT 2)
1	subgenre_remarks	Barley loaned by Ur-Ningal to Nalu; Shulgi 45/Amar-Suen 2; case unopened; seal: Na-lu5-ú ugula dumu Íe/Íar?-[] (CBT 2)
1	subgenre_remarks	Barley loaned from Ur-Igimaåe to Lueåsa; case unopened; seal: Lugal-zag-ge-si dumu Lú-du10-ga nu-bànda; mu Ur-gi4-lum˚ ba-hul; Shulgi 45/Amar-Suen 2 (CBT 2)
1	subgenre_remarks	Barley loaned to åà-gu4 and érin from Lugina to Akalla (CBT 2). A: Case of 17789; seal: A-kal-la dubsar dumu Ur-∂Nin-gis-zi-da (CBT 2)
1	subgenre_remarks	Barley lá-ni su-ga [] d. Ur-é-[] ki Ur-bàd-tibir-ra-ta kishib Ur-dBa-ba6 shim dSHul-gi sá-du11 dSHul-gi gìr Lú-dSHim-kù; seal illegible
1	subgenre_remarks	Barley má ir11 d. Nì-sha6-ga from Ur-gishgigir to Lú-dNin-gír-su; seal: Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	Barley nì-gál-la a-shà e-na-›RIM-ne, from Ur-mes to Ma-an-sum; seal Ma-an-sum ds d. Lugal-[]
1	subgenre_remarks	Barley nì-gál-la from Ikalla; case unopened; seal: Gu-za-ni dubsar dumu Lú-dingir-ra åa13-dub-ba (CBT 2)
1	subgenre_remarks	Barley of Enlilla received by Gù-dé-a; seal: Gù-dé-a ds d. Ur-dUtu
1	subgenre_remarks	Barley on boats from Nabaåa to Urkisalla; case unopened; seal: Ur-ki-sal4-la dumu Lugal-pa-è (CBT 2)
1	subgenre_remarks	Barley on the boat of Ur-Baba son of Dúr-du10; seal: Lú-gish-zi ds d. Lú-a-[]
1	subgenre_remarks	Barley produced by the field a-ba-al-la harvested by Ur-ni9-gar and Lú-dingir-ra, son of the énsi; sealed (CBT 2)
1	subgenre_remarks	Barley rations (åe-ba da-ba-ke4 tuå é-gal) from Lu-Lagaå to Lugal-gugal; seal: Lugal-gú-gal dubsar dumu Lú-∂[Ba-ba6] (CBT 2)
1	subgenre_remarks	Barley rations (åe-ba kab-ra áb itu 2-kam) from Ur-bagar to Ur-åa6-ga-mu; case unopened; seal: Ur-åa6-ga-mu dubsar dumu Lugal-inim-gi-na; months xi-2-xii (CBT 2)
1	subgenre_remarks	Barley rations for Ursheilla and Alla coming from Ur-ISH-Baba; [seal].
1	subgenre_remarks	Barley rations for donkeys, from Mash-mash; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley rations for dumu-dab5-ba from Lú-du10-ga to Ur-Ningiszida; seal: Ur-dNin-gis-zi-da ds d.SHesh-kal-la.
1	subgenre_remarks	Barley rations for engar from Ur-Nanåe to Lugaluruda sa12-du5; case unopened; seal: Lugal-uru-da sa12-du5 dumu [å-zi-da] sa12-du5 (CBT 2)
1	subgenre_remarks	Barley rations for gurush employed as water bearer; [seal].
1	subgenre_remarks	Barley rations for géme and nu-bànda; seal: Géme-dLama nin-dingir dBa-ba6 Ur-dDa-mu ds d. Ur-sha6-ga ir11-zu
1	subgenre_remarks	Barley rations for plowmen and their helpers from Bazi to Ur-é-ninnu; seal: Ur-é-ninnu ds d. Al-la-mu shabra
1	subgenre_remarks	Barley rations for sheep; kishib Ur-dEN.ZU, Lú-Má-ganki; seal: Ur-dEN.ZU d. Ur-gú-en-na
1	subgenre_remarks	Barley rations for sig7-a, gurush and dù-a-ku5; seal: Ur-dNanshe d. Lum-ma
1	subgenre_remarks	Barley rations for the dumu mar-sa-me from Lugina, delivered at the place of the sukkal-mah; seal: Ur-dBa-ba6 ds d. Na-mu.
1	subgenre_remarks	Barley rations for the un-íl in the gìr-sì-ga gish-gi from Bazi to Habazizi; seal: Ha-ba-zi-zi ds d. Lú-kal-la nu-bànda
1	subgenre_remarks	Barley rations for the àga-ush mar-tu; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley rations for weaver women in Ur, from Nanna-iåa to Ur-ni9-gar; seal: Ur-ni9-gar dubsar dumu Lú-∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Barley rations for àga-ush delivered by Ahuni, gìr A-pil-zu-zi; seal: Ur-dBa-ba6 ds d. Na-mu.
1	subgenre_remarks	Barley rations from Ur-badtibirra to Ur-Baba the ú-íl; seal: Ur-dBa-ba6 d. Lú-dNin-gír-su
1	subgenre_remarks	Barley received by En-ni-lu; seal: En-ni-lu ds d. Lugal-d[].
1	subgenre_remarks	Barley received by Lu-Baba from Ur-Enlilla; case unopened; seal: Ur-∂Ba-ba6 dumu Ur-GIÍ.gigir ugula (CBT 2)
1	subgenre_remarks	Barley received by Lu-Nanna; seal: Lú-dNa-rú-a ds d. Ur-sha6-ga
1	subgenre_remarks	Barley received by Lugal-shà-lá son of Me-dingir; seal illegible.
1	subgenre_remarks	Barley received by Nammah from Ur-∂Igi-ma-åè; unopened envelope; seal: Nam-zi-tar-ra dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Barley received by Ur-Baba from Ur-ni9-gar; seal illegible (CBT 2)
1	subgenre_remarks	Barley received by Ur-Babba; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Barley received by Ur-Kalkal from several persons; seal: Lú-dKal-kal ds d. Ur-dLama
1	subgenre_remarks	Barley received by Ur-Ninmug and Ur-åa6-ga for hired labourers (CBT 2). A: Case of 15966; barley received by Ur-∂Nin-mug and Ur-åa6-ga for hired labourers; seal: Ur-åa6-ga dumu Gudu4-mu gudu4 ∂Nin-dar-a (CBT 2)
1	subgenre_remarks	Barley received by Ur-dam; seal: Ur-dam d. Lú-dBa-ba6 ga-esh8 Gú-ab-baki.
1	subgenre_remarks	Barley received by Ur-∂Iåtaran from Ur-bàd-tibir-ra; seal: Ur-∂Iåtaran dubsar dumu [] (CBT 2)
1	subgenre_remarks	Barley received by Ur-∂Nanåe from Ur-ab-ba; su-su-da; seal: Ur-∂Nanåe dubsar dumu Nam-mah (CBT 2)
1	subgenre_remarks	Barley received by Urpumah from Iemu; 18 sìla she á 5 sìla síg-bi 12 sar-àm; seal: Ur-pú-mah ds d. Lú-[  ].
1	subgenre_remarks	Barley received by Íakuge; seal: Íà-kù-ge [ds dumu Lú-kal-la] (CBT 2)
1	subgenre_remarks	Barley returned by Ur-Baba; seal: Ur-gar ds d. Lugal-gaba
1	subgenre_remarks	Barley returned by Ur-Ningirsu; kiåib Urgar; case unopened; seal: Ur-gar dubsar dumu [] (CBT 2)
1	subgenre_remarks	Barley returned to Lú-dingir-ra; seal: Lú-kiri4-zal dumu Ur-d[]
1	subgenre_remarks	Barley seed for Ur-Nanshe to Ur-Nanna; seal: Lú-dNa-rú-a ds d. Ur-dBa-ba6
1	subgenre_remarks	Barley seed from Ur-Lamma sanga of Ninåubur to Uråaga; case unopened; seal: Ur-åa6-ga dubsar dumu Ur-gu-la (CBT 2)
1	subgenre_remarks	Barley seed received by Lu-Ningirsu from Bazi; case unopened; seal illegible (CBT 2)
1	subgenre_remarks	Barley send from A-li-ih to Lú-dNin-gírid(GIR3xKAR2)-da; seal: Lú-zi-nam d. Inim-na-na
1	subgenre_remarks	Barley shukur énsi from Bazi to Lú-dBa-ba6; seal: Lú-dBa-ba6 d. dNanshe-kam lú-shim
1	subgenre_remarks	Barley shà-gal udu from Lú-kal-la to Lú-ba-a (=Lú-dBa-ba6); seal: Lú-dBa-ba6 ds d. Lú-kal-la
1	subgenre_remarks	Barley shà-gal udu from Namhani to Lugal-igi-hush; seal: Lugal-igi-hush ds d. La-la shabra
1	subgenre_remarks	Barley to buy food (åe åà-gal kù-ta sa10-åè), from Ur-Baba received by Irra-nuid; case unopened; seal: Ir3-ra-nu-id dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Barley to buy oxen, from Atu to Urdukuga; seal: Lú-é-[] ugula gurush-e-ne Ur-du6-kù-ga
1	subgenre_remarks	Barley to buy reed for Ur-Nanshe; seal: Ur-dNanshe ds d. Al-la.
1	subgenre_remarks	Barley to buy reed in Ur, from Bazi to Lu-Nina; seal: Lú-dNinaki ds d. Ur-dNanshe.
1	subgenre_remarks	Barley to buy reed; from Ur-Enlilla; seal illegible
1	subgenre_remarks	Barley to fatten sheep, from A-gi4 to Lú-kal-la; seal Ur-é-ninnu ds d. Lú-du10-ga sanga dNin-gír-su
1	subgenre_remarks	Barley to fatten sheep; seal: Lú-dKal-kal ds d. Ur-dLama
1	subgenre_remarks	Barley transfer; kishib Lú-má-gu-la; seal: Lú-má-gu-la ds d. []
1	subgenre_remarks	Barley transfer; seal illegible
1	subgenre_remarks	Barley transferred from Bazi to Mansina; case unopened; seal: Ma-an-sì-na dubsar dumu Lú-kir4-zal (CBT 2)
1	subgenre_remarks	Barley transferred from Guzani to Lugal-ezem; É-sa-ra-hi-ta; case unopened; seal: dumu [] / Lugal-ezem sic! (CBT 2)
1	subgenre_remarks	Barley transferred from Lu-Baba to Ur-Baba son of Bazi; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Barley transferred from Lú-dingir-ra to Ur-∂En-líl-lá (CBT 2). A: Case of 16457; seal: Ur-∂En-líl-lá dubsar dumu Inim-åa6 kuruåda (CBT 2)
1	subgenre_remarks	Barley transferred from Mani to Ur-tibir-ra; case unopened; seal: Ur-bàd-tibir-ra dumu Gu-[]; Shulgi 45/Amar-Suen 2 (CBT 2)
1	subgenre_remarks	Barley transferred from Nimgirannezu to Lugalluåaåa; case unopened; seal: Lugal-lú-åa6-åa6 dubsar dumu Nimgir-åà-kúå-an-na (CBT 2)
1	subgenre_remarks	Barley transferred from Ur-Enlilla to Ur-ki-síg-ka, åe åà-gal érin-na; seal: Ur-ki-síg-ka dubsar dumu ∂Nanåe-kam ugula (CBT 2)
1	subgenre_remarks	Barley transferred from Ur-Igalim to Atu; case unopened; seal: A-tu dubsar dumu Lú-∂Nanåe dubsar hé-dab5 (CBT 2)
1	subgenre_remarks	Barley transferred from Ur-Nanåe to Ur-Nanåe; case unopened; seal: Ur-∂Nanåe dubsar dumu Ur-é-an-na (CBT 2)
1	subgenre_remarks	Barley transferred from Ur-Ningiszida to Ur-Nanåe (CBT 2). A: Case of 18206; seal: Ur-∂Nanåe dubsar dumu Lú-du10-ga ka-gur7-ka (CBT 2)
1	subgenre_remarks	Barley transferred from Ur-Nungal to Dada; case unopened; seal: Da-da dubsar dumu Ur-kal-la; Shulgi 45/Amar-Suen 2 (CBT 2)
1	subgenre_remarks	Barley transferred from Uråaga to Lubimu (CBT 2). A: Case of 18767; seal: Lú-bi-mu dubsar dumu Ur-∂Ig-alim (CBT 2)
1	subgenre_remarks	Barley transferred from the sanga of Ninmar to Íeå-åeå; case unopened; seal: Íeå-åeå dubsar dumu Nam-ha-ni (CBT 2)
1	subgenre_remarks	Barley unloaded from the boat of Ir11-mu; seal: Lú-Nina.ki dubsar dumu Ur-[∂Nanåe] (CBT 2)
1	subgenre_remarks	Barley wages of SHulgi-bani from Turam-ili; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley which Ur-Igalim has to return (CBT 2). A: Case of 18782; seal: Ur-∂Ig-alim dubsar dumu Ur-[] (CBT 2)
1	subgenre_remarks	Barley á lú hun-gá á má hun-gá ù á é-duru5 nu-zi-zi; seal: Ur-dBa-ba6 ds d. Na-ba-sha6
1	subgenre_remarks	Barley åà-gal hé-dab5; seal: Ur-é-ninnu dubsar dumu Lú-du10-ga sanga ∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Barley åà-gal udu from Atu; seal: Lugal-gú-gal dubsar dumu Lú-∂[ ] (CBT 2)
1	subgenre_remarks	Barley, SHu-igi-du sá-du11 dNin-a-zu ki Ur-bàd-tibir-ra kishib Ur-dNanshe; seal: Lú-bi-mu d. Ur-dNanshe
1	subgenre_remarks	Barley, for seed and wages, from Alla to Atu; seal: A-tu ds d. Na-di-lí.
1	subgenre_remarks	Barley, gur of 62 sìla, for flour, she nì-gál-la é-dNin-gír-su-ta kishib Ma-an-sì; seal: Ma-an-sì ds d. Lugal-[]
1	subgenre_remarks	Barley, gur zabar-ta sá-du11-shè from Bazi to SHesh-shesh; seal: SHesh-shesh d. NI.NI lú-ùr-ra (ùr written nigin)
1	subgenre_remarks	Barley, gìr Hu-pu-uk-she-en; seal: Ur-dEn-líl-lá ds d. Ka-sha6 kurushda.
1	subgenre_remarks	Barley, kishib Ur-bàd-tibir-ra Nam-zi-tar-ra tùm-dam zi-re-dam; seal: Nam-zi-tar-ra ds d. Ba-zi.
1	subgenre_remarks	Barley, lá-ni káb-du11-ga, to be returned to the temple of Nanshe; seal: Ur-é-ninnu ds d. Al-la-mu shabra.
1	subgenre_remarks	Barley, lá-ni su-ga Ur-dun má-lah4 kishib Lú-kal-la gìr Ur-dBa-ba6 gu-za-lá; seal: Ur-dBa-ba6 ds d. Lú-du10-ga sanga dNin-gír-su
1	subgenre_remarks	Barley, lá-ni su-ga from Abbakalla to Lú-du10-ga; seal: Lú-du10-ga ds d. Ur-dBa-ba6
1	subgenre_remarks	Barley, lá-ni su-ga from Gudea to Mani;  seal: Ma-ni sagi dGù-dé-a d Ur-dLama.
1	subgenre_remarks	Barley, lá-ni su-ga from Lú-dNin-gír-su to Lú-ush-gi-na; seal: Lú-ush-gi-na ds
1	subgenre_remarks	Barley, lá-ni su-ga from Ur-Baba to Ur-Enlilla; seal: Ur-dEn-líl-lá ds d. Ka-sha6 kurushda
1	subgenre_remarks	Barley, lá-ni su-ga from Ur-dNin-gis-zi-da to Lú-kal-la; seal: Ur-é-ninnu ds d. Lú-du10-ga sanga d.Nin-gír-su
1	subgenre_remarks	Barley, mur-gu4, she-numun a-shà a-làl-shè mu Ur-bàd-tibir-ra-shè kishib Ur-dBa-ba6 gìr Lú-dPa-du; seal: Ur-dBa-ba6 d. Ur-sha6-sha6 sagi é-dBa-ba6?
1	subgenre_remarks	Barley, regular delivery for rations, from Ur-Ningiszida to dUtu-a; seal: dUtu-a ds d. Ur-dNanshe.
1	subgenre_remarks	Barley, she lá-ni su-ga ki Pú-ta-ta kishib Ur-tur; seal Ur-gar ds d. Lugal-lú-sha6-sha6
1	subgenre_remarks	Barley, she lá-ni su-ga shà-gal gu4-udu from Ur-Baba to Lugal-gugal; seal: Lugal-gú-gal ds d. Lú-dBa-ba6
1	subgenre_remarks	Barley, she nì-gál-la A-pi4-sal4-ta from Ikalla to Ur-Nanshe; seal: Ur-dNanshe ds d. Lú-du10-ga ka-gur7-ka.
1	subgenre_remarks	Barley, she nì-gál-la from Nadi to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ba-zi.
1	subgenre_remarks	Barley, she nì-gál-la ki En-e-ki-ág; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Barley, she nì-gál-la ki I3-kal-la-ta; she-ba sipa mar-tu-shè; seals: Nì-ú-rum ds d. Ku-li nu-bànda, Ur-sha6-ga-mu d. Ku-li
1	subgenre_remarks	Barley, she nì-gál-la ki Na-ba-sha6 sa12-du5-ka; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Barley, she nì-gál-la, from Lú-é-sukud-rá to dUtu-a; seal: dUtu-a ds d. Ur-dNanshe
1	subgenre_remarks	Barley, she shà-gal udu; seal illegible
1	subgenre_remarks	Barley, she zì-ka from Lú-ki-nu-nirki; seal: Ur-dBa-ba6 ds d. Ur-íd-eden-na
1	subgenre_remarks	Barley, she á lú-hun-gá gishkiri6 dSHul-gi; seal: Lú-dNin-gír-su ds d. I3-kal-la
1	subgenre_remarks	Barley, she á-géme from Lú-kal-la to Ur-Ishtaran; seal: Ur-dIshtaran ds d. Na-ba-sha6
1	subgenre_remarks	Barley, she-ba ì-du8 and shim; seal: Gìr-dBa-ba6-ì-dab5 shabra [] ir11-zu
1	subgenre_remarks	Barley, she-zì-ka ki Ur-é-gal-ta kishib Ur-dBa-ba6 gìr Lú-dingir-ra gu-za-lá; seal: Ur-dBa-ba6 ds d. Ur-íd-eden-na
1	subgenre_remarks	Barley, shà-gal amar-ku5-eden-na-shè, from Lugal-ezem to Ur-SHulpae; seal: Ur-dSHul-pa-è d. Du-du-pu-um.
1	subgenre_remarks	Barley, shà-gal gurush érin from Ur-Baba to []; seal: Ur-ki-gu-la d. Zi-[] ga-[]
1	subgenre_remarks	Barley, shà-gal hé-dab5 ki Ur-bàd-tibir-ra-ta kishib Lugal-bára-ge-si gìr Ur-dBa-ba6; seal: Lú-bára-ge-si ds d. Ur-d[]
1	subgenre_remarks	Barley, shà-gal hé-dab5 é-dLama from Urtur; seal: Ur-tur-tur d. Lú-d[]
1	subgenre_remarks	Barley, shà-gal lú al-dab5-ba ki Nam-ha-ni-ta; seal: Ba-ga-a d. Ur-dBa-ba6
1	subgenre_remarks	Barley, shà-gal udu from Lú-kal-la ta Lú-dKal-kal; seal: Lú-dKal-kal ds d. Ur-dLama
1	subgenre_remarks	Barley, shà-gal udu from Si-dù; seal: Lú-dKal-kal ds d. Ur-dLama
1	subgenre_remarks	Barley, shà-gal udu niga; seal: Géme-dNanshe nin-dingir dBa-ba6 Zum-zum ir11-zu
1	subgenre_remarks	Barley, shà-gal udu, from Lu-Baba to Lu-Ningirsu; seal illegible
1	subgenre_remarks	Barley, shà-gal érin from Ur-dEn-líl-lá to Gududu; seal: Gu-du-du lunga d. Ka-[kù]
1	subgenre_remarks	Barley, shà-gal érin hun from Guzani; seal: Ur-dNanshe d. Ur-sha6-ga
1	subgenre_remarks	Barley, shà-gal érin má-gish-ì-ka from Lú-ush-gi-na to ·-ma-ni; seal dedicated to AS, ·-ma-ni ds d. [] ir11-zu
1	subgenre_remarks	Barley, shà-gal érin-na from Lú-kal-la to Lugal-shà-lá; seal: Lugal-shà-lá d. Lú-[]
1	subgenre_remarks	Barley, shà-gal érin-na from Ur-Nanshe; kishib Ur-gá-nun; seal: Ur-gá-nun ds d. []
1	subgenre_remarks	Barley, si-il-la-ak; seal Ur-dNanshe ds d. A-tu
1	subgenre_remarks	Barley, sá-du11 en-nu-gu-la from Lugal-hé-gál to Na-di; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley, sá-du11 shabra from Má-gur8-re to SHu-dNin-shubur; seal: SHu-dNin-shubur [] ir11 Ur-mes
1	subgenre_remarks	Barley, sá-du11 énsi from Nammah-Baba to Bur-Mama; seal: Bur-Ma-ma dumu Pàd-da-a sanga [] (CBT 2)
1	subgenre_remarks	Barley, zì-ba Ur-dBa-ba6 d. SHesh-tur-tur im-ta shu-ùr-ra ki SHesh-kal-la-ta kishib Ur-dBa-ba6; seal: Ur-dBa-ba6 ds d. []
1	subgenre_remarks	Barley, á lú hun-gá, from Lú-du6-ga-ta; kishib dUtu-mu dumu dab5-ba; seal: dUtu dumu-dab5-ba mu! pro dUtu-mu dumu-dab5-ba
1	subgenre_remarks	Barley, á-lú-hun-gá from Ur-Nanshe; seal: Esh-a-bi d. Ad-da nu-bànda
1	subgenre_remarks	Barley, åe-ba dam-gàr-ne, from Lu-hurim to Ningirsu-inim-iåa; seal: Ur-∂Ba-ba6 dubsar dumu Ab-ba-[mu] (CBT 2)
1	subgenre_remarks	Barley, åà-gal udu-niga-åè; case unopened; seal: Lú-∂Kal-kal dubsar dumu Ur-∂Lamma; Shulgi 47 ii-v (CBT 2)
1	subgenre_remarks	Barley, åà-gal érin bala tuå-a, from Lukalla; seal: Lugal-[Eridu˚-åè] dumu A-tu (CBT 2)
1	subgenre_remarks	Barley, åà-gal érin gi-zi-åè, transferred from Bazi to Dugganizi (CBT 2). A: Case of 21324; seal: Du11-ga-ni-zi dubsar dumu Ur-åa6-ga [sanga ∂Nin-gis-zi-da]; cf 18769a (CBT 2)
1	subgenre_remarks	Barley, è-ba àga-ush ki Hu-ba-a gìr Nu-úr-dEN.ZU ki Lú-gi-na-ta; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Barley-loan; åe ur5-ra engar nu-bànda; largely defaced; case unopened; seal: Ku5-da (CBT 2)
1	subgenre_remarks	Barley; she lá-ni su-ga ki Nimgir-shà-kúsh-ta dUtu-a shu-ba-ti; seal: dUtu-a ds d. Ur-dNanshe
1	subgenre_remarks	Baskets (gir-lam) from Ga-a to Ur-ab-ba, gi girdub síg-kur; seal: Ur-ab-ba ds d. Ba-zi
1	subgenre_remarks	Baskets (giå zi si-ig un-íl-aå) from Urdun received by Lu-Ninåubur; seal: Lú-∂Nin-åubur dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Baskets (gurdub) from Urguenna to Íu-Adad; royal seal of Íu-Sin, Íu-∂Adad dumu [] [nu-bànda] ir11-zu (CBT 2)
1	subgenre_remarks	Baskets and branches of palm-trees transferred from Ur-abba to Ur-Lamma son of Urgar; seal: Ur-∂Lamma dubsar dumu Ur-gar (CBT 2)
1	subgenre_remarks	Baskets for Dada the gala on the order of the sukkalmah, received by the gardener; seal: Ur-∂Lamma dubsar dumu Ir11-mu (CBT 2)
1	subgenre_remarks	Baskets from Ur-abba to Lu-Ningirsu; seal Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	Baskets of dates to the palace for the boat má u4-zal-la; seal: Ur-dIg-alim d. Hu-ru-mu
1	subgenre_remarks	Beans (gú-gal, åe-lú) received by Urdun; seal illegible (CBT 2)
1	subgenre_remarks	Beans for the bala from Ur-é-gal (gú-tur-tur, ú-tir); seal: Nam-ha-ni dubsar dumu Hu-wa-wa (CBT 2)
1	subgenre_remarks	Beans, gú-gal for the field from ›-zi-mu-ta; seal: Lugal-ti-ra-ásh ds d. Lú-dBa-ba6
1	subgenre_remarks	Beans, gú-gal-gal gú-tur-tur, ú-tir from A-gi4 to Nam-ha-ni; seal: Nam-ha-ni ds d. Hu-wa-wa
1	subgenre_remarks	Beans, ku-mul from SHada to Ur-ni9-gar in Tummal; seal: Ur-ni9-gar ds d. Lú-dNanshe.
1	subgenre_remarks	Beer and flour; seal: Lú-[] dubsar dumu Ur-∂[] (CBT 2)
1	subgenre_remarks	Beer as regular delivery to the shabra from Magurre to SHu-Ninshubur; seal: SHu-dNin-shubur àga-ush
1	subgenre_remarks	Beer deliveries; seal: Ur-dLama ds d. Ir11-mu
1	subgenre_remarks	Beer for the king from Lu-Ningirsu; royal seal of SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	Beer for the shabra delivered by Má-gur8-re to SHu-dNin-shubur; seal: SHu-dNin-shubur [] ir11 Ur-mes
1	subgenre_remarks	Beer for the sukkalmah; kishib: Lú-me-lám; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Beer from Bí-du11-ì-sha6 to Ur-ab-ba; from month iv to vii; seal []
1	subgenre_remarks	Beer from Lú-dNin-gír-su for the má-u4-zal-la in the palace; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	Beer transferred to Urlam; seal illegible (CBT 2)
1	subgenre_remarks	Beer? from Ur-Baba to A-gi4; seal: [] []-sha6-ga [dam]-gàr; adherances of the case
1	subgenre_remarks	Bitumen for a 60 gur boat of Lugal-nanga, from Ur-Baba to Ur-Igalim; seal: Ur-dIg-alim ds d. Ur-sha6-ga nu-bànda kurushda.
1	subgenre_remarks	Bitumen for several boats (má lugal, má-uz-ga) from Nì-ga to Ur-Igalim; seal: Ur-dIg-alim ds d. Ur-dBa-ba6 sanga dNin-gír-su.
1	subgenre_remarks	Bitumen for the temple of SHulgi in URUxKAR2ki; from Agi4, gìr Ur-sag-ùbaki; seal 2 cols: Ur-dLama énsi Lagashki Ba-zi ds d. Na-di ir11-zu
1	subgenre_remarks	Bitumen from Al-la-bi to Ur-Baba; seal: Lugal-sha6-ga ds d. Ur-dBa-ba6
1	subgenre_remarks	Bitumen from SHesh-shesh, kishib Ur-dIg-alim; seal: Ur-dIg-alim ds d. Ur-sha6-ga nu-bànda kurushda
1	subgenre_remarks	Bitumen from several rivers, gú-na-kam; seal illegible.
1	subgenre_remarks	Bitumen gi6-gíd-bi ù du10-ush pú lugal ba-ra-du8 kash-dé-a lugal shà Tum-ma-al ki Lú-ki-nu-nir dam-gàr-ta; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Bitumen recorded on the tablet of Lu-Ningirsu-isha; seal: Lú-dNin-gír-su-ì-sha6 d. Ad-da má-lah4.
1	subgenre_remarks	Bitumen, gi-su7 ma-an-sim e-su gíd-dè from Lu-Kinunir; seal: Ur-dIg-alim ds d. Ur-sha6-ga nu-bànda kurushda
1	subgenre_remarks	Bought barley for flour from Ir11; seal: Ur-dBa-ba6 ds d. Ur-íd-eden-na.
1	subgenre_remarks	Bovines for the plowman of Nanshe from Ur-é-gal to Ur-d[Nanshe]; seal: Ur-dNanshe ds d. dNanshe-ì-zu
1	subgenre_remarks	Bovines, a-ru-a An-né-ba-du7-ta ›-úr-bi ùnu ì-dab5; seal: Ur-dun d. ›-úr-bi hi-nì-gá-gàr?.
1	subgenre_remarks	Box 13; faint seal impressions (Kassite style) on edge; 7 lines; *or later
1	subgenre_remarks	Bread and sheep for Ur-sag-pa-è; seal: dSHul-gi-kù-zu ds d. dSHára-kam dub-sar
1	subgenre_remarks	Bread delivered to Lú-é-ba-gár åà A-al-ta-na˚; seal: ∂Íul-gi-kù-zu dubsar dumu ∂Íára-kam dubsar (CBT 2)
1	subgenre_remarks	Bread for the palm-grower in Garåum; seal: å-zi-da dubsar dumu Íeå-åeå (CBT 2)
1	subgenre_remarks	Bread, ninda gin na-ap-ta-num zi-ga Lú-gi-na; seal: Lugal-èn-tar-súd ds d. Lú-dNin-shubur
1	subgenre_remarks	Bread, ninda-gin from Ur-Igalim to Ur-gá-nun-na; seal: Ur-gá-nun-na ds d. Al-ba-ni-du11
1	subgenre_remarks	Bread, èsh-ta-gur-ra shà-gal lú-hu-burx ki Lú-ur-sag-pa-è gudu4-ta; seal dedicated to Ibbi-Sin A-gu-gu ds d. [] ir11-zu
1	subgenre_remarks	Brickmould, giå.ù-åub sig4 al-ur5-ra from Urguenna Ahua the son of Luduga received; seal: Lugal-Eridu˚-åè dumu A-tu [] (CBT 2)
1	subgenre_remarks	Broken; seal: Lú-dUtu ds d. Ba-zi.
1	subgenre_remarks	Bulla numbers
1	subgenre_remarks	Bulla with uneprigraphic seal
1	subgenre_remarks	Bulla, OB seal inscription
1	subgenre_remarks	Bulla, fat sheep received by Ki-tuå-lú (CBT 2)
1	subgenre_remarks	Bulla, receipt of 2 sheep and 2 goats from Ur-∂Lamma; seal: Na-a-na gudu4 ∂Nanåe dumu Lú-∂Nanåe (CBT 2)
1	subgenre_remarks	Bulla: a goat for the weapon of Ningiszida; seal: Ur-∂Nin-gír-su dumu Ki-tuå-lú (CBT 2)
1	subgenre_remarks	Bulla; flat; seal: Lú-åa6-ga aågab dumu Lú-∂Igi-ma-åè? (CBT 2)
1	subgenre_remarks	Bundles of reed and sticks (pa ku5) received by Lú-uru? from Íeå-kal-la; seal: Lú-gisgal dumu Bí-du11 muhaldim; Umma (CBT 2)
1	subgenre_remarks	Bundles of reed from Ur-sha6-ga to Ur-gishgigir; seal: Ur-gishgigir ds d. Ur-dNun-gal.
1	subgenre_remarks	Business Document.  Seal impressions. 5x1x6 lines
1	subgenre_remarks	Business document (record of portion of property received by a son from his father's estate after division with 3 brothers). seal impressions.  16x18 UE 3 lines
1	subgenre_remarks	Business document.  Seal impressions (on envelope only) 8x2x7 UE 2 lines
1	subgenre_remarks	Business document.  Seal impressions. 5x3 lines
1	subgenre_remarks	Business document.  Seal impressions. 8x8 UE 1 lines
1	subgenre_remarks	Business document.  Seal impressions.6 lines
1	subgenre_remarks	Business document.  Seal impressions.8x3x1 lines
1	subgenre_remarks	Business document.Seal impressions. 16x18 lines
1	subgenre_remarks	Business document: list of workmen.  Seal impressions. 14x3x13 UE 2 lines
1	subgenre_remarks	Business document: loan of money.  Seal impressions. 8x2x2 lines
1	subgenre_remarks	Business document: receipt for money. Seal impressions. 5x3x4 UE 2 lines
1	subgenre_remarks	Business document: rent of a field for cultivation.  Seal impression on envelope.  7x1x7 UE 3 lines
1	subgenre_remarks	Business document:loan of barley.  Seal impressions. 6x1x6 UE 2 lines
1	subgenre_remarks	Business document:rent of a house.  Seal impressions. 6x1x6 UE 4 LE 3 lines
1	subgenre_remarks	Business document; (Obv)12x(Rev)8 lines, labels on edges, seal impressions, 6.7x8.25x2.8
1	subgenre_remarks	Business document; Ak.lum.; Seal impressions; (Obv)5x(Rev)4 lines
1	subgenre_remarks	Business document; Kassite seal impressions on all over the surfaces, (Obv)7x(LoE)1x(UE)3 lines
1	subgenre_remarks	Business document; Murashu; 13x4x9 lines; nail impr. rev, seal impr. u.e., le.e.
1	subgenre_remarks	Business document; Seal impressions (same as TMH 5 pl.130); (Obv)7 lines
1	subgenre_remarks	Business document; Ur3 seal impression all over the surfaces; (Obv)6x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Business document; Ur3 seal impression; (Obv)7x(Rev)2 lines
1	subgenre_remarks	Business document; Ur3 seal impressions all over the surfaces, (Obv)8x(Rev)1 lines, *or psbly.-/XIIa/1
1	subgenre_remarks	Business document; Ur3 seal impressions on Obv,UE&LE; tablet(Obv)19x(Rev)21x(UE)3x(LE)3 lines, case 5 lines
1	subgenre_remarks	Business document; from days 18-24; seal impressions all over the surfaces; (Obv)7x(Rev)0 lines
1	subgenre_remarks	Business document; seal impression; (Obv)6x(LoE)3x(Rev)6 lines
1	subgenre_remarks	Business document; seals; 6x0x7x2x2? lines
1	subgenre_remarks	Business document; seals; 6x5 lines
1	subgenre_remarks	Business document; w/a stamp seal impression & a label on LoE.; (Obv)4x(Rev)4 lines
1	subgenre_remarks	Business document; w/seal impressions; (Obv)6x(Rev)1 lines
1	subgenre_remarks	Business record; seal impressions all over the surfaces; (Obv)6x(Rev)2 lines
1	subgenre_remarks	Business record; seal impressions all over the surfaces; (Obv)7x(Rev)2 lines
1	subgenre_remarks	Business record; w/seal impressionss all over the surfaces; (Obv)6x(Rev)0 lines
1	subgenre_remarks	Business; labels?; seals; 2 lines
1	subgenre_remarks	Business; seals
1	subgenre_remarks	Business; seals 10x3x6x1(le.e.) lines
1	subgenre_remarks	Business; seals 10x5x2(u.e.) lines
1	subgenre_remarks	Business; seals 6x1x7x2(u.e.e) lines
1	subgenre_remarks	Business; seals; 11x2 (le.e.) lines
1	subgenre_remarks	Business; seals; 11x2(lo.e.)x5 lines
1	subgenre_remarks	Business; seals; 13x3x12x3 lines
1	subgenre_remarks	Business; seals; 14x1x11x2(u.e.) lines
1	subgenre_remarks	Business; seals; 1x1 line
1	subgenre_remarks	Business; seals; 1x4 lines
1	subgenre_remarks	Business; seals; 4x3 lines
1	subgenre_remarks	Business; seals; 5x2x6x2(u.e.) lines
1	subgenre_remarks	Business; seals; 6 lines
1	subgenre_remarks	Business; seals; 6x2x5x1(le.e.) lines
1	subgenre_remarks	Business; seals; 6x2x6x3(u.e.)x2(le.e.) lines (case=7x1x7x4(u.e.)x2(le.e.) lines)
1	subgenre_remarks	Business; seals; 6x3 lines
1	subgenre_remarks	Business; seals; 7 lines
1	subgenre_remarks	Business; seals; 7x4x8x2 lines
1	subgenre_remarks	Business; seals; 8x1x8 lines
1	subgenre_remarks	Business; seals; 8x6x2x1 (u.e.) line; 4.9x4.1x2.3 cm
1	subgenre_remarks	Business; seals; 9x3x4+x1(u.e.)x2(le.e.) lines
1	subgenre_remarks	Business; seals; labels; 13x2x14x1 (u.e.0 lines
1	subgenre_remarks	Business; stamp seals; 7 lines
1	subgenre_remarks	Carcasses for temple ceremonies (ír-súd-a dNa-rú-a) from Ur-dIg-alim to Lú-sha6-ga; seal: Lú-dNa-rú-a muhaldim lugal d. A-ab-ba
1	subgenre_remarks	Carcasses for the hé-dab5 working in a field, received by Lukalla from Niurum; seal: Lú-kal-la dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Carcasses of cattle from Ku-li to the géme-ush-bar; seal: Ur-dNin-gis-zi-da ds d. Lú-d[Ba-ba6]
1	subgenre_remarks	Carcasses of sheep and bread for the àga-uå in Saguba; seal: ∂Íul-gi-kù-zu dubsar dumu ∂Íára-kam dubsar (CBT 2)
1	subgenre_remarks	Carcasses of sheep eaten by the weaver women; seal: Ur-∂Ba-ba6 dubsar dumu Lú-me-lám (CBT 2)
1	subgenre_remarks	Carcasses of sheep for boat workers (má du8-a, má-a gish gub-ba; seal: Ur-gar ds d. Ur-sha6-ga.
1	subgenre_remarks	Carcasses of sheep from Nì-ú-rum to the ad-kub4; seal: Ur-dNanshe ds d. Lú-d[Lama]
1	subgenre_remarks	Carcasses of sheep from Urbagar to Íulgi-kuzu; seal: ∂Íul-gi-kù-zu dubsar dumu ∂Íára-kam dubsar (CBT 2)
1	subgenre_remarks	Carcasses of sheep transferred from Gudea to the women weaver, kiåib Lú-∂Nisaba; seal illegible (CBT 2)
1	subgenre_remarks	Case frag(?):not inscribed, bullae w/seal impressions
1	subgenre_remarks	Case of 17844; seal: Ka-tar-∂Ba-ba6 dumu Eren-da gu-za-lá (CBT 2)
1	subgenre_remarks	Case of 23832, seal: Ur-dLama d. Eren-da gu-za-lá
1	subgenre_remarks	Case of 23918; seal: Ur-dSHul-pa-è d. Lugal-DU
1	subgenre_remarks	Case of 24883; seal: Ur-dNin-gis-zi-da d. Ur-sag-ku5 ì-rá-rá.
1	subgenre_remarks	Case of 24885; uninscribed seal
1	subgenre_remarks	Case of 25283;seal: Ma-ni sagi dGù-dé-a d. Ur-dLama.
1	subgenre_remarks	Case of 25285seal: Ur-dIg-alim ds d. Ur-sha6-ga; from AS 1 viii 15 to AS 1 xii 15
1	subgenre_remarks	Case of 25302; seal: Lú-gi-na ds d. Ur-ba-[gár].
1	subgenre_remarks	Case of 25304seal: Lugal-da-gár ds d. Ur-dNanshe
1	subgenre_remarks	Case of 26352; seal: Ur-ab-ba ds d. Ba-zi ds zì-da
1	subgenre_remarks	Case of 27482; seal: Lú-dingir-ra ds d. Ur-tur
1	subgenre_remarks	Case of 27805; seal: Ur-dLama ds d. Ba-zi
1	subgenre_remarks	Case of 27806; seal: Ur-gu-la ds d. Ur-tur nu-bànda kurushda
1	subgenre_remarks	Case of 28066; seal: Mu-zu ds d. Ur-ab-ba
1	subgenre_remarks	Case of 28076; seal illegible
1	subgenre_remarks	Case of 29679; seal: Ur-dNin-mar-ki ds d. Lugal-sha6-ga ds
1	subgenre_remarks	Case of 29901; seal: I3-du-du d. Na-ba-sha6
1	subgenre_remarks	Case tablet; division of paternal estate; seals; 4x2x16x1(le.e.) lines; 9.5x6x2.7 cm
1	subgenre_remarks	Case unopened; mostly illegible; seal: dedicated to Íulgi, Ur-∂Lamma di-ku5 ir11-zu (CBT 2)
1	subgenre_remarks	Case; receipt of [...] from A-gi4; gìr Na-ba-åa6; seal: Ur-gu-la dubsar dumu Ur-kù-nun-na (CBT 2)
1	subgenre_remarks	Case; receipt of barley; lá-ni su-ga zì-ka-åè; seal: Ur-gar dubsar dumu Lugal-gaba (CBT 2)
1	subgenre_remarks	Case; receipt of seed barley (åe-numun); sealed (CBT 2)
1	subgenre_remarks	Case; sealed with 19 impressions of the same seal: Ur-∂Nanåe dubsar dumu Ur-∂Ig-alim; the inner tablet was inscribed in two columns (CBT 2)
1	subgenre_remarks	Cattle arua from Lu-balashaga, received by Ahua the ùnu; seal: A-hu-a d. En-za-ra.
1	subgenre_remarks	Cheese, ga-àr from Lú-dNa-rú-a to Lú-sha6-ga; seal: Ur-dNin-mug ds d. Lú-dBa-ba6
1	subgenre_remarks	Containers (ba-rí-ga) transferred from Lu-Ningirsu to Uråaga; case unopened; seal: Ur-åa6-ga-mu dubsar dumu Lugal-inim-gi-na (CBT 2)
1	subgenre_remarks	Contains only badly effaced seal impressions (phps.3mil.BC.)
1	subgenre_remarks	Contract (rare); Purchase of a donkey; seal impressions all over the surfaces; (Obv)11x(LoE)2x(Rev)10 lines
1	subgenre_remarks	Contract (witnesses).  Inscribed outer case of an inscribed clay tablet.  Seal impressions. 8 lines
1	subgenre_remarks	Contract agreement concerning money.  Seal impressions on case. 7x1x8 UE 1 lines
1	subgenre_remarks	Contract and witnesses; seals; 9x9x1 (le.e.)
1	subgenre_remarks	Contract concerning  hired workers; seal; 3x5x2 lines
1	subgenre_remarks	Contract concerning a silver bracelet; seals; 10x7 lines
1	subgenre_remarks	Contract concerning division or exchange of shares in an estate; seals; 13x10 lines
1	subgenre_remarks	Contract concerning grain; seals; 7x5 lines
1	subgenre_remarks	Contract for harvest labor; seals.  6x2x6 UE 3 lines
1	subgenre_remarks	Contract for harvest labor; seals. 7x2x5 UE 2 lines
1	subgenre_remarks	Contract for the delivery of goods; stamp seals with labels; 9x9x3(u.e.)x2(le.e.) lines
1	subgenre_remarks	Contract for the hire of ?; seals; 5x2x5x2 lines; 4.2x4.1x2.2 lines
1	subgenre_remarks	Contract for the hire of a worker for 1 year; seal (on envelope only) 6x2x8 UE 2 lines
1	subgenre_remarks	Contract for the purchase of homes. Envelope has sealimpressions. 14x2x14 UE 2 lines
1	subgenre_remarks	Contract for the rent of a field; seal impressions; 12X9 UE1 lines
1	subgenre_remarks	Contract for the upper floor of a house for one year; seven seals; 6x2x7x2 lines
1	subgenre_remarks	Contract in regard to a plantation; seal impr on all sides except l.e.; 4x5 lines
1	subgenre_remarks	Contract regarding land, exchange of 2 fields; seal impression; (Obv)13x(Rev)12 lines
1	subgenre_remarks	Contract with seal; (Rev)3 lines
1	subgenre_remarks	Contract with seal; *a card in the drawer says deposited w/Sommerville collection [request of Dr.W.Pepper]""
1	subgenre_remarks	Contract with witnesses; seals; 5x6x2(u.e.) lines
1	subgenre_remarks	Contract, CBS card: Important tablet"; faint seal impressions all over the surfaced; (Obv)7x(LoE)1x(Rev)5 lines *Same seal as about 80 tablets from Nippur."
1	subgenre_remarks	Contract, concerning silver; seals, labels, 11x5 lines
1	subgenre_remarks	Contract, father-in-law renounces right to complain if son-in-law marries; seals; 10x9x2 lines; 6.3x5.1
1	subgenre_remarks	Contract, record of a downpayment for a house; seal.  10x3x7 UE 3
1	subgenre_remarks	Contract, rent of field for 5 years; seal imprssions all over the surfaces; (Obv)10x(Rev)11x(UE)1 lines
1	subgenre_remarks	Contract, sale of office; w/seal impressions all over the surfaces (both tablet & case); tablet:(Obv)16x(Rev)12 lines, case:(Obv)18x(Rev)10 lines
1	subgenre_remarks	Contract.  Inscribed clay.  Seal impressions. 2 lines
1	subgenre_remarks	Contract.  Inscribed outer case of an inscribed clay tablet.  Seal  impressions. 4 lines
1	subgenre_remarks	Contract.  Inscribed, outer case of an inscribed clay tablet.  Seal impressions. 2 lines
1	subgenre_remarks	Contract.  Seal impr on u.e., lo.e., l.e., r.e., and obv. lo. part; 22x26x3(u.e.) lines
1	subgenre_remarks	Contract.  Seal impressions on Rev. 5 lines
1	subgenre_remarks	Contract.  Seal impressions.  10x2x7 lines
1	subgenre_remarks	Contract.  Seal impressions.  7X5 Ue 2 lines
1	subgenre_remarks	Contract.  Seal impressions.  With part of case. case 8x2 lines; one side of tablet exposed 8 lines
1	subgenre_remarks	Contract.  Seal impressions. 13X13 UE2
1	subgenre_remarks	Contract.  Seal impressions. 14x2x11 UE1 lines
1	subgenre_remarks	Contract.  Seal impressions. 3 lines
1	subgenre_remarks	Contract.  Seal impressions. 4x1x6 UE 1 lines
1	subgenre_remarks	Contract.  Seal impressions. 6X2X7 UE2 lines
1	subgenre_remarks	Contract.  Seal impressions. 6X4 UE2
1	subgenre_remarks	Contract.  Seal impressions. 6x2x6 UE 1 lines
1	subgenre_remarks	Contract.  Seal impressions. 7X3X6 lines
1	subgenre_remarks	Contract.  Seal impressions. 7x2x4 UE 4 lines
1	subgenre_remarks	Contract.  Seal impressions. 7x2x5 UE 3 lines
1	subgenre_remarks	Contract.  Seal impressions. 8x6x2 lines
1	subgenre_remarks	Contract.  Seal impressions.11X2X7 lines
1	subgenre_remarks	Contract.  Seal impressions.2lines
1	subgenre_remarks	Contract.  Seal impressions.4 lines
1	subgenre_remarks	Contract.  Seal impressions.4x4 lines
1	subgenre_remarks	Contract.  Seal impressions.6X5 UE1 lines
1	subgenre_remarks	Contract.  Seal impressions.9X6 lines
1	subgenre_remarks	Contract.  The inscribed outer case of an inscribed clay tablet.    Seal impressions. 2 lines
1	subgenre_remarks	Contract.  The inscribed outer case of an inscribed clay tablet.    Seal impressions.1 line
1	subgenre_remarks	Contract.  The inscribed outer case of an inscribed clay.  Seal impressions. 2 lines
1	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.  Seal impression only
1	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.  Seal impression only.
1	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.  Seal impressions. 1 line
1	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.  Seal impressions. 2 lines
1	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.  Seal impressions. 4x1 LE 1 lines
1	subgenre_remarks	Contract.  The outer case of an inscribed clay tablet.Seal impressoins only
1	subgenre_remarks	Contract.  The outer case of an inscribed clay.  Seal impression with inscription. 3 lines
1	subgenre_remarks	Contract.  The outer case of an inscribed clay.  Seal impressions only
1	subgenre_remarks	Contract.  The outer case of an inscribed clay.  Seal impressions only'
1	subgenre_remarks	Contract.  The outer case of an inscribed clay.  Seal impressions only.
1	subgenre_remarks	Contract.  The outer case of an inscribed clay.  Seal impressions.3 lines
1	subgenre_remarks	Contract.  The outer inscribed case of an inscribed clay tablet.    Impression of seal inscription. 3 lines
1	subgenre_remarks	Contract.  The outer inscribed case of an inscribed clay tablet.    Seal impressions.  2 lines
1	subgenre_remarks	Contract.  The outer inscribed case of an inscribed clay tablet.    Seal impressions. 2 lines
1	subgenre_remarks	Contract.  The outer inscribed case of an inscribed clay.  Impression of seal inscription. 3 lines
1	subgenre_remarks	Contract.  The outer inscribed case of an inscribed clay.  Seal impressions. 3 lines
1	subgenre_remarks	Contract.  With seal impressions in fine state of preservation. 8x2x6 UE 2 lines
1	subgenre_remarks	Contract. Case has seal impressions.  5 lines
1	subgenre_remarks	Contract. Seal Impression. 1 line
1	subgenre_remarks	Contract. Seal impressions. 20x2x20 lines
1	subgenre_remarks	Contract: legal decision concerning a field.  Seal impressions. 14x14 lines
1	subgenre_remarks	Contract: loan of barley without interest.  Seal impressions. 5x3x5 UE 2 lines
1	subgenre_remarks	Contract: loan of money.  Seal impressions. 7x1x6 UE 3 lines
1	subgenre_remarks	Contract: receipt for barley in account of the proce of a house.  Seal impressions. 7x3x5 UE 4 lines
1	subgenre_remarks	Contract: rent of a field for cultivation.  With inscribed case covered with seal impressions and repaired. 6x3x7 UE 3 LE 1 lines
1	subgenre_remarks	Contract: rent of a field. Seal impressions on envelope.  10x1x6 lines
1	subgenre_remarks	Contract: rent of a house.  Seal impressions.  9x10 lines
1	subgenre_remarks	Contract: rent of a house.  Seal impressions. 6x2x5 UE 3 lines
1	subgenre_remarks	Contract: rent of a house.  Seal impressions.7x2x6 UE 2 lines
1	subgenre_remarks	Contract: rent of a house;  Seal impressions. 8X7 lines
1	subgenre_remarks	Contract:receipt of money, the price of barley.  Seal impressions.7x2x4 UE 3 lines
1	subgenre_remarks	Contract; 2x1x4 lines; partial seal impr
1	subgenre_remarks	Contract; 3 seal impressions & 3 labels on UE, 2 seal impressions & 3 labels on LE; (Obv)14x(LoE)3x(Rev)1 lines
1	subgenre_remarks	Contract; 4 brothers povide for the sustenance of their sister; Seal impressions (3 lines of inscription) on tablet & case, Tablet (Obv)15x(Rev)18x(UE)2 lines, Case (Obv)15x(Rev)18 lines,
1	subgenre_remarks	Contract; 5x3 lines; seal impr.
1	subgenre_remarks	Contract; 6 lines; seal impr.
1	subgenre_remarks	Contract; 6(u. or lo. e.)x2 lines; seal impr le.e.
1	subgenre_remarks	Contract; 8x2x7x2(u.e.) lines; 4.5x3.7x2 cm (Case=9x4 lines; seals)
1	subgenre_remarks	Contract; Aramaic inscription; seals; labels; 3 lines
1	subgenre_remarks	Contract; Description of a house; Seal impressions; (Obv)6x(Rev)3 lines
1	subgenre_remarks	Contract; Division of inheritance, chiefly consisting of rights to priestly offices; Seal impressions; (Obv)25x(Rev)26 lines
1	subgenre_remarks	Contract; Hire of a slave; Tablet:(Obv)5x(LoE)3x(Rev)5x(LE)1 lines; Case 6x8x2 lines, seal impressions all over the surfaces;
1	subgenre_remarks	Contract; Lease; 6x1x4x3 lines; seal impressions all over the surfaces;
1	subgenre_remarks	Contract; List of persons (PBS 8/2 149); Seal impressions; (Obv)11x(Rev)8 lines
1	subgenre_remarks	Contract; Loan of barley from the temple of (d)Shamash; Seal impressions; (Obv)8x(Rev)8 lines
1	subgenre_remarks	Contract; Loan of barley with interest; seal impressions; (Obv)8x(Rev)11 lines
1	subgenre_remarks	Contract; Loan of barley, with interest; Seal impressions on case only; Tablet (Obv)7x(Rev)7 lines, Case (Obv)8x(Rev)9x(LE)1 lines
1	subgenre_remarks	Contract; Loan of money, without interest; Seal impressions; (Obv)7x(Rev)11x(UE)1x(LE)1 lines
1	subgenre_remarks	Contract; Promise to deliver money; Seal impressions; Case (Obv)10x(Rev)10x(UE)1x(LE)1 lines
1	subgenre_remarks	Contract; Purchase of a house by two partner; Seal impressions; (Obv)12x(Rev)15x(UE)3 lines
1	subgenre_remarks	Contract; Purchase of a house; Seal impressions; (Obv)13x(Rev)13 lines
1	subgenre_remarks	Contract; Purchase of an old donkey; seal impressions all over the surfaces; 1 label on Rev, 2 labels on LE; 9x9x2 lines
1	subgenre_remarks	Contract; Rental of a field; 15x1x13x1 lines; seal impressions all over the surfaces;
1	subgenre_remarks	Contract; Rental of a field; Sippar; 9x5x2 lines; seal impressions all over the surfaces; 2 labels & 2 seal impressions on LE.
1	subgenre_remarks	Contract; Rental of a slave girl; Sippar; Tablet: 5x2x5x3 lines;* Case:6x7x3 lines, seal impressions all over the surfaces;
1	subgenre_remarks	Contract; Sale of an official's right to an income; Redemption of pristly office; seal impressions; (Obv)10x(Rev)13x(UE)3 lines
1	subgenre_remarks	Contract; Sale of slaves; Seal impressions, (Obv)12x(Rev)8 lines
1	subgenre_remarks	Contract; Seal impression on tablet and case; tablet:(Obv)10x(Rev)11 lines, case:(Obv)5x(Rev)11 lines
1	subgenre_remarks	Contract; Seal impressions;
1	subgenre_remarks	Contract; Seal impressions; (Obv)illegible, (Rev)14 lines
1	subgenre_remarks	Contract; cncg. the limits of 2 houses' plots; w/seal impressions all over the surfaces of both tablet & case; tablet:(Obv)20x(Rev)22 lines; case:(Obv)0x(Rev)10 lines
1	subgenre_remarks	Contract; concerning dates; inscribed Aramaic docket; seals with labels Murashu?; 8x4x9 lines
1	subgenre_remarks	Contract; concerning shares; Murashu?; aramaic endorsment; seals; labels; 7x1 lines
1	subgenre_remarks	Contract; concerning shares; seals; 5 lines
1	subgenre_remarks	Contract; concerning silver; seals; 7 lines
1	subgenre_remarks	Contract; day 11 to 14; seal impressions on all the edges; (Obv)6x(Rev)3 lines
1	subgenre_remarks	Contract; days 26-30; seal impressions all over the surfaces; (Obv)6x(Rev)3 lines
1	subgenre_remarks	Contract; decision concerning payment for a priestly office; seal impressions all over the surfaces; (Obv)12x(Rev)10 lines
1	subgenre_remarks	Contract; division of inheritance; Seal impressions; (Obv)20x(Rev)21x(UE)2 lines
1	subgenre_remarks	Contract; division of inheritance; seal impressions on case & tablet; (Obv)18x(Rev)21 lines
1	subgenre_remarks	Contract; exchange of two houses of equal value; seal impressions on all the surfaces; (Obv)10x(Rev)11x(UE)1 lines
1	subgenre_remarks	Contract; field sale; Seal impressions all over the surfaces; (Obv)12x(Rev)7x(UE)1 lines
1	subgenre_remarks	Contract; field sale; seal impressions on Obv.&LE; (Obv)10x(Rev)6 lines
1	subgenre_remarks	Contract; for the hire of ------; seal impressions all over the surfaces ; 5x3x3 lines
1	subgenre_remarks	Contract; from XII-6 to I-6; seal impressions on all over the surfaces; (Obv)7x(Rev)3 lines
1	subgenre_remarks	Contract; list of cattle; seals; 12x9 lines
1	subgenre_remarks	Contract; only personal names preserved; seals; labels; 1x5 lines
1	subgenre_remarks	Contract; part of a seal and three labels; 1x0 lines
1	subgenre_remarks	Contract; purchase of field for cemetery by a king; seal impressions all over the surfaces; (Obv)16x(Rev)12 lines
1	subgenre_remarks	Contract; seal
1	subgenre_remarks	Contract; seal impr on tablet obv, rev and l.e., case on all sides except u. e.; case 18x18x2 lines; tablet 15x17(rev)x3(u.e.)x2(lo.e.)x1(l.e.) lines
1	subgenre_remarks	Contract; seal impr. on both sides; 1 line
1	subgenre_remarks	Contract; seal impr; 2 lines
1	subgenre_remarks	Contract; seal impression on Rev; (Obv)6x(LoE)2x(Rev)4 lines
1	subgenre_remarks	Contract; seal impression; (Obv)1x(Rev)4 lines
1	subgenre_remarks	Contract; seal impression; (Rev)4 lines
1	subgenre_remarks	Contract; seal impressions all over the surfaces; (Obv)5x(Rev)7x(LE)1 lines
1	subgenre_remarks	Contract; seal impressions on Obv,Rev,LE,UE&LoE., (Obv)6x(Rev)1 lines
1	subgenre_remarks	Contract; seal impressions; (Obv)13x(Rev)11 lines
1	subgenre_remarks	Contract; seal impressions; (Obv)15x(Rev)11 lines
1	subgenre_remarks	Contract; seal impressions; (Obv)2x(Rev)1 lines
1	subgenre_remarks	Contract; seal impressions; (Obv)4x(Rev)1 lines
1	subgenre_remarks	Contract; seal impressions; (Obv)5 lines, (Rev)blank
1	subgenre_remarks	Contract; seal impressions; (Obv)6 lines, (Rev)blank
1	subgenre_remarks	Contract; seal impressions; 2 lines
1	subgenre_remarks	Contract; seal impressions; 8 lines
1	subgenre_remarks	Contract; seal; 13x12 lines
1	subgenre_remarks	Contract; seal; 14x17 lines
1	subgenre_remarks	Contract; seal; 4x5 lines
1	subgenre_remarks	Contract; seal; 5 lines
1	subgenre_remarks	Contract; seal; label; 4x5 lines
1	subgenre_remarks	Contract; seals
1	subgenre_remarks	Contract; seals and labels; originally traces of Aramaic in ink, now baked; 7x2x2(le.e.) lines
1	subgenre_remarks	Contract; seals, labels; 14x3 lines
1	subgenre_remarks	Contract; seals, labels; 8x2 lines
1	subgenre_remarks	Contract; seals. 9x10 lines
1	subgenre_remarks	Contract; seals;
1	subgenre_remarks	Contract; seals; 10x1 lines
1	subgenre_remarks	Contract; seals; 11x2(u.e.)x2(le.e) lines
1	subgenre_remarks	Contract; seals; 12x10 lines
1	subgenre_remarks	Contract; seals; 12x3x14x1(u.e.) lines
1	subgenre_remarks	Contract; seals; 12x8 lines
1	subgenre_remarks	Contract; seals; 13x11 lines
1	subgenre_remarks	Contract; seals; 13x2x10x1(u.e.) lines
1	subgenre_remarks	Contract; seals; 13x3x6x1(u.e.) line
1	subgenre_remarks	Contract; seals; 14x11 lines
1	subgenre_remarks	Contract; seals; 14x3x11x2(u.e.)x1(le.e.) lines
1	subgenre_remarks	Contract; seals; 19x10x3(u.e.0 lines
1	subgenre_remarks	Contract; seals; 3 lines
1	subgenre_remarks	Contract; seals; 4x3 lines
1	subgenre_remarks	Contract; seals; 5x2x4x2x2(le.e) lines
1	subgenre_remarks	Contract; seals; 6 lines
1	subgenre_remarks	Contract; seals; 7 lines
1	subgenre_remarks	Contract; seals; 7x1x3x1(le.e.) lines
1	subgenre_remarks	Contract; seals; 7x1x7x3(u.e.)x1(le.e.) lines
1	subgenre_remarks	Contract; seals; 7x2x5x2(u.e.)x2(le.e.) lines
1	subgenre_remarks	Contract; seals; 7x3x8x3(u.e.) lines
1	subgenre_remarks	Contract; seals; 8x2x10 lines
1	subgenre_remarks	Contract; seals; 8x4 lines
1	subgenre_remarks	Contract; seals; 9x3x8x1(u.e.) lines; 5.8x4.2x2.5 cm
1	subgenre_remarks	Contract; seals; Murashu?; 19x2x15 lines
1	subgenre_remarks	Contract; seals; dupl. Bu88-5-12,57 (Meissner, BAP 107); 18x4x20x3 lines
1	subgenre_remarks	Contract; seals; labels;
1	subgenre_remarks	Contract; seals; labels; 11x12 lines
1	subgenre_remarks	Contract; seals; labels; 12x2x9 lines
1	subgenre_remarks	Contract; seals; labels; 14x15 lines
1	subgenre_remarks	Contract; seals; labels; 1x4 lines
1	subgenre_remarks	Contract; seals; labels; 1x6 lines
1	subgenre_remarks	Contract; seals; labels; 2x4 lines
1	subgenre_remarks	Contract; seals; labels; 5x3 lines
1	subgenre_remarks	Contract; seals; labels; 6x3 lines
1	subgenre_remarks	Contract; seals; labels; 7x2(wrapped around right edge)
1	subgenre_remarks	Contract; seals; labels; Murashu?; 18x10 lines
1	subgenre_remarks	Contract; seals; witnesses; 19x20x20x21 lines
1	subgenre_remarks	Contract; seals; witnesses; 7x1 line
1	subgenre_remarks	Contract; seals;13x6x2(u.e.)x2(le.e) lines
1	subgenre_remarks	Contract; shares of an estate?; seals; witnesses; 10x6 lines
1	subgenre_remarks	Contract; stamp seals with labels; 7x2x? lines
1	subgenre_remarks	Contract; the same seal impressions all over the surfaces; (Obv)7x(Rev)1 lines
1	subgenre_remarks	Contract; w/seal impression; 3 lines
1	subgenre_remarks	Contract; w/seal impression; Harper; 16-2-13-89; (Obv)5x(Rev)5 lines
1	subgenre_remarks	Contract; w/seal impressions all over the surfaces; nail marks on RE; (Obv)5x(Rev)1 lines
1	subgenre_remarks	Contract; w/seal impressions; (Obv)6x(Rev)1 lines; *ITI.SHE MU.1.KAM.DIRI (See Brinkman MSKH p.193, n.7)
1	subgenre_remarks	Contract; w/seal impressions; (Obv)8x(Rev)6 lines
1	subgenre_remarks	Contract; witnesses; seals;
1	subgenre_remarks	Contract; witnesses; seals; 3x5 lines
1	subgenre_remarks	Contract; witnesses; seals; 5 lines
1	subgenre_remarks	Contract; witnesses; seals; 6 lines
1	subgenre_remarks	Contract?/ Sippar; 6x1x6x2 lines; a seal impression on Rev.
1	subgenre_remarks	Contract?; legal decision concerning a priestly office?; seal impressions all over the surfaces, (Obv)18x(Rev)23x(UE)4 lines
1	subgenre_remarks	Contract?; seals; 3 lines
1	subgenre_remarks	Contract?; seals; 5 lines
1	subgenre_remarks	Contract?; seals; 6 lines
1	subgenre_remarks	Contract?; seals; 7x5 lines
1	subgenre_remarks	Contract?; witesses only; seals; 3 lines
1	subgenre_remarks	Contracts (3) for partition of courtyards; seals; 16x17 lines
1	subgenre_remarks	Contracts; three seals; 7x5x2 lines
1	subgenre_remarks	Contribution (bal) of bundles of reed and manu-wood for the giåbun-feast of Urnamma. Seal: Lugal-ezem ds d. dumu Lugal-e2-ma[h-e?] åabra.
1	subgenre_remarks	Conveyance; seal impressions on RE.&LE; (Obv)7x(Rev)0 lines
1	subgenre_remarks	Copper for the smith Ur-Ningiszida; seal: Ur-dNin-gis-zi-da simug []
1	subgenre_remarks	Corpses from Gudea to the àga-ush of the king; seal Dingir-mu / gésh-da lugal / dumu A-ba-ni-da.
1	subgenre_remarks	Corpses of cattle from Duggazida for the weaver women; seal: Ur-ni9-gar ds d. Ur-d[].
1	subgenre_remarks	Corpses of sheep transferred to weaver women for food; seal: Ur-dBa-ba6 ds d. Lú-me-lám
1	subgenre_remarks	Court case: dispute over shares of an estate; seals; 10x14 lines
1	subgenre_remarks	Cumin (åe-lú) rations for 20 guruå, received by Dagu from Ur-Enlilla; case unopened; seal: Da-gu ugula dumu  Lú-∂[ ] (CBT 2)
1	subgenre_remarks	Cumin (ú-tir) and beans from Ur-e-gal to SHà-da; seal: Ur-é-gal ds d. []
1	subgenre_remarks	Cumin (ú-tir, she-lú) from Ur-é-gal to Lú-dingir-ra for the bala; seal: Lú-dingir-ra ds d. Lú-sha6-ga
1	subgenre_remarks	Cylinder Seal impression only
1	subgenre_remarks	Cylinder seal impressions.  Harper's mark Ni. 2-2-19-89.  *Peters describes as Nippur I, although Ur II tablets are characteristic to Nippur II.  I" came from Tablet Hill
1	subgenre_remarks	Date lost.      Not sealed.   Summaries.
1	subgenre_remarks	Date lost.     Not sealed.
1	subgenre_remarks	Date not legible.   Not sealed.   Allocation of workers.
1	subgenre_remarks	Date only, seals; 3 lines
1	subgenre_remarks	Date only; seals; 2 lines
1	subgenre_remarks	Date only; seals; 3 lines?;
1	subgenre_remarks	Date only; seals; 5 lines
1	subgenre_remarks	Dated IE 12/   Sealed "...  Receipt for seed barley.
1	subgenre_remarks	Dated SS 7/v/6 Notsealed.   Inspection, withdrawal and allocation of workers.
1	subgenre_remarks	Dates for Ur from Ur-abba to Lu-Ningirsu, 4 gur sag-bi 0; 1.5; seal: Lú-dNin-gír-su ds d.Ir11-mu dub-sar
1	subgenre_remarks	Dates from Lú-du10-ga to Ur-abba; seal: Ur-ab-ba dubsar dumu Ba-zi dubsar síg-ka (CBT 2)
1	subgenre_remarks	Dates from Ur-ab-ba to Lú-dNin-gír-su; kù shim-ma-dingir-re-ne; seal: Lú-dNin-gír-su ds d. Ir11-mu
1	subgenre_remarks	Dates from Ur-ab-ba to Lú-dingir-ra; seal: Lú-dingir-ra d. Ur-dLi9-si4 [].
1	subgenre_remarks	Dates from Ur-ab-ba to Ur-dBa-ba6; seal: Ur-dBa-ba6 d. énsi Lagashki []
1	subgenre_remarks	Dates from Ur-dIg-alim, lá-ni–àm kishib Ab-ba santana; seal: Ab-ba-gul-la ds d. Ur-tur-tur
1	subgenre_remarks	Dates issued to Ur-∂Iåtaran by Ur-ab-ba; seal: Ur-gar dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Dates received by Inim-kù; seal? (CBT 2)
1	subgenre_remarks	Dates received by Ur-abba; seal: Ur-ab-ba dubsar dumu Ba-zi dubsar síg-ka (CBT 2)
1	subgenre_remarks	Dates é-hul-a from Gaa to En-in-na-kal (CBT 2). A: Case of 19015; seal En-in-na-kal dumu É-nun-[] (CBT 2)
1	subgenre_remarks	Dates, zú-lum from Urabba; kishib Urgar d. Lugal-gaba shà Ninaki; seal: Ur-gar ds d. Lugal-gaba
1	subgenre_remarks	Dattes from Alla to Ur-ab-ba; seal: Ur-ab-ba ds d. Ba-zi ds síg-ka
1	subgenre_remarks	Dead sheep from ›-zi to Lú-kal-la; seal: Lú-kal-la ds d. Ur-dLama
1	subgenre_remarks	Dead sheep; udu ki!-ug7 a-shà gi-kam Gù-dé-a dumu La-ni zi-ga kishib sha13-dub-ba; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Decision of a court of justice; seal Impressions. *Seems to have come from Nippur; (Obv)13x(Rev)12 lines
1	subgenre_remarks	Decree (rikiltu) of governor of Nippur regarding activities of persons should they leave Nippur; seals; 10x10x3(lo.e.)x1(l.e.)
1	subgenre_remarks	Defaced [seal].
1	subgenre_remarks	Deficit of barley []; seal: Ur-dEn-líl-lá ds d. Ka-sha6 kurushda.
1	subgenre_remarks	Deficit of barley from the rá-gaba Niurum to Ur-Ningiszida; seal: Ur-dNin-gis-zi-da ds d. Lugal-sha6-ga.
1	subgenre_remarks	Deficit of barley of the plowmen; seal: Lú-Ninaki ds d.Ur-dNanshe.
1	subgenre_remarks	Deficit of barley returned by Niurum to Ur-Baba son of Bazi; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Deficit of barley returned by Ur-Baba to Ur-gishgigir; seal Ur-gishgigir ds d. Ur-dIg-alim ka-gur7-dNin-gír-su-ka.
1	subgenre_remarks	Deficit of barley; seal: Lú-dBa-ba6 ds d. Lú-kal-la.
1	subgenre_remarks	Deliver of 2 sheep to Lú-du10-ga udu kab-lu-lu; seal: Lú-du10-ga d. Ur-dNanshe
1	subgenre_remarks	Deliveries of barley for various persons. Seal: illegible (3 lines).
1	subgenre_remarks	Delivery of barley; seal; 5x4 lines
1	subgenre_remarks	Delivery of female workers for working in the field Kamari. Seal: Ur-{d}Åara2 ds d. Lugal-nanga2
1	subgenre_remarks	Delivery of one sheep to Ur-SHulpae; seal: Ur-dSHul-pa-è sipa dumu Lugal-DU ir11-dNanshe
1	subgenre_remarks	Delivery of reeds; w/seal impressions; (Obv)6x(Rev)6 lines
1	subgenre_remarks	Delivery of regular bread; seal: ∂Ig-[alim- ] dumu Lú-∂[] (CBT 2)
1	subgenre_remarks	Delivery; seals; 6x3 lines
1	subgenre_remarks	Deteriorated; seal illegible
1	subgenre_remarks	Dida nì-sískur-ra gìr Ab-ba-mu d. Ba-a-da; seal illegible
1	subgenre_remarks	Disinheritance document?; seals; 8x11 lines
1	subgenre_remarks	Division of a house of an estate; seals; 6x6 lines
1	subgenre_remarks	Division of field; seal impressions on LE.,UE.,Rev., (Obv)(i)30x(ii)29x(Rev)(iii)25x(iv)3 lines.
1	subgenre_remarks	Division of inheritance between 2 brothers; Seal impressions; (Obv)18x(Rev)18x(UE)2 lines
1	subgenre_remarks	Division of inheritance; seal impressions; (Obv)25x(Rev)28 lines
1	subgenre_remarks	Division of property between two brothers; seals; 25x4x23x3(u.e.) lines; 11.1x6.1x3.0 cm
1	subgenre_remarks	Division?; (Obv)7x(Rev)5 lines, seal impressions on Obv, UE & RE.
1	subgenre_remarks	Docket for a hired harvester; seal; cf 29-13-123, 29-13-144, 29-13-145; 29-13-146, 29-13-147; 2x3 lines
1	subgenre_remarks	Docket for the hire of a harvester; cf 29-13-120; seals;  2x4 lines
1	subgenre_remarks	Docket for the hire of a harvester; seals; cf. 29-13-120; 2x3 lines
1	subgenre_remarks	Docket from a leather bag containing 1 pan of barley belonging to Lú-kal-la, "sealed" by Ur-∂Nun-gal s. of Da-da. (CBT 1)
1	subgenre_remarks	Docket with anepigraphic seal
1	subgenre_remarks	Donkeys transfered from Ir3-ri-ib to the sukkal-mah; seal: Gù-dé-a ds d.La-ni sha13-dub-ba-ka.
1	subgenre_remarks	Economic text; w/seal impressions; 6 lines
1	subgenre_remarks	Economic; 3 lines, Edge: seal impression.
1	subgenre_remarks	Economic; seal; 3 lines; 2.8x1.9x1.4cm
1	subgenre_remarks	Economic; seal; 7x2 lines
1	subgenre_remarks	Economic; seals; 6x3x8x3(u.e.)x2(le.e). lines
1	subgenre_remarks	Economic; seals; 7x3x3x3 lines; 4.8x4.5x2.1 cm
1	subgenre_remarks	Economic; seals; 7x5 lines
1	subgenre_remarks	Economic; w/seal impressions all over the surfaces; (Obv)5x(LoE)2x(Rev)1 lines; 3.5 X 2.3 X 1.6 cm.
1	subgenre_remarks	Emmer from Ur-badtibirra to Abbakalla; seal: Ab-ba-kal-la ds d. Ur-sukkal.
1	subgenre_remarks	Emmer from Ur-bàd-tibira to Lugal-ezem, sá-du11 dSHul-pa-è bàd sì-ga; seal: Lugal-ezem d. Gish-a-ni gudu4 dLugal-itu-da
1	subgenre_remarks	Emmer from the field ambar received by Mansum; seal illegible (CBT 2)
1	subgenre_remarks	Emmer transferred from Lubimu to Ur-èå-du10-nun; case unopened; seal: Ur-∂Eå3-du10-nun dumu Íà-lá-sùd (CBT 2)
1	subgenre_remarks	Emmer wheat from Ur-Enlilla to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Ba-zi.
1	subgenre_remarks	Emmer, zíz from Da-da to Lú-mar-sa; seal: [Lú-mar-sa] ds d. Ur-sha6-ga
1	subgenre_remarks	Entry concerning the receipt of 12 lambs for divination; ba-ni-priests; seals; 10x3x4 lines; 6.75x4.25x2.3 cms
1	subgenre_remarks	Erin and guruå; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Eroded; flour for Ur-Baba; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Eroded; lú ki-na gish-gá-dam gish.tukul-e dab5-ba-ta; royal seal of SHulgi, Lú-dBa-ba6 rá-gaba ir11-zu
1	subgenre_remarks	Eroded; seal illegible
1	subgenre_remarks	Ewe arua from Lubalaåaga to Huru sipa ama-gan; seal illegible (CBT 2)
1	subgenre_remarks	Ewes from Lu-Baba to Anana; case unopened; seal: å-na-na dumu Lú-∂Ba-ba6 àga-uå ú-du-[lu] (CBT 2)
1	subgenre_remarks	Ewes åu-gíd sá-du11 ∂Nanåe-åè, from Íeåkalla to Na-a-na the gudu4; seal: Na-a-na gudu4 ∂Nanåe dumu Lú-∂Nanåe (CBT 2)
1	subgenre_remarks	Excess of barley in the account, from Ur-Igimashe to Ur-Baba; seal: Ur-dLama énsi Lagashki Ur-dBa-ba6 ds d. Ur-íd-eden-na ir11-zu.
1	subgenre_remarks	Excess of barley returned by Lugina to Urbagar; seal: Ur-ba-gár ds d. Lú-igi-sha6-sha6 ka-gur7.
1	subgenre_remarks	Excess of barley returned by Ur-kal-la to Ur-gu-la; seal: Ur-gu-la d. Lugal-ash lú-shim.
1	subgenre_remarks	Exchange of courtyards; witnesses; seals; 16x14 lines
1	subgenre_remarks	Exchange of houses; PN1 gives a 1sar 16 gin house plot to PN2 in exchange for 1 sar plot and 1 shekel of silver; witnesses; bur-gul seal; 15x9 lines; 7.5x4.5
1	subgenre_remarks	Exchange of temple offices for field property; w/seal impressions; Harper: Ni.2-219-89; (Obv)11x(Rev)13x(UE)3 lines
1	subgenre_remarks	Exchange of temple offices; witnesses; seals; 11x6 lines
1	subgenre_remarks	Expenditure of barley and flour made by Lugal-ushumgal; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	Expenditure of barley for the shabra; seal; Ur-mes ds d. Ur-dLama
1	subgenre_remarks	Expenditure of bread from Addagina to Ur-Ningiszida; seal: Ur-∂Nin-gis-zi-da dubsar dumu Ur-∂Ig-alim ka-gur7 (CBT 2)
1	subgenre_remarks	Expenditure of flour for the siskur lugal in the temple of Nindara; seal: Ur-mes dubsar dumu Gù-dé-a (CBT 2)
1	subgenre_remarks	Expenditure of flour; seal: A-gu []
1	subgenre_remarks	Expenditure of grain; seal impressions all over the surfaces; 4x1x3 lines
1	subgenre_remarks	Expenditures of barley; seals; 3x5 lines
1	subgenre_remarks	Expenditures of bread; seal; cf N 739: same date and seal; 3x6x1 line
1	subgenre_remarks	Expenditures of?; seals; 4 lines
1	subgenre_remarks	Fabric for the thrones of the sukkalmah, from Urguenna to Ur-Lamma (CBT 2). A: Case of 19947; seal: Ur-∂Lamma dubsar dumu Ir11-mu (CBT 2)
1	subgenre_remarks	Face eroded; seal illegible
1	subgenre_remarks	Faint seal impressions.
1	subgenre_remarks	Fat received by Íeå-kal-la from Ur-uå-gíd-da; seal: Íeå-kal-la dubsar dumu Ur-ab-ba (CBT 2)
1	subgenre_remarks	Field account; w/seal impressions; (Obv)5x(Rev)3 lines
1	subgenre_remarks	Field lease agreement; seals; 9x9 lines
1	subgenre_remarks	Field surfaces; shukur engar-ra nu-ù-ta-zi; seal: Lú-kiri4-zal ds d. Ur-dBa-ba6.
1	subgenre_remarks	Field work (zar-tab-ba); seal: Lugal-é-[mah-e] dubsar dumu Lugal-kù-ga-[ni] (CBT 2)
1	subgenre_remarks	Figues, gish.pèsh hád ki Ur-dInanna-ta nì-u4-sakar kishib Lú-d[]; seal: Ur-d.[] ds d. Ba-zi/mu
1	subgenre_remarks	Fine oil received by Íeå-kal-la from Ur-∂Nanåe, gìr Nam-mah-∂Ba-ba6; seal: Íeå-kal-la [ds dumu Ur-ab-ba] (CBT 2)
1	subgenre_remarks	Fine seal impression (First Kassite style)
1	subgenre_remarks	Fine seal impression all over the surfaces; (Obv)7x(LoE)1x(Rev)1 lines
1	subgenre_remarks	Fine seal impression; 1 line
1	subgenre_remarks	Fine seal impressions
1	subgenre_remarks	Fine seal impressions (Plough seal); 21x22 lines; 11.45x6.7x3.1 cm
1	subgenre_remarks	First quality bread from Abbashaga to Ur-Igalim; seal: Ur-dIg-alim ds d. Lugal-ki-gal-la.
1	subgenre_remarks	First quality dates from Urgar to Ekibi for the bala; seal: É-ki-bi ir11 [] (CBT 2)
1	subgenre_remarks	Fish (ku6 nì-ki) for the èsh-èsh, from Ur-Baba to Lú-ush-gi-na; seal: Lú-ush-gi-na d. In-ta-è-a
1	subgenre_remarks	Fish (ku6-NE) from Ur-Ninmug to Lu-Nanna; seal: Lú-∂Nanna dubsar d Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Fish and barley for several persons from Gudea for Lukirzal, for the érin; case unopened; seal: Lú-kir4-zal dumu Nimgir-DI-NE (CBT 2)
1	subgenre_remarks	Fish as food for the weaver women of the ensi from Lukalla, kiåib Un-íl (CBT 2). A: Case of 19509; sealed (CBT 2)
1	subgenre_remarks	Fish oil (ì-ku6) from Urguenna for the marsa of Guabba; received by 30-àm; seal: Ab-ba-kal-la d. Ur-é-an-na
1	subgenre_remarks	Fish oil (ì-ku6) received by Nammah from Urguenna; seal illegible (CBT 2)
1	subgenre_remarks	Fishes from Ur-Enki for the marsa; seal: Ur-∂Ba-ba6 dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Flour (dabin ninda-bala-shè) from Lu-marsa to Lu-Ningirsu.seal: Lú-dNin-gír-su ds d. Ir11-mu.
1	subgenre_remarks	Flour (dabin ì-dub é énsi-gal má Ur-∂Lamma) from Guzani to Mansina; case unopened; seal: Ma-an-sì-na dubsar dumu Lú-kir4-zal (CBT 2)
1	subgenre_remarks	Flour (dabin) from Urdam; on the boat of Ur-dSag-[ùbaki] son of Lú-URUxKAR2ki; kishib Mansina; seal: Ma-an-sì-na ds d. Lú-kiri4-zal
1	subgenre_remarks	Flour (esha) from Ur-Lama to Ur-Baba; seal: Ur-dBa-ba6 d NI-NI-MU lú-ùr-ra.
1	subgenre_remarks	Flour and beer taken in account by Lumagula; seal: Lú-má-gu-la dubsar dumu Du-du; 4 col.; Shu-Sin 2 to Ibbi-Sin 2 (CBT 2)
1	subgenre_remarks	Flour for 2 gurush for 2 months xi-xi2; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Flour for SHulgi-turi from Pi-ru-ru; seal: Ur-dBa-ba6 ds d. Na-mu.
1	subgenre_remarks	Flour for Ur shipped in vessels; 420 sìla zì-gu duk-bi 20-àm; kishib Lú-dNin-gír-su d. Bazi; from Lú-gu-la; seal: Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	Flour for gan-tush, from Urgar to Lú-nimgir; seal: Lú-nimgir ds d. AB-[]
1	subgenre_remarks	Flour for poultry (kaskal.muåen) from Ur-Nanåe to Ur-Igalim; seal: Lugal-ki-gal-la dubsar dumuLú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Flour for poultry (kaskal.muåen) from Urgar to Ur-Igalim; seal: Lugal-ki-gal-la dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Flour for poultry (kaskal.muåen); seal: Lú-bi-mu dubsar dumu Ur-∂Ig-alim (CBT 2)
1	subgenre_remarks	Flour for poultry, fromUr-gar to dUtu-mu ì-du8; seal: ·-ma-ni ds d. Mu-[]
1	subgenre_remarks	Flour for sailors from Urmes; seal: Lú-Ninaki má-lah4 d. Ur-sha6-ga
1	subgenre_remarks	Flour for scribes; from Ur-Enlil; seal: Ur-mes ds d. Ur-dLamma
1	subgenre_remarks	Flour for sá-du11 in Nippur; [seal] (CBT 2)
1	subgenre_remarks	Flour for the boat-men from Ur-Baba to Mansum; seal: Ma-an-sì-na ds d. Lú-kiri4-zal.
1	subgenre_remarks	Flour for the boats of Bazi and Lugal-hegal; case unopened; seal: Ur-∂Nin-gis-zi-da dubsar dumu Ur-åu-ga-lam-ma (CBT 2)
1	subgenre_remarks	Flour for the ensi in Nina; case unopened; seal: royal seal of Íulgi, Ur-∂Lamma di-ku5 ir11-zu (CBT 2)
1	subgenre_remarks	Flour for the kash-dé-a lugal from Ur-dEn-líl-lá; seal: Ur-dIg-alim ds d. Lú-dNin-gír-su
1	subgenre_remarks	Flour for the sons of the sukkalmah and the girsiga; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Flour for the érin going to Madga received by Ursagku; case unopened; seal: Ur-sag-ku5 dumu å-na-na (CBT 2)
1	subgenre_remarks	Flour for the érin in Ti-ma-at-dEn-líl-lá; royal seal of IS, A-bu-tzab àga-ush gal-gal dumu ì-lí-[] ir11-zu
1	subgenre_remarks	Flour for young cattle and cows from Mani to Niurum; seal: Ur-dLama énsi Lagashki Nì-ú-rum rá-gaba ir11-zu.
1	subgenre_remarks	Flour for érin, from Lú-dNin-shubur; seal: Ur-ki-su7-ka ds d. []
1	subgenre_remarks	Flour from A-mur-ilum lú-mash-gi6-ka ki Da-hi from Ur-dIg-alim; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Flour from Katar-Baba to Lú-kal-la; seal: Lú-kal-la ds d. Ur-dLama
1	subgenre_remarks	Flour from Kuli to Urnigar; seal: Ur-ni9-gar d. Ur-sukkal
1	subgenre_remarks	Flour from Lu-Dumuzi to Urbagar; tablet in case; seal: Ur-ba-gár [] (CBT 2)
1	subgenre_remarks	Flour from Lu-Ninåubur for the food of the érin é Ur-∂Utu; seal: Gù-dé-a dubsar dumu Ur-∂Utu nu-bànda (CBT 2)
1	subgenre_remarks	Flour from Lu-Ninåubur; case unopened; seal: Ur-åa6-ga dubsar dumu Du-du (CBT 2)
1	subgenre_remarks	Flour from Lugal-Anzu to Lu-marsa; months vii-viii (CBT 2). A: Case of 18943; Lú-mar-sa åu-ba-ti; seal: Ur-∂[] dubsar dumu[] (CBT 2)
1	subgenre_remarks	Flour from Lugal-kuzu to Ur=SIn; seal: Ur-dEN.ZU ds d. Lú-bi-mu
1	subgenre_remarks	Flour from Lú-dUr-Asar to Lú-dNin-shubur; seal Lú-dNin-shubur ds d. Ur-sha6-ga
1	subgenre_remarks	Flour from Lú-dUr-asar to Lu-Ninshubur; seal: Lú-dNin-shubur ds d. Ur-sha6-ga;  
1	subgenre_remarks	Flour from Lú-dUr-asar to Mansina; mu en-mah-an-na en-dNanna mash-e <ì>-pàd; seal: Ma-an-sì-na ds d. Lú-kiri4-zal.
1	subgenre_remarks	Flour from Mansina to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ur-íd-eden-na.
1	subgenre_remarks	Flour from Namhani to Ur-Lama; seal: Ur-dLama d. Eren-da gu-za-lá.
1	subgenre_remarks	Flour from Pú-ta for Al-la; seal: Ur-dNanshe ds d. Ur-é-an-na
1	subgenre_remarks	Flour from Ur-Baba to Lu-Ningirsu; seal: Lú-∂Nin-gír-su dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Flour from Ur-Baba to Ur-Lamma; seal: Ur-∂Lamma dubsar dumu A-ti-[da] (CBT 2)
1	subgenre_remarks	Flour from Ur-Giåbare to Atu; case unopened; seal: A-tu dubsar dumu Lú-∂Nanåe dubsar hé-dab5; Shulgi 46/Amar-Suen 3 (CBT 2)
1	subgenre_remarks	Flour from Ur-Igalim to Urulal; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Flour from Ur-Ningiszida to Atu; seal: A-tu ds d. Lú-dNanshe ds hé-dab5.
1	subgenre_remarks	Flour from Ur-Nintu to Ur-lugal; seal: Ur-lugal d. SHesh-kal-la shabra
1	subgenre_remarks	Flour from Ur-Sin to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Lugal-sig
1	subgenre_remarks	Flour from Ur-dEn-líl-lá; seal: Ur-dEn-líl-lá ds d. Inim-sha6 kurushda
1	subgenre_remarks	Flour from Ur-dIg-alim to Lú-gi-na, to be returned; seal: Lú-gi-na d. Kab-ush
1	subgenre_remarks	Flour from Ur-dNanshe for Ma-an-sì-na; seal: Ma-an-sì-na ds d. Lú-kiri4-zal
1	subgenre_remarks	Flour from Ur-dUtu to Lugal-me-lám; seal: Lugal-me-lám ds d. Ur-d[]
1	subgenre_remarks	Flour from Urdam to Lu-Narua; seal: Lú-dNa-rú-a ds d. Ur-sha6-ga.
1	subgenre_remarks	Flour from Urgar to Mansina; seal: Ma-an-sì-na ds  d. Lú-KA-
1	subgenre_remarks	Flour from Urzikumma to Lu-Narua (CBT 2). A: Case of 19010; seal: Lú-∂Na-rú-a dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Flour from different proveniences loaden on a boat for Nippur; seal: Ur-dIg-alim ds d. Lú-dNin-gír-su
1	subgenre_remarks	Flour from the sanga of Nin-mar-ki to Ur-bára; seal: Ur-bára dub-<<sar>> d. Nì-dBa-ba6
1	subgenre_remarks	Flour from the storehouse hi-gál to Ur-dNanshe-gishBAD; seal: Ur-dNanshe d. Lugal-E!-mah
1	subgenre_remarks	Flour from the énsi; seal: Ur-dNanshe ds d. Ur-dBa-ba6 shabra
1	subgenre_remarks	Flour giå.kiri6 Su-har˚, from Lugal-Anzu to Urmes; unopened envelope; seal: Ur-mes dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Flour loaded on boats from Lú-dingir-ra; seal: Lú-dNa-rú-a ds d. Ur-sha6-ga
1	subgenre_remarks	Flour loaden on 2 boats; seal: Lugal-kù-zu ds d. Lú-dingir-ra
1	subgenre_remarks	Flour loaden on a boat from Namhani to Ur-ni9-gar and Ku5-da; seal: Ku5-da muhaldim d. Ur-dIshtaran; Ur-ni9-gar ds d. Un-íl.
1	subgenre_remarks	Flour loaden on a boat, from Namhani to Urbishebadu11; seal: Ur5-bi-shè-ba-du11 d. Ur-kù-nun má-gín.
1	subgenre_remarks	Flour loaden on boat from Ur-Baba; kishib Ur-dNanshe má-lah4; seal: Ur-dNanshe má-lah4 d. Lú-dingir-ra
1	subgenre_remarks	Flour loaden on boats for Nippur, zì bala-a; seal: Lú-dNa-rú-a ds d. Ur-sha6-ga.
1	subgenre_remarks	Flour loaden on the boat of Lugal-shà-lá from Lú-dAsar, received by Mansina; seal: Ma-an-sì-na ds d. Lú-kiri4-zal.
1	subgenre_remarks	Flour of the ebagar from Duggazida to Lu-Ningirsu, má Lú-bala-åa6-ga má-gín; seal: Lú-∂Nin-gír-su dubsar dumu Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Flour on the boat of Urdun transferred from Lugalluåaåa to Lu-Narua; case unopened; seal: Lú-∂Na-rú-a dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Flour received by  Lú-GIÍ.apin-du10 from Du-ti-rí; seal Lú-GIÍ.apin-du10 [ ]; Drehem (CBT 2)
1	subgenre_remarks	Flour received by Lu-Ningirsu from Kuli; tablet in case; seal: Lú-∂Nin-gír-su dubsar dumu [] (CBT 2)
1	subgenre_remarks	Flour received by Lubimu; case unopened; seal: Lú-bi-mu dubsar dumu Ur-∂Ig-alim; Shulgi 46/Amar-Suen 3 (CBT 2)
1	subgenre_remarks	Flour received by Ur-Hendursag (CBT 2). A: Case of 18209; seal illegible (CBT 2)
1	subgenre_remarks	Flour received by Ur-Nanåe from Ur-∂Igi-ma-åè; seal: Ur-∂Nanåe dubsar dumu Ur-[] (CBT 2)
1	subgenre_remarks	Flour sent to Namhani; case unopened; seal: Ma-an-sì-na dubsar dumu Lú-kir4-zal (CBT 2)
1	subgenre_remarks	Flour shà é-duru5-shè; seal: Ur-dBa-ba6 ds d. IS-sha6-ga ú-du-lu
1	subgenre_remarks	Flour to be returned; seal illegible
1	subgenre_remarks	Flour tranferred from Niurum to Lu-Nanna (CBT 2). A: Case of 18779; seal: Lú-∂Na-rú-a dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Flour transferred from Katar-Baba to Lukalla, zì-gíd-da kiåib-aå-a (CBT 2). A: Case of 18778; seal: Lú-kal-la dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Flour transferred from Kuli to Lubalaåaga son of Ur-Nindara; case unopened; seal illegible (CBT 2)
1	subgenre_remarks	Flour transferred from Lu-Narua to Kuli; case unopened; seal: Ku-li dubsar dumu Ki-ág-mu (CBT 2)
1	subgenre_remarks	Flour transferred from Lu-Ningirsu to Ur-åugalamma; seal: Ur-åu-ga-lam-ma dubsar dumu Da-da (CBT 2)
1	subgenre_remarks	Flour transferred from Ur-Hendursag to Eunamti (CBT 2). A: Case of 18781; seal: É-ú-nam-ti muhaldim ir11 Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Flour transferred from Ur-Igimaåe to Urtur; seal: Ur-tur dubsar dumu Lú-∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Flour transferred from Urulal to Lukalla (CBT 2). A: Case of 18827; seal: Lú-kal-la dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Flour zì-ka Ki-nu-nirki-ra ki Ur4-re-ba-du7-ta kishib Ur-gar dumu Lugal-gaba má Ur-é-an-na dumu Ur-gar shà Ninaki; seal: Ur-gar ds d. Lugal-gaba
1	subgenre_remarks	Flour é-muhaldim lugal, from Mansum to Kur-ta-mu-gi4; seal: Ur-ki-gu-la d. Ur-dBa-ba6
1	subgenre_remarks	Flour, dabin from Udenishaga for Lu-Ninshubur; seal: Lú-dNin-shubur d. Ur-dEN.ZU muhaldim.
1	subgenre_remarks	Flour, dabin má Nì-ú-rum ki Na-ba-sha6-ga kishib Ur-gar gìr Engar-du10-ga; seal: Ur-gar ds d. A-tu ds hé-dab5
1	subgenre_remarks	Flour, dabin nì-kú-a géme-bànda bala zal-la; from month vi to month xii; seal: Ur-mes ds d. Ur-dLama
1	subgenre_remarks	Flour, dabin zì é dNin-gis-zi-da, má Ir11-ta; seal: Ma-an-sì-na ds d. Lú-kiri4-zal
1	subgenre_remarks	Flour, dabin zì-ba é-sukkal-e-ne, ki Na-ra-am-ì-lí gìr I-din-Ir3-ra; seal: Ur-dBa-ba6 ds d. Na-mu
1	subgenre_remarks	Flour, nì-dab5 gish-kin-ti; seal: Ur-dBa-ba6 ds d. Na-ma
1	subgenre_remarks	Flour, shà-gal tur-mushen-shè ki Ur-gar-ta Ur-dIg-alim shu-ba-ti; seal: Lugal-[] ds d. Lú-d[]
1	subgenre_remarks	Flour; dabin from Lu-Anzu to Lu-marsa; seal: Ur-dIg-alim ds d. Ur-[].
1	subgenre_remarks	Flour; seal: Lú-dNa-rú-a ds d. Ur-sha6-ga.
1	subgenre_remarks	Fodder for asses; sealed (CBT 2)
1	subgenre_remarks	Food expense: ak-lum; seal impressions all over the surfaces; (Obv)6x(Rev)4 lines
1	subgenre_remarks	Food for amar-ku5; from banati to Urmes the shabra; seal: Ur-mes ds d. Ur-dLamma
1	subgenre_remarks	Food for guruå and érin (bala gub-ba, bala tuå-a) from Lubimu to Lu-Baba; case unopened; seal: Lú-∂Ba-ba6 dubsar dumu Íà-da-nu-du10 (CBT 2)
1	subgenre_remarks	Food items (shim, she-li) for the boat má-u4-zal-la; seal: Lú-dBa-ba6 d. dNanshe-ga! lú-shim.
1	subgenre_remarks	For sealing bricks;
1	subgenre_remarks	Four grinding stones (har-åu-sì-ga åà géme  giå-ì sur-sur) from Lu-Ninåubur to Abbakalla; seal: Ab-ba-kal-la dubsar dumu Ur-é-[an-na] (CBT 2)
1	subgenre_remarks	Fragment of an envelope; seal: Ur-[] ds d. Ur-dNin-gír-su.
1	subgenre_remarks	Fragment of the protocol concerning silver, part of the ilku obligation of PN; seals.  8 lines
1	subgenre_remarks	Fragment; seal: Gù-dé-a ds d. Lú-dEn-líl-lá.
1	subgenre_remarks	Fragment; sealed (CBT 2)
1	subgenre_remarks	Garlic (sum gaz) for the kaå4 from Lu-dugga to Ur-Ningirsu the sukkal; seal illegible (CBT 2)
1	subgenre_remarks	Garlic from Lú-dGish-bar-è to Ur-Lama for the bala in Ur; seal: Ur-dLama ds d. Ir11-mu.
1	subgenre_remarks	Garlic seed from SHà-da; seal: Ur-dBa-ba6 ds d. Lugal-im-ru-a
1	subgenre_remarks	Garments for Ur-Baba s. of Nì-ú-rum lú-hu-burx, from Lú-kiri4-zal []; seal: A2-zi-da ds d. SHesh-shesh; rev. broken
1	subgenre_remarks	Garments from Ur-Baba to dUtu-di-ne; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Garments from Ur-é-gal Ur-dNin-pìrig; seal: Ur-dNin-pìrig ds d. Ur-sha6-ga nu-bànda gu4
1	subgenre_remarks	Garments received by Ur-Baba (CBT 2). A: Case of 19012; seal illegible (CBT 2)
1	subgenre_remarks	Garments received by Utu-mu; seal: dUtu-mu d. Lú-dBa-ba6
1	subgenre_remarks	Garments transfered from the weavers to Utumu; seal: dUtu-mu ugula lú-[] d. Lú-d[]
1	subgenre_remarks	Garments withdrawn from Lu-Ningirsu; (CBT 2). A: Case of 18802; badly disintegrated; seal dedicated to Íulgi [] (CBT 2)
1	subgenre_remarks	Garments á-gish-gar-ra géme-ush-bar énsi; case unopen; seal: Ku5-da-dBa-ba6 ds d. Ur-dNun-gal ugula ush-bar
1	subgenre_remarks	Garments; seal: SHesh-du10-ga ds d. Ur-é-an-na
1	subgenre_remarks	Garments; túg-ba sa-bu-umki-shè from Lú-ush-gi-na to SHul-gi-ì-lí; seal, illegible
1	subgenre_remarks	Gazi from Ur-dEn-ki; seal: Lú-dingir-ra ds d. Lugal-sha6-ga
1	subgenre_remarks	Gish.hashhur hád ki Ur-dInanna-ta zi-ga kishib Lú-dDumu-zi; seal illegible
1	subgenre_remarks	Goats and kids handed over by the shepherd (ú-du-lu) to Ur-Baba; case unopened; seal: Ur-∂Ba-ba6 dumu É-kù-ga (CBT 2)
1	subgenre_remarks	Goats from Sidu to Urmes son of Gaga; case unopened; seal: Ga-ga dumu Lú-∂[] [] (CBT 2)
1	subgenre_remarks	Goats from Ur-dLama son of U2-du-lu to Ur-mes; seal: Ur-mes sipa gír-gír
1	subgenre_remarks	Goats; seal: Ur-d[] sipa [] []
1	subgenre_remarks	Goods received by Ur-∂Lamma from Ur-∂Igi-ma-åè; seal: Ur-∂Lamma dumu Ab-ba-gi-na (CBT 2)
1	subgenre_remarks	Grain delivery for sá-du11 and nì-ezem-ma over 13 months by Lú-dingir-ra son of Ab-ba-mu; sealed (CBT 2)
1	subgenre_remarks	Grant of 1 gur 30 qa of grain from a retiring man (nig-shid til-la) to Damu-eribam; seal impressions all over the surfaces; (Obv)5x(Rev)4x(LE)1 lines
1	subgenre_remarks	Groats from Lugal-GIÍ.gigir-re to Urbiåe lú-åim; case unopened; seal: Ur5-bi-åè dumu A-tu lú-åim (CBT 2)
1	subgenre_remarks	Gulkišar-epic (SEAL); Nadali, Davide, Envisioning the Past (2016), p. 119: Samsuditana- Epic
1	subgenre_remarks	Gurush for canal work; seal: Lugal-zag-ge-si ds d. Ur-dIg-alim
1	subgenre_remarks	Gurush work over a few months; case and tablet; seal: Lú-d[] ds d. Lú-dBa-ba6
1	subgenre_remarks	Guruå and géme moving boats; seal: Ur-∂En-líl-lá dubsar dumu Inim-åa6 kuruåda (CBT 2)
1	subgenre_remarks	Guruå and hired men, control of Ur-Numuåda; case unopened; seal: Ur-∂Nu-muå-da dubsar dumu Du-du sanga Urub.ki (CBT 2)
1	subgenre_remarks	Guruå and oxen; seal illegible (CBT 2)
1	subgenre_remarks	Guruå controlling the waterflow at the canal Íulgi-pirig; kiåib Akalla dumu Kuli; case unopened; [seal] (CBT 2)
1	subgenre_remarks	Guruå for irrigation work, ka íd-lugal-muå-huå gub-ba; seal: Lugal-zag-ge-si dubsar dumu Ur-∂[Ig-alim] (CBT 2)
1	subgenre_remarks	Guruå moving a boat (má  giå gibil-ga) to Nippur; seal: Lú-∂Ig-alim dumu Nam-ha-ni lú-ùr?-a (CBT 2)
1	subgenre_remarks	Guruå moving a boat-load of flour to Nippur; seal: Lú-Urub˚ dubsar dumu Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Guruå to tow a boat; case unopened; seal: Ir11-∂Ba-ba6 dubsar dumu Ab-ba-ni [] (CBT 2)
1	subgenre_remarks	Guruå under the orders of Ur-∂Lamma; case unopened; seal: Ur-∂Lamma dubsar dumu Ur-gar; months vii-x (CBT 2)
1	subgenre_remarks	Guruå working on reed, control Ur-∂Nin-gír-su dumu sanga ∂Nin-dun; case unopened; seal: Ur-∂Nin-gír-su dubsar dumu Ur-GIÍ.gigir; months viii-x (CBT 2)
1	subgenre_remarks	Guruå, érin (CBT 2). A: Case of 18775; seal illegible (CBT 2)
1	subgenre_remarks	Géme work; 432 géme u4-1-shè from Lu-Narua, kishib Lú-gu-la dumu Ur-dIgi-zi-bar-ra; seal: Lú-gu-la ds d. Ur-dIgi-zi-bar-ra
1	subgenre_remarks	Géme work; seal: Lugal-kù-zu ds d. Ur-ni9-gar kush7
1	subgenre_remarks	Ha-lúm from Ur-gishgigir to Lú-dingir-ra; seal: Lú-dingir-ra ds d. Hé-ti
1	subgenre_remarks	Half a mana of silver from Lugina to the merchant A-gi4; seal: Ur-ni9-gar d. Ur-sha6-ga dam-gàr.
1	subgenre_remarks	Half of cylinder seal, seeming imitation of lapis lazuli
1	subgenre_remarks	Harper:  Contract".  Seal impressions. 9x3 lines"
1	subgenre_remarks	Harper:  Contract.  Seal impressions.9x2x8 UE 2 lines
1	subgenre_remarks	Harper:  Contract."  Seal impressions.4x5 lines"
1	subgenre_remarks	Harper:  Table of Ammi-satana." faint seal impressions. 6x2x4 UE 3 lines"
1	subgenre_remarks	Hide of sheep transferred from Lu-Igimaåe to Ur-Lamma; case unopened; seal: Ur-∂Lamma dumu Kal-la aågab (CBT 2)
1	subgenre_remarks	Hides from Nammah to Ur-abba; seal: Ur-ab-ba dubsar dumu Ba-zi dubsar síg-ka (CBT 2)
1	subgenre_remarks	Hides from Ur-Haia to Ur-Nanåe; case unopened; seal: Ur-∂Nanåe dubsar dumu Ur-∂Ig-alim (CBT 2)
1	subgenre_remarks	Hides from Ur-gú-en-na to Ur-Ningiszida aågab; mu-ús-sa [] ezem-[]; [seal] (CBT 2)
1	subgenre_remarks	Hides from Urguenna to Luåaga in Ambar˚; seal: Lú-åa6-ga  aågab dumu Lú-∂Igi-ma-åè (CBT 2)
1	subgenre_remarks	Hides of dead animals: kuå ri-ri-ga zú-si-ta, kiåib Ni-gi-ni su-si-ik (CBT 2). A: Case of 19319; seal: Ni-gi-ni dumu [] (CBT 2)
1	subgenre_remarks	Hides of dead sheep from Lu-Igimashe to Apilum; seal: A2-bí-lum ashgab Ir11-dDumu-zi d. Lú-du10-ga.
1	subgenre_remarks	Hides of oxen and sheep; nì-zi-zi uru-shè ki Lú-sha6-ga-ta ba-zi kishib é-dub-ba; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Hides of oxen, kush gu4, from Ur-dHa-ìa to the messenger house; kishib and seal: Ur-dNanshe ds Ur-dIg-alim
1	subgenre_remarks	Hides of sheep, gán dKa-si-gi4-dè, from Lu-Ninshubur to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Ba-zi.
1	subgenre_remarks	Hilprecht?, (Obv)13x(Rev)9x(UE)8x(LE)1 lines, stamp seal impressions on UE., a thumb mark on LoE.
1	subgenre_remarks	Hilprecht?, (Obv)19x(LoE)1x(Rev)13 lines, Rev.2 seal impressions and 2 labels.
1	subgenre_remarks	Hilprecht?, (Obv)9x(LoE)1x(Rev)6 lines, seal impression on the LoE.
1	subgenre_remarks	Hire of A2-dag-ga as shesh-tab-ba by Nam-zi-tar-ra; seal: Nam-zi-tar-ra ds d. Ur-dLama
1	subgenre_remarks	Hire of a servant of PN in protocol form; seals.  4x1x6 UE 2 lines
1	subgenre_remarks	Hire of harvesters; seal; 4x1x3 lines
1	subgenre_remarks	Hire of slaves; seal impressions; 12x10 lines
1	subgenre_remarks	Hiring of a servant. Inscribed.  Seal impressions. 6x1x8 UE 3 lines
1	subgenre_remarks	Honey (làl and li) from Ur-Enki to Lú-dNin-gír-su; seal: Lú-dNin-gír-su ds d. Ir11-mu
1	subgenre_remarks	Honey for the festival of Baba from Lú-Ki-nu-nir˚ the merchant to Nin-a-na (CBT 2). A: Case of 15951; seal illlegible (CBT 2)
1	subgenre_remarks	Honey from Ur-sha6-ga to Lú-dNin-gír-su, sukur sag-s`-ga-ash; seal; Lú-dNin-shubur ds d. Ir11-[]
1	subgenre_remarks	Honey, làl and shim, received by Lugal-gú-gal from Ur-gú-en-na;  seal: Lugal-gú-gal ds d. Lú-dBa-ba6
1	subgenre_remarks	Hullentafel; dowery; seals; 14x1x13x1 (le.e.) lines; 8.1x6.0x3.1 cms
1	subgenre_remarks	Hullentafel; dowry (?); seals; 14x5x13 lines; 9.9x6.0x3.6 cm
1	subgenre_remarks	Hullentafel; heritage; seals; labels; 14x18x3(u.e.) lines; 10x6.5x2.6 cms
1	subgenre_remarks	Hé-dab5 employed in field work; case unopened; seal: Ur-ni9-gar dubsar dumu Lú-∂Nin-åubur (CBT 2)
1	subgenre_remarks	Illegible because of case; seal: SHà-ba-na-sig shabra É-zi-mu ir11-zu
1	subgenre_remarks	Ilum-rapi, the merchant, received apples, using the seal of Baba-tab; "when his seal is produced, this tablet will be destroyed."#
1	subgenre_remarks	Inheritance; division of fields; seals; 13x15x1 (lo.e.)x 18x19 lines; 9.6x6.7x3.5 cms
1	subgenre_remarks	Inscribed, with case (inscribed, with seal impressions) repaired. 4x3x6 UE 2 LE 2 lines
1	subgenre_remarks	Inscribed.  Seal impressions.  7x1x7 UE 3 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 24x3x20 UE 3 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 4x2x4 UE 1 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 4x2x5 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 5x5 UE 1 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 8x6 UE 5 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 8x9 UE 3 lines
1	subgenre_remarks	Inscribed.  Seal impressions. 9x3x9 lines
1	subgenre_remarks	Inscribed.  Seal impressions.13x14 UE 2 lines
1	subgenre_remarks	Inscribed.  Seal impressions.8x3x6 UE 3 lines
1	subgenre_remarks	Inscribed.  With Inscribed case, repaired and seal impressions. 8x2x8 UE 2 lines
1	subgenre_remarks	Inscribed.  With case (seal impressions, repaired).  5x3x6 UE 2 lines
1	subgenre_remarks	Inscribed.  With case, repaired.Seal impressions (0n envelope only) 6x2x6 UE 2 LE 2 lines
1	subgenre_remarks	Inscribed.  With fine case, repaired. Seal impressions on envelope. 7x1x7UE2 LE 1 lines
1	subgenre_remarks	Inscribed.  With fragment case (repaired). Seal impressions on case.  14x12 lines
1	subgenre_remarks	Inscribed.  With fragment case, rapaired. Seals (on envelope only) 7x2x8UE 2 lines
1	subgenre_remarks	Inscribed. seal impressions.  13x4 UE 1 lines
1	subgenre_remarks	Interest (maå?) passing from Lugalnammah to Lu-Lagaå, gìr Lugal-ezem; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Inventory of all kinds of flour, in the charge of Ur-∂Ig-alim (CBT 2). A: Case of 16226; seal illegible (CBT 2)
1	subgenre_remarks	Inventory of sheep and rations in grain; seal: Ur-∂EN.ZU dumu Ur-gú-en-na rá-gaba (the sign en is written twice upside down) (CBT 2)
1	subgenre_remarks	Inventory of various objects; seals; 9X1X9
1	subgenre_remarks	Investiture of 6 offices in the temple of Enki and Damgalnunna by 2 men; Seal impressions all over the surfaces; (Obv)6x(Rev)4x(UE)4 lines
1	subgenre_remarks	Irregular, w/fine seal impression(pseudo-Kassits?)
1	subgenre_remarks	Issue (zi-ga) of a goat; case unopened; seal dedicated to Íulgi, Ur-∂Lamma di-ku5 ir11-zu (CBT 2)
1	subgenre_remarks	Issue (zi-ga) of barley from Lugal-a-ma-ru; seal: å-zi-da dubsar dumu Íeå-åeå (CBT 2)
1	subgenre_remarks	Issue of barley; seal: Ur-[zi] má-lah4 dumu Ur-Ma-ma (CBT 2)
1	subgenre_remarks	Issue of flour (åik, dub-dub), pease-meal and eåa, withdrawn by Ur-∂Lamma (?); seal of the ensí. (CBT 1)
1	subgenre_remarks	Item received from Ur-Nungal by Su-shim-[] a-ush-tur; seal illegible.
1	subgenre_remarks	Items for the festival; shim, làl, nì-ezem-ma-shè ki Ur-sha6-ga-ta to Lú-sha6-ga; seal: Lú-sha6-ga ds d. Ab-ba-mu
1	subgenre_remarks	Kiåib  Lugal-lú-åa6-åa6; tablet in case; seal illegible; Amar-Suen 1/Shu-Sin 1 (CBT 2)
1	subgenre_remarks	Label for basket containing sealed documents of Lukala
1	subgenre_remarks	Label.  Seal impression.  Holes at corner.  Triangular.
1	subgenre_remarks	Label; seed of sum-sikil from Íadu to Kaa the santana; seal: Ka5-a dumu Ur-é-an-na [] åu-∂En-líl (CBT 2)
1	subgenre_remarks	Lard (ì-sháh) from Ur-abba to Ni-Baba; seal: Nì-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Lard from Urabba to Urguenna; seal: Ur-gú-en-na dubsar dumu Lú-dingir-ra (CBT 2)
1	subgenre_remarks	Large reed mat for a boat, with bread, from Ludingirra to Lugalnammah; seal: Lugal-nám-mah dumu Za-a-a lú [] (CBT 2)
1	subgenre_remarks	Large reed-mat from Lu-Ningirsu to Akalla; seal: A-kal-la dubsar dumu Ur-åa6-ga dubsar [] (CBT 2)
1	subgenre_remarks	Lease of a house.  Seal impressions (on case only).  9x2x7 UE 3 lines
1	subgenre_remarks	Lease of land; seal impressions on all the edges & Rev; *5th year after the capture of Isin; (Obv)10x(LoE)1x(Rev)5 lines
1	subgenre_remarks	Leather for the house of the messengers and to make glue (åe-gín) received by Kuraniåa; case unopened; seal: Gú-ra-ni-ì-åa6 dumu Lugal-[ ] (CBT 2)
1	subgenre_remarks	Leather from Lu-Igimaåe to Luåaga; seal: Lú-åa6-ga aågab dumu Lú-∂Igi-ma-åè (CBT 2)
1	subgenre_remarks	Leather from Lú-sha6-ga to Ur-dLama; seal: Ur-dLama [  ].
1	subgenre_remarks	Leather received by Ur-∂Nanåe; seal illegible (CBT 2)
1	subgenre_remarks	Leather, kush é-sir from Lú-sha6-ga to SHesh-kal-la; seal: SHesh-kal-la ds d. Nam-mah
1	subgenre_remarks	Leather; case unopened; seal illegible (CBT 2)
1	subgenre_remarks	Ledger of materials weighed in minas and shekels; seal; 4x4 lines; 8.5x3.2x3.1cm
1	subgenre_remarks	Ledger of rations for ummanu; seals; 7x2 lines
1	subgenre_remarks	Ledger of workers and barley; seals; 7x1x5 lines
1	subgenre_remarks	Ledger; Personal and month names, and numbers preserved; seals; 12x11 lines
1	subgenre_remarks	Ledger; barely, emmer and other commodities; seals; 2x1(u.e.) lines
1	subgenre_remarks	Ledger; cattle; listed by age; seal; 11x6 lines
1	subgenre_remarks	Ledger; cereal rations?; seal; 9x1 lines
1	subgenre_remarks	Ledger; cereals; seal; 13x11 lines
1	subgenre_remarks	Ledger; cereals; seals; 5x3 lines
1	subgenre_remarks	Ledger; expenditures for days 18-29; seal of Enlil-nadin-ahhe; 8x1 line
1	subgenre_remarks	Ledger; expenditures of barley for a man between 28/V-10/IV; seals; 8x5 lines
1	subgenre_remarks	Ledger; expenditures; seal of Enlil-nadin-ahi; cf. 29-15-778, 29-15-780; 6 lines
1	subgenre_remarks	Ledger; expenditures; seals; 5x1 line
1	subgenre_remarks	Ledger; impression of seal? w/inscription on Rev.mid.Lo.part; (Obv)14x(Rev)18x(UE)1 lines
1	subgenre_remarks	Ledger; only personal names preserved on obv; seals; 18x6 lines
1	subgenre_remarks	Ledger; only personal names preserved; seal; 8x1 line
1	subgenre_remarks	Ledger; oxen and cattle; scribe: Awel-Marduk; seal; 11x10 lines
1	subgenre_remarks	Ledger; personal names only; seal; 16x9 lines
1	subgenre_remarks	Ledger; rations; seals; 5x4 lines
1	subgenre_remarks	Ledger; seals; 1310 lines
1	subgenre_remarks	Ledger; seals; 7 lines
1	subgenre_remarks	Ledger; seals; cereals (qa); 11x9 lines
1	subgenre_remarks	Legal document; case fragment: 9 lines, seal impressions, *tablet missing
1	subgenre_remarks	Legal document; w/seal impressions; Harper's mark Ni.41-2-16-89 (Feb. 16).*Peters describes as Nippur I, though Ur II tablets are characteristic to Nippur II. I" came from Tablet Hill
1	subgenre_remarks	Legal testimony; mentions both Damiq-ilishu and Rim-Sin; seals on envelope; 17x5x24x26
1	subgenre_remarks	Legal; seal; 8x7 lines
1	subgenre_remarks	Length of a wood from Ur-abba; seal: E2-íd-lú-ru ds [?]
1	subgenre_remarks	Letter concerning a field: Awilamma to Awel-d.?; seals; 6x5 lines
1	subgenre_remarks	Letter enclosed in an envelope.  Sealed and addressed to Lushtamar.
1	subgenre_remarks	Letter order; seal
1	subgenre_remarks	Letter order; seals; 2 lines
1	subgenre_remarks	Letter order; seals; 3x3 lines
1	subgenre_remarks	Letter to Ka[...]; 4x2x4 lines; seal impr. on le.e., lo.e., u.e. & rev.
1	subgenre_remarks	Letter to Lustamar concerning a claim against a house.  Enclosed in envelop and sealed.
1	subgenre_remarks	Letter, from Gimil-ili to Ibi-ilim; cylinder seal impressions of all the sides, letter complete, envelope with eight seal impressions.  Tablet:(Obv)7x(LoE)1x(Rev)8x(UE)2x(LE)2 lines, Envelope:(Obv)2 lines, *date: before Hammurapi
1	subgenre_remarks	Letter, to(ana) awe^[lim]; 1 line, 4 impressions of the same cylinder seal
1	subgenre_remarks	Letter.  Fine seal impressions. 9X1X2 lines
1	subgenre_remarks	Letter.  To Sin-[..].  Obv.6 lines. Rev.a part of a seal impression.
1	subgenre_remarks	Letter; Letter to Luga^; Tablet:(Obv)19x(Rev)7 lines, Case:seal impressions only
1	subgenre_remarks	Letter; seals; 7x7 lines
1	subgenre_remarks	Letter; three seals; 5x2x4x2 lines
1	subgenre_remarks	Lg case of 7126 with fine seal impressions; Letter?;
1	subgenre_remarks	Liqtum for the wood (giå.hum) of the royal boat issued by A-gi4 to Lú-∂Nin-gír-su son of Ba-zi; case unopened; seal illegible (CBT 2)
1	subgenre_remarks	List nominative of men; seal?
1	subgenre_remarks	List of accounts with peculiar Kassite seal impression with metal cap on UE.&LE.; (Obv)8x(Rev)11 lines
1	subgenre_remarks	List of cattle and donkeys (a-ru-a gifts to the temple) handed over by Ba-a to Lú-∂Nin-gír-su. / Case: Text and date same as on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	List of farmers; seals; 13x10 lines
1	subgenre_remarks	List of food supplies; Ur3 seal impression all over the surfaces; (Obv)8 lines, (Rev)blank
1	subgenre_remarks	List of garments and descriptions; seals; 15x1 lines
1	subgenre_remarks	List of grain assignments; seal impressions all over the surfaces; (Obv)12x(LoE)2x(Rev)6x(UE)2 lines
1	subgenre_remarks	List of names.  Seal impression.  Upper part of a small tablet
1	subgenre_remarks	List of names; Remarkable Greek(?) Seal impression" (Actually a stamp seal impression.  The design is not clear and shows no evidence to identify it as a Greek seal.); (Obv)9x(LoE)1x(Rev)1 lines"
1	subgenre_remarks	List of officials and employees; w/seal impressions; (Obv)14x(Rev)11 lines
1	subgenre_remarks	List of receipts of grain; w/seal impressions; (Obv)5x(Rev)6x(UE)1x(LE)2 lines
1	subgenre_remarks	List of various quantities of animals; seals; 5x4x1 line
1	subgenre_remarks	List of workers and tools; seals; 8x10x1(u.e.) lines
1	subgenre_remarks	List; seal impressions all over the surfaces; (Obv)4x(LoE)2x(Rev)4 lines
1	subgenre_remarks	Literary excerpts; seal; 5x4 lines
1	subgenre_remarks	Litigation over the repayment of a loan of silver; Babylon; (LoE)3 seals, 3 labels; (UE)2 seals, 2 labels; (LE)1 seal, 1 label; (RE)1seal, 1 label; 12x13 lines
1	subgenre_remarks	Loan of 2 1/2 shekels of gold; witnesses; seals; 8x8x1(le.ed.) lines
1	subgenre_remarks	Loan of a cow; seal
1	subgenre_remarks	Loan of barley (åe åuku énsi åe ur5-ra-åè) received by Ur-giå-dar-dù from Ur-ni9-gar; case unopened; seal: Ur-giå-dar-dù dumu Ur-∂Nin-gis-zi-da (CBT 2)
1	subgenre_remarks	Loan of barley for Ur-Ningiszida from Ur-Enlilla; case unopened; seal: Ur-∂Nin-gis-zi-da dub-sar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Loan of barley for dumu gu4-gur-da, given by Bazi; seal: Ur-Ma-ma d. Nam-ha-ni
1	subgenre_remarks	Loan of barley for engar, dumu gu4-gur and dumu da-ba, from Abbakalla to Mansum; seal: Ma-an-sum ds d. Du11-ga-dingir.
1	subgenre_remarks	Loan of barley for field workers (she-ur5-ra she shukur-ra énsi; seal: Ma-an-sum ds d. Du11-ga-dingir
1	subgenre_remarks	Loan of barley for field workers: engar, dumu gu4-gur, dumu-da-ba; case unopened; seal: NI-NI dumu Ur-dun nu-bànda (CBT 2)
1	subgenre_remarks	Loan of barley for the dumu-da-ba ì-dub é-duru5 Ur-li ki Ba-zi-ta. Seal: Du-du [...] (CBT 3)
1	subgenre_remarks	Loan of barley for érin; seal: Lú-Lagashki dumu Ba-za-a.
1	subgenre_remarks	Loan of barley form Ur-Baba to SHakuge; seal SHà-kù-ge ds d. Lú-kal-la
1	subgenre_remarks	Loan of barley from Ba-zi to Du-du-ni. Seal: Du-du-ni ugula bànda-dab5-ba dumu Ir11-hé-du10 (CBT 3)
1	subgenre_remarks	Loan of barley from Bazi; seal illegible
1	subgenre_remarks	Loan of barley from Ur-badtibirra to Ur-Igalim; seal: Ur-dIg-alim d. Da-da.
1	subgenre_remarks	Loan of barley from Urbadtibirra to Abbakalla, to be returned; seal: Ab-ba-kal-la dumu A-a-gu-ni
1	subgenre_remarks	Loan of barley from the sanga of Nin-mar-ki to Lugal-ur-sag; seal: Lugal-ur-sag gala-mah Hu-rímki
1	subgenre_remarks	Loan of barley to buy wool; seals; 9x1x6x2(u.e.)x1(le.e) lines; 6.5x4.3x1.7 cm
1	subgenre_remarks	Loan of barley to érin; she-ur5-ra érin-na du6-sa-bar-ta ki Ba-zi-ta kishib Ur-dIg-alim d. Ush-mu nu-bànda Ur-sha6-ga gìr A-tu; seal: Ur-dIg-alim ds d. Ush-mu
1	subgenre_remarks	Loan of barley with interest; seals; 2x4 lines
1	subgenre_remarks	Loan of barley with interest; seals; 6x5 lines
1	subgenre_remarks	Loan of barley, 16 gur 8 gín kù-babbar lá-dam; seal: Ur-dBa-ba6 ds d. Lugal-im-ru-a nu-bànda
1	subgenre_remarks	Loan of barley, with and without interest, and loan of money, without interest; seal impressions on tablet & case; tablet (Obv)9x(Rev)7 lines, case (Obv)10x(Rev)9 lines
1	subgenre_remarks	Loan of barley, with interest; seal impressions on case & tablet; (Obv)8x(Rev)9 lines
1	subgenre_remarks	Loan of barley, åe ur5-ra maå gá-gá, from Ur-bàd-tibir-ra to Ur-∂Iåkur dumu E-a. Seal: Ur-∂Iåkur dumu E-a [...] (CBT 3)
1	subgenre_remarks	Loan of barley, åe ur5-ra érin {giå}ma-nu ki Ba-zi-ta kiåib ∂Nanåe-kam ugula. Seal: ∂Nanåe-kam ugula dumu Lú-pàd-da (CBT 3)
1	subgenre_remarks	Loan of barley; case half-broken; seal illegible
1	subgenre_remarks	Loan of barley; seals.  7x1x7 UE 2 lines
1	subgenre_remarks	Loan of grain and money with interest;Sippar; four seals with names; 6x1x6x1 line
1	subgenre_remarks	Loan of grain with interest in money; 10x10 lines; 7.4x5x2.7 cm; seal impr
1	subgenre_remarks	Loan of grain with interest; seals; 8x2x8 lines
1	subgenre_remarks	Loan of grain; w/seal impressions; (Obv)4x(Rev)4x(UE)2x(LE)1 lines
1	subgenre_remarks	Loan of grain; w/seal impressions; (Obv)6x(Rev)4 lines
1	subgenre_remarks	Loan of money; seal impressioons all over the surfaces; (Obv)6x(Rev)7x(UE)3 lines
1	subgenre_remarks	Loan of silver from the wool business of the palace to be repaid in one month; seals.  7x3x6 UE 3 lines
1	subgenre_remarks	Loan of silver to buy a slave girl, a female ox driver; seals;  9x2x7x3(u.e.)x1(le.e.) lines; 6.4x4.7x2.6 cm
1	subgenre_remarks	Loan of silver to buy oil; seals; 6x6x1(u.e.)x3 (le.e.) lines; 3.8x.46x2.6 cms
1	subgenre_remarks	Loan of silver to buy wool to be repaid in 1 month.  Seal impressions.  8x2 lines
1	subgenre_remarks	Loan of silver with interest at 25% to lu-d-Inanna from Ur-d-IMl d-Inanna; seals; 5x8x1 lines"
1	subgenre_remarks	Loan of silver with interest with house as collateral; seals; 10x11x1 (u.e.)
1	subgenre_remarks	Loan of silver with interest; seals; 8 lines
1	subgenre_remarks	Loan of silver without interest; seals; 5x7x1(u.e.) lines
1	subgenre_remarks	Loan of silver; seals; 7x3x7x3 lines; 4.5x4.2x1.4 cm
1	subgenre_remarks	Loan of silver; seals; 7x7 lines
1	subgenre_remarks	Loan of silver; w/seal impressions; (Obv)4x(Rev)7 lines
1	subgenre_remarks	Loan to be returned; seal: Al-la dumu Ku5-da ugula (CBT 2)
1	subgenre_remarks	Loan with interest; seals; 9x4 lines
1	subgenre_remarks	Loan without interest; w/seal impressions; (Obv)8x(LoE)2x(Rev)6x(UE)1 lines
1	subgenre_remarks	Loan; seal impressions; (Obv)4x(Rev)6x(UE)1 lines
1	subgenre_remarks	Loan; witnesses; seals; 8x1(le.e.) lines
1	subgenre_remarks	Loans of barley; seal illegible
1	subgenre_remarks	Lí-iq-tum from the merchant Ur-Íulpae and planks for the boat of the sukkalmah; seal: Lú-∂Nin-gír-su dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Male sheep delivered by Du11-ga-zi-da to A-a-kal-la; case unopened; seal: Ur-[] dubsar dumu Lú-∂[] (CBT 2)
1	subgenre_remarks	Manumission document; 12 lines, 2 kinds of seal impressions on all the sides.  *A piece of paper in the drawer says 4886 to 4900 ? 6/26/67""
1	subgenre_remarks	Marriage contract of a priest of enlil, pre-marital agreement; seal impressions; (Obv)17x(Rev)18 lines
1	subgenre_remarks	Marriage contract; seal impressions; lines uncountable
1	subgenre_remarks	Marriage contract; seals; 18x1x20x5 lines; 11.x8.8x2.2 cm
1	subgenre_remarks	Marriage contract; seals; 5x5x2(u.e.) lines
1	subgenre_remarks	Mechant account; seals; 5 lines
1	subgenre_remarks	Memo concerning 24 harvesters for Shamash; seven seals; 4x3 lines
1	subgenre_remarks	Memo concerning wool; seals; 8x3 lines
1	subgenre_remarks	Memorandum concerning field work; seals; 5x1x5x2(u.e.) lines
1	subgenre_remarks	Memorandum of a loan of money.  Inscribed seal impressions. 7x3x7 UE 2 LE 1 lines
1	subgenre_remarks	Memorandum.  Seal impressions of two lions attacking a gazelle. 8x1x4 UE 1 lines
1	subgenre_remarks	Messenger; seal: [] ds d. Ur-d[].
1	subgenre_remarks	Metal objects from Ur-Ningiszida to En-abzu-ki-ág; seal: Ur-dSHul-pa-è ds d. Hé-sha6
1	subgenre_remarks	Metal, urudu and an-na ki dam-gàr-ta Ur-dNin-gis-zi-da shu-ba-ti; seal: Ur-dNin-gis-zi-da simug d. A2-zi-da
1	subgenre_remarks	Mill stones, na4 har-shu-sì-ga a-ru-a dNin-mar-ki shà-gal [] ki Lú-hu-rímki kishib Lú-dNin-gír-su; seal: Lú-dNin-gír-su ds d []
1	subgenre_remarks	Milling work of géme; seal: Ir11-dLama d.Ur-mes lú-mug.
1	subgenre_remarks	Money given for the purchase of commodities elsewhere; 8x2x7x3 lines; 2 labels on LE, 1 label on Rev; seal impressions all over the surfaces; cf.Landsberger & Balkan, Belleten 14, p.247
1	subgenre_remarks	Mostly illegible; [seal] (CBT 2)
1	subgenre_remarks	Mostly illegible; seal illegible (CBT 2)
1	subgenre_remarks	Mostly illegible; seal: Al-la dubsar dumu Nam-zi (CBT 2)
1	subgenre_remarks	Murashu Archive; w/seal impression; (Obv)4x(Rev)5x(UE)1x(LE)2 lines
1	subgenre_remarks	Murashu Archives; (Obv)7x(Rev)8 lines; 1 seal & 1 label on RE.
1	subgenre_remarks	Murashu Archives; 1 stamp seal imp.& 1 label on Rev.; (Obv)14x(Rev)6 lines
1	subgenre_remarks	Murashu Archives; Seal impressions on UE.&LE., nail impression on Rev., (Obv)13x(Rev)5 lines
1	subgenre_remarks	Murashu Archives; W/Seal impressions; (Obv)7x(Rev)4 lines; LoE:2 stamp seal imps, 2 labels; Rev:1 stamp seal imp, 1 label; RE:1 stamp seal imp, 1 label
1	subgenre_remarks	Murashu Archives; contract in dialogue form; w/seal impressions; (Obv)5x(Rev)2 lines
1	subgenre_remarks	Murashu Archives; debt; w/seal impressions on Obv.&UE; (Obv)3x(Rev)4x(UE)4 lines
1	subgenre_remarks	Murashu Archives; debt; w/seal impressions; (Obv)6x(Rev)2x(LE)2 lines
1	subgenre_remarks	Murashu Archives; lease to Murashus; (LoE)1 seal impression & 2 labels; (Rev)2 seal impressions & 2 labels; (Obv)6x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Murashu Archives; miscellaneous contract, loan of consumption; w/seal and thumbnail impressions; (Obv)6x(Rev)3x(UE)3 lines
1	subgenre_remarks	Murashu Archives; miscellaneous contract, release of distrained debtors, in dialogue form; a seal impression, a nail impression & a label on LoE; a label on LE; (Obv)9x(Rev)2x(LE)2 lines; * Stolper drops a label of a seal impr. on LoE.
1	subgenre_remarks	Murashu Archives; mortgage, 50 gur dates; w/seal impressions; (Obv)9x(Rev)7 lines
1	subgenre_remarks	Murashu Archives; mortgage; (Obv)5x(Rev)2 lines; w/seal impressions
1	subgenre_remarks	Murashu Archives; mortgage; w/seal impressions; (Obv)4x(LoE)2x(Rev)2 lines
1	subgenre_remarks	Murashu Archives; names of witnesses; w/thumbnail and seal impressions; (Obv)2x(Rev)9x(LE)2 lines
1	subgenre_remarks	Murashu Archives; receipt; a seal impression & a label on LE; (Obv)1x(LoE)2x(Rev)6 lines
1	subgenre_remarks	Murashu Archives; receipt; w/a seal impression & a label on LE.; (Obv)11x(LoE)2x(Rev)10 lines
1	subgenre_remarks	Murashu Archives; receipt; w/seal impressions; (Obv)4x(Rev)3x(UE)2 lines
1	subgenre_remarks	Murashu Archives; taxes; w/Hittite(?) seal impression; (Obv)7x(Rev)7x(UE)4 lines
1	subgenre_remarks	Murashu Archives; taxes; w/seal impressions on LoE.&Rev, labels on LoE.; (Obv)6x(Rev)6 lines
1	subgenre_remarks	Murashu Archives; taxes; w/seal impressions; (Obv)4x(Rev)3 lines
1	subgenre_remarks	Murashu Archives; taxes; w/seal impressions; (Obv)5x(Rev)3x(LE)2 lines
1	subgenre_remarks	Murashu Archives; taxes; w/seal impressions; (Obv)8x(Rev)2x(UE)3x(RE)3 lines
1	subgenre_remarks	Murashu Archives; w/(Rev)a seal impression & a label, (LE)seal impression & a label; (Obv)2x(LoE)2 lines
1	subgenre_remarks	Murashu Archives; w/Aram. inscription; seal impressions on LoE & RE.; (Obv)6x(Rev)6x(UE)1 lines
1	subgenre_remarks	Murashu Archives; w/seal impression; (Obv)4x(Rev)3x(UE)2 lines
1	subgenre_remarks	Murashu Archives; w/seal impressions; (Obv)2x(Rev)2 lines
1	subgenre_remarks	Murashu Archv.: (Obv)15x(Rev)10 lines, (LoE,UE,LE)2 seal impressions & 2 labels, (Rev)1 seal impression & 3 nail marks & a label,(RE)1 label.
1	subgenre_remarks	Murashu Archv.; 2 labels and a seal impression on LE, 3 labels and 3 seal impressions on LoE.; (Obv)16x(Rev)13x(UE)4 lines.
1	subgenre_remarks	Murashu Archv.;thumb-nail impressions.  (Obv)11x(LoE)3x(Rev)7x(LE)3 lines, a seal impression and a label on UE.
1	subgenre_remarks	Murashu Arcv.; (LoE & UE) 3 seal impressions & 3 labels, (UE)2 seal impressions & 2 labels, (Obv)13x(Rev)8 lines.
1	subgenre_remarks	Murashu Arcv.; Seal impressions and labels on (Obv)1,(LoE)3,(UE)2,(LE)1 & (RE)2, (Obv)14x(Rev)7 lines.
1	subgenre_remarks	Murashu archive; unclassifiable; w/seal impressions; 8 lines
1	subgenre_remarks	Murashu, (Obv)10x(LoE)1x(Rev)8 lines, seal impressions on edges &.Rev. 5x6x2.5
1	subgenre_remarks	Murashu, (Obv)10x(Rev)8 lines, nail impression on UE., seal impressionson LE., 6.9x8.3x2.6
1	subgenre_remarks	Murashu, (Obv)11x(LoE)1x(Rev)10 lines, seal impressions & signatures on edges & Rev., 6.25x8.4x2.9
1	subgenre_remarks	Murashu, (Obv)11x(LoE)2x(Rev)7 lines, seal impressionson Rev.& edges, 6.3x8.2x2.85
1	subgenre_remarks	Murashu, (Obv)11x(Rev)6 lines, seal impressions & signature on UE., LoE., Rev., 2 lines Aramaic on upper edge, 6.65x8x3
1	subgenre_remarks	Murashu, (Obv)11x(Rev)7 lines, 2 seal impressions & 2 labels on UE., nail impression?, inked Aramaic edoresement on LoE.& Rev., 6x6.2x2.6
1	subgenre_remarks	Murashu, (Obv)11x(Rev)7, seal impressions & nail impressions, signatures on edges, 6.95x8.3x3
1	subgenre_remarks	Murashu, (Obv)11x(Rev)8 lines, seal impressions on Rev.
1	subgenre_remarks	Murashu, (Obv)11x(Rev)9 lines, nail & seal impressions on edges, 6.58x7.75x2.9
1	subgenre_remarks	Murashu, (Obv)11x(Rev)9 lines, seal impressions & signature on edges, 6.3x8.5x3.25
1	subgenre_remarks	Murashu, (Obv)12x(LoE)1x(Rev)6 lines, seal impressions& signature on edges, 6.1x7.8x2.75
1	subgenre_remarks	Murashu, (Obv)12x(LoE)2x(Rev)10 lines, nail impression on LoE., seal impressions on UE.& LE., 6.15x8.05x3.1
1	subgenre_remarks	Murashu, (Obv)12x(Rev)7 lines, seal impressions on Rev.& edges, 8.2x6.35x3.1
1	subgenre_remarks	Murashu, (Obv)12x(Rev)8 lines, seal impression in edges, 5.85x7.6x2.95
1	subgenre_remarks	Murashu, (Obv)12x(Rev)8 lines, seal impression on Rev.& edges, 5.95x6.94x2.87
1	subgenre_remarks	Murashu, (Obv)13x(LoE)1x(Rev)9 lines, seal impressions & signature on UE.,LE.& LoE., 6.6x8.65x3.2
1	subgenre_remarks	Murashu, (Obv)13x(LoE)3x(Rev)10x(UE)1 lines, nail & seal impression on UE.& LE., 8.4x6.24x2.8
1	subgenre_remarks	Murashu, (Obv)13x(Rev)10 lines, seal impressions, nail impressions & signatures on edges, cloth impression on Rev., LoE.published as LE., 6.4x8.1x3
1	subgenre_remarks	Murashu, (Obv)13x(Rev)10, seal impressions, signatures on edges & Rev., 6.15x8.45x3
1	subgenre_remarks	Murashu, (Obv)13x(Rev)6 lines, seal impressions & signature on Rev.& edges, 8.3x9.5x3.35
1	subgenre_remarks	Murashu, (Obv)13x(Rev)7 lines, seal impressions on edges & Rev., 6.55x7.95x2.8
1	subgenre_remarks	Murashu, (Obv)13x(Rev)7 lines, seal impressions on edges, nail impression on LoE., 6x7.7x2.8
1	subgenre_remarks	Murashu, (Obv)13x(Rev)8 lines, seal impressions & signature on edges, 6.6x8.15x2.78
1	subgenre_remarks	Murashu, (Obv)13x(Rev)8 lines, seal impressions, nail impression & signatures on UE.,LE.& Rev., 6.45x7.55x3
1	subgenre_remarks	Murashu, (Obv)14x(Rev)12 lines, seal impressions on LE., nail impression on LoE., Aramaic on UE., *not left as BE 10 52.
1	subgenre_remarks	Murashu, (Obv)14x(Rev)7 lines, seal impressions & signature on all edges except RE., Aramaic endorsement in ink on Rev., 6.9x8.9x3.15
1	subgenre_remarks	Murashu, (Obv)14x(Rev)8 lines, seal impressions on LE.&LoE., nail impression on LE., 6.5x8.25x3.05
1	subgenre_remarks	Murashu, (Obv)15x(Rev)6 lines, seal impressions on edges, 7.6x9.65x3.1
1	subgenre_remarks	Murashu, (Obv)18x(Rev)8 lines, seal impression & signature on edges, 8.1x6.4x3.2
1	subgenre_remarks	Murashu, (Obv)5x(Rev)8 lines, seal impression & signature on Obv.
1	subgenre_remarks	Murashu, (Obv)6x(Rev)6 lines, nail & seal impressions on edges, 6.95x8.4x3.1, *catalogue says day 5.
1	subgenre_remarks	Murashu, (Obv)6x(Rev)8 lines, seal impression on Obv.& edges
1	subgenre_remarks	Murashu, (Obv)8x(LoE)2x(Rev)5 lines, seal impressions on UE.&LoE., inked Aramaic on Obv.
1	subgenre_remarks	Murashu, (Obv)8x(Rev)13 lines, seal impressions & signature on Obv.,LE.,& LoE.
1	subgenre_remarks	Murashu, (Obv)8x(Rev)5, seal & label on UE., 4.4x6x2.8
1	subgenre_remarks	Murashu, (Obv)8x(Rev)6 lines, seal impressions & signature on edges, 7.84x10.85x3.3
1	subgenre_remarks	Murashu, (Obv)8x(Rev)8 lines, seal impressions on LE.& LoE., 6.6x7.9x3
1	subgenre_remarks	Murashu, (Obv)9x(LoE)1x(Rev)8 lines, seal impressions on LE.
1	subgenre_remarks	Murashu, (Obv)9x(Rev)10 lines, seal impressionson LoE.& Rev., 5.9x7.6x2.65
1	subgenre_remarks	Murashu, (Obv)9x(Rev)6 lines, seal impressions & signatures on edges, 7.1x5.5x3.1
1	subgenre_remarks	Murashu, (Obv)9x(Rev)6 lines, seal impressions & signatures on edges, 9.7x6.6x2.8
1	subgenre_remarks	Murashu, 4 lines of Aramaic inscription on Rev.& UE., seal impression on edges & Rev., (Obv)11x(LoE)3x(Rev)8 lines, 5.98x7.5x2.6
1	subgenre_remarks	Murashu, Aramaic or Rev., (Obv)13x(LoE)1x(Rev)9 lines, nail impression on Rev., seal impressions on edges, 6.35x8x2.7
1	subgenre_remarks	Murashu, Lease of certain fish pools; seal impressions on 3 edges & Rev., (Obv)14x(Rev)6 lines, 6.08x8.7x2.9
1	subgenre_remarks	Murashu, Release given for a claim for damages arising from trespass; (Obv)17x(LoE)4x(Rev)15 lines, seal & nail impressions on edges & Rev., 7.5x9x3.25
1	subgenre_remarks	Murashu, Traces of Aramaic on Rev., (Obv)11x(Rev)7 lines, seal impressions & signatures on Rev.& edges, 6.35x8.35x2.95
1	subgenre_remarks	Murashu, a mortgage; seal impressions on UE.& LE., nail impression on LoE., (Obv)11x(LoE)2x(Rev)8 lines, 6x7.2x2.75
1	subgenre_remarks	Murashu, agreement to abandon legal precedings; seal impressions on LoE., UE.&LE., (Obv)14x(Rev)13 lines, 7.5x10(fr)x3.2
1	subgenre_remarks	Murashu, agreement to farm certain lands and split the profits; Aramaic inscriptions incised on LE.& Rev., (Obv)9x(LoE)2x(Rev)6 lines, seal impressions on LE.& Rev., Mus.Photo 1179, 4.3x5.35x1.75
1	subgenre_remarks	Murashu, gift of silver as the tax; 2 lines of Aramaic incised on Rev., seal impressions on Obv.&UE., (Obv)7x(Rev)6 lines, 5.2x6.4x2.4, *BE 10 78, pl.5 no.7
1	subgenre_remarks	Murashu, hire of oxen; (Obv)11x(Rev)9 lines, nail & seal impressions on Rev., publ.mentions 2 faint lines of Aramic on Obv., 7.6x8.7x2.7
1	subgenre_remarks	Murashu, lease of fields of other property by a slave; seal impressions on Rev.&LE., (Obv)16x(Rev)9 lines, 7.9x10(fr)x3.1
1	subgenre_remarks	Murashu, nail & seal impressions, (Obv)9x(Rev)7x(UE)1 lines, signatures on edges, 5.25x6.4x2.5
1	subgenre_remarks	Murashu, obligation for the repayment of dates in kind; seal impression on Rev., (Obv)8x(LoE)1x(Rev)7 lines, 5.65x7.2x2.35
1	subgenre_remarks	Murashu, officer's receipt for a year's tax on 7 estates; seal impressions oh Obv.& UE., (Obv)9x*(UE)1x(Rev)8 lines, 8.5x10.5x3.2, *this line is for insertion after KU3.BABBAR on following line on Obv. (see pl.42)
1	subgenre_remarks	Murashu, reassignment of debt & security to another individual; (Obv)10x(LoE)3x(Rev)10 lines, seal impression & nail impression on edges & Rev., 5.4x6.8x2.48
1	subgenre_remarks	Murashu, receipt for one year's taxes on 3 fields; seal impressions on edges &.Rev., (Obv)14x(LoE)2x(Rev)8x(UE)1 lines
1	subgenre_remarks	Murashu, seal impression & signature on LoE.&LE., (Obv)9x(Rev)10 lines, 5.8x6.75x2.75
1	subgenre_remarks	Murashu, seal impressions, (Obv)10x(Rev)10x(UE)1 lines, signatures on edges & top of Rev., 6.15x7.5x2.75
1	subgenre_remarks	Murashu, seal impressions, signatures on edges, (Obv)8x(Rev)7 lines
1	subgenre_remarks	Murashu, statement of taxes received by a slave for his Persian master; seal impression on Obv., (Obv)6x(Rev)8 lines, 5.8x7.9x2.75
1	subgenre_remarks	Murashu; (Obv)10x(LoE)1x(Rev)5x(UE)1 lines, nail & seal impressions on edges, 5.05x6.05x2.4
1	subgenre_remarks	Murashu; (Obv)10x(Rev)10 lines, seal impression on edges, Rev., 7.1x8.4x2.85
1	subgenre_remarks	Murashu; (Obv)10x(Rev)6 lines, 2 seal impressions on edges, Aramaic inscription on Rev.in ink, Mus.Photo 1184, 6.65x8.15x2.88
1	subgenre_remarks	Murashu; (Obv)10x(Rev)7 lines, seal & nail impressions on edges, 6.25x7.75x3.1
1	subgenre_remarks	Murashu; (Obv)10x(Rev)7 lines, seal impression on UE., 5.5x6.75x2.6
1	subgenre_remarks	Murashu; (Obv)10x(Rev)7 lines, seal impressions on UE.&LoE., 6.2x7.7x2.75
1	subgenre_remarks	Murashu; (Obv)10x(Rev)8 lines, seal impressions on all the surfaces, 6.5x7.8x3
1	subgenre_remarks	Murashu; (Obv)10x(Rev)9 lines, seal impressions on LoE.& Rev., 7x8.65x2.95
1	subgenre_remarks	Murashu; (Obv)10x(Rev)9 lines; Rev:nail marks, 1 label; UE:2 stamp seal imps., 2 labels; LE:1 stamp seal imp.
1	subgenre_remarks	Murashu; (Obv)11x(LoE)2x(Rev)10 lines, seal impressions on UE.&LE., 6.2x7.8x3.25
1	subgenre_remarks	Murashu; (Obv)11x(Rev)8 lines, nail & seal impresssions on LE., 5.7x7.45x2.4
1	subgenre_remarks	Murashu; (Obv)11x(Rev)8 lines, seal & nail impressions, 6.3x7.1x2.5
1	subgenre_remarks	Murashu; (Obv)11x(Rev)8 lines, seal impressions on edges, nail impression of Rev., 6.1x7.2x2.7
1	subgenre_remarks	Murashu; (Obv)12x(LoE)1x(Rev)7 lines, seal impressions on edges, 5.9x7.7x2.85
1	subgenre_remarks	Murashu; (Obv)12x(Rev)10 lines, seal impressions on edges, 6.2x7.5x2.85
1	subgenre_remarks	Murashu; (Obv)12x(Rev)11 lines, seal impressions on edges, 6.2x7.9x2.9
1	subgenre_remarks	Murashu; (Obv)12x(Rev)9 lines, nail & seal impressions on edges & Rev., 6.4x8.1x3
1	subgenre_remarks	Murashu; (Obv)12x(Rev)9 lines, nail impression on UE., seal impression on RE., 6.35x8.1x3.1
1	subgenre_remarks	Murashu; (Obv)12x(Rev)9 lines, seal impressions & signature on edges & Rev., 6.4x6.8x2.8
1	subgenre_remarks	Murashu; (Obv)12x(Rev)9 lines, seal impressions on edges & Rev.,6.35x8.4x2.98, *sic
1	subgenre_remarks	Murashu; (Obv)12x(Rev)9 lines, seal impressions on edges, 6.4x8.15x2.95
1	subgenre_remarks	Murashu; (Obv)12x(Rev)9 lines, seal impressions on edges, nail impression on Rev., 7.2x8.1x2.8
1	subgenre_remarks	Murashu; (Obv)13x(LoE)1x(Rev)9 lines, Aramaic inscripition on LoE., seal impression on edges, 6.5x8.05x3
1	subgenre_remarks	Murashu; (Obv)13x(Rev)8 lines, seal & nail impressions on edges, 6.75x8.4x3
1	subgenre_remarks	Murashu; (Obv)13x(Rev)9 lines, seal impressions on edges, 6.6x9.3x3.25
1	subgenre_remarks	Murashu; (Obv)13x(Rev)9 lines, seal impressions on edges, 8.5x7.2.8
1	subgenre_remarks	Murashu; (Obv)14x(LoE)1x(Rev)5 lines, seal impressions on LE.&LoE., 6.7x8.2x2.6
1	subgenre_remarks	Murashu; (Obv)15x(LoE)1x(Rev)11 lines, seal & nail impressions on edges, 8.6x6.9x3.1
1	subgenre_remarks	Murashu; (Obv)15x(Rev)11 lines, seal impressions on edges, nail impression on Rev., 6.55x7.95x3.2
1	subgenre_remarks	Murashu; (Obv)19x(LoE)1x(Rev)3 lines; 2 stamp seal imps & 2 labels on Rev.
1	subgenre_remarks	Murashu; (Obv)19x(Rev)15 lines, 2 lines of Aramaic on RE., seal impressions on edges, 8.85x10.25x2.95
1	subgenre_remarks	Murashu; (Obv)4x(LoE)3x(Rev)9 lines, seal impressions on Obv, UE.&LE
1	subgenre_remarks	Murashu; (Obv)7x(Rev)6 lines, labels on edges, seal impressions, 6.35x7.85x2.95
1	subgenre_remarks	Murashu; (Obv)8x(Rev)6 lines; a stamp seal imp.& a label on RE; * fully seen on TuM 2-3 145
1	subgenre_remarks	Murashu; (Obv)8x(Rev)7 lines, seal impressions on edges, cloth impression on UE., 8.2x6.5x3
1	subgenre_remarks	Murashu; (Obv)9x(LoE)1 lines; 1 seal imp, 1 label on UE.&LoE.
1	subgenre_remarks	Murashu; (Obv)9x(LoE)1x(Rev)8 lines, seal & nail impressions on edges, 5.35x6.7x2.25
1	subgenre_remarks	Murashu; (Obv)9x(LoE)1x(Rev)9x(UE)1 lines, Aramaic inscription incised on UE., nail & seal impressions on Rev., 5.2x6.25x2.3
1	subgenre_remarks	Murashu; (Obv)9x(Rev)7 lines, seal impressions on edges, 6.3x7.95x2.7
1	subgenre_remarks	Murashu; (Obv)9x(Rev)7x(UE)1 lines, seal impression & signature on LE., inked Aramaic endorsement on RE.
1	subgenre_remarks	Murashu; (Obv)9x(Rev)8 lines, seal impression on LE., black U-shaped mark said to be on Rev. now barely visible, 4.75x5.95x2
1	subgenre_remarks	Murashu; 1 stamp seal imp, 1 label; (Obv)9x(LoE)4x(Rev)8 lines
1	subgenre_remarks	Murashu; 2 seal impressions & 2 labels on UE.&LoE., (Obv)10x(Rev)9 lines, 4.95x6.3x2.4
1	subgenre_remarks	Murashu; 3 lines of Aramaic incised on LoE., contains name of the god Ninib, (Obv)8x(Rev)7x(UE)2 lines, seal impressions on LE.
1	subgenre_remarks	Murashu; A lease of sheep and goats, Aramaic endorsement incised on Rev., seal impression on Rev., (Obv)8x(LoE)1x(Rev)3 lines, 4.5x5.8x2.2, Mus.Photo 1188
1	subgenre_remarks	Murashu; Aram. docket on Rev.; (Obv)10x(Rev)8 lines; 1 seal & 1 label on LE.
1	subgenre_remarks	Murashu; Aramaic endorsement on Obv., (Obv)7x(Rev)7 lines, seal impressions on edges, 5.95x7.5x2.75
1	subgenre_remarks	Murashu; Aramaic inscription on RE.&LE., seal impressions on edges and Rev., (Obv)13x(Rev)11 lines, 6.05x7.24x2.7, Mu.Photos 1175,1177,a,1179-82, Clay Aram.Endors.mistakenly cites BE 9 60 instead of BE 10 60
1	subgenre_remarks	Murashu; Aramaic on Obv.&LoE., (Obv)7x(Rev)9 lines, seal impression on LE.
1	subgenre_remarks	Murashu; Aramaic traces on Rev., seal impressions on LoE.&UE., (Obv)10x(Rev)7 lines, 5.25x7.05x2.45
1	subgenre_remarks	Murashu; Faint inked Aramaic on UE., seal impressions & labels on LoE.& LE., (Obv)8x(Rev)8x(UE)1 lines, PBS 2/1 copy & p. 48 give year as 6.
1	subgenre_remarks	Murashu; Hilprecht, (Obv)12x(Rev)4x(UE)3x(LE)3 lines, seal impressions on the LE.& UE.
1	subgenre_remarks	Murashu; Hilprecht?, (Obv)13x(LoE)3x(Rev)8x(LE)3 lines, (UE)2 labels, seal impressions on (UE)2 & (LE)1, 3 nail marks on LoE.
1	subgenre_remarks	Murashu; Hilprecht?, (Obv)9x(Rev)6x(UE)2 lines, seal impressions on the UE.& LoE.
1	subgenre_remarks	Murashu; Inked Aramaic inscription on Obv., seal impressions on LoE.&RE., nail impression on UE., (Obv)6x(Rev)5 lines, 7.8x6.2x2.9
1	subgenre_remarks	Murashu; Inked Aramaic on Rev., seal impressions on LoE.& UE, labels on Obv.&LoE., nail impression on LE, (Obv)8x(Rev)6x(LE)1 lines, 5.7x6.8x2.7
1	subgenre_remarks	Murashu; LE:1 seal imp, 1 label; (Obv)7x(Rev)6x(UE)1 lines
1	subgenre_remarks	Murashu; LoE: 1 seal impr; (Obv)10x(Rev)7 lines
1	subgenre_remarks	Murashu; LoE:1 label; Rev:1 seal imp.& 1 label; UE: 1 seal imp.& 1 label; (Obv)8x(Rev)8 lines
1	subgenre_remarks	Murashu; LoE:1 seal imp.& 1 label; (Obv)7x(Rev)7x(UE)1 lines
1	subgenre_remarks	Murashu; LoE:1 seals, 1 label; LE:1 label; (Obv)9x(Rev)6 lines
1	subgenre_remarks	Murashu; LoE:1 stamp seal imp, 1 label; Rev:1 seal imp, 1 label; (Obv)5x(Rev)3 lines
1	subgenre_remarks	Murashu; LoE:2 stamp seal imp & 2 labels; Rev:1 stamp seal imp & 1 label; UE:2 stamp seal imps & 2 labels; LE:1 stamp seal imp & 1 cylinder seal imp & 2 labels; (Obv)11x(Rev)9 lines
1	subgenre_remarks	Murashu; LoE:2 stamp seal imps, 2 labels; Rev:1 nailmark, 1 label; (Obv)1x(Rev)7 lines
1	subgenre_remarks	Murashu; Mortgage; stamp seal imp.& nailmark on UE.; (Obv)4x(Rev)2 lines
1	subgenre_remarks	Murashu; Obv.damaged since publication, (Obv)12x(LoE)3x(Rev)8 lines, seal impressions on edges & Rev., 5.95x7.9x2.5, *day is possibly 21 (so old catalog), tablet is broken
1	subgenre_remarks	Murashu; Rev:1 nailmark, 1 label; UE:2 stamp seal imps., 2 labels; LE:1 label; (Obv)10x(Rev)6 lines
1	subgenre_remarks	Murashu; Rev:1 seal imp; LE:1 seal imp, 1 label; (Obv)10x(LoE)3x(Rev)6 lines
1	subgenre_remarks	Murashu; Rev:1 stamp seal imp & 1 label; UE:1 stamp seal imp & 1 label; LE:1 stamp seal imp & 1 label; (Obv)12x(Rev)9 lines
1	subgenre_remarks	Murashu; Rev:1 stamp seal imp.& 1 label; (Obv)8x(Rev)2 lines
1	subgenre_remarks	Murashu; Rev:1 stamp seal imp.& 1 label; (Obv)8x(Rev)4 lines
1	subgenre_remarks	Murashu; Rev:2 stamp seal imp, 1 label; LE:1 stamp seal imp, 1 label; (Obv)9x(LoE)1x(Rev)5 lines
1	subgenre_remarks	Murashu; Rev:3 cylinder seal imp, 1 stamp seal imp, 4 labels; LE:1 label; (Obv)14x(Rev)5 lines
1	subgenre_remarks	Murashu; Seal LE:1 seal imp.& 1 label; (Obv)10x(LoE)3x(Rev)8 lines
1	subgenre_remarks	Murashu; Seal impressions & signatures on UE.,LoE.&LE., (Obv)10x(Rev)7 lines, 6.05x7.9x2.75
1	subgenre_remarks	Murashu; Seal impressions on edges, & Rev., (Obv)9x(Rev)5 lines, *small pieces in the same box, one of them is inscribed.
1	subgenre_remarks	Murashu; Signatures on LE. & Rev., seal impression, (Obv)11x(LoE)3x(Rev)6 lines, 5.6x6.7x2.55, 4 lines of Aramaic.
1	subgenre_remarks	Murashu; Thumb-nail and seal impressions, seal impressions and labels on UE and LoE.; (Obv)12x(Rev)7x(UE)3x(LoE)3 lines.
1	subgenre_remarks	Murashu; Traces of 2 lines of Aramaic,  seal impressions, (Obv)11x(Rev)8 lines, signatures on edges, 6.35x7.8x2.8
1	subgenre_remarks	Murashu; UE: 1 stamp seal imp & 1 label; LE: 1 stamp seal imp, nailmarks, 1 label; (Obv)11x(Rev)2 lines
1	subgenre_remarks	Murashu; UE:1 label; RE:1 stamp seal imp.& 1 label; (Obv)11x(Rev)8 lines
1	subgenre_remarks	Murashu; UE:1 seal imp, 1 label; RE:1 seal imp, 1 label; (Obv)15x(Rev)14 lines
1	subgenre_remarks	Murashu; W/Aramaic dockets, seal impressions; (Obv)19x(LoE)6x(Rev)17x(UE)8x(LE)4x(RE)3 lines; *Driver Aramaic Documents, pp.46f.
1	subgenre_remarks	Murashu; W/fine seal impressions, 1 depicting 2 dogs; (Obv)12x(Rev)10x(UE)7 lines
1	subgenre_remarks	Murashu; W/seal depicting hunt of wild boar on horseback; (Obv)16x(LoE)10x(Rev)12x(UE)1x(LE)2 lines
1	subgenre_remarks	Murashu; W/seal impression & a label on LoE.; Aramaic on UE; (Obv)8x(Rev)9 lines
1	subgenre_remarks	Murashu; W/seal impression; 3 separate groups of fragments; (Obv)16x(Rev)11x(UE)1 lines
1	subgenre_remarks	Murashu; W/seal impressions; (Obv)10x(Rev)2 lines; UE: 2 seals, 1 label; LE: 1seals, 1 label
1	subgenre_remarks	Murashu; W/seal impressions; (Obv)15x(LoE)1x(Rev)13x(UE)5x(LE)5 lines
1	subgenre_remarks	Murashu; W/seal impressions; LoE:2 seals, 2 labels, UE:3 seals, 3 labels, LE:2 seals, 2 labels
1	subgenre_remarks	Murashu; W/seal impressions; thumbnail marks
1	subgenre_remarks	Murashu; W/several fine seal impressions; (Obv)18x(LoE)5x(Rev)19x(UE)4x(LE)6 lines
1	subgenre_remarks	Murashu; inked Aramaic docket on Rev., seal impression on LoE., (Obv)9x(Rev)7xlines, 1-line insertion on UE., 6.2x8.5x2.4
1	subgenre_remarks	Murashu; lease of lands for 3 years, 3 lines of Aramaic docket incised on Rev., seal impressions, (Obv)12x(Rev)6 lines, 8x10.3x3.6
1	subgenre_remarks	Murashu; nail impression on Rev., seal impressions on edges, one line of Aramaic on Rev.in ink, (Obv)8x(Rev)7 lines, 5.95x8.05x2.8
1	subgenre_remarks	Murashu; nail impression on UE., seal impressions on LoE.,Rev.& LE., (Obv)12x(Rev)8 lines, 6.15x8.15x3.15
1	subgenre_remarks	Murashu; one year's lease of sheep, Aramaic inscription on Rev.in ink; nail impression on RE., seal impressions on LoE.,Rev.,UE.&LE., (Obv)15x(Rev)11 lines, Mus.Photos 1171, 1173-75.
1	subgenre_remarks	Murashu; possibly Aramaic endorsement of upper part of Rev., (Obv)9x(Rev)6 lines, nail & seal impressionss on edges, 5.3x6.6x2.45
1	subgenre_remarks	Murashu; receipt; LoE: 1 stamp seal imp.& 2 labels; (Obv)4x(Rev)4 lines
1	subgenre_remarks	Murashu; receipt; w/seal impressions, 2 fine; w/thumbnail mark; (Obv)8x(LoE)3x(Rev)6x(LE)2 lines
1	subgenre_remarks	Murashu; seal impression on LE., (Obv)11x(LoE)3x(Rev)10x(UE)2 lines, 6.5x7.9x2.9
1	subgenre_remarks	Murashu; seal impression on LE., (Obv)11x(Rev)8 lines, 6x7.1x2.7
1	subgenre_remarks	Murashu; seal impression on LE., (Obv)13x(Rev)10 lines, 5.7x7.15x2.6
1	subgenre_remarks	Murashu; seal impression on LE., (Obv)7x(Rev)6 lines, 5.14x6.8x2.6
1	subgenre_remarks	Murashu; seal impression on LE., (Obv)8x(Rev)6 lines, 5.2x7.3x2.2
1	subgenre_remarks	Murashu; seal impression on LE., nail impression on LoE., (Obv)8x(Rev)7x(UE)1 lines, 5.2x6.5x2.3
1	subgenre_remarks	Murashu; seal impression on LE., nail impression on LoE., (Obv)9x(Rev)9 lines, 6.55x7.6x3
1	subgenre_remarks	Murashu; seal impression on LoE., (Obv)10x(LoE)1x(Rev)8x(UE)1 lines, 6.3x7.9x2.7
1	subgenre_remarks	Murashu; seal impression on LoE., (Obv)10x(LoE)1x(Rev)9lines, 6x7x2.85
1	subgenre_remarks	Murashu; seal impression on LoE., (Obv)10x(Rev)7 lines, 5.4x6.7x2.35
1	subgenre_remarks	Murashu; seal impression on LoE., (Obv)13x(LoE)1x(Rev)8x(UE)1 lines, 6.58x8.3x2.6
1	subgenre_remarks	Murashu; seal impression on LoE., (Obv)9x(Rev)8 lines, incised Aramaic docket: 2 lines on UE., 1 line of LE., 6x7.6x2.9
1	subgenre_remarks	Murashu; seal impression on Obv., (Obv)8x(Rev)10 lines, 5.6x6.65x2
1	subgenre_remarks	Murashu; seal impression on RE., (Obv)5x(Rev)5 lines, 5.9x7.3x2.5
1	subgenre_remarks	Murashu; seal impression on RE., (Obv)5x(Rev)8 lines, 6.45x8.3x2.8
1	subgenre_remarks	Murashu; seal impression on RE., (Obv)9x(Rev)1x(UE)1 lines, 6.15x7.5x3.3
1	subgenre_remarks	Murashu; seal impression on Rev., (Obv)12x(Rev)8 lines, 7.2x8.6x2.8
1	subgenre_remarks	Murashu; seal impression on Rev., (Obv)14x(Rev)8 lines, 6.8x8.7x3.1
1	subgenre_remarks	Murashu; seal impression on Rev., (Obv)17x(Rev)12 lines, 7.1x8.5x2.8
1	subgenre_remarks	Murashu; seal impression on Rev., (Obv)19x(Rev)10 lines, 8.2x11.2x3.3
1	subgenre_remarks	Murashu; seal impression on Rev., (Obv)7x(Rev)8 lines, 5.4x6.3x2.1
1	subgenre_remarks	Murashu; seal impression on Rev., largely effaced, (Obv)13x(Rev)8 lines, 7.1x9x2.9
1	subgenre_remarks	Murashu; seal impression on Rev., nail impression & label on LE., (Obv)11x(Rev)6 lines, 6.5x8.5x2.6
1	subgenre_remarks	Murashu; seal impression on Rev., nail impression on LE., (Obv)12x(LoE)1x(Rev)7 lines
1	subgenre_remarks	Murashu; seal impression on Rev., nail impression on LE., (Obv)13x(Rev)5 lines, 6.3x8x2.6
1	subgenre_remarks	Murashu; seal impression on Rev., nail impression on LE., (Obv)13x(Rev)6 lines, 6.2x7.9x2.3
1	subgenre_remarks	Murashu; seal impression on UE., (Obv)10x(Rev)8 lines, 6.2x7.3x2.5
1	subgenre_remarks	Murashu; seal impression on UE., (Obv)6x(Rev)9 lines, 6.3x8x3
1	subgenre_remarks	Murashu; seal impression on UE., Aramaic incised on Rev.& LE., (Obv)13x(LoE)2x(Rev)9 lines, 6.3x7.5x2.6
1	subgenre_remarks	Murashu; seal impression on UE., nail impression on LoE., (Obv)8x(Rev)7 lines, 5.2x6.3x2.5
1	subgenre_remarks	Murashu; seal impressions and labels on LoE.&Rev., (Obv)10x(Rev)8x(LE)2, 5.8x7.15x2.5
1	subgenre_remarks	Murashu; seal impressions and labels on all edges, (Obv)14x(LoE)1x(Rev)8x(UE)1 lines, 6.8x8.6x3.25
1	subgenre_remarks	Murashu; seal impressions intended; LE:1 label; UE:2 labels; (Obv)10x(Rev)10x(UE)1 lines
1	subgenre_remarks	Murashu; seal impressions on LE.& UE., nail impression on LoE., (Obv)12x(Rev)11 lines, 6x8.36x2.6
1	subgenre_remarks	Murashu; seal impressions on LoE.& LE., nail impression on UE., (Obv)12x(Rev)9 lines, 5.85x7.38x2.7
1	subgenre_remarks	Murashu; seal impressions on LoE.,Rev.&LE., (Obv)14x(Rev)6 lines, 6.92x8.68x2.9
1	subgenre_remarks	Murashu; seal impressions on LoE.,Rev.&RE., (Obv)14x(LoE)2x(Rev)8x(UE)1 lines, 7.1(fr.)x6.4x2.5
1	subgenre_remarks	Murashu; seal impressions on LoE.,Rev.,UE.&LE., (Obv)13x(Rev)6 lines, 6.2x8.43x2.9
1	subgenre_remarks	Murashu; seal impressions on LoE.,Rev.,UE.&LE., (Obv)9x(Rev)8 lines, 7x8.5x2.8
1	subgenre_remarks	Murashu; seal impressions on LoE.,UE.&LE., (Obv)13x(LoE)1x(Rev)9 lines, publ.gives wrong date.
1	subgenre_remarks	Murashu; seal impressions on LoE.,UE.&LE., (Obv)14x(LoE)1x(Rev)14 lines, 6.63x7.63x3.3
1	subgenre_remarks	Murashu; seal impressions on Obv.,Rev.&LE., (Obv)9x(Rev)9 lines, 7.8x8.8x3.1
1	subgenre_remarks	Murashu; seal impressions on Rev.& LE., nail impression on UE., (Obv)20x(LoE)4x(Rev)11 lines, 7.8x9.6x3.35
1	subgenre_remarks	Murashu; seal impressions on Rev.& edges, (Obv)11x(LoE)2x(Rev)8 lines, 6.4x7.75x2.8
1	subgenre_remarks	Murashu; seal impressions on Rev.& edges., (Obv)14x(Rev)9 lines, 7.35x8.8x3.15
1	subgenre_remarks	Murashu; seal impressions on Rev.&UE., label on LE., (Obv)9x(LoE)3x(Rev)6 lines, 4.9x3.8x2.2
1	subgenre_remarks	Murashu; seal impressions on Rev.&UE., nail impression on LE., (Obv)10x(Rev)7 lines, 5.1x6.2x2.45
1	subgenre_remarks	Murashu; seal impressions on Rev., doodles" on the bottom of Obv.& top of Rev. (Obv)11x(Rev)6 lines, 6.95x8.6x2.5"
1	subgenre_remarks	Murashu; seal impressions on Rev.,LoE.&LE., garment impression on Rev., nail impression on UE., (Obv)12x(LoE)1x(Rev)8 lines, 6x7.9x2.7
1	subgenre_remarks	Murashu; seal impressions on Rev.,UE.&RE., (Obv)20x(Rev)19 lines, 11.3x10.5x3.55
1	subgenre_remarks	Murashu; seal impressions on UE.& LE., (Obv)10x(Rev)6 lines, 6.4x7.7x2.5
1	subgenre_remarks	Murashu; seal impressions on UE.& LE., (Obv)14x(Rev)6 lines, publ.(p.45) gives wrong date.
1	subgenre_remarks	Murashu; seal impressions on UE.& LE., nail impression on LoE., (Obv)10x(Rev)10 lines, 6.3x7.8x2.9
1	subgenre_remarks	Murashu; seal impressions on UE.& RE., nail impression on LE., Aramaic inscription on Rev., (Obv)12x(LoE)4x(Rev)9 lines, 5.95x7.6x3.05
1	subgenre_remarks	Murashu; seal impressions on UE.&LE., (Obv)10x(Rev)11 lines, 5.8x7.1x2.35
1	subgenre_remarks	Murashu; seal impressions on UE.&LE., (Obv)10x(Rev)6 lines
1	subgenre_remarks	Murashu; seal impressions on UE.&LE., (Obv)10x(Rev)8 lines, 6.45x7.95x2.9
1	subgenre_remarks	Murashu; seal impressions on UE.&LE., (Obv)11x(LoE)1x(Rev)4 lines, 5.35x6.65x2.7
1	subgenre_remarks	Murashu; seal impressions on UE.&LE., (Obv)11x(LoE)2x(Rev)5 lines, 6.2x7.2x2.6
1	subgenre_remarks	Murashu; seal impressions on UE.,LE.&RE., (Obv)8x(LoE)2x(Rev)9 lines, 6.1x5.1x2.4
1	subgenre_remarks	Murashu; seal impressions on all edges and Rev., (Obv)12x(Rev)7 lines, 7.1x8.9x3.45
1	subgenre_remarks	Murashu; seal impressions on edges & Obv., inked Aramaic on Rev., (Obv)11x(Rev)7 lines, 6.7x8.15x3
1	subgenre_remarks	Murashu; seal impressions on edges & Rev., (Obv)10x(Rev)6 lines, 6.2x7.7x3
1	subgenre_remarks	Murashu; seal impressions on edges & Rev., (Obv)11x(LoE)2x(Rev)10 lines, 6.1x7.6x2.7
1	subgenre_remarks	Murashu; seal impressions on edges & Rev., inked Aramaic on Rev., (Obv)13x(LoE)2x(Rev)8 lines, 6.2x7.9x3.1
1	subgenre_remarks	Murashu; seal impressions on edges, (Obv)11x(Rev)7 lines, 6x7.83x2.8
1	subgenre_remarks	Murashu; seal impressions on edges, (Obv)11x(Rev)8 lines, 6.3x8.05x2.6
1	subgenre_remarks	Murashu; seal impressions on edges, (Obv)17x(Rev)16, 7.25x9.3x3
1	subgenre_remarks	Murashu; seal impressions on edges, (Obv)8x(Rev)8 lines, 5.3x6.45x2.5
1	subgenre_remarks	Murashu; seal impressions on edges, (Obv)8x(Rev)8 lines, 6.45x7.95x3
1	subgenre_remarks	Murashu; seal impressions on edges, (Obv)8x(Rev)9 lines, day publ. as 18, 6.2x8.2x2.8
1	subgenre_remarks	Murashu; seal impressions on edges, nail impression & inked Aramaic on Rev., (Obv)10x(Rev)8 lines, 7.3x5.8x2.55
1	subgenre_remarks	Murashu; seal impressions on edges, nail impression on Rev., (Obv)10x(Rev)7 lines, 6.25x8x2.6
1	subgenre_remarks	Murashu; seal impressions on edges, nail impression on Rev., (Obv)13x(Rev)10 lines, 5.7x7.7x2.6
1	subgenre_remarks	Murashu; seal impressions on edges, nail impression on UE., (Obv)12x(Rev)9 lines, 6.25x7.4x2.7
1	subgenre_remarks	Murashu; seal impressions on edges, traces of Aramaic on Rev., (Obv)9x(Rev)8 lines, 5.45x6.4x2.4
1	subgenre_remarks	Murashu; traces of Aramaic inscription on UE.&Rev., seal impressions on LoE.&RE., (Obv)10x(LoE)2x(Rev)10 lines, 6.05x7.95x3.1
1	subgenre_remarks	Murashu; traces of Aramic inscription on LoE.(publication erroneauly says LE.), (Obv)10x(Rev)9 lines, seal impression on LE, nail impression on UE., 6.15x7.3x2.4
1	subgenre_remarks	Murashu; traces of inked Aramaic inscription on Rev., (Obv)12x(LoE)1x(Rev)10 lines, seal impressions on edges, nail impression on Rev., 6.3x7.98x2.8
1	subgenre_remarks	Murashu; w/beautiful seal(sheep); (Obv)12x(LoE)5x(Rev)10x(UE)5 lines
1	subgenre_remarks	Murashu; w/fine seal impressions on Obv& LoE; (Obv)9x(Rev)9x(UE)2 lines; Obv:1 seal, 1 label; LoE:2 seals, 2 labels; Rev:1 seal, 1 label; LE:1 seal, 1 label
1	subgenre_remarks	Murashu; w/fine seal impressions, cf.12953; 3 stamp seal imps & 3 labels on UE; (Obv)11x(Rev)2 lines
1	subgenre_remarks	Murashu; w/fine seal impressions, male head w/pointed cap and 4 large horses pasturing; (Obv)15x(LoE)6x(Rev)14x(UE)6x(RE)2 lines
1	subgenre_remarks	Murashu; w/fine seal impressions, one w/female head; (Obv)17x(LoE)4x(Rev)12x(UE)1x(LE)8 lines
1	subgenre_remarks	Murashu; w/fine seal impressions; (Obv)10x(LoE)4x(Rev)14x(UE)6x(LE)6x(RE)3 lines
1	subgenre_remarks	Murashu; w/fine seal impressions; (Obv)20x(LoE)7x(Rev)14x(UE)6x(LE)7 lines
1	subgenre_remarks	Murashu; w/fine seal impressions; (Obv)5x(Rev)2 lines; Rev:1 stamp seal imp, 1 label; UE:2 stamp seal imps, 2 labels; RE: 1 seal imp.
1	subgenre_remarks	Murashu; w/fine seal impressions; (Obv)8x(LoE)3x(UE)6x(LE)3 lines
1	subgenre_remarks	Murashu; w/peculiar seal impressions; 2 stamp seal imps & 2 labels on Rev; (Obv)18x(Rev)6 lines
1	subgenre_remarks	Murashu; w/seal & thumbnail impressions; (Obv)10x(Rev)9x(LE)1x(RE)2 lines
1	subgenre_remarks	Murashu; w/seal and thumbnail impressions; (Obv)11x(LoE)1x(Rev)4x(UE)6x(LE)5 lines
1	subgenre_remarks	Murashu; w/seal impression on RE; (Obv)8x(Rev)9x(LE)1 lines
1	subgenre_remarks	Murashu; w/seal impression; (Obv)12x(LoE)3x(Rev)9x(UE)2x(LE)2 lines
1	subgenre_remarks	Murashu; w/seal impression; (Obv)12x(LoE)7x(Rev)9x(LE)7 lines
1	subgenre_remarks	Murashu; w/seal impressions & thumbnail impressions; (Obv)11x(LoE)1x(Rev)7 lines; UE:2 stamp seal imps, 2 labels; LE:1 stamp seal imp, 1 label
1	subgenre_remarks	Murashu; w/seal impressions & thumbnail mark; (Obv)9x(Rev)8 lines; LoE:1 thumbnail mark, 1 label; Rev:1 seal, 1 label; LE:1 seal, 1 label
1	subgenre_remarks	Murashu; w/seal impressions & thumbnail marks; (Obv)8x(Rev)10 lines; LoE:1 seal, 1 label; LE:3 nail marks, 1 label; RE:2 seals, 2 labels
1	subgenre_remarks	Murashu; w/seal impressions & thumbnail marks; (Obv)9x(Rev)6 lines; Rev:1 seal, 1 label; LoE:2 nail marks, 1 label; LE:1 seal, 1 label
1	subgenre_remarks	Murashu; w/seal impressions, fragment of hunting scene on 1 of seal impressions; (Obv)9x(Rev)6 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)11x(LoE)1x(Rev)6 lines; UE, LE:1 stamp seal, 1 cylinder seal imp. & 2 labels (cylinder seals stamped like stamp seals)
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)11x(LoE)1x(Rev)7 lines; LoE:2 seals, 2 labels; UE:1 seal, 1 label; LE:1 seal, 1 label
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)11x(LoE)4x(Rev)8x(UE)3x(LE)3 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)11x(Rev)7x(LE)3 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)12x(LoE)1x(Rev)9x(UE)1 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)12x(LoE)7x(Rev)6x(UE)4x(LE)3 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)13x(LoE)2x(Rev)10x(UE)4x(LE)4x(RE)3 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)13x(LoE)3x(Rev)15x(UE)3x(LE)6x(RE)1 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)13x(LoE)4x(Rev)12 lines; UE:2 seals, 2 labels; LE:1 seal, 1 label; RE:3 seals, 3 labels
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)13x(LoE)6x(Rev)14x(UE)6x(LE)3 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)13x(Rev)12 lines; LoE:1 stamp seal imp., 2 labels; Rev:1 cylinder seal imp., 1 label; UE:2 stamp seal imps, 1 cylinder seal imp, 3 labels; RE:1 cylinder seal imp, 1 label
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)13x(Rev)5 lines; LoE:2 seals, 2 labels; UE:2 seals, 2 labels; LE:2 seals, 2 labels; RE:1 label
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)14x(LoE)3x(Rev)10x(UE)5x(LE)3x(RE)3 lines; *broken off
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)14x(LoE)3x(Rev)9x(UE)2 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)14x(LoE)4x(Rev)9x(UE)4x(LE)4x(RE)6 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)19x(LoE)3x(Rev)17x(UE)10x(LE)3x(UE)2 lines
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)8x(Rev)7 lines; LoE: 2 stamp seal imps, 2 labels; Rev:2 nail marks, 1 label; LE:1 cylinder seal imp(stamped), 1 label
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)8x(Rev)8x(UE)1 lines; 1 stamp seal imp.& 1 label on LoE.&LE
1	subgenre_remarks	Murashu; w/seal impressions; (Obv)9x(Rev)5x(UE)3x(RE)2 lines
1	subgenre_remarks	Murashu; w/seal impressions; *surfaces abraded
1	subgenre_remarks	Murashu; w/seal impressions; 3 stamp seal imps.&3 labels on Obv.; (Obv)5x(LoE)3x(Rev)8x(UE)1 lines
1	subgenre_remarks	Murashu; w/seal impressions; Aramaic 2 lines; (Obv)7x(Rev)5 lines; LoE:2 seal imprs, 2 labels; UE:3 seal imprs, 3 labels; LE:1 seal impr, 1 label; RE:1 seal impr, 1 label
1	subgenre_remarks	Murashu; w/seal impressions; Joined to a tablet"; (Obv)13x(LoE)1x(Rev)7x(LE)3 lines"
1	subgenre_remarks	Names and assignments; Seal impressions (Kassite with Ur3); (Obv)16x(Rev)5 lines
1	subgenre_remarks	Names of witnesses; w/thumbnail and seal impression; (Rev)4 lines; UE:1 stamp seal imp, 1 label; Rev:1 nailmark, 1 label
1	subgenre_remarks	Note about two men: åeå Lugal-dun-nir-re dumu Da-da dub-sar lugal; itu ezem- mah du?-dam; case unopened; sealed; kiåib Lugal-du24-ùr-re (CBT 2)
1	subgenre_remarks	Notice: 30 sìla åe lugal kiåib sanga; seal: Ur-∂Ba-ba6 dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Oath concerning the sealing of a tablet.
1	subgenre_remarks	Obligation to deliver dates, yeild of the garden"; tablet = 384A; seal; 5X2X6 UE 2 LE 3"
1	subgenre_remarks	Oblong, bearing a small but perfect seal.  Unusual scene on seal.  Sun god in the background
1	subgenre_remarks	Obv broken; seal: Lú-bala-sha6 d. Ha-ti-lí gudu4 dNanshe
1	subgenre_remarks	Obv seal imprs; rev trace of a string?
1	subgenre_remarks	Obv. 20 lines; *according to the old catalog, CBS14473 is cylinder seal made of shell!
1	subgenre_remarks	Obv. 3 lines, Rev. 1 line.  Seal impressions on Obv., Rev. & RE.
1	subgenre_remarks	Obv. broken; seal: Lú-dNám-mah ds d. Da-da
1	subgenre_remarks	Obv. lost.  Fine seal impressions. 4 lines
1	subgenre_remarks	Obv.1 line, Rev.3 lines. Seal impression.
1	subgenre_remarks	Obv.1 seal impression only.
1	subgenre_remarks	Obv.2 lines, Rev.3 lines, UE.1 line, a seal impression.
1	subgenre_remarks	Obv.2 lines, UE.1 line.  Seal impression on UE.
1	subgenre_remarks	Obv.2 lines, UE.2 lines. A seal impression on Obv.
1	subgenre_remarks	Obv.3 lines, Rev.2 lines, UE.2 lines & a seal impression, LE.a seal impression & a label.
1	subgenre_remarks	Obv.3 lines, Rev.2 lines, UE.label & a seal impression.
1	subgenre_remarks	Obv.3 lines, Rev.2 lines.  Fragmental seal impression on Lo.E.
1	subgenre_remarks	Obv.3, Rev.1 lines, Kassite seal impressions on Rev. & RE.
1	subgenre_remarks	Obv.4 lines, LoE.a label & a seal impresion, Rev.4 lines.
1	subgenre_remarks	Obv.4 lines, Rev.4 lines.  Seal impressions on all the sides and the edges.
1	subgenre_remarks	Obv.4 lines, Rev.5 lines, a seal impression.
1	subgenre_remarks	Obv.4 lines, Rev.5 lines.  Stamp seal impression.
1	subgenre_remarks	Obv.5 lines, LoE. 2 labels & a seal impression, Rev.3 lines, LE.a seal impression & a label.
1	subgenre_remarks	Obv.5 lines, LoE.1 line & a seal impression, Rev.1 line, LE.2 lines (label?), a seal impression.
1	subgenre_remarks	Obv.5 lines, Rev.3 lines, UE.2 lines (labels?) & 1 Seal impression.
1	subgenre_remarks	Obv.5 lines, Rev.3 lines. A seal impression on LE.
1	subgenre_remarks	Obv.7 lines, Rev.5 lines, UE.1 line, LE.a seal impression & label (3 lines.)
1	subgenre_remarks	Obv.7, Rev.8 lines. A Kassite seal impression on the LE.
1	subgenre_remarks	Obv.9 lines, Rev.6 lines. Stamp seal impression on LE.
1	subgenre_remarks	Obv.mutilated, illegible, Rev.6 lines. Seal impression and label on LoE.
1	subgenre_remarks	Obv:2 lines. Seal impressions on Obv. & UE.
1	subgenre_remarks	Official's payment; 4x2x4(rev) lines; seal impressions
1	subgenre_remarks	Official's salary; Tablet:(Obv)5x(LoE)1x(Rev)3 lines, Case:(Obv)5x(Rev)4 lines, effaced nail marks on LE., seal impressions on all over the surface, effaced
1	subgenre_remarks	Official's salary; a half-destroyed seal impression on LE; (Obv)4x(LoE)2x(Rev)5x(UE)1 lines
1	subgenre_remarks	Official's salary; case rev. center wanting; seal impr on all sides; tabl 4x3x4 lines; case 5x3x3 lines
1	subgenre_remarks	Official's salary; case tablet; seal impressions on all sides of case; tablet 4x2 lines; case 5x4 lines
1	subgenre_remarks	Official's salary; case:seal impressions on all sides; Tablet:(Obv)4x(LoE)1x(Rev)4x(UE)1 lines, Case:(Obv)5x(Rev)5x(UE)1 lines
1	subgenre_remarks	Official's salary; case:seal impressions on all sides; Tablet:(Obv)4x(LoE)2x(Rev)3 lines, Case:(Obv)5x(LoE)2x(Rev)2 lines
1	subgenre_remarks	Official's salary; case:seal impressions on all sides; Tablet:(Obv)4x(Rev)4 lines, Case:(Obv)4x(Rev)4 lines
1	subgenre_remarks	Official's salary; case:seal impressions on all sides; Tablet:(Obv)5x(LoE)2x(Rev)5 lines, Case:(Obv)5x(LoE)4x(Rev)3 lines
1	subgenre_remarks	Official's salary; seal impressions all over the surfaces;* it would damage impressions; (Obv)5x(LoE)1x(Rev)3 lines
1	subgenre_remarks	Oil (gish-ì) á-gish-gar-ra ì-sur-me) from Lu-Ningirsu to Ur-abba; seal: Ur-ab-ba ds d. Ba-zi.
1	subgenre_remarks	Oil (ì-gish) for Apilisha and Irra-mudane; seal: Ir3-ra-mu-da-ne rá-gaba ir11-[].
1	subgenre_remarks	Oil (ì-gish) for Ur-Ningiszida; seal Ur-dNin-gis-zi-da ds d. Ba-zi
1	subgenre_remarks	Oil (ì-gish) from Ir11-dam to Lugal-sha6-sha6; seal: Nì-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Oil (ì-gish) from Nin-a-zu to Ur-ab-ba mu síg-ùz-shè; seal: Ur-ab-ba [?].
1	subgenre_remarks	Oil (ì-gish) from Ur-abba to Ur-ushgidda; seal: Ur-dIg-alim d. Gu-za-ni.
1	subgenre_remarks	Oil (ì-gish) from Ur-ki-ne for Ur-Ningiszida; seal: Ur-dNin-gis-zi-da ds d. Ba-zi.
1	subgenre_remarks	Oil (ì-gish) from Urabba to Lu-Narua; seal: Lú-dNa-rú-a ds d. Ur-dIshkur.
1	subgenre_remarks	Oil for gurush Má-ad-ga-ash, from Ur-ab-ba to Ur-gishgigir; seal Ur-gishgigir d. Ma-an-sum
1	subgenre_remarks	Oil for the amar-ku5; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Oil for the boat of Amar-Sin from Ur-Abba to Ur-Baba; seal illegible (CBT 2)
1	subgenre_remarks	Oil from Lugal-igi-hush; shà-gal gishtukul-e dab5-ba-ke4-ne; seal: Ur-dBa-ba6 d. Ma-an-sum gu-za-lá
1	subgenre_remarks	Oil from Ur-ab-ba to Lu2-{d}nin-szubur; purpose nig2 u4-tusz-a he2-dab5-sze3; plus frag of case with seal of Lu2-{d}nin-szubur ds d Lu2-{d}Ba-ba6
1	subgenre_remarks	Oil from Ur-ab-ba to Lú-dNarua; seal: Lú-dNa-rú-a ds d. Ur-sha6-ga
1	subgenre_remarks	Oil from Ur-ab-ba to Ur-gar; rev. broken; seal
1	subgenre_remarks	Oil from Ur-abba to Ur-Nin-MAR.KI; case unopened; seal: Ur-∂Nin-MAR.KI dubsar dumu Lugal-åa6-ga dubsar; months i-xii (CBT 2)
1	subgenre_remarks	Oil received by Lú-∂Nin-åubur from Ur-ab-ba, controller Lú-∂Ig-alim; seal: Lú-∂Nin-åubur dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Oil received by Lú-∂Nin-åubur from Ur-ab-ba; seal: Lú-∂Nin-åubur dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Oil received by Íeå-kal-la from Ur-uå-gíd-da, gìr Ba-zi; seal: Íeå-kal-la dubsar dumu Ur-ab?-[ba] (CBT 2)
1	subgenre_remarks	Oil which Íeå-kal-la received from Ur-ki-gu-la; seal: Íeå-kal-la dubsar dumu Ur-ab-ba (CBT 2)
1	subgenre_remarks	Oil, she gish-ì, from Ur-ab-ba to Gu-za-ni; seal illegible
1	subgenre_remarks	Oil, ì from Ir11-mu to Du-ti-rí; iti ezem-me-ki-gál; seal dedicated to Shulgi; seal illegible
1	subgenre_remarks	Oil, ì-gish for Lú-dNin-gír-su; seal: Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	Oil, ì-gish from SHesh-kal-la to Ur-dBa-ba6 gu-za-lá su-su-dam; seal: Ur-dBa-ba6 d. Lú-dNin-gír-su
1	subgenre_remarks	Oil, ì-gish from Ur-ab-ba to Ur-Ninmarki; seal: Ur-dNin-mar-ki ds d. Lugal-ushumgal
1	subgenre_remarks	Oil, ì-gish from Ur-ab-ba to Ur-gír-gal; seal dedicated to SHulgi, dNanna-zi-da zabar-dab5 ì-kash?-a-[] sagi mah ugula mash-shu-gíd-gíd-ke4-ne ir11-zu
1	subgenre_remarks	Oil, ì-gish from Ur-ab-ba; seal: Ur-dDumu-zi ds d. Ka5-a má-lah4-gal
1	subgenre_remarks	Oil, ì-gish from Ur-abba for the érin gi-gibil; seal illegible
1	subgenre_remarks	Oil, ì-gish ki SHeshkalla kishib Nì-ú-rum ì-ba géme ush-bar; seal: Nì-ú-rum ds d.[]
1	subgenre_remarks	Oil, ì-gish ki Ur-ab-ba-ta lú Hu-burx ba-ab-shésh kishib Ur-dBa-<ba6>; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Oil, ì-gish ki Ur-ab-ba-ta ì-su-e-ak; seal: Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	Oil, ì-gish ì-ba hé-dab5 ki Ur-ab-ba-ta kishib Lugal-im-ru-a gìr Lú-dEN.ZU; seal: Lugal-im-ru-a ds d. Gi-mu
1	subgenre_remarks	Oil, ì-gish ì-túg-ge ak from Ur-ab-ba; seal: Ur-dNin-mar.ki-ka ds d. Lugal-sha6-ga ds
1	subgenre_remarks	Oil, ì-gish, from Ur-abba to Ur-Lama; seal: Ur-dLama ds d. Ur-gar
1	subgenre_remarks	Oil, ì-gish; case eroded; seal: Lú-d[] ds d. Lugal-iti-da
1	subgenre_remarks	Oil, ì-giå ì-túg-ge ak-dè, from Ur-abba to Guzani (CBT 2). A: Case of 19317; sealed (CBT 2)
1	subgenre_remarks	Oil, ì-nun, ì-gish received by Lú-dNin-gír-su; seal: Lú-dNin-gír-su ds d. Ir11-mu
1	subgenre_remarks	Old barley from Bazi for Kituslu in the mill; case unopened; seal: Mar-tu (written right to left) sagi (CBT 2)
1	subgenre_remarks	On barley; mostly illegible (CBT 2). A: Case of 21888; seal illegible (CBT 2)
1	subgenre_remarks	One brickmould from Lu-Ningirsu to Lugalnammah; seal: Lugal-nám-mah dubsar dumu Da-da (CBT 2)
1	subgenre_remarks	One carcass of a sheep, 40 sila of bread (igi-3-gál-bi íb-ta-tur) Íulgi-kuzu received from Urbagar; seal: ∂Íul-gi-kù-zu dubsar dumu ∂Íára-kam dubsar (CBT 2)
1	subgenre_remarks	One fat-tailed sheep åu-gíd sá-du11 lugal from Ur-Baba to Ur-Lagaå; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	One gi lugal Ur-dNanshe su-su-dam; seal illegible
1	subgenre_remarks	One gur of barley, she-ur5-ra dEn-líl-lá-shè, from Ur-Enlilla to Lu-Babba nu-bànda Gù-dé-a; seal: Lú-dBa-ba6 d. Ur-gishgigir
1	subgenre_remarks	One gur of fish (ku6 sheg6) from Ur-Ninmug to Lú-dNin-gír-su; gìr Lú-dNanna; seal: Lú-dNin-gír-su ds d. Ir11-mu
1	subgenre_remarks	One géme arua shir-di / na-ash-di é bur-sag dNin-mar-ki-ka; seal: Ur-dLama d. Lugal-sud4-dè lú-[] dNin-mar-ki-ka
1	subgenre_remarks	One ox and 2 arua transfered from An-ne-ba-du7 to Lú-dNin-gír-su; seal: Lú-dNin-gír-su d. Nam-ha-ni
1	subgenre_remarks	One ox in surplus transferred from Dingir-åa6-ga to Lú-Lagaå˚ (CBT 2). A: Case of 18780; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe nu-bànda kuruåda (CBT 2)
1	subgenre_remarks	One reed-mat from Lú-dNin-gír-su to Ur-Baba; seal: Ur-dBa-ba6 ds d. Ur-sha6-[ga]
1	subgenre_remarks	One sheep from Ba-a to Lugal-inim-gi-na; seal: Lugal-da-ga ugula d. Lú-dNa-rú-a lú-túg
1	subgenre_remarks	One year old ox, arua Anne-badu, received by Irdam; seal: Ir11-dam ùnu []
1	subgenre_remarks	Only date legible; seal?; 3x1x2 lines
1	subgenre_remarks	Only part of date preserved, w/seal impressions; 2 lines
1	subgenre_remarks	Ox from Ur-Enki for Abbakalla; seal: Ur-∂En-ki dumu Ur-Ma-ma dam-gàr (CBT 2)
1	subgenre_remarks	Ox taken in charge; seals; 5x7 lines
1	subgenre_remarks	Oxen and donkeys available to the ploughman of Ningiszida; seal illegible (CBT 2)
1	subgenre_remarks	Oxen and donkeys bought for money; seal: Ur-dNanshe ds d. dNanshe-ì-zu
1	subgenre_remarks	Oxen and donkeys returned, received by Aabba in the temple of Ningirsu (CBT 2). A: Case of 18770; seal: A-ab-ba dumu Ni9-gar (CBT 2)
1	subgenre_remarks	Oxen and sheep shu-gi4 Nibruki-shè; seal: Na-ba-sha6 ds d. Hé-na-ti
1	subgenre_remarks	Oxen for plowing from the sanga of Nanshe, kishib Ur-Ma-ma nu-bànda-gu4; seal: Ur-Ma-ma nu-bànda-gu4 dumu Ir11-é-[]
1	subgenre_remarks	Oxen transferred from Kaamu to Lu-Lagaå; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Oxen, gu4 kishib Ur-dun sipa-gu4 ki SHà-ba-na-sig-ta; seal: Ur-dun sipa-gu4 d. Hu-[]
1	subgenre_remarks	Palm-leaves from Urabba to Lú-Ningirsu; seals: 1. Ur-ab-ba dubsar dumu Ba-zi dubsar síg-ka, 2. Ur-∂Nin-gír-su dubsar d Ba-[] (CBT 2)
1	subgenre_remarks	Palm-leaves transferred from Ur-Baba to Lu-Baba; tablet in case; seal: ∂Íul-gi nita kalag-ga lugal ¨ri˚-ma lugal an-ub-da límmu-ba Lú-∂Ba-ba6 rá-gaba ir11-zu (CBT 2)
1	subgenre_remarks	Palm-trees (giå.giåimmar giå.ga gam-gam-ma) transferred from Aga to Ur-Ninmar; case unopened; seal: Ur-∂Nin-MAR.KI dubsar dumu Nam-ha-ni (CBT 2)
1	subgenre_remarks	Palmtree byproducts: zé-na, gìr-lam, pa gishgishimmar from Lagash to Nippur, from Ur-Ishtaran to Ur-èsh-kù-ga; seal: Ur-èsh-kù-ga ds d. Ab-ba-gi-na
1	subgenre_remarks	Palmtree byproducts: zé-na, nì-ki-luh ki Kash4-ta kishib Har-sha6-ga; seal: Lú-dNin-gír-su ds d. Ur-èsh-kù-ga
1	subgenre_remarks	Part of Aramaic docket on UE., (Obv)13x(Rev)10x(UE)1 lines, seal impressions & signatures on edges, 6.4x6.6x2.75
1	subgenre_remarks	Partial seal impression, the same sealing as 14205
1	subgenre_remarks	Partition document; division of house and money among two brothers; seal impr on all sides, 12x16x2(u.e.) lines
1	subgenre_remarks	Partition document; seal impressions; (Obv)20x(LoE)2x(Rev)17 lines
1	subgenre_remarks	Partition of a houe and fields between two persons; seals; 4x4 lines
1	subgenre_remarks	Partition; seals; 6x3 lines
1	subgenre_remarks	Partnership agreement; dissolution of one partnership and formation of another; seals; 8x10x4 (u.e.) lines
1	subgenre_remarks	Paylist for 2 months; seal Ur-∂Ig-alim dubsar dumu Lú-∂[Nin-gír-su] (CBT 2)
1	subgenre_remarks	Paylist of women.  2 stamp seal impressions on lower end of Rev. 6X1X5
1	subgenre_remarks	Payment of an official's salary, days 1-6; seal impr on all edges; 6x5 lines
1	subgenre_remarks	Payment of an official's salary; 4x1x3 lines; seal impr u.e.; correct date no longer legible
1	subgenre_remarks	Payment of an official's salary; Seal impressions all over the surface, (Obv)5x(LoE)1x(Rev)3 lines.
1	subgenre_remarks	Payment of an official's salary; seal impressions on all over the surface, (Obv)5x(Rev)6 lines.
1	subgenre_remarks	Payment of an official's salary; tablet 3x2x2(rev) lines; case 5x3 lines, seal impr. on all sides.  Erasure of ca. 3 lines on tablet obv.
1	subgenre_remarks	Payment of an officials salary; Seal impressions on Obv.&LE., (Obv)4x(Rev)2x(UE)2 lines.
1	subgenre_remarks	Payment of money.  Seal impressions.
1	subgenre_remarks	Payment of official's salary, days 16-23; seal impr on edges; 6x4 lines
1	subgenre_remarks	Payment of salaries; seal impr le.e., lo.e; 5x4(rev)x3(u.e.) lines
1	subgenre_remarks	Payment of taxes.  Seal impressions.4x2x3 lines
1	subgenre_remarks	Payment(statement).  Seal impressions. 5X1X4 lines
1	subgenre_remarks	Payments; from temple archives; seal impr on obv, rev., u.e., l.e., r.e.; 8x1(u.e.) lines
1	subgenre_remarks	Pickaxes (ha-bù-da) received by Lú-Gù-dé-a from Lú-dingir-ra; seal: Lú-Gù-dé-a ds d. Lú-dBa-ba6?
1	subgenre_remarks	Pickaxes taken in account by Ur-shagalamma; 3 seals: Ur-shu-ga-lam-ma ds d. Ur-dNin-gis-zi-da ugula simug?; Ur-dNun-gal nu-bànda gu-za-lá d. Eren-da; A2-zi-da ds d. SHesh-shesh.
1	subgenre_remarks	Pigfat and dead sheep from Lú-dNin-gír-su to Nì-ú-rum rá-gaba; gìr Gù-dé-a bala-bi 12-àm; seal: seal dedicated to SHulgi Nì-ú-rum rá-gaba ir11-zu
1	subgenre_remarks	Pomponio: bulla with the name of an object and the anthroponym of an ugula(
1	subgenre_remarks	Pregnant cows from Lú-dingir-ra to Ad-da; seal: Ad-da ds d. Lugal-d[] sanga dInanna
1	subgenre_remarks	Price of oxen from the merchant Ur-Nanåe to ¨-ú the sanga; seal: É-ka-[] dubsar dumu Lú-[] (CBT 2)
1	subgenre_remarks	Promissory note; seal impressions on case; (Obv)8x(Rev)9x(UE)1 lines; Tablet 52 X 45 X 16 mm; Case 62 X 42 X 22 mm
1	subgenre_remarks	Pseudo Kassite seal impressions on all the surface except RE., (Obv)5x(LoE)1x(Rev)3 lines.
1	subgenre_remarks	Pulses and cumin for seeding from Inim-Baba-idab to Ur-Nanshe gu-za-lá; seal: Géme-dLama nin-dingir-dBa-ba6 Ur-dNanshe má-lah4? d. Lú-dBa-ba6 ds ir11-zu.
1	subgenre_remarks	Purchase agreement for 2 copper horns on order with the final price to be paid with interest at 1 1/2 gur barley per 1 shekel of silver; seals; 6x6 lines
1	subgenre_remarks	Purchase of X for 9 shekels of gold; witnesses; seals; 9x9 lines
1	subgenre_remarks	Purchase of a field; (Obv)11x(LoE)1x(Rev)11 lines, seal impressions on Rev.& 4 edges.
1	subgenre_remarks	Purchase of a field; w/seal impressions; (Obv)12x(Rev)15x(UE)3 lines
1	subgenre_remarks	Purchase of a garden; seal impressions; (Obv)12x(Rev)0x(UE)1 lines
1	subgenre_remarks	Purchase of a house; (Obv)14x(LoE)2x(Rev)3 lines, seal impression on Obv.& L.E.
1	subgenre_remarks	Purchase of a house; seal impressions all over the surfaces; (Obv)11x(Rev)10x(UE)1 lines
1	subgenre_remarks	Purchase of a house; seal impressions; (Obv)11x(Rev)11 lines
1	subgenre_remarks	Purchase of a house; seal impressions; (Obv)14x(Rev)10 lines
1	subgenre_remarks	Purchase of a portion of a house; w/seal impressions; tablet:(Obv)14x(Rev)11 lines, case:(Obv)15x(Rev)10 lines
1	subgenre_remarks	Purchase of a slave; seals. 10x3x10 lines
1	subgenre_remarks	Purchase of a slave; seals; labels; 12x3x5x2(u.e.) lines
1	subgenre_remarks	Purchase of a special kind of house.  Many seal impressions.
1	subgenre_remarks	Purchase of a temple office; W/seal impressions on Rev.,UE.&LE; ruled; (Obv)12x(Rev)17 lines; *d:the year of the king Di, in which the lu3-mah of the goddess Nininsina was installed; *ruled
1	subgenre_remarks	Purchase of field property; Tablet(Obv)14x(Rev)15x(LoE)1 lines, seal impressions on all the edges, Case(Obv)16x(LoE)1x(Rev)15x(UE)1 lines, seal impressions on all over the surfaces.
1	subgenre_remarks	Purchase; cf Wilcke Zikir Sumim 450ff; seal;11X17
1	subgenre_remarks	Rations for asses and an ox; seal of Lú-∂Nanna (CBT 2)
1	subgenre_remarks	Rations for builders transferred from Ur-ni9-gar to Ur-∂Lamma; seal: Ur-∂Lamma dubsar dumu Ur-∂Ba-ba6 åitim (CBT 2)
1	subgenre_remarks	Rations for fishermen (gi-gíd) from Luågina to Lu-Ningirsu; seal: Lú-∂Nin-gír-su dubsar dumu Ur-∂Nanåe; Shulgi 46/Amar-Suen 3 (CBT 2)
1	subgenre_remarks	Rations for gurush lú gish-ùr-ka-me, ki sukkal-mah; seal: Ur-dBa-ba6 ds d. Ir11
1	subgenre_remarks	Rations for guruå and érin transferred from Ur-ni9-gar to Ur-Igalim; seal illegible (CBT 2)
1	subgenre_remarks	Rations for various men; kiåib Ur-ki-sal4-la ù-tum kiåib Eå3-am zi-re-dam; seal: Ab-ba-mu dumu Ur-é-an-na (CBT 2)
1	subgenre_remarks	Rations for weaver women; seal: SHul-é-dù-dù ds d. Ur-d[] mu-bànda gu4
1	subgenre_remarks	Read mats from Ludingirra to Lumelam; seal: Lú-me-lám dubsar dumu Lú-[] (CBT 2)
1	subgenre_remarks	Reassignment of a debt of silver due in one month; seal.  7x2 lines
1	subgenre_remarks	Reassignment of obligation for silver. seal impressions. 7X2X7 UE 3 lines
1	subgenre_remarks	Receipt  of 2 sheeps received from Ur-Dumuzida. Seal: {d}Åu-{d}Suen lugal-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / A-a-kal-la ensi2 Umma{ki} arad2-zu.
1	subgenre_remarks	Receipt (many signs obliterated by seal) for a commodity. (CBT 1)
1	subgenre_remarks	Receipt (åu-ba-ti) of 2 gá-líl-åum; åà ∂Nin-MAR.KI; seal: Ur-∂Dumu-zi dubsar dumu Ka5-a má-lah4-gal (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of barley (CBT 2). A: Case of 22892; seal: Ur-∂Nanåe dubsar dumu Ur-é-an-na (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of barley by Lú-bi-mu from Lú-∂Nin-åubur; tablet in case; seal: Lú-bi-mu dubsar dumu Ur-∂Ig-alim (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of barley from Alla to Lú-∂[]; åe ur5-ra érin-e kú-a; tablet in case; seal: Lú-∂Ba-ba6 dumu Lú-∂[]; mu [...]˚ ba-h[ul] (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of barley; from Lugalkuzu to Lugal-magurre; sealed; Umma month name, itu åe-kar-gál (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of barley; mu érin-na; case unopened; seal: Ur-∂Nisaba dumu Lugal-[] sa12-du5 àga-uå; inscribed at 90° to normal (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of barley; åe-numun a-åà é-gibil-li-åè (CBT 2). A: Case of 23099; seal: Lú-∂Na-rú-a dubsar dumu Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of bulug si-è from Lugal-uå-gi-na to Ur-∂Lamma (CBT 2). A: Case of 22904; seal: Ur-∂Lamma dumu Ur-mes lú-åim (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of flour (dabin) from Ur-∂Lamma é ∂Nin-gír-su (CBT 2). A: Case of 23087; seal: Ma-an-sì-na dubsar dumu Lú-kir4-zal (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of flour; case unopened; seal: Lugal-mí-ús-sá dumu Lá-[] nu-bànda-gu4 (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of ox-hides and sheep-skins (CBT 2). A: Case of 23069; seal: Lú-∂Nin-gír-[su] dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Receipt (åu-ba-ti) of seed barley from Bazi to Akalla (CBT 2). A: Case of 23002; seal: A-kal-la dubsar dumu NE-NE [] (CBT 2)
1	subgenre_remarks	Receipt for 1 1/2 ma-na fo silver, issued as wages for the mechant and as maå-da-ri-a ezen-mah, which Lú-∂Dumu-zi received from Níg-ga. / Case: Text, as far as preserved, same as on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 1 1/5 royal gur of fine bread and for 4 4/5 gur of ordinary bread, received by Lú-urú§ and Ur-∂Åul-pa-è from Ur-∂KAB. / Case: Textx same as on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 1 sheep; seals; 4x3x1 lines
1	subgenre_remarks	Receipt for 10 royal gur of barley which A-hu-a s. of Lú-dùg-ga received from Ur-∂En-líl-lá out of the storehouse of the Enlil-temple for the purchase of reeds. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 10 spoons of sliver which Lú-∂Dumu-zi received from Ur-ab-ba. / Case: Text like that on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 13 1/2 gur of barley, the rations for 15 calves at  9/10 gur each. / Case: Text same as on tablet. Seal on case (CBT 1)
1	subgenre_remarks	Receipt for 13 sealed documents; Sippar; 4x3 lines
1	subgenre_remarks	Receipt for 24 royal gur of barley, produce of the field of the é-∂Sumukan, which Ur-åu-ga-lam-ma, the brewer, received from Lú-dúg-ga. / Case: Text corresponding to that on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 3 hoes; seals; Sippar; 6x3 lines
1	subgenre_remarks	Receipt for 4 5/6 royal pan of barley which Ur-∂Nin-líl received from Ma-an-SUM as food for workmen. / Case: Text like that on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 4 sheqel of silver borrowed for 6 months at a rate of 20 %; seal impressions on Rev(2),LoE(2),RE(1); (Obv)10x(Rev)5 lines; *Year in which King Rim-Sin occupied the city of Damiq-ilishu;
1	subgenre_remarks	Receipt for 40 gún of bitumen. / Case: Text same as on tablet with a few variant readings. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for 9 rams which Á-åa6-ga received from Lú-åa6-ga, "sealed" by Ur-∂IG-alim. (CBT 1)
1	subgenre_remarks	Receipt for a cow which Ur-∂Nanåe received from An-ni-ba-du7. / Case: Text corresponding to that on tablet; the cow is qualified as a-ru-a. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for a donkey which Lú-gu-la received from A-a-kal-la; Drehem (CBT 2). A: Case of 15932; seal dedicated to Íulgi, Da-a agrig dumu I3-[] ir11-zu; Drehem (CBT 2)
1	subgenre_remarks	Receipt for barley from Ur-bàd-tibir-ra; si-ì-tum nì-ka9-ak é-udu-ka; su-su-dam; seal: Íà-kù-ge dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Receipt for barley issued by Bazi to Atu; case unopened; seal: A-tu dumu Ur-tur-tur (CBT 2)
1	subgenre_remarks	Receipt for barley loan with interest; Drehem calendar; seals; 4x3 lines
1	subgenre_remarks	Receipt for barley.  Seal impression. 7x1x3 UE 2 lines
1	subgenre_remarks	Receipt for barley; seal Ur-[] sipa [] (CBT 2)
1	subgenre_remarks	Receipt for barley; seal; 6x4 lines
1	subgenre_remarks	Receipt for barley; seal; 6x7 lines
1	subgenre_remarks	Receipt for barley; seals; 6x3 lines
1	subgenre_remarks	Receipt for beer; seal; 3x1 line
1	subgenre_remarks	Receipt for beer; seals; 4x3 lines
1	subgenre_remarks	Receipt for bitumen (cf. 12476) which Ur-∂Ba-BA6 received from the gá-nun-GIÅ. / Case: Same text as on tablet, bitumen qualified as esír a-ba-al har-sag. Same year as on tablet, no month. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for bran; seal; 3x1 line
1	subgenre_remarks	Receipt for bricks; Seal impressions; (Obv)6x(Rev)8 lines
1	subgenre_remarks	Receipt for combed wool; seal; 5x4 lines
1	subgenre_remarks	Receipt for copper plow; seals; ?x3 lines
1	subgenre_remarks	Receipt for emmer; w/seal impressions all over the surfaces; (Obv)5x(Rev)4x(UE)1 lines
1	subgenre_remarks	Receipt for flour (details damaged), received by Ur-∂IG-alim s. of Lú-∂Nin-gír-su from Ur-TUR s. of Ur-åa6-ga. / Case: Text like that on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for food; seal impressions, (Obv)3x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Receipt for garlic, onions, seals, and ten servants; 5x6 lines
1	subgenre_remarks	Receipt for goods (details obliterated by fragment of case). / Case: Seal on case. (CBT 1)
1	subgenre_remarks	Receipt for goods for Ur-∂Gu4-ná-a from Íeå-kal-la; seal Ur-∂Gu4-ná-a [ds dumu Ur-mes?]; Umma (CBT 2)
1	subgenre_remarks	Receipt for grain delivered; seal; 3x2x2x1 line
1	subgenre_remarks	Receipt for loan of barley with interest; seals; 5x4 lines
1	subgenre_remarks	Receipt for loaned barley with interest at 1/3 amt.; seals; 5x4 lines
1	subgenre_remarks	Receipt for money.  Seal impressions. 5X1X6 UE1 lines
1	subgenre_remarks	Receipt for one sheep for regular offering; seals. 6x3x2 lines
1	subgenre_remarks	Receipt for payment of rent on a field; Murashu?; seals with names; 9x7 lines
1	subgenre_remarks	Receipt for rations for days 14-1 in the hand of" Nahiranu; seals; 7x2 lines"
1	subgenre_remarks	Receipt for rations; seals; 7x1 line
1	subgenre_remarks	Receipt for reeds; seal; 3x2 lines
1	subgenre_remarks	Receipt for sattukku offering for the ensi; seals; 6x4 lines
1	subgenre_remarks	Receipt for sesame oil; Drehem calendar; seal; 7x5 lines
1	subgenre_remarks	Receipt for sesame; incomplete case; seal: Ur-∂Nanåe sipa udu niga ∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Receipt for silver for rations; seals. 4x3x2 UE 1 lines
1	subgenre_remarks	Receipt for silver loan with  security; seals; 8x8 lines
1	subgenre_remarks	Receipt for silver loan with interest; seal; 6x7 lines
1	subgenre_remarks	Receipt for silver loan without interest; seals; 6x7x3 lines
1	subgenre_remarks	Receipt for silver; seals; 6x1x1x2(u.e.) lines; 4.6x4.3x.2.2 cms
1	subgenre_remarks	Receipt for slave price; w/seal impression on case; 40 X 35 X 13 mm.
1	subgenre_remarks	Receipt for the contribution (bal) of 13 leather du10-gan-bags. Seal: Ur-{d}Nun-gal ds d. Lugal-e2-mah-e.
1	subgenre_remarks	Receipt for the contribution (bal) of barley assigned to the payment of a hired boat. Seal: Lugal-e-ba-an-åa6 ds d. Ur-{d}Iåtaran.
1	subgenre_remarks	Receipt for the contribution (bal) of ca. 60 kg. of ma-nu-wood. Seal: Mu-ni ds d. A-a-kal-la guda2 {d}Nin-ur4-ra.
1	subgenre_remarks	Receipt for the contribution (bal) of reed baskets. Seal: illegible.
1	subgenre_remarks	Receipt for the delivery of small cattle; seals
1	subgenre_remarks	Receipt for the part payment, on an order from the owner, of a fixed revenue upon a field; seal impr on rev & l.e.; 8x1x8 lines
1	subgenre_remarks	Receipt for the transfer of 36 male worker to the account of Baåa. Seal: Ba-åa6 ds d. Lugal-åa6-ga.
1	subgenre_remarks	Receipt for u-sa-ki-ir MartuKI mahir; w/seal impression;
1	subgenre_remarks	Receipt for wool from Lipit-Ishtar to Ili-iqisham; seals; 6x6x2 lines
1	subgenre_remarks	Receipt for wool; seal impressions on all the sides; (Obv)4x(LoE)2x(Rev)5 lines
1	subgenre_remarks	Receipt for wool; seal; 5x4 lines
1	subgenre_remarks	Receipt fpr 40(+x) sheep and 35 máå allocated for food of the shepherds of Gír-su§, and issued by Ur-en-gal-du-du to Lú-∂Ba-BA6/Ú. / Case: Same text. Seal on case. (CBT 1)
1	subgenre_remarks	Receipt given for wool received for another; seal impressions on Obv,LoE,Rev,UE.&RE.; (Obv)5x(LoE)1x(Rev)1 lines
1	subgenre_remarks	Receipt of 0,1,0 åim sig5 lugal from Ur-tur to Lu-Ningirsu; seal: Lú-∂Nin-gír-su dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Receipt of 1 ewe received by Lukala from Nigduga. Seal: Lú-kal-la ds d. Ur-e11-e kuå7
1	subgenre_remarks	Receipt of 1 gi-gur-basket received from Agu, åà-bal-a. Seal: Åeå-åa6-ga ds d. Lugal-gu3-de2-a.
1	subgenre_remarks	Receipt of 1 gur-basket received by Luninura fom Agu. Seal: Lú-{d}Nin-ur4-ra d. Lugal-[]
1	subgenre_remarks	Receipt of 1 lamb on behalf of Åulginada lu2-en-nun-ga2, received from Uåmu. Seal: {d}Åu-{d}Suen lugal-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / A-a-kal-la ensi2 Umma{ki} arad2-zu.
1	subgenre_remarks	Receipt of 1 leather sack received by Akalla singer from Akalla. Seal: {d}Åul-gi nita-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / Ur-{d}Li9-si4 ensi2 Umma{ki} arad2-zu.
1	subgenre_remarks	Receipt of 1 male worker received by Dingira from Dada. Seal: Dingir-ra-[kam] ds d. Lu2-g[a]
1	subgenre_remarks	Receipt of 1 mat and 4 gi-u3-suh5 received by Luninura from KAåulpa´e. Seal: Lu2-{d}[Nin-ur4-ra] [ds] d. Lugal-[giri3?-nun?]
1	subgenre_remarks	Receipt of 1 åerrum-mat for a ship loaded with flour. Seal: Lu2-Ib-gal ds d. Ur-gi6-par4 guda2 {d}Inanna.
1	subgenre_remarks	Receipt of 10 cloths. Seal: {d}Amar-{d}Suen nita-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / Ur-{d}Li9-si4 ensi2 Umma{ki} arad2-zu.
1	subgenre_remarks	Receipt of 1080 l of barley as la2-NI-ta-su-ga, received from Luhegal. Seal: Åeå-a-ni ds d. A-na-mu
1	subgenre_remarks	Receipt of 118 sheep carcasses (dìm udu ba-ug7); mu-gemé-uå-bar-åè; case unopened; seal: ∂Utu-mu dubsar dumu Nam-ha-ni ab-ba uru (CBT 2)
1	subgenre_remarks	Receipt of 12 male workers for irrigation works in the field Lamah. Seal: Ur-ni9-gar ds d. Lu2-gi-na.
1	subgenre_remarks	Receipt of 120 kg of reed. Seal: Mu-ni ds d. A-a-kal-la guda2 {d}Nin-ur4-ra.
1	subgenre_remarks	Receipt of 13 young he-goats and two horns(?) received by La’amu from Ur-Åe’ila. Seal: La-a-mu sipa {d}Nin-Zabalam3{ki}.
1	subgenre_remarks	Receipt of 144 l of é-a-bitumen for the governor's ship. Seal: Ur-e2-mah ds d. Da-da.
1	subgenre_remarks	Receipt of 150 male workers for the guda-priest of Ninhursag-gula, received by Lugal-ezem from Lugal-nilagare. Seal: Lugal-ezem ds d. Lugal-e2-mah-e åabra.
1	subgenre_remarks	Receipt of 2 dead sheeps received from Åeåkalla. Seal: Lu2-kal-la ds d. Ur-e11-e kuå7.
1	subgenre_remarks	Receipt of 2 mats. Seal: [Ku3]-{d}Nin-ur4-ra ds d. Na-DI [l]u2-ÅIMxNIG2
1	subgenre_remarks	Receipt of 2 pestles received by Nigurum from Åeåkalla. Seal: Nig2-u2-rum ds d. {d}Nanna-i3-zu.
1	subgenre_remarks	Receipt of 2 sieves for fine flour received from Baza. Seal: Lugal-si-NE-e ds Lugal-åa6-[ga]
1	subgenre_remarks	Receipt of 2 workers in service for irrigation works. Seal: [...] nu-banda3 g[u4 ...] dumu Lugal-nig2-[lagar-e].
1	subgenre_remarks	Receipt of 20 sheep carcasses (dìm udu); tablet in case; seal of Íu-∂Nin-åubur, nu-bànda uå-bar, dedicated to Ur-∂[Ba-ba6] énsi of Urusagrig, Su-∂Nin-åubur ir11-zu (CBT 2)
1	subgenre_remarks	Receipt of 21 male workers for carrying flour to the quay. Seal: Ur-zu ds d. A2-zi-da.
1	subgenre_remarks	Receipt of 3 gur-baskets as nig2-diri-payment for ka-e2-gal, received from Agu. Seal: Lu2-dingir-ra ds d. Ur-∂Ba-ba6.
1	subgenre_remarks	Receipt of 3 reed baskets with straw for Gaeå, received from Ur-Åulpa’e. Seal: Inim-{d}Åara2 ds d. Lugal-iti-da.
1	subgenre_remarks	Receipt of 30 male worker for irrigation works. Seal: Lu2-du10-ga ds d. He2-ma-DU.
1	subgenre_remarks	Receipt of 300 l  of barley seed from ki-su7-gu-la a-åa3 la2-mah, received from Lu-Åulgira. Seal: Ur-{d}Åul-pa-e3 d. Ur-{d}[Iåtaran lu2 udu-niga.
1	subgenre_remarks	Receipt of 3000 l of dry bitumen received by Sarrum-ili from the governor of Umma. Seal: {d}Åul-gi nita-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / [...]-i3?-li2 [...] [x [...] arad2-zu.
1	subgenre_remarks	Receipt of 4 gi-hal-baskets. Seal: [A?-[a-a?] d. Ur-T[E? ...].
1	subgenre_remarks	Receipt of 40 l of (emmer) groats received from Lugina. Seal: Ur-Zabalam3{ki} ds aga3-us2 I3-kal-la.
1	subgenre_remarks	Receipt of 6 goats from Lú-∂Nin-gír-su (máå); case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe nu-bànda (CBT 2)
1	subgenre_remarks	Receipt of 6 sheep carcasses from Nì-ú-rum (dìm udu) by a female weaver of Girsu; åà Ki-nu-nir˚; seal: Lú-∂Gù-dé-a dubsar dumu [Ti-ma-...] (CBT 2)
1	subgenre_remarks	Receipt of 60 dead sheeps received from Lu-Utu. Seal : Lu2-kal-la ds d. Ur-e11-e kuå7.
1	subgenre_remarks	Receipt of 60 l of barley as wages for hired UN.IL2. Seal: Ur-{d}Nun-gal ds d. Ur-{d}Åara2 åa13-dub-ba-ka.
1	subgenre_remarks	Receipt of 63 dead sheep; seal: Ad-da dubsar dumu Da-a-da (CBT 2)
1	subgenre_remarks	Receipt of 80 bundles of manu-wood  received by Adu from Zina. Seal: [...]-mu-[(x)]  ds dum[u ...].
1	subgenre_remarks	Receipt of 9 gur-dub-EN-baskets received from Agu. Seal: Lugal-si-NE-e ds d. Lugal-åa6-ga.
1	subgenre_remarks	Receipt of <se>.har.gu4.ri.nu; seal; 5x4 lines
1	subgenre_remarks	Receipt of ? from 4/VI to 1/VII; seal of Enlil-nadin-ahe; 6x1 line
1	subgenre_remarks	Receipt of GI.DUR reed; seal; 5x7 lines
1	subgenre_remarks	Receipt of TUKUxUD-wood for {dug}utul2-gal-gal, received from Agu. Seal: Ur4!-åa3-ta-lu2 d. Ur-åu-ku3-ga guda2.
1	subgenre_remarks	Receipt of ZI3.KAL; Drehem calendar; seals; 3x3 lines
1	subgenre_remarks	Receipt of [] for the riten of ki-{d}Suen received by Huwawa from Åeåkala. Seal: Lu2-[{d}]«Nin»-[e]zem ds d. E[n...]
1	subgenre_remarks	Receipt of []+1 male workers. Seal: illegible (2 lines)
1	subgenre_remarks	Receipt of a container for tablets received from Ur-Åulpa’e. Seal: illegible.
1	subgenre_remarks	Receipt of a dead sheep. Seal: Lu2-kal-la ds d. Ur-e11-e kuå7.
1	subgenre_remarks	Receipt of a deficit of 330 l of barley, which was delivered to Ur. Seal: Ur-{d}Li9-si4 ensi2 Umma{ki} Lu2-kal-la ds.
1	subgenre_remarks	Receipt of a lamb and barley received from Uåmu. Seal: {d}Åu-{d}Suen lugal-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / A-a-kal-la ensi2 Umma{ki} arad2-zu.
1	subgenre_remarks	Receipt of a quantity of ... for the purchase of ... Seal: {d}Åu-{d}Suen lugal-kal-ga lugal Uri5{ki}-ma lugal {d}Ub-da-limmu2-ba / [...] ensi2 Umma{ki} arad2-zu.
1	subgenre_remarks	Receipt of a reed-mat received by Lu-Åara from Åeåkalla. Seal: Lu2-{d}Åara2 ds d. Uru-bar-r[e?].
1	subgenre_remarks	Receipt of a åerrum-mat used to cover a ship loaded with flour. Seal: Ur-{d}Nin-tu ds d. A-ab-ba-ni åabra {d}Nin-ur4-ra.
1	subgenre_remarks	Receipt of an unidentified object for the mu-DU of the king received by Ur-Nintu from Na’ua. Seal: Ur-∂Nin-tu ds d. Du11-ga.
1	subgenre_remarks	Receipt of aromatics; seals; 4x4 lines
1	subgenre_remarks	Receipt of aromatics?; seal
1	subgenre_remarks	Receipt of arrears of 30 male workers. Seal: Ur-{d}Ma-mi d. A2-zi-da.
1	subgenre_remarks	Receipt of barley (sá-du11 ∂Inanna) from Ur-bàd-tibir-ra; seal: Lú-∂Utu dub-sar dumu Nì-∂Ba-ba6); marginal note: 80 gur (CBT 2)
1	subgenre_remarks	Receipt of barley (sá-du11 ∂Íulgi) from Ur-bàd-tibir-ra; gìr Na-na; seal: Lú-URUxKåR˚ (CBT 2)
1	subgenre_remarks	Receipt of barley (zì, åe) for géme-àr from Niurum; lá-ni su-ga Lugal-síg-su13; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Receipt of barley (åe numun mur-gu4 á hun-gá åe amar-ra ù åe-ba un-íl; case unopened; seal: Ur-∂Gá-tùm-du10 dubsar dumu Lú-∂Igi-ma-åè (CBT 2)
1	subgenre_remarks	Receipt of barley (åe-ba un-íl é-lugal) from Ur-bàd-tibir-ra; seal: Lú-∂Nin-åubur dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Receipt of barley and beer from Íà-kù-ge; seal: Ur-∂En-líl-lá dubsar dumu Inim-åa6 kuruåda (CBT 2)
1	subgenre_remarks	Receipt of barley and emmer received from Arad. Seal: Lu2-dingir-ra ds d. Ku3-åa6-ga.
1	subgenre_remarks	Receipt of barley as wages (á hun-gá); case unopened; seal of ¨-ma-gi-na (CBT 2)
1	subgenre_remarks	Receipt of barley by brewer; seal; Nippur calendar; 6x3 lines; 3.9x3.2
1	subgenre_remarks	Receipt of barley for captives. Seal: Ur-{d}Åara2 ds d.Gu2-u3-[DIB]
1	subgenre_remarks	Receipt of barley for workers; seals; 5x4 lines
1	subgenre_remarks	Receipt of barley from Bazi; case unopened; seal: Na-ba-åa6 dubsar dumu Ur-ni9-gar (CBT 2)
1	subgenre_remarks	Receipt of barley from Ikalla; åe nì-gál-la á lú-hun-gá-åè; case unopened; seal: Lú-bala-åa6-ga dubsar dumu Ur-∂Nin-gis-zi-da (CBT 2)
1	subgenre_remarks	Receipt of barley from Lugal-gú-gal; åe-ba sipa-ne; case unopened; seal: Gù-dé-a dubsar dumu Sag-∂Nanna-zu lú-zi nì na-ga-ab-tum? (CBT 2)
1	subgenre_remarks	Receipt of barley from Lugal-melam; lá-ni su-ga; case unopened; 2 seals: 1. Ur-gar dubsar dumu Lugal-lú-åa6-åa6; 2. Lú-∂Ba-ba6 rá-gaba dedicated to Íulgi (CBT 2)
1	subgenre_remarks	Receipt of barley from Lú-gi-na for rá-gaba; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Receipt of barley from Lú-kal-la; gìr Lugal-im-ru-a; seal: Du11-ga-ni-zi dubsar dumu Lú-gi-na; mu-ús-sa mu-ús-sa-a-bi (CBT 2)
1	subgenre_remarks	Receipt of barley from Lú-kal-la; under seal of Ur-∂Íul-pa-è (but tablet not sealed) (CBT 2)
1	subgenre_remarks	Receipt of barley from Lú-åa6-ga-mu; åà-gal érin-é-∂Nanåe-ka-åè; case unopened; seal: Ur-åu-ga-lam-ma dubsar dumu Lugal-uru?-da? (CBT 2)
1	subgenre_remarks	Receipt of barley from Na-ba-åa6; åe numun a-åà ∂Amar-∂EN.ZU-ki-ág-∂Nin-gír-su-ka-ke4; case unopened; seal: Lugal-∂Íul-gi dubsar dumu ∂Utu-mu (CBT 2)
1	subgenre_remarks	Receipt of barley from Na-du10; gìr Ur-∂Ba-ba6 dumu Hi-lí!; case unopened; seal: Lú-∂Na-rú-a dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-Igalim to Lu-kirzal; åe amar-e kú-åè; case unopened; kiåib: Lú-kir4-zal; seal: Ur-∂Ba-ba6 dubsar dumu Ur-∂Kal-kal (reading not sure) (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; gìr Lú-gá; seal: Lú-∂Ig-alim dumu Lú-gu-[la] lú kisal búr (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; gìr Ur-∂Nin-giå-zi-da; sá-du11 ∂Íul-gi; seal: Lú-dingir-ra dumu Lú-∂Nin-dar-a gudu4 ∂Íul-gi (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; gìr Íà-kù-ge; seal: Lú-me-lám dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; gìr ∂Lamma-uru-na; seal: Lú-∂Ba-ba6 dumu ∂Nanåe-kam lú åim (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; seal: Lú-∂Nin-gír-su dubsar dumu ∂Nanåe-kam lú-åim? (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; åà-gal hé-dab5 gu4-åè; gìr ∂Ba-ba6-íb-gu-ul; kiåib Lugal-zag-ge-si sanga; seal: Lugal-zag-ge-si dubsar dumu Ur-∂Nin-[Ig-alim] (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-bàd-tibir-ra; åà-gal hé-dab5 gu4-åè; seal: Ur-∂Ig-alima dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-ni9-gar; seal: Ka5-a-mu dubsar dumu Lugal-zà-ge-si (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-{d}En-ki; lá-ni su-ga; case unopened; seal: Ur-{d}Nin-gisz-zi-da dubsar dumu Lugal-sza6-ga (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-∂En-líl-lá; gìr Ur-bàd-tibir-ra; seal: Lugal-kin-gi4-a dubsar dumu Ur-∂[] (CBT 2)
1	subgenre_remarks	Receipt of barley from Ur-∂Nanåe; åà-gal gu4-åè; case unopened; seal: ∂Utu-mu dumu Ur-[] (CBT 2)
1	subgenre_remarks	Receipt of barley loan from Lú-bi-mu (åe ur5-ra); é ∂Gá-tùm-du10; case unopened; seal: En-in-na-kal nu-bànda gu4 ∂Nanåe dumu Má-gur8-re (CBT 2)
1	subgenre_remarks	Receipt of barley loan of Inanna; seal; 6x4 lines
1	subgenre_remarks	Receipt of barley loan with interest; seal; 5x8 lines
1	subgenre_remarks	Receipt of barley loan with interest; seal; Nippur calendar; 3x4 lines; 4.3x3.5
1	subgenre_remarks	Receipt of barley loan; seal; 5x5 lines
1	subgenre_remarks	Receipt of barley rations (åe-ba un-íl); case unopened; seal: Ab-ba-mu dubsar dumu Lú-Nina˚ (CBT 2)
1	subgenre_remarks	Receipt of barley rations for two female slaves; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Receipt of barley rations from Gu-za-ni (åe-ba hé-dab5-ba); case unopened; seal: Ur-mes dumu Lú-∂Dumu-zi ugula (CBT 2)
1	subgenre_remarks	Receipt of barley rations; é ∂Íul-gi-me; case unopened; seal: Al-la dubsar dumu Lú-URUxKåR˚ (CBT 2)
1	subgenre_remarks	Receipt of barley seed; seals; 4x4
1	subgenre_remarks	Receipt of barley seed; seals; 4x6 lines
1	subgenre_remarks	Receipt of barley seed; seals; 5x4 lines
1	subgenre_remarks	Receipt of barley, emmer, etc; seals; 5x5 lines
1	subgenre_remarks	Receipt of barley-loan; åe ur5-ra engar nu-bànda; case unopened; seal: Nam-ha-ni (CBT 2)
1	subgenre_remarks	Receipt of barley; case unopened; seal: Hu-ti dumu Hé-ti gu-za-lá (CBT 2)
1	subgenre_remarks	Receipt of barley; case unopened; seal: Ku-li dubsar dumu Ki-ág-mu (CBT 2)
1	subgenre_remarks	Receipt of barley; case unopened; seal: Lugal-dub-lá dumu Ur-tur-tur-[?] (CBT 2)
1	subgenre_remarks	Receipt of barley; case unopened; seal: Lú-∂Kal-kal dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Receipt of barley; case unopened; seal: Ur-∂Gilgames dubsar dumu Al-la (CBT 2)
1	subgenre_remarks	Receipt of barley; ki Ka5-a gu-za-lá; seal: Lú-∂Nin-gír-su dubsar dumu Ba-zi; case unopened (CBT 2)
1	subgenre_remarks	Receipt of barley; kiåib Da-gi-mu; seal illegible (CBT 2)
1	subgenre_remarks	Receipt of barley; lá-ni su-ga; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Receipt of barley; seal
1	subgenre_remarks	Receipt of barley; seal: Ur-mes dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Receipt of barley; seal: Ur-ni9-gar dubsar dumu Lú-∂Nanåe (CBT 2)
1	subgenre_remarks	Receipt of barley; seal: Ur-∂En-líl-lá dubsar dumu Inim-åa6 kuruåda (CBT 2)
1	subgenre_remarks	Receipt of barley; seal; 5x4 lines
1	subgenre_remarks	Receipt of barley; seals; 3 lines
1	subgenre_remarks	Receipt of barley; seals; 3x1 line
1	subgenre_remarks	Receipt of barley; seals; 3x2 lines
1	subgenre_remarks	Receipt of barley; seals; 4 lines
1	subgenre_remarks	Receipt of barley; seals; 4x3 lines
1	subgenre_remarks	Receipt of barley; seals; 4x4 lines
1	subgenre_remarks	Receipt of barley; seals; 4x5 lines
1	subgenre_remarks	Receipt of barley; seals; 5x2 lines
1	subgenre_remarks	Receipt of barley; seals; 5x3 lines
1	subgenre_remarks	Receipt of barley; seals; 9x6 lines
1	subgenre_remarks	Receipt of barley; åe a-åà ∂Nin-tu má-a si-ga; case unopened ; seal: Ur-∂En-líl-lá dubsar dumu Inim-åa6 kuruåda (CBT 2)
1	subgenre_remarks	Receipt of barley; åe ur5-ra érin-na; case unopened; seal: Lú-gu-la dumu Lugal-[] nu-bànda gu4 (CBT 2)
1	subgenre_remarks	Receipt of barley; åe ur5-ra érin-na; tablet in case; seal: Ur-åa6-ga dubsar dumu E3-ne-bi sa12-du5 ∂Dumu-zi (CBT 2)
1	subgenre_remarks	Receipt of barley; åe-ba lú mar-sa from Ki-tuå-lú; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Receipt of barley; åe-ba nu-GIÍ.kiri6-àm; case unopened; seal: Ur-sukkal lú [] dumu Ur-[] (CBT 2)
1	subgenre_remarks	Receipt of barley; åe-ba ù åà-gal anåe from Kú-du-uq-åe-in; seal: Ur-∂Ba-ba6 dubsar dumu Na-mu (CBT 2)
1	subgenre_remarks	Receipt of barley; åà-gal gu4 udu-åè; case unopened; seal: Lugal-gú-gal dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Receipt of barley; åà-gal érin Ma-ad-ga-åè; case unopened; seal: Ur-sag-ku5 dumu å-na-na (CBT 2)
1	subgenre_remarks	Receipt of barley; é-àr-àr-åè; case unopened; seal: I-ta-è-a dubsar dumu Lú-du10-ga sanga ∂Nin-gír-su-ka (CBT 2)
1	subgenre_remarks	Receipt of baskets?. Seal: Lú-kal-[la] ds [d.?]
1	subgenre_remarks	Receipt of beer; seal: Ur-∂Ba-ba6 dubsar dumu [] (CBT 2)
1	subgenre_remarks	Receipt of beer; seal; 5x1 line
1	subgenre_remarks	Receipt of beer; seal; 6x4 lines; date possibly IS 3
1	subgenre_remarks	Receipt of beer; seals; 4x3 lines
1	subgenre_remarks	Receipt of beer; seals; 5x4 lines
1	subgenre_remarks	Receipt of bread (ninda gin) from Itaea; case unopened; seal: Ur-∂Ig-alim dub-sar dumu Ur-ni9-gar (CBT 2)
1	subgenre_remarks	Receipt of bronze nails (giå.kak zabar) by A-lá-ì-åa6; Ur?; sealed (CBT 2)
1	subgenre_remarks	Receipt of ca. 30 kg. of UD-gunu-wood from the field of the e2-uz-ga, received from E’urbidu. Seal: Lu2-åa6-i3-zu ds d. A-kal-la.
1	subgenre_remarks	Receipt of ca. 30 kg. of branches for 21-gu4-gaz, received from Uremaå. Seal: Mu-ni d. A-a-kal-la guda2 ∂Nin-ur4-ra.
1	subgenre_remarks	Receipt of ca. 7.5 kg. of gi-wool, received by Åeåkalla from Lugal-ezem. Seal: Ur-{d}Li9-si4 ensi2 Umma{ki} / Åeå-kal-la ds d. [...] arad2-zu.
1	subgenre_remarks	Receipt of ca. 90 kg. of reeds for the e2-uz-ga. Seal: En-kaå4 ds d. Ur-{d}Iåtaran.
1	subgenre_remarks	Receipt of corn and beans; case:w/seal impressions; *Peters describes as Nippur I, although Ur3 tablets are characteristic to Nippur II.  I" came from Tablet Hill
1	subgenre_remarks	Receipt of corn; w/seal impressions, bearing king's name; 4 lines
1	subgenre_remarks	Receipt of dead sheeps received from Lukalla. Seal: Lu2-kal-la ds d. Ur-e11-e kuå7.
1	subgenre_remarks	Receipt of emmer for different people. Seal: Arad2-mu ds d. Ur-ni9-gar kuå7.
1	subgenre_remarks	Receipt of emmer loan without interest; seal; 5x6 lines
1	subgenre_remarks	Receipt of emmer; seal; 5x2 lines
1	subgenre_remarks	Receipt of esa; seal
1	subgenre_remarks	Receipt of female workers for 1 day; seals; 5x5 lines
1	subgenre_remarks	Receipt of fine flour (níg-àr-ra) by A-tu AB-NA; case unopened; seal: A-tu dumu Lú-∂Nin-gír-su lú kaå; in year name: en Unug˚-ke4 åu-du7-du7-dè (CBT 2)
1	subgenre_remarks	Receipt of flour (dabin) from Lú-du10-ga; seal: Lú-dingir-ra dubsar dumu Lugal-é-mah-e (CBT 2)
1	subgenre_remarks	Receipt of flour (dabin); case unopened; kiåib-ba-na ti; seal: Lú-∂[Nin-åubur] dubsar dumu Lú-∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Receipt of flour (dabin); é ∂Dumu-zi; seal: Ur-∂Ba-ba6 dubsar dumu Ha-ba-lug-gé (CBT 2)
1	subgenre_remarks	Receipt of flour (zì) from Ur-Baba; seal: Lú-åa6-ga dubsar dumu Ur-åa6-ga (CBT 2)
1	subgenre_remarks	Receipt of flour (zì-gu) from Aridubuq; åà bala-a; kiåib Lú-∂En-[...]; seal: ∂Íára-mu-túm dubsar dumu Ur-kù (CBT 2)
1	subgenre_remarks	Receipt of flour from Ur-Baba (dabin sig15); case unopened; seal: Ma-an-sì-na dubsar dumu Lú-kir4-zal (CBT 2)
1	subgenre_remarks	Receipt of flour from Ur-Iåtaran (dabin); case unopened; seal: Lú-ba dubsar dumu A-mu (CBT 2)
1	subgenre_remarks	Receipt of flour from Ur-ni9-gar (zì-KAL-KAL, dabin); case unopened; seal: Ur-∂Nisaba dubsar dumu Íà-kù-gi sanga ∂Gá-tùm-du10 (CBT 2)
1	subgenre_remarks	Receipt of flour from Ur-é-ninnu (dabin) (CBT 2). A: Case of 23056; seal: seal: Lú-kal-la dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Receipt of fodder for oxen and equids. Seal: Ur-{d}Suen ds d. Ur-{giå}gigir.
1	subgenre_remarks	Receipt of food; case unopened; sealed (Ur-∂Lamma) (CBT 2)
1	subgenre_remarks	Receipt of gazi si-è and åe zibitum from Ur-Baba; seal: Nam-ha-ni dubsar dumu Hu-wa-wa (CBT 2)
1	subgenre_remarks	Receipt of grain; seal impressions; (Obv)5x(Rev)4 lines; 45 X 36 X 11 mm.
1	subgenre_remarks	Receipt of grain; w/seal impressions; (Obv)5x(Rev)5x(UE)2 lines
1	subgenre_remarks	Receipt of gu-flour.Seal: Lu2-dingir-ra ds d.Ur-{d}Ba-ba6
1	subgenre_remarks	Receipt of hides for the goddess Gula, received from Akalla. Seal: Ur-∂Åul-pa-e3 d. Ur-∂Iåtaran lu2 udu-niga.
1	subgenre_remarks	Receipt of ku-mah; w/seal impressions; (Obv)5x(Rev)4 lines
1	subgenre_remarks	Receipt of ku6-åe, ku6-kù-ga and åà-dub-ba from Gù-dé-a; case unopened; seal: Íeå-åeå dumu Ur-∂[] (CBT 2)
1	subgenre_remarks	Receipt of loan of barley (åe ur5-ra) as rations for workmen from Ur-ni9-gar; case unopened; seal: Ur-∂Ig-alima dubsar dumu [] nu-bànda (CBT 2)
1	subgenre_remarks	Receipt of loan of oil with interest; seal; 4x4 lines
1	subgenre_remarks	Receipt of loan; seals
1	subgenre_remarks	Receipt of munu4-si-è from Lú-kal-la; seal: Ur-∂Íul-pa-è dumu [] lú-åim (CBT 2)
1	subgenre_remarks	Receipt of oil (ì-giå lugal, ì-åáh, ì-túg-ge ag-dè; tablet in case; seal: Lú-∂Ba-ba6 rá-gaba with dedication to Íulgi (CBT 2)
1	subgenre_remarks	Receipt of oil (ì-giå lugal, ì-åáh, ì-túg-ka-bar-ra ag-dè); case unopened; seal: A-hu-um-∂Da-mu Lú-∂Nanna dubsar bàn-da (CBT 2)
1	subgenre_remarks	Receipt of oil (ì-giå) for women; åà Nibru˚; seal: Ur-mes dubsar dumu Ur-∂Lamma (CBT 2)
1	subgenre_remarks	Receipt of pea flour; seals;
1	subgenre_remarks	Receipt of rations for guruå and géme; seal: Nam-mah dubsar dumu Ur-∂Nin-bára kab-sar (CBT 2)
1	subgenre_remarks	Receipt of reed baskets received by Urdumuzida from Åeåkala. Seal: Ur-{d}[Dumu-zi-da] d. Ir3?-[...] [    ] DIM2?
1	subgenre_remarks	Receipt of sar.x; seals; 4x4 lines
1	subgenre_remarks	Receipt of se.har.amar.ri.nu; seal; 4x5 lines
1	subgenre_remarks	Receipt of se.har.gu4.ri.nu; seals; 4x7 lines
1	subgenre_remarks	Receipt of seed-barley (åe-numun-åè); case unopened; seal: A-(a)-kal-la dubsar dumu Ab-ba-gi-na sa12-du5 (CBT 2)
1	subgenre_remarks	Receipt of seed-barley (åe-numun-åè); case unopened; seal: Al-la dubsar dumu Lú-URUxKåR˚; fabric impression (CBT 2)
1	subgenre_remarks	Receipt of seed-barley from Lugal-zag-ge-si; case unopened; seal: Gù-dé-a dubsar dumu Ur-∂Utu nu-bànda (CBT 2)
1	subgenre_remarks	Receipt of seed-barley; seal: Lugal-izkim-zi dubsar dumu Lú-∂Giå-bar-è; tablet in case (CBT 2)
1	subgenre_remarks	Receipt of seed-barley; seal: Íeå-kal-la dumu Un-íl; tablet in case; mu-ús-sa x [...] (CBT 2)
1	subgenre_remarks	Receipt of sesame oil; seal; 5x4 lines
1	subgenre_remarks	Receipt of sheep (udu NI, udu niga); case unopened; seal: Lugal-nám-mah dubsar dumu Da-da (CBT 2)
1	subgenre_remarks	Receipt of sheeps received from Urru. Seal: Arad2-mu ds Ur-ni9-[gar (kuå7)].
1	subgenre_remarks	Receipt of sheeps received from Urru. Seal: Lu2-kal-la ds d. Ur-e11-e kuå7.
1	subgenre_remarks	Receipt of silver loan without interest; seals; 5x5 lines
1	subgenre_remarks	Receipt of silver loan; seal; 5x6 lines
1	subgenre_remarks	Receipt of silver loan; seals; 5x5 lines
1	subgenre_remarks	Receipt of silver received by Akala from Åeåkala. Seal: A-a-kal-la ds. d. U[r-U.UD].KID-gar kuå7
1	subgenre_remarks	Receipt of silver; seals; 6x6 lines
1	subgenre_remarks	Receipt of skins für a plough. Seal: Lu2-{d}Åara2-[an-dul3] ds d. Lu2-[..] sa12-d[u5]
1	subgenre_remarks	Receipt of sprouted malt; seals; 5x3 lines
1	subgenre_remarks	Receipt of threshed barley. Seal: Lugal-e2-mah-e ds d. Lugal-ku3-ga-ni.
1	subgenre_remarks	Receipt of u2.girx.gunu.sa?; seal; 5x4 lines
1	subgenre_remarks	Receipt of wages in barley for workmen; é ∂Nin-dar-a; case unopened; seal: Ur-∂SA.KALAM dumu Nam-ha-ni ugula un-íl (CBT 2)
1	subgenre_remarks	Receipt of wages in barley; seals; 5x8 lines
1	subgenre_remarks	Receipt of weighed textiles (CBT 2). A: Case of 23302; sealed (CBT 2)
1	subgenre_remarks	Receipt of wooden beams; Ur-Nusku; seals; 4x5 lines
1	subgenre_remarks	Receipt of wooden pieces of ships received by Ur-{d}Geåtin-an-ka from the governor. Seal: Ur-{d}Geåtin-an-ka ma2!-lah4 ensi2 Umma{ki}-ka dumu Lugal-sukkal.
1	subgenre_remarks	Receipt of wool, sheeps of the governor, received from Ur-Dumuzida. Seal: Nin9-he2-li2-a dam A-a-kal-la dumu Ur-{d}Da-mu.
1	subgenre_remarks	Receipt of wool. Seal: Ur-gi6-par3 ds d. A-a-kal-la
1	subgenre_remarks	Receipt of zi3-kal; seal; 4x4 lines
1	subgenre_remarks	Receipt(?) of barley; seal: Lú-∂Nin-gír-su dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Receipt.  Seal impressions. 6X3X6 UE 2 lines
1	subgenre_remarks	Receipt.  Seal impressions. 6x2x3 UE 3 lines
1	subgenre_remarks	Receipt; case opened, seal impr all sides; tabl 5x1x1(rev) lines; case 5x1x1(rev) lines
1	subgenre_remarks	Receipt; case:same seal impressions on all the sides, Tablet:(Obv)5x(LoE)2x(Rev)1 lines, Case:(Obv)5x(LoE)2x(Rev)1 lines
1	subgenre_remarks	Receipt; case:seal impressions on all sides; Tablet:(Obv)5x(Rev)3 lines, Case:(Obv)5x(Rev)4 lines
1	subgenre_remarks	Receipt; case:seal impressions on all sides; Tablet:Tablet frag, (Obv)3x(LoE)3x(Rev)3x(UE)1 lines, Case:(Obv)4x(LoE)3x(Rev)3 lines
1	subgenre_remarks	Receipt; case:seal impressions on all the sides; Tablet:(Obv)4x(LoE)1x(Rev)3 lines, Case:(Obv)5x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Receipt; case:seal impressions on all the sides; Tablet:(Obv)4x(LoE)2x(Rev)2 lines, Case:(Obv)4x(LoE)2x(Rev)4 lines
1	subgenre_remarks	Receipt; case:seal impressions on all the sides; Tablet:(Obv)4x(LoE)2x(Rev)3 lines, Case:(Obv)5x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Receipt; case:seal impressions on all the sides; Tablet:(Obv)4x(LoE)3x(Rev)3x(UE)1 lines, Case:(Obv)5x(LoE)2x(Rev)4 lines
1	subgenre_remarks	Receipt; flour; seals; 4x1 line
1	subgenre_remarks	Receipt; mu us-sa bad is-ku-da/d.ba-zi x mu-us-sa-bi; seal
1	subgenre_remarks	Receipt; mu-us-sa dUr-Ninurta lugal-e urudu-alan-mah en-lil-ra mu-na-dim; seals; 6x4 lines
1	subgenre_remarks	Receipt; seal impr on envelope; tabl 4x1x3x1(u.e.) lines; case 4x2x2(rev) lines
1	subgenre_remarks	Receipt; seal impressions all over the surfaces; tablet:(Obv)5x(loE)2x(Rev)3 lines, case:(Obv)5x(LoE)2x(Rev)4 lines
1	subgenre_remarks	Receipt; seal of AmarSin king of Ur; 4 lines
1	subgenre_remarks	Receipt; seal: Inim-∂Inanna àga-uå lugal (CBT 2)
1	subgenre_remarks	Receipt; seal; 4 lines
1	subgenre_remarks	Receipt; seal; 4x3 lines
1	subgenre_remarks	Receipt; seal; 5 lines
1	subgenre_remarks	Receipt; seal; 5 lines; 4.2x3.6
1	subgenre_remarks	Receipt; seal; 5x4x1 line
1	subgenre_remarks	Receipt; seal; 6x5x1 lines
1	subgenre_remarks	Receipt; seal; not Nippur calendar
1	subgenre_remarks	Receipt; seal;4 lines
1	subgenre_remarks	Receipt; sealed (CBT 2)
1	subgenre_remarks	Receipt; seals; 4x1x3 lines
1	subgenre_remarks	Receipt; seals; 5 lines
1	subgenre_remarks	Receipt; seals; 5x3 lines
1	subgenre_remarks	Receipt; seals; 6x6x2(u.e.) lines; mu Bur-Sin lugal-e ki-aga en-lil-la su-nir gal ku-gi inim-bi .....
1	subgenre_remarks	Receipt; seals; mu bad3-x-a-x; 5x3 lines
1	subgenre_remarks	Receipt; w/seal impression; (Obv)4x(Rev)4 lines
1	subgenre_remarks	Receipt?; seal; 4 lines
1	subgenre_remarks	Receipt?; seal; Drehem calendar; 1x1 line
1	subgenre_remarks	Receipt?; seals; 3x2 lines
1	subgenre_remarks	Receipt?; seals; 5 lines
1	subgenre_remarks	Receipt?; seals; 6x3x1(u.e.)x1(le.e.) lines
1	subgenre_remarks	Reciept of ku-mah; w/seal impressions; (Obv)6x(Rev)1 lines
1	subgenre_remarks	Record of 1 guruå-worker who died on the ffield and was handed over yo be carried away. / Case: Text same as on tablet. Seal on case.
1	subgenre_remarks	Record of 1 male worker who has to tow a ship loaded with barley to Nippur. Seal: Bi2-du11-ga ds d. La-a-åa6
1	subgenre_remarks	Record of 1 woman-day who has worked in the cleaning of furrows. Seal: Ur-{d}[...] ugula [kikken [...].
1	subgenre_remarks	Record of 10 male workers who have worked with emmer and barley in the field of Guedena. Seal: Lum-ma ds d. Lu2-{d}Nin-åubur.
1	subgenre_remarks	Record of 122 woman-days who have done irrigation works in Apisal. Seal: Ur-{d}Åara2 ds d. Lugal-nanga2 nu-banda3-gu4 {d}Åara2.
1	subgenre_remarks	Record of 20 royal gur of barley issued by Ad-da to porters as food for calves. / Case: text corresponding to that on tablet. Seal on case. (CBT 1)
1	subgenre_remarks	Record of 20 women who have been in service for irrigation works. Seal: Ur-{d}TUG2.AN-ka ds d. Ur-{d}Nin-su sa12-du5-ka.
1	subgenre_remarks	Record of 3 workers for 10 days. Seal: illegible (2 lines).
1	subgenre_remarks	Record of 40 women who have carried barley and emmer from Kian to Umma. Seal: Ab-ba-gi-na ds d. Lugal-ma2-gur8-re.
1	subgenre_remarks	Record of 5 male workers who have been in service in kun-zi-da-canals. Seal: Ur-e11-e ds d. Ur-ni9-gar.
1	subgenre_remarks	Record of 50 male workers who have threshed emmer. Seal: Ur-[dun] ds d. Da-da
1	subgenre_remarks	Record of 72 giå.éme-rín-hi-a 18 giå.ù-suh5 mar-sa-åè; case unopened; kiåib Ur-mes; seal: Lú-∂[]-na dubsar dumu [] (CBT 2)
1	subgenre_remarks	Record of 8 workers who have loaded barley in a boat and sailed downstream. Seal: Arad2-mu ds d. Ur-ni9-[gar (kuå7)].
1	subgenre_remarks	Record of 9 male workers who have cut reeds in the field of Lugal.EN.ZU? Seal: Ur-e2-an-na ds d. Bar-ra-an.
1	subgenre_remarks	Record of UN.IL2 who have worked on earth piling. Seal: Ur-{d}TUG2.AN-ka ds d. Ur-{d}Nin-su sa12-du5.
1	subgenre_remarks	Record of a deficit; seal; 4x3 lines
1	subgenre_remarks	Record of a payment of grain; seal impressions on all the sides; (Obv)5x(Rev)1 lines
1	subgenre_remarks	Record of an official's salary; seal impressions on all the sides; (Obv)4x(LoE)1x(Rev)3 lines
1	subgenre_remarks	Record of asses brought in as a-ru-a gifts by various persons (CBT 2). A: Case of 17797; seal ∂Nin-MAR.KI-[ka] sipa? dumu Nam-ha-ni (CBT 2)
1	subgenre_remarks	Record of dates delivered to the palace. / Case: Text of tablet abbreviated. Seal on case. (CBT 1)
1	subgenre_remarks	Record of debt w/promissory condition; seal impressions on Obv,LE,RE.&Rev.; (Obv)5x(LoE)2x(Rev)4 lines
1	subgenre_remarks	Record of deliveries of figs and dates; seal: Lú-[ ] dubsar dumu Nam-mah? (CBT 2)
1	subgenre_remarks	Record of down payment for a house; seal.  9x3 lines
1	subgenre_remarks	Record of hired workers who have drawn earth from a canal. Seal: Lugal-e2-mah-e ds d. Lugal-ku3-ga-ni.
1	subgenre_remarks	Record of kinds of beer; Seal impressions all over the surfaces; (Obv)4x(Rev)7 lines
1	subgenre_remarks	Record of male workers (guruå UN.IL2) assigned to the granary of sahar-ú-ú. Seal: Lu2-dingir-ra ds d. Da-da-a.
1	subgenre_remarks	Record of male workers who have carried reeds, received from Dada. Seal: illegible (3 lines).
1	subgenre_remarks	Record of male workers who have loaded flour in a ship. Seal: Ur-∂Nin-su ds d. Ur-e2-nun-na.
1	subgenre_remarks	Record of male workers who have towed rafts to Nippur. Seal: Unken-ne2 ds d. Ur-{giå}gigir.
1	subgenre_remarks	Record of payments; seal impressions Obv,LoE,LoE.& UE; (Obv)5x(Rev)5x(UE)1 lines
1	subgenre_remarks	Record of rations for workmen (guruå); åe ur5-ra dumu-dab5-ba-åè; case unopened; seal: I-åar-ì-lí dumu ¨-a-a); in the text i-åa-ÍI-ì-lum (CBT 2)
1	subgenre_remarks	Record of small numbers of 4 kinds of goats, the a-ru-a gift of Sag-Nin-e-zu s. of Ur-GÁ-da gudú, which [NN.] took over from An-ni-ba-du7. / Case: Text corresponding to ll. 3-8 of tablet, name of recipient ending in ...gi4. Seal on case. (CBT 1)
1	subgenre_remarks	Record of wool; seal: Lú-∂Ba-ba6 dubsar dumu ∂Utu-bar-ra [sanga] (CBT 2)
1	subgenre_remarks	Record of workers (UN.IL2) who have ... mun-gazi and plastered a house. Seal: Lu2-du10-[ga ...] / dumu Ur-{d}[...].
1	subgenre_remarks	Redemption document of the fatherly house; (Obv)15x(Rev)13 lines, seal impressions on Rev.& 4 edges.
1	subgenre_remarks	Reed bundles from Mansum to Urguenna, ga-gi4 síg-kur-shè; seal: Ur-gú-en-na ds d. Lú-dingir-ra.
1	subgenre_remarks	Reed bundles from Ur-Baba to Kitushlu; seal dedicated to SHulgi, Ki-tush-lú ds d. Lú-[] 
1	subgenre_remarks	Reed for baskets from Mansum to Ur-sha6-ga; seal: Ur-sha6-ga ds d. Ur-d[Nin-X]
1	subgenre_remarks	Reed from Abba to Lú-dInanna; seal: Lú-dInanna d. Lú-na-rú-a
1	subgenre_remarks	Reed from the field en-gaba-rá; from I3-kal-la to Lú-dingir-ra shà bala-a; seal: Lú-dingir-ra ds d. []
1	subgenre_remarks	Reed from the store from Mansi (gá-nun-ta); case unopened; seal: Lugal-ki-gal-la dubsar dumu Lú-∂Ba-ba6; Shulgi 45/Amar-Suen 2 (CBT 2)
1	subgenre_remarks	Reed mat (gi kid åú) for the boat of Urkisal, received by Lu-Ningirsu, [seal] (CBT 2)
1	subgenre_remarks	Reed mat for a boat (kid má) from Ludingirra to Lugal-uåime the guzala; seal: Lugal-ú-åim-e dumu Ab-ba-[åa6-ga] (CBT 2)
1	subgenre_remarks	Reed mat for boats received by Akalla; seal illegible (CBT 2)
1	subgenre_remarks	Reed má ì-zú-lum-ka dù-dè gá-nun-gish-ta; [seal].
1	subgenre_remarks	Reed workers, carpenters ki  giå-ì-gub-ba Lú-∂Nin-gír-su in the gú-eden; seal: Íà-kù-ge dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Regular deliveries of barley to the ensi from Baddari to Íeå-åeå; case unopened; seal: Íeå-åeå dumu NI-NI lú-ùr-ra (CBT 2)
1	subgenre_remarks	Regular deliveries of beer for the shabra, sískur má-gur8, in Ur; seal: Ur-dNin-shubur dumu [] ir11 Ur-[]
1	subgenre_remarks	Regular delivery of flour; seal illegible (CBT 2)
1	subgenre_remarks	Regular delivery of reed, sa-gi-shid; sá-du11 ku5 dBa-ba6-ta gá-nun-gish-ta gi-gibil-lá má-uz-lugal-shè.seal: Ab-ba-mu d. Ur-é-an-na
1	subgenre_remarks	Remainder of an account of barley of Ur-Ningiszida (åe si-ì-tum nì-ka9-ak); case unopened; seal: Ur-∂Nin-gis-zi-da dubsar dumu Ur-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Remainder of an account of barley transferred from Íeå-kal-la to Nì-∂Ba-ba6 son of Atu; seal: Nì-∂Ba-ba6 dumu Atu lú kaå? (CBT 2)
1	subgenre_remarks	Remainder of an account of fish, to be returned, from Gudea to Allagula (CBT 2). A: Case of 19510; seal: Al-la-gu-la dubsar dumu Al-ba-ni-dudu11 (CBT 2)
1	subgenre_remarks	Remainder of an account of small cattle to be returned by Lú-∂Nin-åubur; unopened envelope; seal: Lú-∂Nin-åubur dumu KA-NA; Shulgi 48 - Amar-Suen 1 (CBT 2)
1	subgenre_remarks	Remainder of barley, yield for the year Ad 24; seals. 13 lines
1	subgenre_remarks	Remainder of fine beer, passing from Abbashaga to Lu-dingirra, mu dNin-gír-su-ì-mah-shè; seal: Lú-dingir-ra ds d []
1	subgenre_remarks	Remainder of flour transferred from Akalla to Urguenna; seal: Ur-∂Nanåe dubsar dumu Lú-dingir-ra (CBT 2)
1	subgenre_remarks	Remainder of the account of fish from Gudea to Udeniåaga; to be returned; case unopened; seal: Ur-∂Nin-MAR.KI dubsar dumu Lú-∂Nanna (CBT 2)
1	subgenre_remarks	Remainder of the barley account of Urtur dumu å-na-mu; case unopened; seal: Ur-tur dubsar dumu Lú-∂Nin-gír-su (CBT 2)
1	subgenre_remarks	Remainder of the goats account of Akalla; seal: A-a-kal-la ds d. Ur-dLama nu-bànda
1	subgenre_remarks	Rendering of accounts cncg.house-property; w/seal impressions; (Obv)15x(LoE)1x(Rev)12 lines
1	subgenre_remarks	Rent of a field; (Obv)12x(Rev)12 lines, seal impressions on Obv, Rev, UE.& LE.
1	subgenre_remarks	Rent of a house; (Obv)7x(Rev)6 lines, seal impressions on all the surfaces.
1	subgenre_remarks	Rental of a field for cultivation; seals; 7x2x8x4 lines; 5.8x4.2x19 cm
1	subgenre_remarks	Rental of a field for cultivation; seals; 7x7x3(u.e.) lines; 5.6x4x2.2 cm
1	subgenre_remarks	Rental of a field; seal; 9x8 lines; 6.1x4.4
1	subgenre_remarks	Rental of a field; seals; 10x10 lines
1	subgenre_remarks	Rental of a field; seals; 9x1x6x1(le.e) lines
1	subgenre_remarks	Rental of a field; seals; 9x9 lines; 6.2x4.6x2.4 cm
1	subgenre_remarks	Rental of a girru; Cf CAD G 93a; four seals; 6x2x6x3 lines
1	subgenre_remarks	Rental of a house to be devoted to the temple; seals; 9x3x11x1(u.e.)x2(le.e) lines
1	subgenre_remarks	Rental of a house; PN1 rents a house to PN2 for an annual rent of 1/4 shekel of silver; witnesses; stone seals; 8x7 lines; 5.9x3.6
1	subgenre_remarks	Rental of field for sesame cultivation; seals; 12x4 lines
1	subgenre_remarks	Rental of oxen; Murashu archive; seals; 9x9 lines; 87x67x26mm.
1	subgenre_remarks	Rental of sheep and goats; seal & nail impressions, Aramic docket, (Obv)20x(Rev)14 lines, 9x10.3x3.05
1	subgenre_remarks	Rental of the journey of the divine weapon; cf CBS 24; seals; Sippar; 6x5x1 line
1	subgenre_remarks	Rental of the journey of the divine weapon; cf. Harris AS 16, pp. 217 ff.; 8x8x2 lines; seal impressions all over the surfaces;
1	subgenre_remarks	Rental of the journey of the divine weapon; seals; 12x2 lines
1	subgenre_remarks	Rental; seals; labels; 4x2 lines
1	subgenre_remarks	Rest of the barley account of Ur-badtibirra; seal: Urmes má-lah4 d. Ur-Ma-ma.
1	subgenre_remarks	Returned goat; 1 másh lá-ni su-ga ki Na-ba-sha6-ta kishib Ab-ba-kal-la, gìr Lú-nam-tar-ra gu-za-lá; seal: Ab-ba-kal-la gudu4 d. Lugal-du10-ga gudu4 dNanshe-kam
1	subgenre_remarks	Returney barley from Ur-Enlilla to Ur-dNanshe, érin gi-gibil-lá-me; seal: Ur-dNanshe ds d. Al-la.
1	subgenre_remarks	Rev. seal impressions; Copy (Varchieft).???????; 4 lines
1	subgenre_remarks	Reverse of another tablet; seal: dUtu-mu ugula lú-dab5-ba d. Lú-dBa-ba6
1	subgenre_remarks	Royal expenditure; case unopened; seal: Ur-ni9-gar dubsar dumu[] (CBT 2)
1	subgenre_remarks	SHe gish-ì for seed from Ur-abba to Aabba; seal: A-ab-ba d. Ur-ni9-gar
1	subgenre_remarks	SHim 3 dug-kam, shim ì-zag-ga dBa-ba6 from Nì-ga the merchant; [seal].
1	subgenre_remarks	SHim from A-gi4 to Inim-dBa-ba6-ì-dab5; seal: Géme-dLama nin-dingir dBa-ba6 Inim-dBa-ba6-ì-dab5 rá-gaba ir11-zu
1	subgenre_remarks	SHim, hi-li, ésir é-duru5 kash-ú-sa-a-da kash é-ab-ba-tag from Ur-guenna to Ninana; seal: Lú-dNin-gír-su ds d. Ur-é-ninnu.
1	subgenre_remarks	SHim, she-li, ésir-é-a from Ur-gú-en-na to Ur-dNanshe; seal Ur-dNanshe ds d. Ur-é-an-na
1	subgenre_remarks	SHà-bi-ta tablet about barley for satukkus, donkeys and ú-íl; top broken;seal: dDumu-zi dushumgal-an-na dLugal-URUxKAR2 Lú-dGírim dub-sar d. [] ugula []; second piece in the box not from the same tablet
1	subgenre_remarks	SM catalogue: Ur-šulpae provides silver; tablet/seal of the ensi
1	subgenre_remarks	SM catalogue: Zadok: house sale; first witness is palace scribe, followed by several judges; copy of the deed; original was extensively sealed (by buyer, palace scribe, judges, and scribe); included nail marks of at least the sellers
1	subgenre_remarks	SM catalogue: Zadok: list of women, each preceded by "6 ma-na"; seal impressions on rev. of tanittu-bel and Bel-kisir
1	subgenre_remarks	SM catalogue: about 18 shekels of silver enter into the palace, seal of the ensi
1	subgenre_remarks	SM catalogue: asst. animals ša PNN maru/marutu. some notes concerning unsealed transactions
1	subgenre_remarks	SM catalogue: black clay tablet with three seal impression on reverse. this is an adoption text in which Šelwahu, son of Ipshahalu adopts Akuya, son of Katiri
1	subgenre_remarks	SM catalogue: expenditure (zi-ga) of something, sealed by the ensi2
1	subgenre_remarks	SM catalogue: expenditure of 4 goats, sealed by a shepherd of the nakabtum
1	subgenre_remarks	SM catalogue: expenditure of a sheep. sealed with a seal dedicated to Šu-Suen
1	subgenre_remarks	SM catalogue: expenditure of bread written over sealings. 
1	subgenre_remarks	SM catalogue: expenditure of one ox; sealed with a seal dedicated to the king
1	subgenre_remarks	SM catalogue: expenditure of sheep for the goddesses ninlil and Inanna on the occasion of the eš3-eš3 festival. tablet is large and sealed
1	subgenre_remarks	SM catalogue: fake of old assyrian sealed tablet 
1	subgenre_remarks	SM catalogue: fake old assyrian sealed tablet 
1	subgenre_remarks	SM catalogue: fragment of a sealed envelope. 
1	subgenre_remarks	SM catalogue: fragment, only part of a seal extant
1	subgenre_remarks	SM catalogue: half of a sealed docket (uninscribed)
1	subgenre_remarks	SM catalogue: hollow egg shaped bulla that contained 48 little stones. the text is an account of animals entrusted to a shepherd. 
1	subgenre_remarks	SM catalogue: large sealed tablet--3 sheep and a female kid become an offering (sizkur2)
1	subgenre_remarks	SM catalogue: late achaem. in view of the several seal-impressions; damaged deed concerning barley and dates. witnessed tablet. 
1	subgenre_remarks	SM catalogue: list of men and their seals
1	subgenre_remarks	SM catalogue: list of women's names and men's seals
1	subgenre_remarks	SM catalogue: missing. accession book describes it : "3rd dynasty of ur tablet (in case). ibkua son of haraqum (cf. seal) has received 10 shekels of silver at interest from guratum." the tablet was present in 1962 but is now unaccounted for
1	subgenre_remarks	SM catalogue: one fattened ox is a delivery. seal of Ur-šulpae
1	subgenre_remarks	SM catalogue: piece of clay in tablet shape which was sealed by ilum-bani but never inscribed
1	subgenre_remarks	SM catalogue: receipt of a fattened lamb, sealed by the royal cook
1	subgenre_remarks	SM catalogue: receipt of a grain, which is a loan with interest imposed. seal of išme-ilum, son of zu-ti; seal is anomalous for an Ur III tablet. is this tablet from Nippur? 
1	subgenre_remarks	SM catalogue: receipt of dates. tablet in sealed envelope. 
1	subgenre_remarks	SM catalogue: receipt of grain sealed by the šabra-official
1	subgenre_remarks	SM catalogue: receipt of grain written over seal impressions
1	subgenre_remarks	SM catalogue: receipt of sheep and goats; seal of urkugnunna
1	subgenre_remarks	SM catalogue: receipt. signs are obscured by sealing
1	subgenre_remarks	SM catalogue: seal and personal names extant
1	subgenre_remarks	SM catalogue: sealed docket of expenditures from the office of Abasaga
1	subgenre_remarks	SM catalogue: sealed docket with seal dedicated to amar-sin
1	subgenre_remarks	SM catalogue: sealed receipt for ga-ar3--cheese curds
1	subgenre_remarks	SM catalogue: sealed tablet--an ox is called šu-gid2
1	subgenre_remarks	SM catalogue: sealed tablet--receipt of fattened sheep
1	subgenre_remarks	SM catalogue: sealed tablet. a PN's delivery is "šu bar-ra"--released? seal is of the išib priest
1	subgenre_remarks	SM catalogue: sealed tablet: a list of mountain-sheep with fleece that died. (ri-ri-ga). 
1	subgenre_remarks	SM catalogue: sealed tablet: a person named huwawa receives a har.ab stone and ... 
1	subgenre_remarks	SM catalogue: sealed tablet: cattle, sheep & goats are a kaš-de2-a offering
1	subgenre_remarks	SM catalogue: sealed tablet: conveyance of various sheep and goats in ur
1	subgenre_remarks	SM catalogue: sealed tablet: dugga /urkugnunna (his brother) receive fattened animals
1	subgenre_remarks	SM catalogue: sealed tablet: expenditure of animals
1	subgenre_remarks	SM catalogue: sealed tablet: expenditure of close to 40 sheep/ goats
1	subgenre_remarks	SM catalogue: sealed tablet: expenditure of livestock on various days, received by dugga
1	subgenre_remarks	SM catalogue: sealed tablet: expenditure of sheep & goats
1	subgenre_remarks	SM catalogue: sealed tablet: fattened sheep are a a 'regular offering' (sa2-du11)
1	subgenre_remarks	SM catalogue: sealed tablet: goats are transferred between a Drehem official and a fattener
1	subgenre_remarks	SM catalogue: sealed tablet: leather (?) and reeds for cattle are the excess of the accounting
1	subgenre_remarks	SM catalogue: sealed tablet: legal document about the sale of a female slave with witnesses
1	subgenre_remarks	SM catalogue: sealed tablet: list of guruš workers who are transporting items on a boat
1	subgenre_remarks	SM catalogue: sealed tablet: list of sheep & goats received by abbakalla son of lu-Ningirsu
1	subgenre_remarks	SM catalogue: sealed tablet: list of sheep and the people who conveyed them
1	subgenre_remarks	SM catalogue: sealed tablet: loan of silver with no interest imposed. 
1	subgenre_remarks	SM catalogue: sealed tablet: one sheep is a delivery for a mašdaria offering
1	subgenre_remarks	SM catalogue: sealed tablet: oxen are called šu-gid2
1	subgenre_remarks	SM catalogue: sealed tablet: oxen are slaughtered for the kitchen for the men getting šuku-rations
1	subgenre_remarks	SM catalogue: sealed tablet: quantities of dates over a period of several years
1	subgenre_remarks	SM catalogue: sealed tablet: rations of grain for the new year are distributed to named men
1	subgenre_remarks	SM catalogue: sealed tablet: receipt for beer? or oxen of ok quality (us2-sa) at a rate of 1 ban2 and 5 silas
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of 4 lambs(?)
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of 42 sheep/goats
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of a grass-fed ox. 
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of a lamb
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of a quantity of ni.gal (?) destined to ka-id2-[da]
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of an ox
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of animals
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of goats
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of goats, seal of urkugnunna
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of lambs
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of sheep and goats over several days
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of two goats
1	subgenre_remarks	SM catalogue: sealed tablet: receipt of wool
1	subgenre_remarks	SM catalogue: sealed tablet: sheep are šu-gid2 and are taken in charge
1	subgenre_remarks	SM catalogue: sealed tablet: the receipt of grain for workers' wages is witnessed
1	subgenre_remarks	SM catalogue: sealed tablet: the transfer of over 2 gur of bran is called ša3-bala-a
1	subgenre_remarks	SM catalogue: sealed tablet: transfer of manu-wood is called ša3-bala-a
1	subgenre_remarks	SM catalogue: sealed tablet: transfer of sheep/goats
1	subgenre_remarks	SM catalogue: sealed tablet: transfer of sheep/goats between two Drehem officials
1	subgenre_remarks	SM catalogue: sealed tablet: urkugnunna receives 2 fattened sheep
1	subgenre_remarks	SM catalogue: sealed tablet: urkugnunna receives 39 animals
1	subgenre_remarks	SM catalogue: sealed tablet: urkugnunna receives lambs and goats
1	subgenre_remarks	SM catalogue: sealed tablet: urkugnunna receives oxen. seal or urkugnunna (arad2-zu type)
1	subgenre_remarks	SM catalogue: sealed tablet; receipt of 10 sheep
1	subgenre_remarks	SM catalogue: tablet basket tag for sealed documents from shepherds in Girsu
1	subgenre_remarks	SM catalogue: tablet with sealed envelope stuck to the obverse. receipt of grain in an intercalary month
1	subgenre_remarks	SM catalogue: tablet within sealed case. sealings on obv. and rev
1	subgenre_remarks	SM catalogue: text about the distribution of oxen for cultic purposes written over sealings
1	subgenre_remarks	SM catalogue: unbroken env.--dispersal of grain and emmer; sealed by the servant of the ereš-dingir-priestess of bau. 
1	subgenre_remarks	SM catalogue: unbroken env.--grain is taken by a merchant, sealed by a šabra-priest
1	subgenre_remarks	SM catalogue: unbroken env.--grain, a loan to erin2-workers is received; sealed by the secretary of the runner ? (sukkal kas4)--this man occurs also in hsm 6203 = 1909.5.39
1	subgenre_remarks	SM catalogue: unbroken env.--receipt of grain sealed by a sukkal kas4--secretary of a runner?
1	subgenre_remarks	SM catalogue: unbroken env.--receipt of grain, balance payable (la2-ia3 su-ga), sealed by the granary supervisor (ka-guru7)
1	subgenre_remarks	SM catalogue: unbroken env.--seed grain received, sealed by the granary supervisor (ka-guru7)
1	subgenre_remarks	SM catalogue: unbroken, sealed envelope: receipt of grain from two different fields in different months for a regular offering
1	subgenre_remarks	SM catalogue: unbroken, sealed tablet. grain rations for geme2
1	subgenre_remarks	SM catalogue: unopened envelope: old equids are received by a kennelman, whose seal is dedicated to the king Šulgi. 
1	subgenre_remarks	Sale contract; seals; 7x2x8x1 line
1	subgenre_remarks	Sale of 4 1/2 gana of a field for 4 1/2 shek. of silver; seals; envelope = N 1147-N 1165a; 11x10 lines
1	subgenre_remarks	Sale of a field; seals; 10x10 lines
1	subgenre_remarks	Sale of a field; seals; 7 lines
1	subgenre_remarks	Sale of a field; seals; Date: mu bad3-ma3 za.ri.ki; 14x2 lines
1	subgenre_remarks	Sale of a field; witnesses; case = Ni. 9254; seals; 16x18 lines
1	subgenre_remarks	Sale of a house plot; PN1 and PN2 sell a 1 2/3 sar house plot and a 1 sar kislah plot to PN3 and PN4 for  8 shekels of silver; witnesses; bur-gul seal; 16x11 lines; 9.7x5.4
1	subgenre_remarks	Sale of a house; seal; 5x6 lines
1	subgenre_remarks	Sale of a house; seals; 10x3 lines
1	subgenre_remarks	Sale of a house; seals; 3x3 lines
1	subgenre_remarks	Sale of a house; witnesses; seals15x9 lines
1	subgenre_remarks	Sale of a temple office for two months; seals; 11x13 lines
1	subgenre_remarks	Sale of a temple office; witnesses; seals; 13x13 lines
1	subgenre_remarks	Sale of an orchard; PN1 and PN2 sell a 9 sar 3 2/3 gin 15 she plot in the nanga orchard; witnesses; bur-gul seal; 9x9 lines; 6.3x5.2
1	subgenre_remarks	Sale of an orchard; seals; 11x8 lines
1	subgenre_remarks	Sale of e2-du-a; seal; 15x13 lines; 9.5x6.0
1	subgenre_remarks	Sale of e2-du-a; seal; 18x7 lines; 8.4x5.7
1	subgenre_remarks	Sale of field; seals; 7x8 lines
1	subgenre_remarks	Sale of grain; four seals; 8x9 lines; loan of silver to buy barley to be repaid in barley
1	subgenre_remarks	Sale of house; seal impressions on tablet & case; tablet (Obv)14x(Rev)16x(UE)3 lines, case (Obv)17x(Rev)19 lines
1	subgenre_remarks	Sale of rights in a temple; Seal impressions; (Obv)12x(Rev)13x(UE)4 lines
1	subgenre_remarks	Sale of temple office; PN1 and PN2 sell 3 or 4 offices in Lugal9aba0 and Ab-ku3-mah temples for  22 1/2 days each to PN3 for 5 1/3 shekels of silver; witnesses; bur-gul seal of sellers; 8.4x5.0cm, ?x?cm
1	subgenre_remarks	Sale of temple office; PN1 and PN2 sell 5 offices in the Shamash temple for 5 days each to PN3 for 8 1/2 shekels of silver; witnesses; bur-gul seal of sellers; 8.7x5.2cm, 10x6.7cm
1	subgenre_remarks	Sale of temple office; PN1 sells 2 or more offices in the Nuska temple with their prebend field for 5 days each to PN 2 for 10 1/2 shekels of silver; witnesses; bur-gul seal of seller; 11.6x6.7, 12.3x6.3
1	subgenre_remarks	Sale of temple office; PN1 sells 6 offices in the Shamash temple for 10 days each to PN2 for 7 1/2 shekels of silver; witnesses; bur-gul seal of seller; 7.7x4.8cm, 9.5x6.3cm
1	subgenre_remarks	Sale of temple office; PN1 sells 6 offices in the Shamash temple for 5 days each to PN 3 for 6 shekels of silver; witnesses bur-gul seal of the seller; 7.4x5.0cm
1	subgenre_remarks	Sale of temple office; PN1 sells 6 offices in the Shamash temple for 5 days each to PN2 for 9 1/2 shekels of silver; witnesses; bur-gul seal of seller; 8.7x5.2, 10.0x6.8
1	subgenre_remarks	Sale of temple office; PN1 sells offices for 15 days each to PN2 for 1/3 mina 5 shekels of silver; witnesses; bur-gul seal of seller; 8.8x5.2cm
1	subgenre_remarks	Sale of temple offices; PN1 and PN2 sell 5 offices in the Lugal-aba temple for 20 days each to PN3 for 11 1/2 shekels of silver. witnesses; bur-gul seal of sellers; 8.8x4.8cm, 9.0x5.8cm
1	subgenre_remarks	Sale of undeveloped land; seal; envelope = N 1234; 10x11x4 lines; Sale of a courtyard for silver; date: mu d-En-lil-[bani lugal-e] eren2 dumu i3-si-in-ki-na su in-ne-bar; seals; 7 lines"
1	subgenre_remarks	Sale or Rental of a field; witnesses; seals; date: mu d-i-te-ni-ka()-se-sa li-ab(d-Samas-ra na-mu
1	subgenre_remarks	Sale; concerning silver; seals; 4x4 lines
1	subgenre_remarks	Sale; seal; 5x4 lines; 8.9x5.8
1	subgenre_remarks	Sale; seals; 8x4 lines
1	subgenre_remarks	Sale; witnesses; seals; 7x9 lines
1	subgenre_remarks	Sale? of a field; seals; 8 lines
1	subgenre_remarks	Sale?; concerns 2 offices and an 8 1/2 gan2 orchard plot, the inheritance of PN; witnesses; bur-gul seal; 9x12 lines; 6.2x4.7
1	subgenre_remarks	Sass. Uninscribed bulla with impression of four stamp seals
1	subgenre_remarks	Seal impr
1	subgenre_remarks	Seal impr on l.e. and lo.e; 7x2x8 lines
1	subgenre_remarks	Seal impr on obv; 6x1x6 lines
1	subgenre_remarks	Seal impr on rev; 8x1x6x1 lines
1	subgenre_remarks	Seal impr on u.e.; 10x2x7 lines
1	subgenre_remarks	Seal impr. lo. e. and le. e.; 3x5(rev) lines
1	subgenre_remarks	Seal impr. on case; tablet 5x2x5x1(u.e.) lines; case 6x2x4x1(u.e.) lines
1	subgenre_remarks	Seal impr; 7x8x2(u.e.) lines
1	subgenre_remarks	Seal impression (but Kassite? PBS 14, 266 classifies as Guti-Gudea period)
1	subgenre_remarks	Seal impression A-buili? warad Enlil""
1	subgenre_remarks	Seal impression all over the surfaces; (Obv)6x(LoE)2x(Rev)4x(UE)1 lines
1	subgenre_remarks	Seal impression on all over the surfaces (Second Kassite style); (Obv)4x(Rev)4 lines
1	subgenre_remarks	Seal impression on tablet & case; (Obv)13x(Rev)13 lines
1	subgenre_remarks	Seal impression only (Ur3 or OB)
1	subgenre_remarks	Seal impression only; 3 lines; 2.2x3.0
1	subgenre_remarks	Seal impression.  Thumb nail impressions.  5 fragments joined.
1	subgenre_remarks	Seal impression; (Obv)5x(Rev)5 lines
1	subgenre_remarks	Seal impressions & signatures on Rev.,UE.,LoE.&LE., (Obv)12x(LoE)1x(lines)7 lines, thumb mark, 6.6x8.6x3.15
1	subgenre_remarks	Seal impressions (Pseudo-Kassite style?)
1	subgenre_remarks	Seal impressions (case). 19x16 UE 1 lines
1	subgenre_remarks	Seal impressions (from the same seal as 6988)
1	subgenre_remarks	Seal impressions (lion); w/stringmarks
1	subgenre_remarks	Seal impressions (on case). 5x2x5 UE 2 lines
1	subgenre_remarks	Seal impressions (same seal as CBS 6746, 14262+, 14270, 14273a)
1	subgenre_remarks	Seal impressions all over the surfaces; (Obv)(i)33x(ii)37x(Rev)(iii)36x(iv)30 lines
1	subgenre_remarks	Seal impressions all over the surfaces; (Obv)11x(LoE)2x(Rev)9 lines
1	subgenre_remarks	Seal impressions all over the surfaces; (Obv)1x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Seal impressions all over the surfaces; (Obv)5x(Rev)4 lines
1	subgenre_remarks	Seal impressions all over the surfaces; (Obv)6x(LoE)1x(Rev)2 lines
1	subgenre_remarks	Seal impressions on LoE,UE.&LE.; (Obv)14x(Rev)15x(UE)1 lines
1	subgenre_remarks	Seal impressions on Obv,Rev,LE.&RE, (Obv)12x(Rev)9 lines
1	subgenre_remarks	Seal impressions on Obv,Rev.& RE.; (Obv)16x(LoE)3x(Rev)10x(UE)6 lines
1	subgenre_remarks	Seal impressions on R.E. & LoE. Obv.2 lines, LoE.1 line, Rev.2 lines.
1	subgenre_remarks	Seal impressions on Rev.& 4 edges, (Obv)5x(Rev)3 lines.
1	subgenre_remarks	Seal impressions on Rev.& edges; (Obv)5x(Rev)4 lines; *or 21?
1	subgenre_remarks	Seal impressions on UE, LoE,& LE.; (Obv)6x(Rev)2 lines
1	subgenre_remarks	Seal impressions on all over the surfaces; (Obv)12x(Rev)13x(UE)2 lines; 3 nailmarks on LE.
1	subgenre_remarks	Seal impressions on all over the surfaces; (Obv)13x(Rev)12x(UE)2 lines; *Cast made before opening of the case.
1	subgenre_remarks	Seal impressions on all over the surfaces; Case:(Obv)5x(LoE)3 lines
1	subgenre_remarks	Seal impressions on all the sides (same design as CBS3053; Second Kassite style)
1	subgenre_remarks	Seal impressions on all the sides; (Obv)3x(LoE)2x(Rev)3x(UE)2 lines
1	subgenre_remarks	Seal impressions on all the surfaces; (Obv)14x(LoE)1x(Rev)8x(RE)2 lines
1	subgenre_remarks	Seal impressions on edges, (Obv)13x(LoE)1x(Rev)9 lines, 7x6x2.5
1	subgenre_remarks	Seal impressions w/inscription
1	subgenre_remarks	Seal impressions w/inscription, same seal as 6743, 14262+, 14270, 14273a
1	subgenre_remarks	Seal impressions(OB) only
1	subgenre_remarks	Seal impressions. 12X2X10 UE2
1	subgenre_remarks	Seal impressions. 12X2X12 UE 2 lines
1	subgenre_remarks	Seal impressions. 12X3X9 lines
1	subgenre_remarks	Seal impressions. 14x3x14 UE 2 lines
1	subgenre_remarks	Seal impressions. 5X1X3 UE1 lines
1	subgenre_remarks	Seal impressions. 6X2X7 UE2 lines
1	subgenre_remarks	Seal impressions.12x2x4 lines
1	subgenre_remarks	Seal impressions; (Obv)13 lines
1	subgenre_remarks	Seal impressions; (Obv)13x(Rev)12 lines
1	subgenre_remarks	Seal impressions; (Obv)14x(Rev)12 lines
1	subgenre_remarks	Seal impressions; (Obv)21x(Rev)14 lines
1	subgenre_remarks	Seal impressions; (Obv)2x(Rev)1 lines
1	subgenre_remarks	Seal impressions; (Obv)7x(Rev)6 lines
1	subgenre_remarks	Seal impressions; (Obv)8x(LoE)2x(Rev)7x(LE)2 lines
1	subgenre_remarks	Seal impressions; 2 lines
1	subgenre_remarks	Seal impressions; 3 lines
1	subgenre_remarks	Seal imprs
1	subgenre_remarks	Seal imprs; inside traces of cords
1	subgenre_remarks	Seal inscribed "Pukushum, son of Hu-..., servant of Ishkur."    Pushukum received a goat from Ba'agi.
1	subgenre_remarks	Seal inscription
1	subgenre_remarks	Seal legend, possibly belonging to the scribe Murish
1	subgenre_remarks	Seal of Nur-beli, son of Urnamish, servant of Utsi-nawir
1	subgenre_remarks	Seal of Sin-eribam, son of Sin-ennam, servant of Manium; cf.for Manium, Simmons JCS 14 pp.79-84, 87.
1	subgenre_remarks	Seal only: Ur-ba-gár dubsar dumu Lú-igi-åa6-åa6 ka-gur7 ∂Nin-MAR.KI-ka (CBT 2)
1	subgenre_remarks	Seal: Eren-da [] sagi; fragment of case (CBT 2)
1	subgenre_remarks	Seal: Ur-sukkal dumu A-tu; fragment of case (CBT 2)
1	subgenre_remarks	Seal; 1 line
1	subgenre_remarks	Seal; 2 lines
1	subgenre_remarks	Seal; uninscribed
1	subgenre_remarks	Sealed bulla with legend of Ishar-mupi, the cupbearer
1	subgenre_remarks	Sealed bulla with legend of a scribe
1	subgenre_remarks	Sealed bulla with legend of a scribe, servant of Naram-Sin
1	subgenre_remarks	Sealed bulla with legend of the scribe Ahu--ahi
1	subgenre_remarks	Sealed bulla with remains of legend
1	subgenre_remarks	Sealed bulla, servant of Naram-Sin
1	subgenre_remarks	Sealed tablet #This tablet was stacked together with 99-15-365, so that the reverse of this tablet and the obverse of the other still fit together perfectly.  There is also a large lump of a third tablet still attached to the obverse of this one.#
1	subgenre_remarks	Sealed tablet regarding bales of reed, well preserved.#
1	subgenre_remarks	Seals and labels only
1	subgenre_remarks	Seals only; labels
1	subgenre_remarks	Seals15x2x11x2 lines; 8.8x5x2.55 cms
1	subgenre_remarks	Seals;
1	subgenre_remarks	Seals; 10x10 lines; 7.5x4.75x2.6 cm
1	subgenre_remarks	Seals; 10x9x3(u.e.) lines
1	subgenre_remarks	Seals; 11x1x10x1(u.e.); 8x4.8x2.6 cms
1	subgenre_remarks	Seals; 2 lines
1	subgenre_remarks	Seals; 3 lines
1	subgenre_remarks	Seals; 5x1 line
1	subgenre_remarks	Seals; 6x4x1(u.e.); 4.6x3.8x2.3 cms
1	subgenre_remarks	Seals; labels; 16x3x2(u.e.); 8.9x5.9x2.4 cms
1	subgenre_remarks	Security document; seal impression all over the surfaces; (Obv)6x(Rev)2 lines
1	subgenre_remarks	Seed barley from SHu-Eshtar to Lu-kirizal; seal: Lú-kiri4-zal ds d. Ur-dBa-ba6
1	subgenre_remarks	Seed barley transferred from Bazi to Lu-Lagaå; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe (CBT 2)
1	subgenre_remarks	Seed barley transferred from Enlil-ziåagal to Duggazida (CBT 2). A: Case of 18769; seal: Du11-ga-zi-da dubsar dumu Ur-åa6-ga sanga ∂Nin-gis-zi-da (CBT 2)
1	subgenre_remarks	Seed of barley a-shà ú-gír-shè ki Ur-dNanshe-ta mu Ab-ba-kal-la d. sanga URUxKAR2ki kishib Ur-dLama ì-dub a-shà mah-ta, mu-ús-sa mu-ús-sa-bi; seal Lú-d[] ds d.
1	subgenre_remarks	Seed ox taken in charge; seals; 5x2 lines
1	subgenre_remarks	Seed-barley from Bazi to Lugal-uru-da; seal: Lugal-uru-da sa12-du5 d. A2-zi-da sa12-du5
1	subgenre_remarks	Seed-barley from Bazi to Lú-bala-sha6-ga; seal: Lú-bala-sha6-ga ds d. Ur-dNin-gis-zi-da
1	subgenre_remarks	Seed-barley from Bazi to Ur-Ninmug; seal: Ur-dNin-mug ds d. Lú-dBa-ba6
1	subgenre_remarks	Seed-barley from SHu-Esh4-tár to Lú-Baba; seal Lú-dBa-ba6 ds d. Ur-shu-ga-lam-ma
1	subgenre_remarks	Seed-barley from SHu-Esh4-tár to Ur-tur; seal: Ur-ni9-gar ds d Ur-sha6-ga nu-bànda kurushda
1	subgenre_remarks	Seed-barley she-shukur-ra énsi received by Lú-gi-gun4; seal: Lú-dEN.ZU ds d. Ur-ba-gár
1	subgenre_remarks	Seed-corn from SHu-Esh4-tár to Ur-dDa-mu; seal: Ur-dDa-mu d. Ga-a
1	subgenre_remarks	Sheep and ma-sá-ab from the ensi; seal: Lú-me-lám ds d.[]
1	subgenre_remarks	Sheep fat taken in account by SHà-kù-ge, gishbad Má-ganki-shè, zú-lum sískur Má-ganki-shè; seal: SHa-kù-gi ds d. Ur-dNanshe.
1	subgenre_remarks	Sheep for the kitchen of the ensi in Ur; ›xU-shè; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu.
1	subgenre_remarks	Sheep from Ba-a to Ur-sag-ùbaki; seal: Ur-sag-ùbaki d. Da-ti-e? sipa
1	subgenre_remarks	Sheep from Bahar to Lu-Lagaå; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe nu-nànda (CBT 2)
1	subgenre_remarks	Sheep from Ilum-ma to A-gu-a; seal: Lú-dBa-ba6 ds d. Ur-dNanshe
1	subgenre_remarks	Sheep from Lukalla to Ur-Lamma to be returned; seal: Ur-∂Lamma dubsar dumu Ur-∂[] (CBT 2)
1	subgenre_remarks	Sheep hides transferred from Ur-Damu to Ur-Lisi; seal: Ur-∂Li9-si4 dubsar dumu Ur-dun (CBT 2)
1	subgenre_remarks	Sheep transferred from Lugal-ki-gal-la to Lú-Lagaå˚; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe? blank line (CBT 2)
1	subgenre_remarks	Sheep withdrawn from Lugal-nám-mah; seal illegible
1	subgenre_remarks	Sheep åu-gíd received by Lú-Lagaå˚ from Gù-dé-a (CBT 2). A: Case of 16428; seal: Lú-Lagaå˚ dubsar dumu Si-dù nu-bànda [kuruåda], 16428a (CBT 2)
1	subgenre_remarks	Sheep, udu kab-lu-lu mu-túm; mu-ús-sa-a mu ús-sa-a-bi; seal: Ur-dAsar-lú-hi d. Ur-gu
1	subgenre_remarks	Sheep; udu gun-na Lú-du10-ga mu IS 2 sum-mu mu IS3 ì-til; kishib Ushmu; seal Ush-mu ds d. Lugal-sha6-ga
1	subgenre_remarks	Shorn sheep for the house of Urdun; seal: Lugal-nám-mah dubsar dumu Da-da; Shulgi 45/Amar-Suen 2 (CBT 2)
1	subgenre_remarks	Shu ba-an-ti; W/seal impression; 2 lines
1	subgenre_remarks	Side 1: 1 line, side 2: 2 lines.  Seal impressions on Side 1.
1	subgenre_remarks	Side 1: 2 lines, side 2:1 line & 2 labels?, seal impression.
1	subgenre_remarks	Side 1:1 line, side 2:seal impression.
1	subgenre_remarks	Side 1:2 lines, side 2:2 lines.  Seal impression.
1	subgenre_remarks	Side 1:3 lines, edge: 2 lines (labels?) & a seal impression.
1	subgenre_remarks	Side 1:4 lines.  Seal impression on Edge.
1	subgenre_remarks	Side 1:5 lines. Side 2:2 lines, a seal impression.
1	subgenre_remarks	Side 1:7 lines.  L.or R.E.:a seal impression.
1	subgenre_remarks	Side: 4 lines, edge?:1 line.  Seal impression on the side.
1	subgenre_remarks	Signature & seal impr on u.e.; 10x2x7 lines
1	subgenre_remarks	Silver and barley for the oxen on bala work; kishib ab-ba-mu shabra, seal: Ab-ba-mu ds d. nu-bànda sa12-du5
1	subgenre_remarks	Silver and barley from Lugal-shà-lá to Ur-Baba; seal: Géme-dLama nin-dingir-dBa-ba6 Ur-dBa-ba6 ds d. Ur-d[] ir11-zu.
1	subgenre_remarks	Silver as wages for 2 persons; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Silver for dUtu-bar-ra; 2 seals: Ur-ba-gár ds d. Ur-d[]; Ur-ba-gár ds d. Ur-sha6-ga di-ku5 Gú-ab-baki
1	subgenre_remarks	Silver from Balul to Lu-Enlil; seal: Lú-dEn-líl-lá d. Du-du (written Lú-líl-dEn-[lá].
1	subgenre_remarks	Silver from Dingirmu to Nì-ga for the bala; seal illegible.
1	subgenre_remarks	Silver from Lu-Utu to Ur-Dumuzi; seal: Lú-dDumu-zi d. Ma-ni sagi dGù-dé-a
1	subgenre_remarks	Silver from SHa6-sha6 to the ensi of Lagash, kù-uru-ta nu-è; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	Silver from SHesh-kal-la to Ur-dIg-alim; seal: Ur-dIg-alim ds d. Uru-da-a
1	subgenre_remarks	Silver returned, su-ga Lugal-nu-bànda mu-túm; seal: Lú-dDumu-zi d. Ma-ni sagi dGù-dé-a
1	subgenre_remarks	Silver sag-nu-tuk from Ur-é-gal to I3-kal-la; seal: Lú-má-gu-la ds d. Du-du
1	subgenre_remarks	Silver to be returned (zi-zi-dam); seal: Lú-∂Nin-åubur dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Silver to buy dead oxen from Lu-Ninshubur; seal illegible.
1	subgenre_remarks	Silver to buy tin (kù sù-gan) from Mansum to []; [seal?].
1	subgenre_remarks	Silver, kishib Ur-gishgigir su-su-dam; seal: Ur-gishgigir ds d. Lú-dBa-ba6 ab-ba uru.
1	subgenre_remarks	Silver, á-dam-gàr kù-lá, from A-tu ds hé-dab5 to Ur-Enzu; á-ki-ti-shè kù-sag-tuk; seal: Ur-dEN.ZU d Bar-bar kù-lá dingir si-sá
1	subgenre_remarks	Slave sale; seal; 9x15 lines
1	subgenre_remarks	Small cattle (6 másh) from Ur-Damu to Lú-Lagashki; seal: Lú-Lagashki ds d. Ur-dNanshe nu-bànda kurushda
1	subgenre_remarks	Small cattle []; seal: Lú-dNin-gír-su ds d. Ur-dBa-ba6.
1	subgenre_remarks	Small cattle arua é-in-mah received by dUtu-ba-è; seal: dUtu-ba-è d. Ur-zu
1	subgenre_remarks	Small cattle for the house of Urdun from Lukinunir; seal: Lugal-nám-mah dubsar dumu [Da]-da (CBT 2)
1	subgenre_remarks	Small cattle for the house of Urdun, from Ur-Enki to Lugalnammah; seal: Lugal-nám-mah dubsar dumu Da-da; months ii-vi (CBT 2)
1	subgenre_remarks	Small cattle from Agi for the house of Urdun and the gá-nun giå-åè; seal illegible; months iv-xii (CBT 2)
1	subgenre_remarks	Small cattle from Du11-ga-zi-da to Lú-Lagashki; seal: Lú-Lagashki ds d. Si-dù kurushda dNin-gír-su
1	subgenre_remarks	Small cattle from Lú-bala-sha6-ga to Má-gur8-re sipa; seal: Má-gur8-re d. Lú-dBa-ba6
1	subgenre_remarks	Small cattle from U2-du-du to Ki-tush-lú; seal: Ki-tush-lú d. Ur-mes.
1	subgenre_remarks	Small cattle from Udulu to Abbakalla the fattener; unopened envelope; seal: Ab-ba-kal-la [gudu4?] dumu Lugal-du10-ga gudu4 ∂Nanåe-ka (CBT 2)
1	subgenre_remarks	Small cattle from Ur-Alla to Ikalla; seal: Lú-Lagashki ds d. Ur-dNanshe nu-bànda kurushda.
1	subgenre_remarks	Small cattle received by Amar-ka5-a and Puzur4-Ir3-ra (CBT 2). A: Case of 18776; seal: Amar?-ka5?-a dumu Lugal-[] (CBT 2)
1	subgenre_remarks	Small cattle shu-gíd, arua, from Lú-bala-sha6-ga to Lú-Lagashki; seal: Lú-Lagashki ds d. Ur-dNanshe nu-bànda kurushda
1	subgenre_remarks	Small cattle to be returned; seal: I3-pàd-da d. Lú-kiri4-zal kurushda dNin-mar-ki
1	subgenre_remarks	Small cattle transferred from Ur-Baba to Lu-Lagaå; case unopened; seal: Lú-Lagaå˚ dubsar dumu Ur-∂Nanåe, last line empty; mu Ki-maå˚ a-rá 2-kam (CBT 2)
1	subgenre_remarks	Small cattle transferred from the custody of Gù-dé-a son of Un-íl to Ur-åa6-ga son of Da-AN (CBT 2). A: Case of 16360; seal: Ur-åa6-ga dumu Da-AN (CBT 2)
1	subgenre_remarks	Statement about 2 sig7-a working in 2 giå.kiri6 (CBT 2). A: Case of 22910; seal: Kaå4 dubsar dumu A-tu dubsar åim (CBT 2)
1	subgenre_remarks	Statement about barley; seal: [] [] d. Ur-[]
1	subgenre_remarks	Statement about sealing a tablet recording 560 gur of barley
1	subgenre_remarks	Statement of ku-mah at hand; w/seal impressions, bearing king's name;
1	subgenre_remarks	Statement of ku-mah at hand; w/seal impressions; (Obv)4x(Rev)1 lines
1	subgenre_remarks	Statement of payment.  Seal impressions. 3X4 UE1 lines
1	subgenre_remarks	Statement or Note.seal impression. 3x1 lines
1	subgenre_remarks	Statement, An-né-ba-ab-du7 íb-gi-ne; seal: An-né-ba-ab-du7 ds d. Ur-gishgigir
1	subgenre_remarks	Statement: 2 gu4-engar ki 60-sìla-bi ì-tag-bi shu-ba sum nu-hul; seal: Lú-du10-ga d. dNanna-kam
1	subgenre_remarks	Statement: 32 gurush present; seal: Nì-ga-a-ni d. Du-mu nu-gishkiri6.
1	subgenre_remarks	Statement: Abbashaga, Lú-dNin-sún érin é-dSHul-gi-me kishib Lú-uru-sag gìr dNin-mar-ki-ka; seal: Lú-uru-sag ds d. Lú-dNin-gír-su
1	subgenre_remarks	Stone in seal decayed
1	subgenre_remarks	Suit for debt and payment; seal impressions on tablet and case; (Obv)11x(Rev)15x(UE)2 lines
1	subgenre_remarks	Surplus of barley by Urmes, kiåib Ur-∂Nin-MAR.KI (CBT 2). A: Case of 19320; seal: Ur-∂Nin-MAR.KI-ka dubsar dumu Nam-ha-ni (CBT 2)
1	subgenre_remarks	Surplus of barley returned by Niurum to Ur-Baba; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Surplus of emmer in the house of the ensigal received by Ur-Baba son of Bazi from Niurum; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Surplus of small cattle transferred from Ur-Baba to Lu-Lagaå (CBT 2). A: Case of 18777; seal: Lú-Lagaå˚ dubsar dumu Si-dù nu-bànda kuruåda (CBT 2)
1	subgenre_remarks	Tablet (571) Seal impressions.  8x2x5 UE 1 lines
1	subgenre_remarks	Tablet about fattening of cattle; seal: Ur-∂EN.ZU dumu Ur-∂En-[] (CBT 2)
1	subgenre_remarks	Tablet about fattening sheep; seal Ur-∂EN.ZU dumu Ur-[gú-en-na rá-gaba] (CBT 2)
1	subgenre_remarks	Tablet about fattening sheep; seal: Ur-∂EN.ZU dumu Ur-[gú-en-na rá-gaba] (CBT 2)
1	subgenre_remarks	Tablet about sheep fattening; seal: Ur-∂EN.ZU dumu Ur-gú-en-na rá-gaba (CBT 2)
1	subgenre_remarks	Tablet broken; seal: Lugal-ti-ra-ásh-e ds d. Ir11-mu
1	subgenre_remarks	Tablet defaced; lí-iq-tum; seal dedicated to the king Amar-Sin Nibru.ki d.[] pàd-da []
1	subgenre_remarks	Tablet(566). Seal impressions.
1	subgenre_remarks	Tablet(580).  Seal impressions.
1	subgenre_remarks	Tablet:   ;9x2x9x1 lines 6.7x4.3x2.5 cms; Case:    seals; 8x2x8 lines
1	subgenre_remarks	Tablet:(Obv)14x(Rev)12x(UE)1 lines, Case:(Obv)not inscribed,(Rev)6 lines. Seal impressions on all over the surfaces of both tablet & case.
1	subgenre_remarks	Tag for a harvest laborer; three seals; 2x1 line
1	subgenre_remarks	Tag for harvest laborers; seals; 6 lines; 4.3.1x1.8 cms
1	subgenre_remarks	Tag for workers; seals
1	subgenre_remarks	Tag with seal without inscription
1	subgenre_remarks	Tag; objects whose length is given; seal: Ur-dBa-ba6 ds d. [].
1	subgenre_remarks	Talpush-atili sealing
1	subgenre_remarks	Temple Accounts; seal impression on LoE.; (Obv)14x(Rev)10 lines
1	subgenre_remarks	Temple account; Seal impressions all over the surfaces; (Obv)7x(Rev)5 lines
1	subgenre_remarks	Temple account; Ur3 seal impressions all over the surfaces; (Obv)6x(LoE)1x(Rev)3 lines
1	subgenre_remarks	Temple account; Ur3 seal impressions all over the surfaces; (Obv)9x(Rev)9x(UE)1 lines
1	subgenre_remarks	Temple account; Ur3 seal impressions, (Obv)6x(LoE)2x(Rev)2 lines
1	subgenre_remarks	Temple account; Ur3 seal impressions; (Obv)9x(LoE)1x(Rev)2 lines
1	subgenre_remarks	Temple account; seal impression all over the surfaces; (Obv)7x(LoE)2x(Rev)1 lines
1	subgenre_remarks	Temple account; seal impression on Obv(prbly.the same seal as B7294 in PBS 14 539, wrongly pub.as CBS7294); (Obv)13x(UE)1 lines
1	subgenre_remarks	Temple account; seal impression, same seal as Porada, Herzfeld Festschrift no.5; (Obv)15x(Rev)14 lines
1	subgenre_remarks	Temple account; seal impressions all over the surfaces; (Obv)6x(Rev)3 lines
1	subgenre_remarks	Temple account; seal impressions all over the surfaces; (Obv)8x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Temple accounts; seal impressions all over the surfaces, (Obv)9x(Rev)4 lines, *MSKH says VII
1	subgenre_remarks	Temple contract; w/seal impressions; (Obv)5x(Rev)2 lines
1	subgenre_remarks	Temple record, from 16/III/2 to 5/IV/2; seal impressions all over the surfaces(seal w/inscription); (Obv)7x(Rev)0 lines
1	subgenre_remarks	Temple record; Seal impressions all over the surfaces; (Obv)6x(Rev)0 lines
1	subgenre_remarks	Temple record; contract?; w/seal impressions; 2 lines
1	subgenre_remarks	Temple record; faint seal impressions on Obv,LoE,LE,RE.&UE; (Obv)7x(Rev)3 lines
1	subgenre_remarks	Temple record; seal impressions all over the surfaces; (Obv)5x(Rev)3 lines
1	subgenre_remarks	Temple record; seal impressions all over the surfaces; (Obv)5x(Rev)4 lines
1	subgenre_remarks	Temple record; seal impressions all over the surfaces; (Obv)6x(Rev)0 lines
1	subgenre_remarks	Temple record; seal impressions all over the surfaces; (Obv)6x(Rev)5 lines
1	subgenre_remarks	Temple record; seal impressions all over the surfaces; (Obv)7x(Rev)3 lines
1	subgenre_remarks	Temple record; seal impressions all over the surfaces; (Obv)7x(Rev)7 lines
1	subgenre_remarks	Temple record; w/seal impression; (Obv)4x(LoE)1x(Rev)4 lines
1	subgenre_remarks	Temple record?/Contract?; seal impressions all over the surfaces; (Obv)6x(Rev)1 lines
1	subgenre_remarks	Ten carcasses of sheep for the boat of ∂Nin-ma-da?-ki; seal: Ur-∂Nin-MAR.KI dubsar dumu Lú-∂Na-rú-a (CBT 2)
1	subgenre_remarks	The tablet of Lu-Ningirsu recording barley must be brought; seal: Ur-[] ds d. Ur-[].
1	subgenre_remarks	Threshed barley (åe giå-è-a 12 åim/mud5-du 5 ma-na-ta åe kar-ra) from Dingir-igi-la-at; case unopened; seal: Lugal-lú-åa6-åa6 dubsar dumu Nimgir-åà-kúå-an-na (CBT 2)
1	subgenre_remarks	Threshed barley transferred from Urtur to Lugal-uruda and Ur-Baba (CBT 2). A: Case of 18774; seal: Lugal-uruda sa12-du5 dumu å-zi-da sa12-du5 (CBT 2)
1	subgenre_remarks	To be re-catalogued (CBT 2). A: Case of 23083; seal: Ka5-a-mu dumu In-na-kal (CBT 2)
1	subgenre_remarks	Too destroyed for translation. Seal: Ur-[...] ds d. dumu Ur-{d}Åara2 åa13-dub-ba.
1	subgenre_remarks	Traces of seal impression; Usage unknown, not meant for a tag or a jar sealing, used as label or by a seal-cutter to test his seals
1	subgenre_remarks	Transfer of 2 persons; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Transfer of 3 persons from Si-dù to Ku5-da mhaldim; seal: Ku5-da muhaldim d. Ur-dIshtaran.
1	subgenre_remarks	Transfer of []; seal: Ur-dInanna
1	subgenre_remarks	Transfer of a géme from Ki-[] to Gìr-ni-ì-sha6; seal: Gìr-ni-ì-sha6 ds d. []
1	subgenre_remarks	Transfer of apples, gishhashhur ki dNin-mar-ki-ka-ta Ur-dEN.ZU shu-ba-ti; seal: Ur-dEN.ZU d. Lugal-[]
1	subgenre_remarks	Transfer of apples, gishhashhur-hád from Lú-dIg-alim lú-ùr-ra; seal: Lú-dIg-alim d. Nam-ha-ni lú-ùr-a
1	subgenre_remarks	Transfer of barley from Íeå-kal-la to Urmes; seal: Ur-mes dubsar dumu Nam-ha-ni (CBT 2)
1	subgenre_remarks	Transfer of barley; kishib Urgar; gìr Lugal-mí-ús-sa; seal: Ur-gar ds d. Lú-gaba
1	subgenre_remarks	Transfer of cattle in Guabba; seals: Ur-ni9-gar d. Lú-du10-ga; Lú-dNin-[gír-su] ds d. Ur-dBa-ba6 shabra
1	subgenre_remarks	Transfer of flour from Lú-dNin-shubur to Ur-dLama; seal Ur-dLama ds d. Ur-gar
1	subgenre_remarks	Transfer of garments; tablet inside case; seal: Lú-dBa-ba6 ds d. Ur-dEN.[ZU]
1	subgenre_remarks	Transfer of oil; seal: Ab-ba-kal-la ds d. Ur-é-gal
1	subgenre_remarks	Transfer of sheep from Lugal-gú-gal to Ka5-a-mu; udu ì, udu niga mu-du-lum; month 5 to 12;seal: Ka5-a-mu d. NI-NI-mu sipa na-kab-tum
1	subgenre_remarks	Transfer of silver from Ur-baba to Lú-dUtu; seal: Lú-dUtu s d. Ba-zi?
1	subgenre_remarks	Transfer of small cattle form Ba-a to Lú-gú-gal; seal: Lugal-gú-gal ds d. Lú-dBa-ba6
1	subgenre_remarks	Transfer of small cattle from Ezimu to Ur-Baba; envelop and tablet;seal illegible; mu dumu-munus lugal
1	subgenre_remarks	Transfer of wool and bitumen from the merchant Ur-Baba to Ur-Lama; seal
1	subgenre_remarks	Transfer of åim from Nì-ga to Lú-∂Nin-gír-su; seal: Lú-∂Nin-gír-su dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Transport of a bed, gurush má in ná-da to Gaesh; seal: dUtu-bar-ra ds d. A-mu
1	subgenre_remarks	Transport of beer from Má-gur8-re to SHu-dNin-shubur; seal: SHu-dNin-shubur rá-gaba d. Ur-d[]
1	subgenre_remarks	Two dead oxen from the stable taken in account by the géme-hé-dab5 (CBT 2). A: Case of 18203; seal: Lú-∂Nin-åubur dubsar d Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Two female cooks receiving 60 sila of flour, passing from Bamu to Ur-Igalim, gìr Lugal-bàd-uru-na; seal: Ur-dBa-ba6 ds d. Na-mu.
1	subgenre_remarks	Two oxen from A2-ni-ni to the temple of Gatumdu; seal: Ur-gu-la ds d. Ur-kù-nun.
1	subgenre_remarks	Two pihu: offering for the leader of the Kassite infantry; dispursement from malt barley, received by a brewer; sealimpressions; 13X2X12lines
1	subgenre_remarks	Unidentified; Contract?; lu2.lu2.u3-ra (  ) un-gi4-gi4-ne; seals; 3x4 lines"
1	subgenre_remarks	Uninscribed ; seal
1	subgenre_remarks	Uninscribed block of clay; sealed
1	subgenre_remarks	Uninscribed sealing with impressions of two inscribed seals: (1) dSHu-dEN.ZU / lugal kala-ga / lugal Uríki-ma / SHu-ì-lí sukkal / dumu Ur-dNin-mug / ir11-zu; (2) Lú-dNin-gír-su / dub-sar / dumu Lú-[dB]a-ba6 (possibly a recut old Akkadian seal). SR?
1	subgenre_remarks	Uninscribed, w/seal impressions; Cf. Peters' Note book 971. Discovered April 8, 1898
1	subgenre_remarks	Uninscribed, with depression made by a stamp seal
1	subgenre_remarks	Uninscribed; Case from a letter order?; seals; Fine seal impression with winged dragon, lion; the same impression appears on N793 (case frag); not inscribed but has an inscription in seal impression; *or Ur3
1	subgenre_remarks	Uninscribed; complete seal impression
1	subgenre_remarks	Unusual shaped tablet with unusual pattern of sealing.#
1	subgenre_remarks	Ur-gar nagar received barley from Ur-bàd-tibir-ra; seal: Ur-gar nagar (CBT 2)
1	subgenre_remarks	Ur-∂Lamma dumu Inim-ma-gi-na su-su-dam; fragment of case adhering; seal illegible (CBT 2)
1	subgenre_remarks	Various goods as mortuary offerings for Shu-Kabta,withdrawn from Adad-illat (copy).  Not sealed.  
1	subgenre_remarks	Vase (gi-gur) covered with bitumen from Ludingirra to Niurum, son of Lú-na-nam; [seal] (CBT 2)
1	subgenre_remarks	W/2 seal impressions: before the inscription, Amurru a fallen ? attacked by an eagle.  A priest in act of imploration.
1	subgenre_remarks	W/3 impressions of a seal given by Ibi-Sin to the high-priest of Enlil; 2 lines
1	subgenre_remarks	W/6 stamp seal impressions
1	subgenre_remarks	W/Seal impressions; (Obv)1*x(Rev)2 lines; *actually written on RE.as a continuation from Obv.
1	subgenre_remarks	W/fine seal impression all over the surfaces; (Obv)5x(LoE)1x(Rev)5 lines
1	subgenre_remarks	W/gold pin (U.10940--3 cylinder seals & 3 pins)
1	subgenre_remarks	W/illegible seal impression
1	subgenre_remarks	W/part of fine seal impression;
1	subgenre_remarks	W/same seal impressions on Rev,UE,LE.&RE.; Harper's No. Ni 28-2-10-89; (Obv)14x(Rev)12 lines
1	subgenre_remarks	W/seal impression & impression of strings
1	subgenre_remarks	W/seal impression (ED III style)
1	subgenre_remarks	W/seal impression (Hittite style)
1	subgenre_remarks	W/seal impression (same seal as CBS14262, CBS9098, CBS6743, 6746, 9098, 14262+, 14270)
1	subgenre_remarks	W/seal impression (same seal as CBS6743, 6746, 14262+, 14273a)
1	subgenre_remarks	W/seal impression on 1 side & hem impression on the other side
1	subgenre_remarks	W/seal impression on LE.; (Obv)3x(Rev)1 lines
1	subgenre_remarks	W/seal impression outside, rope marks outside; from top of a jar
1	subgenre_remarks	W/seal impression, & traces of strings & surface of the object to which this bulla was attached
1	subgenre_remarks	W/seal impression; (Obv)5x(Rev)4 lines
1	subgenre_remarks	W/seal impression; (Obv)8x(Rev)6 lines
1	subgenre_remarks	W/seal impression; (Obv)8x(Rev)8x(LE)1 lines
1	subgenre_remarks	W/seal impression; * request of Dr.W. Pepper, deposited w/Sommerville Collection;
1	subgenre_remarks	W/seal impression; * time of Murashu's son or later
1	subgenre_remarks	W/seal impression; * time of Murashu's sons
1	subgenre_remarks	W/seal impression; *Peters describes as Nippur I, although Ur II tablets are characteristic to Nippur II.  I" came from Tablet Hill
1	subgenre_remarks	W/seal impression; *Peters describes as Nippur I, although Ur3 tablets are characteristic to Nippur II.  I" came from Tablet Hill
1	subgenre_remarks	W/seal impression; *Peters describes as Nippur I, although Ur3 tablets are characteristic to Nippur II. I" came from Tablet Hill
1	subgenre_remarks	W/seal impression; *time of Murashu's son or later
1	subgenre_remarks	W/seal impression; Harper's mark: Ni.42-2-18-89. *Peters describes as Nippur I, although Ur3 tablets are characteristic to Nippur II. I" came from Tablet Hill
1	subgenre_remarks	W/seal impressions (Seal of son of Mr.A-gi-ia); (Obv)4x(LoE)1x(Rev)3 lines
1	subgenre_remarks	W/seal impressions (inside of a case tablet????).  Harper:  Ni.2-2-19-89.
1	subgenre_remarks	W/seal impressions (same seal as CBS10968); (side)5x(edge)1 lines
1	subgenre_remarks	W/seal impressions (same seal as CBS6743, 6746, 14270, 14273a)
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)4x(LoE)2x(Rev)1 lines
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)5 lines;
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)6x(Rev)0 lines; 4.5 X 3.6 X 1.6 cm.
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)6x(Rev)6 lines; 4.3 X 3.6 X 1.5 cm.
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)7x(Rev)0 lines
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)7x(Rev)0 lines; 3.2 X 3.5 X 1.8 cm.
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)7x(Rev)2 lines
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)7x(Rev)3 lines; 4.1 X 3.5 X 1.6 cm.
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)7x(Rev)4 lines; 3.7 X 3.5 X 1.5 cm.
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)8x(LoE)1x(Rev)0 lines
1	subgenre_remarks	W/seal impressions all over the surfaces; (Obv)8x(Rev)1 lines; 4.0 X 3.5 X 1.6 cm.
1	subgenre_remarks	W/seal impressions all over the surfaes; (Obv)8x(Rev)2 lines; 4.6 X 4.0 X 1.7 cm.
1	subgenre_remarks	W/seal impressions on Obv.& edges; (Obv)12x(Rev)15 lines
1	subgenre_remarks	W/seal impressions on Rev,UE.&LE; (Obv)16x(Rev)16 lines; Harper's No. Ni. 2-13-89
1	subgenre_remarks	W/seal impressions on all edges;  *From the kiln of Tablet Hill; (Obv)11x(Rev)10 lines
1	subgenre_remarks	W/seal impressions on all edges; *from kiln in Tablet Hill; (Obv)17x(LoE)2x(Rev)19x(UE)2 lines
1	subgenre_remarks	W/seal impressions on all over the surfaces; (Obv)7x(Rev)1 lines
1	subgenre_remarks	W/seal impressions; 
1	subgenre_remarks	W/seal impressions; (Obv)13x(LoE)1x(Rev)11x(UE)2 lines
1	subgenre_remarks	W/seal impressions; (Obv)13x(Rev)17 lines
1	subgenre_remarks	W/seal impressions; (Obv)13x(Rev)8 lines
1	subgenre_remarks	W/seal impressions; (Obv)15x(Rev)14 lines
1	subgenre_remarks	W/seal impressions; (Obv)16x(Rev)15 lines
1	subgenre_remarks	W/seal impressions; (Obv)17x(Rev)12 lines
1	subgenre_remarks	W/seal impressions; (Obv)17x(Rev)19 lines
1	subgenre_remarks	W/seal impressions; (Obv)4 lines
1	subgenre_remarks	W/seal impressions; (Obv)4x(LoE)3x(Rev)2 lines
1	subgenre_remarks	W/seal impressions; (Obv)4x(Rev)4 lines
1	subgenre_remarks	W/seal impressions; (Obv)9x(Rev)5 lines
1	subgenre_remarks	W/seal impressions; *found between 7 & 7.5 m below brick pavement dated c.3100 B.C.in the prehistoric settlement;
1	subgenre_remarks	W/seal impressions; *found between 7.5 & 8 m below the same pavement as 19724, dated B.C.3100
1	subgenre_remarks	W/seal impressions; 3 lines
1	subgenre_remarks	W/seal impressions; 5 lines
1	subgenre_remarks	W/seal impressions; 5/9/88: only 1 fragment of CBS 10884 found in drawer; 14 lines on case
1	subgenre_remarks	W/seal impressions; 6 lines
1	subgenre_remarks	W/seal impressions; Harper: Ni.2-2-19-89; (Obv)16x(Rev)19x(UE)2 lines
1	subgenre_remarks	W/seal impressions; Harper: Ni.2-2-19-89; (Obv)7x(Rev)4 lines
1	subgenre_remarks	W/seal impressions; Harper: Ni.2-2-19-89; Tablet:(Obv)9x(Rev)7x(UE)1 lines; Case:9 lines
1	subgenre_remarks	W/seal impressions; Harper; Ni.9-2-14-89. *Peters describes as Nippur I, although Ur3 tablets are characteristic to Nippur II. I" came from Tablet Hill
1	subgenre_remarks	W/seal impressions; Peters' #542; 6 lines
1	subgenre_remarks	W/seal impressions; Peters':#628; (Obv)4x(Rev)2 lines
1	subgenre_remarks	W/seal impressions; Ridge X; (Side 1)3x(Side 2)1 line
1	subgenre_remarks	W/seal impressions; frag1:(Obv)(i)5x(ii)5 lines, frag2:(Obv)5 lines
1	subgenre_remarks	W/seal impressions; incised characters
1	subgenre_remarks	W/seal impressions; linear inscription?
1	subgenre_remarks	W/seal impressions; on cloth
1	subgenre_remarks	W/seal impressions; on incised pottery, relief shows below
1	subgenre_remarks	W/seal impressions; pictographs, star
1	subgenre_remarks	W/seal impressions; seal of Mes-an-ni-padda, lugal Kish(ki) dam-nu-gig""
1	subgenre_remarks	W/seal impressions; trace of string on Rev
1	subgenre_remarks	W/seal impressions; traces of strings inside; copulatio a posteriori""
1	subgenre_remarks	W/seal impressions; traces of strings inside; on a basket!
1	subgenre_remarks	W/seal impressions; traces of strings inside; w/pictograph(?)
1	subgenre_remarks	W/seal impressions; w/traces of strings on Rev.
1	subgenre_remarks	W/seal? impressions
1	subgenre_remarks	W/stamp seal impression on 1 side
1	subgenre_remarks	W/very faint seal impressions; (Obv)4x(LoE)1x(Rev)4x(UE)2 lines
1	subgenre_remarks	Wages for hired guruå from Ur-Nanåe to Ur-Numuåda; case unopened; seal: Ur-∂Nu-muå-da dubsar dumu Du-du sanga Urub.ki (CBT 2)
1	subgenre_remarks	Wheat for Nippur from Ur-dBa-ba6 to Ur-dEn-líl-lá; seal: Ur-dEn-líl-lá; ds d. Inim-sha6 kurushda
1	subgenre_remarks	With 3 seal impressions of the same seal only
1	subgenre_remarks	With 6 identical seal impressions, Bur-gul seals; 3 lines
1	subgenre_remarks	With Akkadian seal impression
1	subgenre_remarks	With impression of magnificent seal
1	subgenre_remarks	With seal impression; (Obv)7x(Rev)7 lines
1	subgenre_remarks	Withdrawal of bread (ninda lugal ninda bala-a-ta) for the sig7-a; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	Withdrawal of dates from the sukkalmah; seal: A2-zi-da ds d. SHesh-shesh
1	subgenre_remarks	Withdrawal of flour (nì-àr-ra zíz-an and dabin) kishib énsi-ka shà Ninaki; seal dedicated to SHulgi Ur-d[Lama} gudu4 d[] [ir11-zu]
1	subgenre_remarks	Withdrawal of sheep for Dumuzi in Guabba passing from Annahilibi to Lu-Igimashe; seal: Lú-dIgi-ma-shè d. Ur-sha6-ga kurushda.
1	subgenre_remarks	Women towing a boat loaden with flour to Nippur, from Lugaligihuå to Ur-Baba; case unopened; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Women working for the food of the hé-dab5 from Habazige to Ur-Baba; seal: Ur-∂Ba-ba6 dubsar dumu Ba-zi (CBT 2)
1	subgenre_remarks	Women, géme nar-dHendur-bil4-sag, ugula Lú-bi-mu; seal illegible
1	subgenre_remarks	Wood delivered to the palace by Lú-du10-ga. Seal dedicated to Åulgi, ∂Åul-gi nita kalag-ga lugal Uri5§-ma lugal an-ub-da límmu-ba-åè! É-a-ni-åa nin-kaskal-la-na [...] in-na-ba (CBT 3)
1	subgenre_remarks	Wool (síg) bar udu shukur-ra a-ka-a gál-la Lú-dIgi-ma-shè kurushda su-su-dam; seal: Lú-dIgi-ma-shè d. Ur-sha6-ga kurushda
1	subgenre_remarks	Wool account; seal
1	subgenre_remarks	Wool for géme work and sa gu from Lugal-dam-[gàr]; seal: Lugal-im-ru-a
1	subgenre_remarks	Wool from Lú-dNin-gír-su Nì-ga dam-gàr shu-ba-ti; seal: Ur-dBa-ba6 d. I3-kal-la []
1	subgenre_remarks	Wool from Lú-kiri4-zal to Lú-inim-nì-sha6-ga; seal: Lú-inim-nì-sha6-ga ds d. Ur-dNanshe
1	subgenre_remarks	Wool from Ur-dNanshe kishib Ku5-da gìr Ur-dBa-ba6; seal Ur-dBa-ba6 d. Du-[]
1	subgenre_remarks	Wool from Ur-sha6-ga to Lú-kiri4-zal; seal: Lugal-ti-ra-ásh-e ds d. Na-mu
1	subgenre_remarks	Wool in the account of Hu-ru the kush7; seal: Ur-dNin-[] d. Al-la.
1	subgenre_remarks	Wool issued by Lukalla to Kilulla; seal: [Mes-e] dubsar dumu Da-[da] (CBT 2)
1	subgenre_remarks	Wool rations for various persons; seal: Ur-mes ds d. Lú-Ninaki
1	subgenre_remarks	Wool received by Bí-du11-ga; seal: Ku5-da-dBa-ba6 ds d. Ur-dNun-gal ugula ush-bar
1	subgenre_remarks	Wool received by Lu-dingirra; seal: Lú-dingir-ra [].
1	subgenre_remarks	Wool to buy oxen given by Lu-Ningirsu to Niga the merchant (CBT 2). A: Case of 18816; seal: Ur-ni9-gar dumu Ur-åa6-ga dam-gàr (CBT 2)
1	subgenre_remarks	Wool to buy oxen, from Lu-Ningirsu; seal: Ur-ni9-gar d. Ur-sha6-ga dam-gàr.
1	subgenre_remarks	Wool? expenditure; seal: Lú-dUtu ds d. Ba-zi
1	subgenre_remarks	Wool? from Ur-∂En-ki to Ba-har-e (CBT 2). A: Case of 22942; seal: Lú-∂Nin-åubur dubsar dumu Lú-∂Ba-ba6 (CBT 2)
1	subgenre_remarks	Work of géme controled bt Ur-Baba; seal: Ur-dBa-ba6 ds d. Ba-zi
1	subgenre_remarks	Work of hé-dab5; case unopened; seal: Lú-∂Ba-ba6 dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	Working time of géme; [seal] (CBT 2)
1	subgenre_remarks	X sar sahar é-kin a-shà da-sal, kishib Ur-den-gal-du-du; seal: Ur-dBa-ba6 d. Lú-[] sa12-du5 Ur-dEn-gal-du-du ds [ir11-zu]
1	subgenre_remarks	Young oxen from Lugal-izkimzi to Ur-Engaldudu (CBT 2). A: Case of 19014; seal illegible (CBT 2)
1	subgenre_remarks	Zé-na ki Ur-d[]-ta kishib Ur-d[]; [seal]
1	subgenre_remarks	[  ] dumu Ur-é-bábbar su-su-dam; seal: [Ur-gu-la?] dumu Ur-é-bábbar; frgt case + tablet.
1	subgenre_remarks	[Barley]; seal: Ur-dam ds d.Ur-dNanshe.
1	subgenre_remarks	[Content]; seal: Ur-dIg-alim ds d. Lú-[dNin-gír-su]
1	subgenre_remarks	[Obv.] seal: Ur-dBa-ba6 ds d Ha-ba-zi-zi.
1	subgenre_remarks	[Obv], oil (ì-gish) for Lú-dNin-shubur, gìr Ama-di-ne; seal: Lú-dNin-shubur dumu Lugal-d[] sukkal mashkim
1	subgenre_remarks	[X] from Mansum to SHeshkalla; seal: SHesh-kal-la ds d. Da-da
1	subgenre_remarks	[] for the marsa, kishib Ur-dLama; [seal].
1	subgenre_remarks	[] from Magurre; seal illegible (CBT 2)
1	subgenre_remarks	[] from Nì-ga the merchant to Ur-Ningiszida; seal: Ur-dNin-gis-zi-da ds d. Lú-[] ì-rá-rá.
1	subgenre_remarks	[] from Ur-abba to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Ba-zi
1	subgenre_remarks	[] transferred from Ur-ni9-gar to Aagina and Ur-eninnu; kiåib Nam-mah-∂Ba-ba6; tablet in case; seal illegible (CBT 2)
1	subgenre_remarks	[]; seal: Ku-li ds d. Ki-ág-mu.seal: Ku-li ds d. Ki-ág-mu.
1	subgenre_remarks	[]; seal: Lugal-síg-sud4 ds d. Ur-dLama
1	subgenre_remarks	[]; seal: Lú-me-lám dubsar dumu Lú-kal-la (CBT 2)
1	subgenre_remarks	animals, gift of king Amar-Suen; sealed by governor
1	subgenre_remarks	bad seal, bad signs in inscription
1	subgenre_remarks	barley from Ur-Shulgi, Ur-Shulpa'e rec'd.  seal of Ur-Shulpa'e
1	subgenre_remarks	bread for the 30th day, seal of the city governor
1	subgenre_remarks	bulla
1	subgenre_remarks	bulla on a string?
1	subgenre_remarks	bulla or bottle top concerning oil
1	subgenre_remarks	case 0f 28057, desintegrated; seal: SHesh-kal-la ds d. Lugal-á-zi-da
1	subgenre_remarks	ceremonial garment with mention of hem sealing
1	subgenre_remarks	cf 29-16-196: same seal impression
1	subgenre_remarks	cf. 29-16-197: same seal impression
1	subgenre_remarks	contract (seal)
1	subgenre_remarks	contract + seals
1	subgenre_remarks	eroded; seal illegible
1	subgenre_remarks	few signs; seals
1	subgenre_remarks	frag with seal in box with 2426 [does not belong]
1	subgenre_remarks	fragment of sealed bulla
1	subgenre_remarks	gish.hashhur? babbar from Urmes to Namzitarra; seal: Nam-zi-tar-ra ds d. Ba-zi
1	subgenre_remarks	gishhashhur from Ir11 to Lú-dIg-alim; seal: Lú-dIg-alim d. Nam-ha-ni lú-ùr-a
1	subgenre_remarks	gishhashhur from Nabi, 1 nì-gal and 1 nì-íl from Gú-ù-mu and Abbamu for the má-u4-zal-la; seal dedicated to SHulgi, Ur-dLama shà-tam ir11-zu
1	subgenre_remarks	gishhashhur from Ur-ba-gár to Lú-dIg-alim; seal: Lú-dIg-alim d. Nam-ha-ni lú-ùr-a
1	subgenre_remarks	gishhashhur from Ur-dLama to Lú-dIg-alim; seal: Lú-dIg-alim d. Nam-ha-ni lú-ùr.
1	subgenre_remarks	gishhashhur hád gishkiri6 ki-gar-ra ki bala-ri-a-shè kishib Ur-gar; seal: Ur-gar ds d. Ur-dun má-lah4-gal.
1	subgenre_remarks	gishpèsh from Ab-ba-mu to Ur-ab-ba; seal: Ur-ab-ba ds d. Ba-zi dub-sar-zì-ka
1	subgenre_remarks	gu4 áb ùr-engar dIg-alim ki A-ma-dingir-ta kishib Ba-zi; seal: Ba-zi ds d. Du-du
1	subgenre_remarks	gurush gishgaba-tab gíd-da ki Ur-sukkal d. Ur-gu-la a-shà nin-zi-ré-na; seal: Ur-kisal ds d. Ur-gu-la
1	subgenre_remarks	hullen tafel?; description of fields; seals. 20x2x20 lines
1	subgenre_remarks	im and dida from Magurre to Lu-Ninshubur; seal: SHu-dNin-shubur àga-ush ir11 Ur-mes
1	subgenre_remarks	kuå-gíd-da åà Ambar˚ (CBT 2). A: Case of 19501; sealed (CBT 2)
1	subgenre_remarks	letter - seal impression (private letter)
1	subgenre_remarks	letter order + rev seal
1	subgenre_remarks	letter to Turam-ili concerning barley obtained from sealed storehouse.
1	subgenre_remarks	modern seal impression
1	subgenre_remarks	personal names of Ur, city governor's seal
1	subgenre_remarks	plowing contract, sealed, with witnesses,
1	subgenre_remarks	seal; 6 lines
1	subgenre_remarks	sealed bulla concerning Shehna (Tell Leilan)
1	subgenre_remarks	sealed bulla with legend of Ilish-takal, son of Pushu-ken
1	subgenre_remarks	sealed bulla with legend of Shu-adda
1	subgenre_remarks	sealed bulla, Pushu-tyabu
1	subgenre_remarks	sealed bulla, kunga2 equids
1	subgenre_remarks	sealed bulla, snake-charmer (?)
1	subgenre_remarks	sealed lentoid bulla
1	subgenre_remarks	sealing
1	subgenre_remarks	sealing, legend of Shu-adda
1	subgenre_remarks	seals with labels; 24x4x24x2(u.e.) lines; 13.3x6.8x3.3 cm
1	subgenre_remarks	seals; 1(lo.e.)x21x1(u.e.) lines; 10.8x6.3x3 cms
1	subgenre_remarks	seals; 10x2x11x3 lines; 7.65x4.7x2.35 lines
1	subgenre_remarks	seals; 11x1x8x2(u.e.) lines
1	subgenre_remarks	seals; 13x5x12x1(u.e.) lines; 9.2x5.45x2.83 cm
1	subgenre_remarks	seals; 15x1x9 lines
1	subgenre_remarks	seals; 2 lines
1	subgenre_remarks	seals; 21x2x20x3(u.e.) lines; 11.5x6x3 cm
1	subgenre_remarks	seals; 29x3x22x2(u.e.) lines; 14.2x7x3.55 lines
1	subgenre_remarks	seals; 6x1x6x2(u.e.) lines; 6.7x4.7x2.2 cms
1	subgenre_remarks	seals; 6x2x6x3 lines; 4.2x4.5x2.2 cms
1	subgenre_remarks	seals; 7x4 lines
1	subgenre_remarks	seals; 8x1x10 lines; 7.05x4.35x2.65 cm
1	subgenre_remarks	seals; 8x1x9x3 lines
1	subgenre_remarks	seals; 9x1x7x2(u.e.)x1(le.e.) lines; 5.8x4.4x2.3 cms
1	subgenre_remarks	seals; bored lengthwise; 10 lines
1	subgenre_remarks	seals; scratchs on obv and rev = x; 7x4x3(u.e.) lines; 5.2x4.6x2.3 cms
1	subgenre_remarks	several irregularities, incl. seal impression 
1	subgenre_remarks	she gish-ì from Urmes received by Ur-dNin-gis-zi-da; seal: Ur-dNin-gis-zi-da ds d. Lú-dUtu []
1	subgenre_remarks	she munu4 she másh-da-ri-a á-ki-ti shu-numun gíd-da kishib Ur-ba-gár; [seal].
1	subgenre_remarks	she shà-gal érin-na ki Ur-dEn-líl-lá-ta; seal: Lú-ush-gi-na d. Hé-ti
1	subgenre_remarks	she-ba nar-dSHul-gi from Ur-ni9-gar, kishib Nam-mah nar; seal: Nam-mah-dBa-ba6 d. Lugal-àm
1	subgenre_remarks	she-lú from Ir11-dam to Id-ni-lí; kishib Lú-dingir-ra; seal: Lú-dingir-ra ds d. Lugal-sha6-ga
1	subgenre_remarks	shim ki Nì-ga-ta; seal: Ur-dNin-gis-zi-da d. Ur-sag-ku5 ì-rá-rá-dNin-[gír-su]
1	subgenre_remarks	shim-ì for the gods, from A-gi4 to Lu-Ningirsu; seal: Lú-dNin-gír-su ds d. Ir11-mu.
1	subgenre_remarks	small fragment of bulla
1	subgenre_remarks	tablet (Obv)4x(Rev)4 lines; case (Obv)3x(Rev)3 lines, seal impression all over the surfaces
1	subgenre_remarks	the same seal as 14205
1	subgenre_remarks	the same sealing as 14205
1	subgenre_remarks	unreadable/sealed
1	subgenre_remarks	very poorly written, and bad seal legend
1	subgenre_remarks	w/Akkadian seal impression
1	subgenre_remarks	w/seal impression (Kassite style);
1	subgenre_remarks	w/seal impression (prbly.Ur3)
1	subgenre_remarks	w/seal impression (pseudo-Kassite?)
1	subgenre_remarks	w/seal impression(archaic)
1	subgenre_remarks	w/seal impressions on LE.&UE.; (Obv)16x(Rev)5 lines
1	subgenre_remarks	w/seals; (Obv)16x(Rev)16 lines
1	subgenre_remarks	with seal impression (Hittite)
1	subgenre_remarks	| gi ka-[shid?] má-zì-da from Lu-Ningirsu; seal: Ur-dIg-alim d. Ur-sha6-ga dub-sar.
1	subgenre_remarks	Ím-sig5 to be returned; seal: Ur-èn dumu Ur-∂Ba-ba6 lú-åim; MN åu-eå-åa of Drehem or Ur (CBT 2)
1	subgenre_remarks	åe-ba engar dumu gu4-gur é-nam-tur, A-kal-la received; months ix-xii (CBT 2). A: Case of 18215; seal: Lugal-[kù-ga-ni] dumu Al-[la åabra]; months ix-xii (CBT 2)
1	subgenre_remarks	ú-kur lugal, zah-<hi>-lisar from SHà-da; kishib Lú-gishgigir d. U2-lu-du, numun a-shà shubur ù gír-nun-shè; seal: Lú-gishgigir d. Ur-sha6-ga
1	subgenre_remarks	“Clay bulla with sealings and cord marks, dealing with cattle.”
1	subgenre_remarks	“Inscribed seal impression on obv. and rev. (seal is no. 88 in Kang, Sumerian Economic Texts from the Umma archive). 
1	subgenre_remarks	“Lines unclear. Bulla.”
1	subgenre_remarks	“The Art of Seals, p. 29, no. 4” From Umma (Piotr Michalowski, 3/12/87).
```

## Seal examples

First 8 seal-candidate rows that also have a matching `&P` entry in the ATF. Matching tried on catalogue `id` as-is (with `P` prefix if missing) and zero-padded to 6 digits with a `P` prefix.

Convention counts among matched seal candidates: {'zero-padded-6': 19, 'as-is': 7653}

### Example 1: catalogue id=`5581` → ATF `P005581` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5898
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005581 = UET 2, 007
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. [...] , [...]
2. 1(N04) , GESZTU~a KA~a
3. , HI UDU~a
4. , DU NI~b

```

### Example 2: catalogue id=`5582` → ATF `P005582` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5899
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005582 = UET 2, 008
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. ,
2. ,

```

### Example 3: catalogue id=`5583` → ATF `P005583` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5901
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005583 = UET 2, 009
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. 3(N01@f) , SI LUGAL EZEN~a
2. 3(N01@f) , PA~a TUN3~a
3. 1(N01@f) , SAL GI? ZI~a NANNA~a
4. 1(N01@f) , BAN~b AMA~b KU3~a
5. 1(N01@f) , URI5 PA~a
6. 1(N01@f)# , AK~a UDU~a
@column 2
1. 1(N01@f) , PA~a KU6~a
2. 1(N01@f) , PA~a ERIM~a KI PIRIG~b1?
3. 1(N01@f) , NIN GAL~a# UR~a# AN#
4. 1(N01@f) , NIN AN GAL~a AK~a
5. 1(N01@f) , U4 SI A

```

### Example 4: catalogue id=`5584` → ATF `P005584` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5902
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005584 = UET 2, 010
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. [...] , [...]
2. [...] , PAD~a#?
3. [...] , NIMGIR AMA~b
4. [...] , SI#
5. 1(N01@f) , LU2# AMAR
6. 1(N01@f) , IGI BUR~a
7. 1(N01@f) , AB~a X X
@column 2
1. 1(N01@f) , X X
2. 1(N01@f) , AK~a#? AN [...]
3. 1(N01@f) , X AMAR MUSZEN#?
4. 1(N01@f) , NIMGIR# AMA~b#
5. , AB~a SZITA~c
@reverse
@column 1
1. , AB~a SZITA~c#? [...]

```

### Example 5: catalogue id=`5585` → ATF `P005585` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5903
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005585 = UET 2, 011
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. [...] , [...] X
2. [...] , SZIM~a NE~a# [...]
3. 1(N01) , [...] X MUSZEN
4. [...] , [...] AL A UKKIN~a#
@column 2
1. , MUN~b#? ANSZE~b
2. , AK~a ZATU687
3. [...] , SZE~a#? MUN~b#

```

### Example 6: catalogue id=`5586` → ATF `P005586` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5908
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005586 = UET 2, 012
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. 1(N01@f) , GESZTIN~c
2. 1(N01@f) , GI6 UR~a
3. 1(N01@f) , SI GA2~a1? A
4. 1(N01@f) , A |GI&GI| GAL~a
5. 1(N01@f) , LUGAL AK~a
6. 1(N01@f) , KU~b2 LI
7. [...] , LU2#? NA~a NUNUZ~a1
@column 2
1. 1(N01@f) , AMAR X [...]
2. 1(N01@f) , IGI SI4~a# [...]
3. 1(N01@f) , DUB~a# [...] DA~a#
4. 1(N01@f) , [...]
5. 1(N01@f) , [...]
6. 1(N01@f) , TUR [...]
7. 1(N01@f) , SI#? [...]

```

### Example 7: catalogue id=`5587` → ATF `P005587` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5913
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005587 = UET 2, 013
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. 2(N14) , GU7 LU2 ME~a KISAL~b1 SI
2. 1(N14) , NE~a SAG
3. 5(N01) , SIG2~a1? SI X
4. 2(N01) , AMAR [...]
@column 2
1. 2(N01) , DILMUN ISZ~a GAL~a
2. 1(N01) , [...]
3. [...] , [...]
@reverse
@column 1
1. [...] , [...] X

```

### Example 8: catalogue id=`5588` → ATF `P005588` (matched via **zero-padded-6**)

Key columns:

```
accounting_period: 
genre: Administrative
google_earth_provenience: 
id_text2: 0
id_text: 5914
language: Sumerian ?
material: clay
object_preservation: 
object_type: sealing
period: ED I-II (ca. 2900-2700 BC)
period_remarks: 
provenience: Ur (mod. Tell Muqayyar)
provenience_remarks: 
subgenre: 
subgenre_remarks: 
object_remarks: 
```

ATF block (max 40 lines):

```
&P005588 = UET 2, 015
#version: 0.1
#atf: lang qpc
@obverse
@column 1
1. [...] , SAR~a NE~a#? UR~a
2. 2(N01@f)# , MUSZEN# A SI
3. 3(N01@f)# , AK~a#
4. 3(N01@f)# , X X X
5. [...] , X X
6. 2(N22@f)#? 3(N01@f) , [...] GIR2~a
7. [...] , [...]
@column 2
1. 1(N14@f) , ME~a UDU~a
2. 1(N22@f) 3(N01@f) , NAM2
@column 3
1. 1(N45@f) 5(N14@f) , BIR~a KI NI~b

```

## Unmatched

Of 22691 seal-candidate rows, **15019** have no matching ATF entry (no transliteration available under catalogue `id`).
