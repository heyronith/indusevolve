import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from indusevolve.loaders.indus_website import _tuples, parse, to_records
from indusevolve.loaders.cisi_mayig import load_dir
from indusevolve.schema import Inscription
from indusevolve.stats import describe


MINI_SQL = """
INSERT INTO SITE (SITEID, NAME) VALUES
("SI1","Test Site");

INSERT INTO GLYPH (GLYPHID, UNICODE) VALUES
(0, "<br>"),
(5,"A"),
(17,"B"),
(740,"JAR");

INSERT INTO SEAL (SEALID, SITEID, MATERIAL, CISI, MUSEUM, WIDTH, HEIGHT, THICKNESS) VALUES
(1, "SI1", "Steatite", "T-1", NULL, 1.0, 1.0, 1.0),
(2, "SI1", "Clay", "T-2", NULL, 1.0, 1.0, 1.0),
(3, "SI1", "Clay", "T-3", NULL, 1.0, 1.0, 1.0);

INSERT INTO INSCRIPTION (SEALID, ISCOMPLETE, DIRECTION) VALUES
(1, "Y", "R/L"),
(2, "Y", "R/L"),
(3, "N", "R/L");

INSERT INTO ICONOGRAPHY(SEALID, DESCRIPTION) VALUES
(1, "Bull");

INSERT INTO GLYPHSEQUENCE (SEALID, GLYPHID, IDX) VALUES
(1,740,0), (1,17,1), (1,5,2),
(2,740,0), (2,0,1), (2,17,2),
(3,0,0);
"""


class TestLoaders(unittest.TestCase):
    def test_tuples_respects_commas_and_parens_in_quotes(self):
        body = '("SI1","Kot Diji (site)"),("SI2","a, b")'
        self.assertEqual(
            _tuples(body),
            [["SI1", "Kot Diji (site)"], ["SI2", "a, b"]],
        )

    def test_indus_website_reading_order_and_line_breaks(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "population-script.sql"
            path.write_text(MINI_SQL, encoding="utf-8")
            db = parse(path)
            records = to_records(db)
            by_id = {r.id: r for r in records}
            self.assertEqual(set(by_id), {"IW-1", "IW-2"})
            self.assertEqual(by_id["IW-1"].signs, ["IW:5", "IW:17", "IW:740"])
            self.assertEqual(by_id["IW-2"].meta["n_lines"], 2)
            self.assertEqual(by_id["IW-2"].signs, ["IW:17", "IW:740"])

    def test_cisi_mayig_reverses_graphemes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sub").mkdir()
            side = [
                {
                    "id": "M-174A",
                    "description": "unicorn seal",
                    "graphemes": [
                        {"id": "P324"},
                        {"id": "P175"},
                        {"id": "P050"},
                    ],
                }
            ]
            (root / "sub" / "m174.json").write_text(json.dumps(side), encoding="utf-8")
            records = load_dir(root)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0].signs, ["P:P050", "P:P175", "P:P324"])
            self.assertEqual(records[0].genre, "seal")

    def test_describe_hapax(self):
        records = [
            Inscription(system="t", id="1", signs=["A", "B"], label="unlabelled"),
            Inscription(system="t", id="2", signs=["A", "C"], label="unlabelled"),
            Inscription(system="t", id="3", signs=["A", "D"], label="unlabelled"),
        ]
        stats = describe(records)
        # A appears 3 times; B,C,D once each → 3 hapax types
        self.assertEqual(stats["hapax_types"], 3)
        self.assertEqual(stats["sign_types"], 4)
        self.assertEqual(stats["texts"], 3)
        self.assertEqual(stats["tokens"], 6)


if __name__ == "__main__":
    unittest.main()
