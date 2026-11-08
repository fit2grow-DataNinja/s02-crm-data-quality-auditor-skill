# S02 Variant 2 — Project status

**Stage:** Synthetic portfolio MVP implementation and comparison evidence; documentation alignment in progress. **Data boundary:** explicitly synthetic CRM CSVs only. **Not production-ready.**

## Goal and architecture
Use a ChatGPT Skill to orchestrate deterministic Python CRM auditing and AI explanation. Compare with the accepted Variant 1 FastAPI/Open WebUI implementation using shared synthetic inputs and rule criteria, without modifying Variant 1.

## Implemented and version-controlled
- `skill/s02-crm-auditor/`: Skill instructions, agent metadata/icon, deterministic Python auditor and CLI, and three header-only CSV templates.
- `tests/test_header_only.py` and `tests/test_audit_rules.py`: 17 synthetic unit/regression cases covering empty inputs, rules, schema rejection, optional associations, and CLI outputs.
- Audit findings are Python-owned; the model may explain but not invent them. No live CRM connection or write capability is part of the implementation.

## Evidence and limitations
- Earlier synthetic audit/parity exercises reported **202 contacts, 121 deals, 92 medium missing-deal-owner findings**, with issue-level parity and matching results in two ChatGPT conversations.
- The header-only three-template execution was reported successful: zero records and issues, all outputs created, partial-reference association coverage.
- Previous local regression-suite execution was reported as **17 tests passed, 0 failures/errors**. The owner subsequently **confirmed successful execution of the regression suite from a fresh Variant 2 GitHub checkout** (2026-11-08). This is user-reported completion, not an assistant-observed run; the exact fresh-checkout log, environment and commit SHA were not supplied. See [validation](docs/validation.md).
- Multi-user installation, sharing, version alignment, and independently captured fresh-checkout evidence remain **untested or unrecorded**. AI explanation fidelity is not guaranteed by Skill instructions.
- SEC-001 sensitivity and approval enforcement are **not implemented**. No real customer CRM data or production claims.

## MVP boundary and deferred work
Equivalent business-rule and reporting scope to Variant 1, with architecture-specific integration: FastAPI/Open WebUI/Podman versus ChatGPT Skill/Python. Comprehensive freshness, close-date reconciliation, missing-association inference from partial exports, customer-specific rule expansion, GitHub CI, load tests, hardened deployment, scheduled audits, notifications, and commercial readiness are deferred. Multi-user capability is a **comparison criterion**, not a required successful multi-user deployment for portfolio MVP acceptance.

## Next tiny action
Review the GitHub-authored [ChatGPT Skill user guide](docs/chatgpt-skill-user-guide.md) and two-variant [portfolio case study](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) for final reviewer sign-off. GitHub remains the authoritative documentation source; reproduce approved guidance in ChatGPT without creating conflicting copies. Fresh-checkout regression execution is user-confirmed, but raw logs remain unavailable.

## References
- [ChatGPT Skill user guide](docs/chatgpt-skill-user-guide.md)
- [Definition of done](docs/definition-of-done.md)
- [Validation](docs/validation.md)
- [Future improvements and commercial readiness](docs/future-improvements-and-commercial-readiness.md)
- [Variant comparison](docs/variant-comparison.md)
- [Variant 1 baseline](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor)
