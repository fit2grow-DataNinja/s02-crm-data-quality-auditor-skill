# Definition of done — Variant 2 synthetic portfolio MVP

**Scope principle:** Match Variant 1's *business audit and reporting* MVP acceptance criteria using a ChatGPT Skill + deterministic Python rather than FastAPI + Open WebUI. Do not require identical infrastructure or production hardening.

## MVP acceptance evidence checklist
- [x] Synthetic Skill runtime can access CSV attachments and invoke deterministic Python (previously exercised; see [validation](validation.md)).
- [x] Python-owned, read-only audit boundary and structured outputs are implemented and committed; AI is limited to explanation, not finding creation.
- [x] Matching rule IDs, severities, issue-level findings, and coverage were reported on the shared synthetic 202/121/92 scenario; clean-checkout parity remains unverified.
- [x] Header-only, missing/invalid schema, core rules and optional association behavior have regression coverage; a local 17-test pass was reported.
- [x] Evaluated rules and unavailable association/freshness/close-date checks are explicit in the audit output design and earlier exercises.
- [ ] Record a consolidated end-to-end ChatGPT demonstration with clear separation of deterministic output and model explanation, suitable for final reviewer sign-off.
- [ ] Complete comparison evidence and review/update the shared portfolio S02 case study.

**Comparison criterion, not an MVP blocker:** Evaluate multi-user installation, distribution, version alignment, deterministic consistency and explanation variability when feasible. Record untested capabilities explicitly; do **not** require successful multi-user deployment to claim synthetic portfolio MVP acceptance. Fresh-checkout test execution remains a recommended reproducibility checkpoint.

**Acceptance status:** Not declared complete by this document update. Checked items identify reported or source-backed evidence, not a new execution or production validation.

## Explicitly out of scope for both variants' portfolio MVP
Real customer CRM data; SEC-001 sensitivity classification, approval and fail-closed enforcement; commercial/production deployment; comprehensive freshness and close-date reconciliation; inference of missing associations from partial exports; additional customer-specific CRM rules; GitHub Actions CI; load/performance testing; hardened operational deployment; scheduled audits, notifications and automated remediation.

## Architecture-specific integration
- **Variant 1:** FastAPI endpoints, multipart uploads, Open WebUI Workspace Tool and Podman/network validation.
- **Variant 2:** ChatGPT Skill invocation, attachment access, Python execution, packaging and installation evidence.

These are different technical acceptance paths to the same audit scenario. Do not transplant Variant 1 API/Podman requirements into Variant 2 or infer Skill distribution guarantees from Variant 1.

## Required for each subsequent change
Define scope and exclusions; use synthetic fixtures only; keep Python findings deterministic; add appropriate regression/negative-path tests; execute and record actual results; update relevant documentation and limitations; request approval before repository changes. **No production-readiness claim.**
