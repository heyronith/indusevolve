import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from indusevolve.schema import Inscription, read_jsonl, write_jsonl


def _valid(**overrides):
    base = dict(
        system="indus",
        id="T-1",
        signs=["IW:740", "IW:2"],
        label="unlabelled",
    )
    base.update(overrides)
    return Inscription(**base)


class TestSchema(unittest.TestCase):
    def test_valid_record_has_no_errors(self):
        self.assertEqual(_valid().validate(), [])

    def test_jsonl_round_trip_with_non_ascii_meta(self):
        record = _valid(meta={"site_note": "Mohenjo-daro, Śiva?"})
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.jsonl"
            n = write_jsonl([record], path)
            self.assertEqual(n, 1)
            loaded = list(read_jsonl(path))
            self.assertEqual(len(loaded), 1)
            got = loaded[0]
            self.assertEqual(got.system, record.system)
            self.assertEqual(got.id, record.id)
            self.assertEqual(got.signs, record.signs)
            self.assertEqual(got.label, record.label)
            self.assertEqual(got.genre, record.genre)
            self.assertEqual(got.direction, record.direction)
            self.assertEqual(got.object_type, record.object_type)
            self.assertEqual(got.site, record.site)
            self.assertEqual(got.complete, record.complete)
            self.assertEqual(got.source, record.source)
            self.assertEqual(got.source_id, record.source_id)
            self.assertEqual(got.meta, record.meta)

    def test_bad_label_reported_and_write_raises(self):
        bad = _valid(label="not-a-label")
        errors = bad.validate()
        self.assertTrue(any("label" in e for e in errors))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.jsonl"
            with self.assertRaises(ValueError):
                write_jsonl([bad], path)

    def test_invalid_signs(self):
        cases = [
            [],
            ["740"],
            ["IW:"],
            ["iw:740"],
        ]
        for signs in cases:
            with self.subTest(signs=signs):
                errors = _valid(signs=signs).validate()
                self.assertTrue(errors)

    def test_duplicate_system_id_raises(self):
        a = _valid()
        b = _valid()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "out.jsonl"
            with self.assertRaises(ValueError):
                write_jsonl([a, b], path)


if __name__ == "__main__":
    unittest.main()
