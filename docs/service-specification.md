# Service specification — Variant 2

## Goal
Run **read-only, deterministic CRM CSV data-quality checks** via an installed ChatGPT Skill and provide AI-assisted explanations grounded in the computed results. Compare equivalent synthetic business-rule scope with Variant 1, without requiring its FastAPI/Open WebUI infrastructure.

## Inputs
- Required explicitly synthetic contacts CSV with `Record ID`, `Email`.
- Required explicitly synthetic deals CSV with `Record ID`, `Deal Name`, `Deal Stage`, `Amount`; `Deal owner` is optional as an input header and supports the missing-owner policy check.
- Optional synthetic associations CSV with `Deal Record ID` and `Contact Record ID`.

## Deterministic outputs
The CLI writes `summary.json`, `issues.csv` and `report.md`. Findings expose rule ID, severity, CRM object, record ID, affected field, observed value and explanation; the summary identifies counts, evaluated checks and coverage limits. ChatGPT may interpret the report but may not compute, change or invent findings.

## Rule scope
Missing/duplicate record IDs; missing/invalid/duplicate contact emails; missing/duplicate deal names; unknown deal stages; missing Negotiation amounts; invalid amounts; missing deal owners from Qualified onward; and unknown contact/deal references in optional association files. Business-rule interpretations (especially owner requirements) are provisional.

## Unavailable evaluations
A partial association list does not prove absent links. Full freshness checks and original close-date reconciliation require reliable source metadata or values that are not in the current inputs. Zero findings are not a claim of exhaustive CRM quality.

## Non-goals
No real customer records; no live CRM reads/writes, automatic remediation, email notifications, CI pipeline, commercial deployment, production hardening, new customer-specific rules, or SEC-001 enforcement. These remain deferred or unimplemented.

## Acceptance and evidence
An installed Skill runtime has been exercised on synthetic CSVs, summary/issue-level parity was reported for the 202/121/92 sample, and the owner confirms successful fresh-checkout regression execution of the 17-test suite. Raw checkout execution logs and multi-user distribution/version evidence are not provided. MVP sign-off and portfolio comparison require documentation of limitations and reviewer acceptance rather than an unsupported production claim. See [validation](validation.md) and [definition of done](definition-of-done.md).
