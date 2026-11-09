# Future improvements and commercial readiness — S02 Variant 2

**Status:** Planning backlog; proposals are not implemented or verified unless separate evidence says otherwise.  
**Scope:** S02 Variant 2 (ChatGPT Skill + deterministic Python). Synthetic CRM data only at the current MVP stage. **Not production-ready.**

## Product vision and decision filter

**S02 Variant 2 is a lightweight, explainable, human-supervised CRM data-quality workflow that can be adapted to specific business rules without requiring a large enterprise data-quality platform.**

This vision governs the current MVP and all future improvements. Before accepting an enhancement, ask:

1. **Lightweight:** Does it minimize infrastructure, dependencies, deployment and maintenance burden?
2. **Explainable:** Can every finding be traced to a deterministic rule, source record and supporting evidence?
3. **Human-supervised:** Are business judgments and consequential actions subject to explicit human review and approval?
4. **Adaptable:** Can business-specific rules be configured or extended without substantial redevelopment?
5. **Practical:** Does it materially improve detection, understanding, prioritization or resolution of CRM data-quality issues?
6. **Focused:** Is its value proportionate to complexity, rather than recreating an enterprise data-quality suite?

Reject, defer or simplify proposals that do not pass this filter. Commercial readiness means meeting applicable safety and operational requirements, **not** adding enterprise-platform features for their own sake.

## Scope boundaries

- **Portfolio MVP:** Demonstrate deterministic CRM auditing via a reusable ChatGPT Skill, with explainable results on explicitly synthetic exports. Current evidence includes a reported successful header-only input test and earlier synthetic-data audit/parity exercises; see [validation](validation.md) and [header-only test](validation/header-only-input-test.md).
- **Product improvements:** Optional, incremental capabilities that advance the vision and are justified by user needs.
- **Commercial readiness:** Deployment-specific controls and verification required before processing real customer CRM data or offering an operational service. Not all controls imply an enterprise architecture.

Do not treat proposed functionality as implemented, or a passing MVP test as commercial readiness.

## Candidate improvements — prioritized by fit, not committed delivery order

| Candidate | Intended value | Lightweight implementation principle | Acceptance evidence needed |
| --- | --- | --- | --- |
| Approach B: GitHub-to-ChatGPT Skill publishing | Keep the approved GitHub user guide authoritative while reducing manual package drift; **deferred beyond portfolio MVP** | On approved merge or manual release, copy `docs/chatgpt-skill-user-guide.md` to Skill `references/user-guide.md`, compare contents, package the full Skill; publish manually unless a supported update interface exists | Verified package contents and documented, authorized update/rollback procedure; no automatic ChatGPT publishing assumed |
| GitHub CI regression automation | Run existing Python tests on code changes; **deferred beyond portfolio MVP, as in Variant 1** | Minimal GitHub Actions workflow using standard-library unittest | Passing clean-checkout CI run and maintained workflow |
| Versioned configurable business rules | Adapt rules, stages, severities and thresholds to a customer | Small validated configuration file; explicit defaults; no arbitrary executable rules | Repeatable tests showing rule changes and explainable outcomes |
| Structured, actionable issue register | Make findings easy to identify, review and resolve | Stable issue IDs, record references, rule ID, severity, evidence, run timestamp, reviewer state; simple export first | Sample review workflow tested with synthetic cases |
| Scheduled rule-based execution | Detect issues regularly (e.g. daily) | Prefer a minimal scheduler and repeatable batch execution over a heavyweight orchestration platform | Reliable repeated synthetic runs, failure reporting, rerun behavior |
| Human validation and approval | Distinguish genuine business issues, exceptions and approved actions | Explicit states, reviewer identity, timestamps and approval evidence; no AI-inferred approval | Tests for approve, reject, exception, and unauthorized action paths |
| Approved owner notifications | Notify responsible deal owners only about reviewer-approved issues | Minimal authenticated email integration; preview and approve recipients/content; no sends without authorization | Synthetic end-to-end notification tests, permission and duplicate-send tests |
| Resolution and recheck tracking | Show whether approved issues were corrected | Link stable issues across runs; avoid premature CRM write-back | Synthetic issue lifecycle and recurrence tests |
| Clearer explanations and summaries | Reduce reviewer effort | AI may summarize deterministic evidence but cannot create or alter findings | Human evaluation and tests for unsupported claims |

### Example future workflow: detect → review → approve → notify → verify

1. Run deterministic audit on an authorized schedule.
2. Produce an issue register identifying the record, rule, severity, evidence and responsible owner (where reliably available).
3. A designated reviewer validates the business relevance of each finding; record decisions such as **confirmed**, **accepted exception**, or **needs investigation**.
4. Only after explicit, recorded approval may the system prepare and send a notification to the appropriate owner. Confirm recipient, content and authorization; prevent duplicate or unintended sends.
5. Re-run checks and track whether the issue is resolved, persists or recurs.

**Design boundary:** The Python audit engine owns findings; human reviewers own business validation and approval; software-enforced controls own notification authorization. An AI explanation or suggestion is never approval. The workflow is a proposed improvement, not an implemented capability.

### Avoid by default

- A general-purpose workflow orchestration suite, unless a simpler scheduler demonstrably fails.
- A complex multi-tenant data platform, broad BI stack, or unnecessary custom UI.
- Automatic CRM record modifications or unsupervised outbound communications.
- AI-generated rule violations that cannot be reproduced by deterministic checks.
- Large-scale integration breadth before a specific use case is validated.

## Commercial readiness — release gates, not optional feature ideas

The required controls depend on the eventual deployment model, customer requirements and data flows. **Real customer CRM data must not be processed under the current synthetic-only MVP.**

| Area | Work to define and verify before applicable real-world deployment |
| --- | --- |
| SEC-001 and data sensitivity | Implement sensitivity classification, explicit approval and fail-closed enforcement; review what may reach AI providers. **SEC-001 is not implemented.** |
| Privacy and data governance | Define lawful basis, retention/deletion, processing roles, residency and contractual obligations as applicable. |
| Identity, access and approvals | Authenticate users, authorize reviewers and senders, log decisions and prevent bypass of human approval. |
| Integration and secrets | Protect credentials and email/CRM access; apply least privilege and secure transport; prevent sensitive logging. |
| Operational reliability | Reproducible installation, versioning, monitoring, scheduled-run failure handling, retries, idempotency and rollback where relevant. |
| Software quality and security | Automated regression and adverse-input tests, dependency checks, safe file handling and bounded resource usage. |
| Business acceptance | Validate actual customer rules, false-positive handling, notification policy and measurable workflow benefit with authorized stakeholders. |
| Support and delivery | Document onboarding, operating responsibilities, incident handling and maintenance appropriate to the chosen offering. |

Commercial release requires evidence for the applicable gates; a roadmap entry or code alone is not proof.

## Current gaps and evidence boundaries

**Scope parity:** Variant 1 and Variant 2 target the same synthetic CRM audit business rules, record-level outputs, and coverage disclosures. Variant 1's FastAPI/Open WebUI/Podman integration and Variant 2's Skill/Python runtime have different technical validation needs. Neither variant requires GitHub CI, production hardening, comprehensive freshness/close-date reconciliation, or full association completeness inference for portfolio MVP acceptance.

- The installed Skill implementation (instructions, Python scripts, agent metadata, icon) and three header-only templates have been committed to the Variant 2 repository.
- Synthetic unit/regression tests are committed (17 cases across header-only and rule/CLI coverage); a prior local 17-test pass was reported. Fresh-checkout regression execution was user-confirmed, without raw logs, tested SHA or environment details; GitHub CI has **not** been performed and remains deferred beyond the portfolio MVP.
- A second ChatGPT user successfully ran the Skill with matching results (owner-confirmed), and the owner confirmed a fresh-checkout test run. Centrally aligned Skill versions, automated packaging/publishing, and repeatable installation/release procedures remain untested or incompletely documented. Successful multi-user deployment is a comparison topic, **not** an additional portfolio MVP blocker.
- Edge-case coverage and SEC-001 enforcement are incomplete.
- The reported header-only test validates empty synthetic schema acceptance. Separate committed Python tests exercise populated association references and invalid schemas; this is not exhaustive malformed-input or security testing.
- No scheduled execution, persistent issue register, reviewer approval workflow, email notification or resolution tracking is currently claimed.

## Portfolio closure
S02 Variant 2's synthetic portfolio MVP was closed on 2026-11-09 alongside Variant 1. This backlog remains open only for separately approved post-MVP improvements; none of its entries is a condition of the completed MVP. See [project status](../PROJECT-STATUS.md) and [validation](validation.md).

## Product discovery and change control

For each proposed improvement, record the user problem, evidence of demand, simplest viable design, dependencies, security implications, measurable acceptance criteria and test evidence. Implement incrementally and reassess the product-vision filter after each step. Preserve the distinction between **proposed**, **implemented**, **tested**, and **commercially approved**.

## Related documents

- [Definition of done](definition-of-done.md): portfolio MVP acceptance
- [Service specification](service-specification.md): supported behavior and scope
- [Security](security.md): security limitations and SEC-001 status
- [Validation](validation.md): executed/reported evidence
- [Project status](../PROJECT-STATUS.md): current progress and next action

This document is a planning reference, not a change to the MVP acceptance criteria.
