# S02 — CRM Data Quality Auditor
## ChatGPT Skill / Variant 2

A completed **synthetic-data portfolio MVP** demonstrating deterministic CRM data checks with AI-assisted explanation through a ChatGPT Skill and Python.

This repository contains the Variant 2 implementation. The portfolio-level use case compares it with a separate FastAPI/Open WebUI implementation.

## Business problem

CRM data issues can reduce confidence in pipeline reporting and create manual review work. S02 explores how to identify specific, reviewable findings in CRM CSV exports and explain them in business language, while keeping audit decisions in deterministic code.

## Solution

The Skill invokes Python to audit synthetic contacts and deals CSV files, with an optional associations file. The Python audit produces structured findings and report artifacts; the Skill presents the results and asks the conversational model to explain them.

**Python determines the audit findings; the AI explains the supplied results.** The workflow does not connect to or edit a CRM. The separation of audit computation and explanation does not guarantee that every model explanation will be faithful; automated explanation verification is not implemented.

## Demonstrated capabilities

- Deterministic validation of selected contact, deal, and association fields.
- Python command-line audit execution through the ChatGPT Skill.
- Structured summary, issue CSV, and Markdown report outputs.
- Coverage reporting that identifies checks not fully evaluated.
- Regression tests for audit rules, input handling, and generated artifacts.
- Reported issue-level parity with Variant 1 on the shared synthetic case.

The shared synthetic scenario recorded **202 contacts, 121 deals, and 92 medium-severity missing-owner findings**. These are review flags under a provisional policy rule, not confirmed business errors.

## Validation

The project includes a 17-test Python regression suite and documented synthetic Skill execution scenarios. See the [validation record](docs/validation.md) for details.

## Scope and limitations

- Synthetic data only. **Do not use real or sensitive customer CRM data.**
- SEC-001 sensitivity tagging and manual approval are **not implemented**.
- The missing-owner rule is provisional and requires business-policy confirmation.
- Partial association exports cannot establish that all relationships are present.
- Comprehensive freshness and original close-date reconciliation require source data not available in the current exports.
- AI explanation faithfulness is not independently verified.
- Centralized Skill release and version-update governance are not established.
- This MVP is not production-ready, commercially validated, or evidence of GDPR compliance or tenant isolation.

See [security status](docs/security.md) for the current data-handling boundary.

## Repository navigation

- [Project status](PROJECT-STATUS.md)
- [Service specification](docs/service-specification.md)
- [Architecture and integration boundaries](docs/architecture.md)
- [ChatGPT user and execution guide](docs/chatgpt-skill-user-guide.md)
- [Skill integration](docs/integration.md)
- [Installation and distribution](docs/deployment.md)
- [Validation evidence](docs/validation.md)
- [Security status](docs/security.md)
- [Decisions](docs/decisions.md)
- [Future improvements and commercial-readiness backlog](docs/future-improvements-and-commercial-readiness.md)
- [Variant comparison](docs/variant-comparison.md)

## Related portfolio materials

- [S02 portfolio use case and two-variant comparison](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md)
- [S02 portfolio service overview](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/services/S02.md)
- [Variant 1 — FastAPI and Open WebUI](https://github.com/fit2grow-DataNinja/s02-crm-data-quality-auditor)
- [Portfolio repository](https://github.com/fit2grow-DataNinja/ai-services-portfolio)
