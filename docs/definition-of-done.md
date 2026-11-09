# Definition of done — Variant 2 synthetic portfolio MVP

**Scope principle:** Match Variant 1's *business audit and reporting* MVP acceptance criteria using a ChatGPT Skill + deterministic Python rather than FastAPI + Open WebUI. Do not require identical infrastructure or production hardening.

## MVP acceptance evidence checklist
- [x] Synthetic Skill runtime can access CSV attachments and invoke deterministic Python (previously exercised; see [validation](validation.md)).
- [x] Python-owned, read-only audit boundary and structured outputs are implemented and committed; AI is limited to explanation, not finding creation.
- [x] Matching rule IDs, severities, issue-level findings, and coverage were reported on the shared synthetic 202/121/92 scenario; clean-checkout parity remains unverified.
- [x] Header-only, missing/invalid schema, core rules and optional association behavior have regression coverage; a local 17-test pass was reported.
- [x] Evaluated rules and unavailable association/freshness/close-date checks are explicit in the audit output design and earlier exercises.
- [x] Accept the recorded end-to-end synthetic ChatGPT audit demonstrations and Python-owned findings as the portfolio demonstration evidence. No new consolidated transcript was independently captured; the earlier demonstrations and their limitations are documented in [validation](validation.md).
- [x] Complete the documented two-variant comparison and close the shared portfolio S02 case study on the available evidence, explicitly retaining untested areas.

**Comparison criterion, not an MVP blocker:** Evaluate multi-user installation, distribution, version alignment, deterministic consistency and explanation variability when feasible. Record untested capabilities explicitly; do **not** require successful multi-user deployment to claim synthetic portfolio MVP acceptance. Fresh-checkout test execution remains a recommended reproducibility checkpoint.

**Acceptance status (2026-11-09): Portfolio MVP accepted and closed for Variant 2, alongside the previously accepted Variant 1.** Checked items refer to source-backed or user-reported evidence, not newly observed executions. The previously open demonstration and comparison review items are closed by portfolio-scope acceptance of the documented evidence, not by claiming new tests or an independent end-to-end transcript. No production-readiness claim.

## Explicitly out of scope for both variants' portfolio MVP
Real customer CRM data; SEC-001 sensitivity classification, approval and fail-closed enforcement; commercial/production deployment; comprehensive freshness and close-date reconciliation; inference of missing associations from partial exports; additional customer-specific CRM rules; GitHub Actions CI; load/performance testing; hardened operational deployment; scheduled audits, notifications and automated remediation.

## Architecture-specific integration
- **Variant 1:** FastAPI endpoints, multipart uploads, Open WebUI Workspace Tool and Podman/network validation.
- **Variant 2:** ChatGPT Skill invocation, attachment access, Python execution, packaging and installation evidence.

These are different technical acceptance paths to the same audit scenario. Do not transplant Variant 1 API/Podman requirements into Variant 2 or infer Skill distribution guarantees from Variant 1.

## Required for each subsequent change
Define scope and exclusions; use synthetic fixtures only; keep Python findings deterministic; add appropriate regression/negative-path tests; execute and record actual results; update relevant documentation and limitations; request approval before repository changes. **No production-readiness claim.**
