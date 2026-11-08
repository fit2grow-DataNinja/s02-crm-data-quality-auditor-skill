# Validation record — Variant 2

**Status:** Synthetic runtime/audit/parity exercises and a local regression run have been reported; independent fresh-checkout verification and multi-user reproducibility remain outstanding. Do not confuse reported results with independently reproduced results.

## Recorded synthetic evidence
1. **Installed Skill runtime and CSV access:** Previously exercised successfully with explicitly synthetic inputs; not a multi-user installation test.
2. **Populated synthetic parity scenario:** Reported 202 contacts, 121 deals, 92 medium-severity `CRM-DEAL-OWNER-MISSING` issues. Summary and issue-level parity against Variant 1 were reported, with matching results in two ChatGPT conversations. This does not establish identical AI explanations or uniform Skill versions.
3. **Header-only three-file scenario:** User-reported command from `/home/oai/skills/s02-crm-auditor`:
   ```bash
   python3 scripts/run_audit.py --contacts /mnt/data/contacts-template.csv --deals /mnt/data/deals-template.csv --associations /mnt/data/associations-template.csv --output /mnt/data/s02-header-only-test
   ```
   Reported exit code 0, empty stderr, zero contacts/deals/issues/associations, three output artifacts, partial-reference-only association coverage, and freshness/close-date reconciliation not evaluated. See [detailed record](validation/header-only-input-test.md).
4. **Python regression tests:** `tests/test_header_only.py` and `tests/test_audit_rules.py` are committed. A prior local execution was reported as **17 passed, 0 failures, 0 errors** after correcting a synthetic test-data writer; no audit logic change was reported. Command: `python3 -m unittest discover -s tests -v`. This is not evidence of GitHub Actions execution or a clean checkout.

## Coverage and evidence boundaries
- Tests target synthetic empty/valid/invalid input, record IDs, email, deal name, stage, amount, owner, association references, and CLI artifacts.
- Freshness and original close-date reconciliation cannot be evaluated without required source metadata; partial association files cannot justify missing-link inference.
- Historical 202/121/92 parity data is not yet incorporated as a committed fixture-based regression test.
- Fresh-checkout installation, repeatable distribution, version governance across users, negative security enforcement, explanation-faithfulness assessment, and CI are unverified or deferred.
- **SEC-001 is not implemented; synthetic data only.** The presence of tests is not production clearance.

## Next verification
From a fresh Variant 2 checkout, run:
```bash
python3 -m unittest discover -s tests -v
```
Record Python version, commit SHA, stdout/stderr, exit code, actual assertions and any failures. Do not mark this verification complete until executed.
