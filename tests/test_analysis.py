"""All records below are artificial; no participant data is used."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("qa_analysis", ROOT / "analysis" / "analyze.py")
qa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qa)


def record(**changes):
    value = {"protocol_version": "0.1.0", "is_synthetic": True, "consent": True, "adult": True, "eligible_experience": True, "P01": 3}
    value.update(changes)
    return value


class AnalysisTests(unittest.TestCase):
    def test_schema_item_count(self):
        self.assertEqual(len(qa.ITEMS), 22)
        self.assertEqual(len(qa.CONTEXT), 8)
        self.assertTrue(set(qa.CORE).issubset(qa.ITEMS))

    def test_accepts_valid_record(self):
        self.assertEqual(qa.validate_record(record()), record())

    def test_rejects_direct_identifiers(self):
        with self.assertRaises(ValueError):
            qa.validate_record(record(email="blocked"))

    def test_rejects_boolean_frequency(self):
        with self.assertRaises(ValueError):
            qa.validate_record(record(P01=True))

    def test_rejects_out_of_range(self):
        with self.assertRaises(ValueError):
            qa.validate_record(record(P01=5))

    def test_rejects_wrong_version(self):
        with self.assertRaises(ValueError):
            qa.validate_record(record(protocol_version="unknown"))

    def test_rejects_missing_required_metadata(self):
        value = record()
        del value["consent"]
        with self.assertRaises(ValueError):
            qa.validate_record(value)

    def test_denominator_excludes_unknown(self):
        rows = [record() for _ in range(30)] + [record(P01="DK", P02=2) for _ in range(10)]
        result = qa.marginal(rows, "P01")
        self.assertEqual(result["valid_n"], 30)
        self.assertEqual(result["counts"]["DK"], 10)
        self.assertEqual(result["frequent_or_always_share"], 1.0)

    def test_absent_optional_is_skip(self):
        result = qa.marginal([record() for _ in range(25)], "role")
        self.assertEqual(result["counts"]["SKIP"], 25)

    def test_small_cell_suppresses_entire_table(self):
        result = qa.marginal([record() for _ in range(25)] + [record(P01=1)], "P01")
        self.assertEqual(result["status"], "withheld")
        self.assertNotIn("counts", result)
        self.assertNotIn("n", result)
        self.assertNotIn("frequent_or_always_share", result)

    def test_small_valid_denominator_suppressed(self):
        rows = [record() for _ in range(10)] + [record(P01="DK", P02=2) for _ in range(30)]
        self.assertEqual(qa.marginal(rows, "P01")["status"], "withheld")

    def test_ineligible_rows_excluded(self):
        rows = [record() for _ in range(30)] + [record(consent=False) for _ in range(5)]
        result = qa.summarize(rows, True)
        self.assertEqual(result["audit"]["counts"], {"included": 30, "excluded": 5})
        self.assertEqual(result["marginals"]["P01"]["n"], 30)

    def test_no_core_observation_is_ineligible(self):
        self.assertFalse(qa.eligible(record(P01="NA")))

    def test_rejects_mixed_origins(self):
        with self.assertRaises(ValueError):
            qa.summarize([record(), record(is_synthetic=False)], True)

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            qa.summarize([], True)

    def test_rejects_no_eligible_records(self):
        with self.assertRaises(ValueError):
            qa.summarize([record(adult=False)], True)

    def test_pair_table_has_only_valid_pairs(self):
        rows = []
        for predictor in (0, 2, 4):
            for outcome in (0, 4):
                rows.extend(record(T01=predictor, P01=outcome) for _ in range(10))
        rows.extend(record(T01="DK") for _ in range(10))
        result = qa.pair_table(rows, "T01", "P01")
        self.assertEqual(result["paired_valid_n"], 60)
        self.assertEqual(result["outcome_high_share_by_predictor"]["0_1"], 0.5)

    def test_rejects_repository_output(self):
        with self.assertRaises(ValueError):
            qa.ensure_external(ROOT / "outputs" / "unsafe.json")

    def test_demo_is_deterministic_and_not_findings(self):
        first, second = qa.demo_records(), qa.demo_records()
        self.assertEqual(first, second)
        result = qa.summarize(first, True)
        self.assertTrue(result["is_synthetic"])
        self.assertIn("NOT STUDY FINDINGS", result["notice"])
        self.assertTrue(result["human_disclosure_review_required"])

    def test_summary_does_not_mutate_inputs(self):
        rows = qa.demo_records()
        before = copy.deepcopy(rows)
        qa.summarize(rows, True)
        self.assertEqual(rows, before)

    def test_cli_demo_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "demo.json"
            command = [sys.executable, str(ROOT / "analysis" / "analyze.py"), "--demo", "--out", str(output)]
            first = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertTrue(json.loads(output.read_text())["is_synthetic"])
            second = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(second.returncode, 2)


if __name__ == "__main__":
    unittest.main()
