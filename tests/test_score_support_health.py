import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "score_support_health.py"
spec = importlib.util.spec_from_file_location("score_support_health", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ScoreSupportHealthTests(unittest.TestCase):
    def test_urgent_old_ticket_with_due_followup_scores_red(self):
        row = {
            "priority": "urgent",
            "status": "open",
            "age_hours": "30",
            "replies": "8",
            "waiting_on_customer": "false",
            "csat": "2",
            "follow_up_due_hours": "1",
        }

        score = module.row_risk(row)

        self.assertGreaterEqual(score, 30)
        self.assertEqual(module.risk_band(score), "red")

    def test_waiting_on_customer_reduces_risk(self):
        base = {
            "priority": "normal",
            "status": "pending",
            "age_hours": "24",
            "replies": "3",
            "csat": "",
            "follow_up_due_hours": "4",
        }
        waiting = dict(base, waiting_on_customer="true")
        not_waiting = dict(base, waiting_on_customer="false")

        self.assertLess(module.row_risk(waiting), module.row_risk(not_waiting))

    def test_summarize_groups_by_owner(self):
        rows = [
            {"owner": "Avery", "priority": "low", "status": "solved", "age_hours": "1", "replies": "1", "waiting_on_customer": "false", "csat": "5", "follow_up_due_hours": "99", "topic": "x", "ticket_id": "1"},
            {"owner": "Avery", "priority": "urgent", "status": "open", "age_hours": "40", "replies": "9", "waiting_on_customer": "false", "csat": "1", "follow_up_due_hours": "1", "topic": "y", "ticket_id": "2"},
        ]

        _, summary = module.summarize(rows)

        self.assertEqual(summary["Avery"]["tickets"], 2)
        self.assertEqual(summary["Avery"]["red"], 1)


if __name__ == "__main__":
    unittest.main()
