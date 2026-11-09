# S02 — CRM Data Quality Auditor (ChatGPT Skill / Variant 2)

**Status:** **Portfolio MVP complete and closed (2026-11-09).** Deterministic synthetic-data Skill implementation, regression tests, reported parity and user-confirmed cross-user reuse are documented. Independent execution transcripts and centrally governed version updates remain unavailable or unverified. **Not production-ready.**

This project implements a reusable ChatGPT Skill that invokes **deterministic Python CRM CSV validation** and asks AI to explain—not invent—the findings. It is compared with the [accepted Variant 1 FastAPI/Open WebUI auditor](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor).

## MVP scope
- Read-only synthetic contacts/deals CSV audit, with optional association references.
- Python-owned rule IDs, severity, record-level issues, counts, and evaluated/unavailable coverage.
- Structured summary, issue CSV, Markdown report, and ChatGPT explanation.
- Synthetic rule/CLI regression tests; GitHub CI is **deferred**, as in Variant 1.

No real CRM data, live CRM connection/write, SEC-001 enforcement, complete freshness/close-date reconciliation, or inferred missing associations from partial exports. No production-readiness claim.

## Project docs
- [Project status](PROJECT-STATUS.md) and [validation](docs/validation.md)
- [Specification](docs/service-specification.md), [architecture](docs/architecture.md), and [definition of done](docs/definition-of-done.md)
- [ChatGPT user and execution guide](docs/chatgpt-skill-user-guide.md), [Skill integration](docs/integration.md), and [installation/distribution](docs/deployment.md)
- [Security](docs/security.md), [decisions](docs/decisions.md), and [future/commercial backlog](docs/future-improvements-and-commercial-readiness.md)
- [Variant comparison](docs/variant-comparison.md), including unverified multi-user consistency

## Test command
From repository root: `python3 -m unittest discover -s tests -v`. See [validation](docs/validation.md) for evidence limitations.

The shared [S02 portfolio case study](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) is maintained separately.

**Closure:** The owner confirmed successful fresh-checkout regression execution and documentation access in the installed Skill; see the [validation record](docs/validation.md) for evidence boundaries. The GitHub-to-ChatGPT publishing workflow (Approach B) and CI remain deferred improvements, not MVP requirements.
