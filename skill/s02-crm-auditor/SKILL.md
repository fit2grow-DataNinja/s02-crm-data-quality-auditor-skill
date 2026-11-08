---
name: s02-crm-auditor
description: Run the S02 deterministic CRM data-quality audit on explicitly synthetic contacts and deals CSV attachments, with optional synthetic association CSV. Use when asked to audit synthetic S02 CRM exports or test Variant 2 parity against Variant 1.
---

# S02 CRM Data Quality Auditor

Run only on explicitly synthetic CSV attachments. SEC-001 is not implemented: never accept real customer, production, or sensitive CRM data. No external services or CRM writes.

Resolve actual attachment paths; do not reconstruct file contents from chat. Require contacts and deals files. Associations are optional. Use `python3` to execute `scripts/run_audit.py --contacts <path> --deals <path> [--associations <path>] --output <directory>` from the installed skill directory. Report the exact command, exit code, stdout and stderr. Do not fabricate results or replace script execution with model judgment.

Python output is authoritative for issue counts, IDs, severities and coverage. Explain only the produced findings. State when association, freshness, or close-date checks are unavailable. Pilot policies are provisional. If execution fails, report the error and do not claim an audit succeeded.
