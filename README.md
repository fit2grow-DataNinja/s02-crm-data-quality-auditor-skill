# S02 — CRM Data Quality Auditor (ChatGPT Skill / Variant 2)

**Status:** Synthetic-data-only Skill implementation and Python regression tests are version-controlled; audit and parity exercises have been reported. Independent fresh-checkout and multi-user reproducibility remain unverified. **Not production-ready.**

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
- [Skill integration](docs/integration.md) and [installation/distribution](docs/deployment.md) (older setup notes require revision)
- [Security](docs/security.md), [decisions](docs/decisions.md), and [future/commercial backlog](docs/future-improvements-and-commercial-readiness.md)
- [Variant comparison](docs/variant-comparison.md), including unverified multi-user consistency

## Test command
From repository root: `python3 -m unittest discover -s tests -v`. See [validation](docs/validation.md) for evidence limitations.

The shared [S02 portfolio case study](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) is maintained separately.

**Next:** Verify the committed Skill and test suite from a fresh repository checkout using explicitly synthetic inputs.
