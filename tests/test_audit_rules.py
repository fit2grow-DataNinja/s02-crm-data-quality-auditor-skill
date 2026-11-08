"""Deterministic S02 Variant 2 audit rule and schema regression tests.

All inputs are created in temporary directories and are explicitly synthetic.
"""
import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skill' / 's02-crm-auditor' / 'scripts'
RUNNER = SCRIPTS / 'run_audit.py'
spec = importlib.util.spec_from_file_location('s02_audit_under_test', SCRIPTS / 'audit.py')
audit_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit_module)

CONTACT_COLUMNS = ['Record ID', 'Email']
DEAL_COLUMNS = ['Record ID', 'Deal Name', 'Deal Stage', 'Amount', 'Deal owner']
ASSOC_COLUMNS = ['Deal Record ID', 'Contact Record ID']


def write_csv(path, columns, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


class AuditRulesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.contacts = self.root / 'contacts.csv'
        self.deals = self.root / 'deals.csv'
        self.associations = self.root / 'associations.csv'
        self.contact_rows = [{'Record ID': 'C1', 'Email': 'one@example.test'}]
        self.deal_rows = [{'Record ID': 'D1', 'Deal Name': 'Synthetic deal', 'Deal Stage': 'Lead Identified', 'Amount': '100', 'Deal owner': ''}]

    def run_audit(self, contacts=None, deals=None, associations=None, contact_columns=None, deal_columns=None, assoc_columns=None):
        write_csv(self.contacts, contact_columns or CONTACT_COLUMNS, self.contact_rows if contacts is None else contacts)
        write_csv(self.deals, deal_columns or DEAL_COLUMNS, self.deal_rows if deals is None else deals)
        if associations is not None:
            write_csv(self.associations, assoc_columns or ASSOC_COLUMNS, associations)
        return audit_module.audit(self.contacts, self.deals, self.associations if associations is not None else None, run_time='2026-01-01T00:00:00+00:00')

    def assert_rules(self, expected, **kwargs):
        summary, issues = self.run_audit(**kwargs)
        actual = {rule: sum(issue['rule_id'] == rule for issue in issues) for rule in expected}
        self.assertEqual(actual, expected, issues)
        self.assertEqual(summary['issues_total'], len(issues))
        return summary, issues

    def test_clean_records(self):
        summary, issues = self.run_audit()
        self.assertEqual(issues, [])
        self.assertEqual((summary['contacts_checked'], summary['deals_checked']), (1, 1))
        self.assertEqual(summary['coverage']['contact_associations'], 'not_evaluated_no_association_export')
        self.assertNotIn('CRM-ASSOCIATION-DEAL-UNKNOWN', summary['evaluated_checks'])

    def test_missing_and_duplicate_record_ids(self):
        contacts = [{'Record ID': '', 'Email': 'a@example.test'}, {'Record ID': 'C2', 'Email': 'b@example.test'}, {'Record ID': 'C2', 'Email': 'c@example.test'}]
        self.assert_rules({'CRM-RECORD-ID-MISSING': 1, 'CRM-RECORD-ID-DUPLICATE': 2}, contacts=contacts)

    def test_missing_invalid_and_duplicate_emails(self):
        contacts = [{'Record ID': 'C1', 'Email': ''}, {'Record ID': 'C2', 'Email': 'not-an-email'}, {'Record ID': 'C3', 'Email': 'X@Example.test'}, {'Record ID': 'C4', 'Email': 'x@example.test'}]
        self.assert_rules({'CRM-EMAIL-MISSING': 1, 'CRM-EMAIL-INVALID': 1, 'CRM-EMAIL-DUPLICATE': 2}, contacts=contacts)

    def test_missing_and_duplicate_deal_names(self):
        deals = [dict(self.deal_rows[0], **{'Record ID': 'D1', 'Deal Name': ''}), dict(self.deal_rows[0], **{'Record ID': 'D2', 'Deal Name': 'Same'}), dict(self.deal_rows[0], **{'Record ID': 'D3', 'Deal Name': 'same'})]
        self.assert_rules({'CRM-DEAL-NAME-MISSING': 1, 'CRM-DEAL-NAME-DUPLICATE': 2}, deals=deals)

    def test_unknown_stage(self):
        self.assert_rules({'CRM-STAGE-UNKNOWN': 1}, deals=[dict(self.deal_rows[0], **{'Deal Stage': 'Not A Stage'})])

    def test_negotiation_amount_missing(self):
        self.assert_rules({'CRM-NEGOTIATION-AMOUNT-MISSING': 1}, deals=[dict(self.deal_rows[0], **{'Deal Stage': 'Negotiation', 'Amount': '', 'Deal owner': 'Owner A'})])

    def test_invalid_amounts(self):
        amounts = ['abc', '-1', 'NaN', 'Infinity']
        deals = [dict(self.deal_rows[0], **{'Record ID': f'D{i}', 'Deal Name': f'Deal {i}', 'Amount': amount}) for i, amount in enumerate(amounts)]
        self.assert_rules({'CRM-AMOUNT-INVALID': 4}, deals=deals)

    def test_comma_separated_amount_is_accepted(self):
        summary, issues = self.run_audit(deals=[dict(self.deal_rows[0], Amount='1,200.50')])
        self.assertEqual(summary['issues_total'], 0, issues)

    def test_owner_required_at_qualified_or_later(self):
        deals = [dict(self.deal_rows[0], **{'Record ID': f'D{i}', 'Deal Name': f'Deal {i}', 'Deal Stage': stage}) for i, stage in enumerate(audit_module.STAGES)]
        summary, issues = self.run_audit(deals=deals)
        owners = [issue for issue in issues if issue['rule_id'] == 'CRM-DEAL-OWNER-MISSING']
        self.assertEqual(len(owners), len(audit_module.STAGES) - 1)
        self.assertTrue(all(issue['severity'] == 'medium' for issue in owners))
        self.assertEqual(summary['by_rule']['CRM-DEAL-OWNER-MISSING'], 6)

    def test_valid_association_and_partial_coverage(self):
        summary, issues = self.run_audit(associations=[{'Deal Record ID': 'D1', 'Contact Record ID': 'C1'}])
        self.assertEqual(issues, [])
        self.assertEqual(summary['coverage']['known_associations_in_file'], 1)
        self.assertEqual(summary['coverage']['contact_associations'], 'partial_reference_only_no_missing_association_inference')
        self.assertIn('CRM-ASSOCIATION-DEAL-UNKNOWN', summary['evaluated_checks'])

    def test_unknown_association_references(self):
        self.assert_rules({'CRM-ASSOCIATION-DEAL-UNKNOWN': 1, 'CRM-ASSOCIATION-CONTACT-UNKNOWN': 1}, associations=[{'Deal Record ID': 'UNKNOWN-D', 'Contact Record ID': 'UNKNOWN-C'}])

    def test_missing_contacts_header_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Contacts export requires'):
            self.run_audit(contact_columns=['Record ID'])

    def test_missing_deals_header_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Deals export requires'):
            self.run_audit(deal_columns=['Record ID', 'Deal Name', 'Deal Stage'])

    def test_missing_association_header_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Association file requires'):
            self.run_audit(associations=[], assoc_columns=['Deal Record ID'])

    def test_no_csv_header_rejected(self):
        self.contacts.write_text('', encoding='utf-8')
        write_csv(self.deals, DEAL_COLUMNS, self.deal_rows)
        with self.assertRaisesRegex(ValueError, 'No CSV header'):
            audit_module.audit(self.contacts, self.deals)

    def test_cli_outputs_match_summary_and_issues(self):
        write_csv(self.contacts, CONTACT_COLUMNS, [{'Record ID': 'C1', 'Email': ''}])
        write_csv(self.deals, DEAL_COLUMNS, self.deal_rows)
        output = self.root / 'out'
        proc = subprocess.run([sys.executable, str(RUNNER), '--contacts', str(self.contacts), '--deals', str(self.deals), '--output', str(output)], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stderr, '')
        payload = json.loads(proc.stdout)
        self.assertEqual(payload['summary']['issues_total'], 1)
        self.assertEqual(payload['issues'][0]['rule_id'], 'CRM-EMAIL-MISSING')
        self.assertEqual(json.loads((output / 'summary.json').read_text())['issues_total'], 1)
        with (output / 'issues.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['rule_id'], 'CRM-EMAIL-MISSING')
        self.assertIn('CRM-EMAIL-MISSING', (output / 'report.md').read_text())


if __name__ == '__main__':
    unittest.main()
