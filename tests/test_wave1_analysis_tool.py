import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "analyze_wave1_export.py"
spec = importlib.util.spec_from_file_location("wave1_tool", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class Wave1ToolTests(unittest.TestCase):
    def make_row(self, pid, pair, idx, pos="Top", chosen="a.png", free="", hard="0", latency="1000", excluded="0"):
        return {
            "participant_id": pid,
            "candidate_id": pair,
            "protocol_version": "wave1-v0.4",
            "language": "lt",
            "presentation_index": str(idx),
            "top_asset": "a.png",
            "bottom_asset": "b.png",
            "choice_position": pos,
            "chosen_asset": chosen,
            "free_text": free,
            "intensity": "3",
            "hard_to_identify": hard,
            "latency_ms": latency,
            "created_at": "2026-08-18 10:00:00",
            "excluded": excluded,
        }

    def test_complete_session_and_pair_counts(self):
        rows = [self.make_row("p1", pair, i + 1) for i, pair in enumerate(sorted(mod.EXPECTED_PAIRS))]
        report = mod.analyze(rows, set())
        self.assertEqual(report["counts"]["participant_ids"], 1)
        self.assertEqual(report["counts"]["complete_6_of_6_participant_ids"], 1)
        self.assertEqual(sum(p["n_rows"] for p in report["pair_summary"]), 6)

    def test_excluded_rows_are_removed(self):
        rows = [
            self.make_row("p1", "CS-PR-01", 1, excluded="1"),
            self.make_row("p2", "CS-PR-01", 1),
        ]
        report = mod.analyze(rows, set())
        self.assertEqual(report["counts"]["excluded_rows"], 1)
        self.assertEqual(report["counts"]["included_rows"], 1)

    def test_no_clear_choice_does_not_create_asset_choice(self):
        row = self.make_row("p1", "CS-PR-01", 1, pos="No clear choice", chosen="—")
        pair = mod.analyze([row], set())["pair_summary"][0]
        self.assertEqual(pair["no_clear_choice"], 1)
        self.assertEqual(pair["chosen_asset_counts"], {})

    def test_blind_template_hides_canonical_candidate_id(self):
        rows = [self.make_row("p1", "CS-PR-01", 1, free="Because it feels clearer")]
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            coding = td / "coding.csv"
            key = td / "key.json"
            mod.write_blind_coding_package(rows, set(), coding, key)
            text = coding.read_text(encoding="utf-8")
            self.assertNotIn("CS-PR-01", text)
            self.assertIn("PAIR-", text)
            key_data = json.loads(key.read_text(encoding="utf-8"))
            self.assertIn("CS-PR-01", key_data["aliases"].values())


if __name__ == "__main__":
    unittest.main()
