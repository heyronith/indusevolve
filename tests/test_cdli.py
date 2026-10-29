import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from indusevolve.loaders.cdli import (
    build_records,
    load_catalogue,
    mark_duplicates,
    tokenize,
)


MINI_ATF = """\
&P000001 = Test Seal 1
#atf: lang sux
@obverse
1. {d}szul-gi
2. lugal uri5{ki}-ma
&P000002 = Test Tablet 2
#atf: lang sux
@obverse
1. 1(disz) udu
@seal 1
1. ur-{d}nansze
2. dumu lu2-{d}utu
@reverse
1. zi-ga
&P000003 = Fake Seal
#atf: lang sux
@obverse
1. lugal
&P000004 = Proto Sealing
#atf: lang qpc
@obverse
1. X
&P000005 = Damaged Seal
#atf: lang sux
@obverse
1. [x] lugal#
&P000006 = Dup Seal
#atf: lang sux
@obverse
1. {d}szul-gi
2. lugal uri5{ki}-ma
"""

MINI_CAT_ROWS = [
    {
        "id": "1",
        "id_text": "1",
        "designation": "Test Seal 1",
        "object_type": "seal (not impression)",
        "genre": "official or display",
        "subgenre": "",
        "language": "Sumerian",
        "period": "Ur III (ca. 2100-2000 BC)",
        "provenience": "Ur (mod. Tell Muqayyar)",
    },
    {
        "id": "2",
        "id_text": "2",
        "designation": "Test Tablet 2",
        "object_type": "tablet",
        "genre": "Administrative",
        "subgenre": "",
        "language": "Sumerian",
        "period": "Ur III (ca. 2100-2000 BC)",
        "provenience": "Umma (mod. Tell Jokha)",
    },
    {
        "id": "3",
        "id_text": "3",
        "designation": "Fake Seal",
        "object_type": "seal",
        "genre": "official or display",
        "subgenre": "",
        "language": "Sumerian",
        "period": "fake (modern)",
        "provenience": "",
    },
    {
        "id": "4",
        "id_text": "4",
        "designation": "Proto Sealing",
        "object_type": "sealing",
        "genre": "Administrative",
        "subgenre": "",
        "language": "undetermined",
        "period": "Uruk III (ca. 3200-3000 BC)",
        "provenience": "",
    },
    {
        "id": "5",
        "id_text": "5",
        "designation": "Damaged Seal",
        "object_type": "seal (not impression)",
        "genre": "official or display",
        "subgenre": "",
        "language": "Sumerian",
        "period": "Ur III (ca. 2100-2000 BC)",
        "provenience": "",
    },
    {
        "id": "6",
        "id_text": "6",
        "designation": "Dup Seal",
        "object_type": "seal",
        "genre": "official or display",
        "subgenre": "",
        "language": "Sumerian",
        "period": "Ur III (ca. 2100-2000 BC)",
        "provenience": "",
    },
]


def _write_fixtures(tmp: Path):
    atf = tmp / "cdliatf_unblocked.atf"
    atf.write_text(MINI_ATF, encoding="utf-8")
    cat = tmp / "cdli_cat.csv"
    fieldnames = list(MINI_CAT_ROWS[0].keys())
    with cat.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(MINI_CAT_ROWS)
    return atf, cat


class TestCdli(unittest.TestCase):
    def test_tokeniser_specials(self):
        toks, dam = tokenize("|SZU.DU|")
        self.assertEqual(toks, ["|šu.du|"])
        self.assertFalse(dam)

        toks, dam = tokenize("3(disz)")
        self.assertEqual(toks, ["3(diš)"])  # one token; sz→š normalisation
        self.assertFalse(dam)

        toks, dam = tokenize("ku₃-babbar")
        self.assertEqual(toks, ["ku3", "babbar"])
        self.assertFalse(dam)

    def test_build_mini_corpus(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            atf, cat = _write_fixtures(tmp)
            catalogue = load_catalogue(cat, "id_text")
            records, exclusions, _unparsed = build_records(atf, catalogue)
            by_id = {r.id: r for r in records}

            self.assertEqual(
                by_id["P000001"].signs,
                [
                    "CU:d",
                    "CU:šul",
                    "CU:gi",
                    "CU:lugal",
                    "CU:uri5",
                    "CU:ki",
                    "CU:ma",
                ],
            )
            self.assertEqual(by_id["P000001"].genre, "seal")
            self.assertEqual(by_id["P000001"].meta["kind"], "A")

            kind_b = [r for r in records if r.meta.get("kind") == "B"]
            self.assertEqual(len(kind_b), 1)
            self.assertEqual(kind_b[0].id, "P000002-seal1")
            self.assertEqual(
                kind_b[0].signs,
                [
                    "CU:ur",
                    "CU:d",
                    "CU:nanše",
                    "CU:dumu",
                    "CU:lu2",
                    "CU:d",
                    "CU:utu",
                ],
            )
            self.assertNotIn("P000002", by_id)

            self.assertEqual(exclusions.get("fake"), 1)
            self.assertEqual(exclusions.get("proto_cuneiform"), 1)

            self.assertFalse(by_id["P000005"].complete)
            self.assertEqual(by_id["P000005"].signs, ["CU:lugal"])

            # Duplicate marking
            all_recs = mark_duplicates(records)
            self.assertEqual(
                {r.id: r for r in all_recs}["P000006"].meta.get("duplicate_of"),
                "P000001",
            )


if __name__ == "__main__":
    unittest.main()
