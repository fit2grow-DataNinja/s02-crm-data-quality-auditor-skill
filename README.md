# S02 — CRM Data Quality Auditor (ChatGPT Skill / Variant 2)

**Status:** Documentation baseline established; Skill runtime and implementation not yet validated. **Private development repository; synthetic data only.**

This project explores a reusable ChatGPT Skill that orchestrates **deterministic Python CRM CSV validation** and asks AI to explain—not invent—the audit findings. It is compared with the [accepted Variant 1 FastAPI/Open WebUI auditor](https://github.com/bb-DataNinja/s02-crm-data-quality-auditor).

The shared [S02 portfolio case study](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md) lives in AI Services Portfolio, not here.

## Project docs

- [Project status](PROJECT-STATUS.md) — next small action and evidence
- [Specification](docs/service-specification.md) and [architecture](docs/architecture.md)
- [Skill integration](docs/integration.md) and [installation/distribution](docs/deployment.md)
- [Validation](docs/validation.md) and [definition of done](docs/definition-of-done.md)
- [Security boundaries](docs/security.md) and [design decisions](docs/decisions.md)
- [Variant comparison protocol](docs/variant-comparison.md) — includes multi-user access, version governance, and deterministic-result consistency

## Next action
Verify the intended Skill environment can read synthetic CSV attachments and execute a small deterministic Python script. Do not treat unverified runtime or multi-user capabilities as implemented.

**No customer CRM data.** SEC-001 sensitivity and approval enforcement is not implemented; this project is not production-ready.
