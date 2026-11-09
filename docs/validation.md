# Validation record — Variant 2

**Status:** Synthetic runtime/audit/parity exercises and a local regression run have been reported; a successful fresh-checkout regression run has now been confirmed by the user; its raw execution evidence and centralized version governance remains outstanding. Do not confuse reported results with independently reproduced results.

## Recorded synthetic evidence
1. **Installed Skill runtime and CSV access:** Previously exercised successfully with explicitly synthetic inputs; not a multi-user installation test.
2. **Populated synthetic parity scenario:** Reported 202 contacts, 121 deals, 92 medium-severity `CRM-DEAL-OWNER-MISSING` issues. Summary and issue-level parity against Variant 1 were reported, with matching results in two ChatGPT conversations. The project owner additionally confirmed that a **second ChatGPT user** ran the same Skill successfully and received matching deterministic audit results. This supports cross-user reuse and result parity, but does not establish centrally enforced Skill version updates or identical AI explanations.
3. **Header-only three-file scenario:** User-reported command from `/home/oai/skills/s02-crm-auditor`:
   ```bash
   python3 scripts/run_audit.py --contacts /mnt/data/contacts-template.csv --deals /mnt/data/deals-template.csv --associations /mnt/data/associations-template.csv --output /mnt/data/s02-header-only-test
   ```
   Reported exit code 0, empty stderr, zero contacts/deals/issues/associations, three output artifacts, partial-reference-only association coverage, and freshness/close-date reconciliation not evaluated. See [detailed record](validation/header-only-input-test.md).
4. **Python regression tests:** `tests/test_header_only.py` and `tests/test_audit_rules.py` are committed. A prior local execution was reported as **17 passed, 0 failures, 0 errors** after correcting a synthetic test-data writer; no audit logic change was reported. Command: `python3 -m unittest discover -s tests -v`. This earlier local run is distinct from the subsequently user-confirmed fresh-checkout run.

## Fresh-checkout regression confirmation (user-reported, 2026-11-08)
The project owner explicitly confirmed that running the 17-test Python regression suite from a fresh Variant 2 repository checkout was **successfully executed**. Treat the fresh-checkout regression checkpoint as **completed on user confirmation**, not as an independently observed execution by the assistant. The prior local run was reported as 17 passed with 0 failures/errors; the fresh-checkout run's exact stdout/stderr, exit code, Python version, checkout commit SHA, and per-test transcript were **not supplied**, so do not invent or attribute those details to it. Command intended for this checkpoint: `python3 -m unittest discover -s tests -v`. No GitHub Actions CI was executed.

## Skill documentation integration (user-reported, 2026-11-09)
The approved GitHub user guide was copied into `skill/s02-crm-auditor/references/user-guide.md`, and `SKILL.md` was updated to direct documentation questions to it. A complete updated Skill ZIP was prepared. During the manual update of the existing ChatGPT Skill, the editor's folder-upload operation imported the guide file at the Skill's top level rather than preserving the `references/` folder. The owner confirmed saving the installed `SKILL.md` with a corresponding `user-guide.md` reference. This installed layout differs from the version-controlled package but does not change the auditor.

The owner then supplied the response to a documentation-only prompt in a new Skill-enabled conversation. The response correctly listed contacts and deals as required, associations as optional, all required headers, the optional `Deal owner` column, and synthetic-only restrictions. It explicitly stated that it consulted `s02-crm-auditor/user-guide.md` (section 2) and did not execute the Python audit. **Result: documentation access and answer consistency passed on user-reported evidence.** The assistant did not independently inspect the Skill runtime or execution trace. This checkpoint does not validate centrally managed updates, ZIP-based replacement of an installed Skill, or audit execution.

## Coverage and evidence boundaries
- Tests target synthetic empty/valid/invalid input, record IDs, email, deal name, stage, amount, owner, association references, and CLI artifacts.
- Freshness and original close-date reconciliation cannot be evaluated without required source metadata; partial association files cannot justify missing-link inference.
- Historical 202/121/92 parity data is not yet incorporated as a committed fixture-based regression test.
- Fresh-checkout regression execution is user-confirmed; independent transcript-level reproduction, repeatable installation procedures, centrally managed version/update governance across users, negative security enforcement, explanation-faithfulness assessment, and CI are unverified or deferred.
- **SEC-001 is not implemented; synthetic data only.** The presence of tests is not production clearance.

## Documentation checkpoint
The ChatGPT-facing user guide and its manual documentation-access verification are complete for the Variant 2 MVP on user-reported evidence. If raw fresh-checkout execution logs later become available, append them without changing the user-confirmed status.
