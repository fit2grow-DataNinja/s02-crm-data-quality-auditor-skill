"""S02 Variant 2: deterministic header-only CSV regression test."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "s02-crm-auditor"
TEMPLATES = SKILL / "assets" / "templates"
RUNNER = SKILL / "scripts" / "run_audit.py"


class HeaderOnlyRegressionTest(unittest.TestCase):
    def test_empty_templates_are_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "output"
            command = [
                sys.executable, str(RUNNER),
                "--contacts", str(TEMPLATES / "contacts-template.csv"),
                "--deals", str(TEMPLATES / "deals-template.csv"),
                "--associations", str(TEMPLATES / "associations-template.csv"),
                "--output", str(output),
            ]
            result = subprocess.run(command, text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stderr, "")
            payload = json.loads(result.stdout)
            summary = payload["summary"]
            self.assertEqual(summary["contacts_checked"], 0)
            self.assertEqual(summary["deals_checked"], 0)
            self.assertEqual(summary["issues_total"], 0)
            self.assertEqual(summary["by_rule"], {})
            self.assertEqual(summary["by_severity"], {})
            self.assertEqual(payload["issues"], [])
            self.assertEqual(summary["coverage"]["contact_associations"],
                             "partial_reference_only_no_missing_association_inference")
            self.assertEqual(summary["coverage"]["known_associations_in_file"], 0)
            self.assertEqual(summary["coverage"]["freshness"],
                             "not_evaluated_no_extract_timestamp")
            self.assertEqual(summary["coverage"]["close_date_source_reconciliation"],
                             "not_evaluated_no_original_value_in_export")
            for name in ("summary.json", "issues.csv", "report.md"):
                self.assertTrue((output / name).is_file(), name)
            self.assertEqual(json.loads((output / "summary.json").read_text())["issues_total"], 0)
            self.assertEqual((output / "issues.csv").read_text().count("\n"), 1)


if __name__ == "__main__":
    unittest.main()
