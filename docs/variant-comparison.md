# S02 Variant comparison protocol

| Criterion | Evidence to collect |
| --- | --- |
| Accuracy and coverage | Same rule IDs, record-level findings, severity, checks evaluated/unavailable on shared synthetic inputs |
| Repeatability | Identical deterministic output across repeated runs (excluding run timestamp where applicable) |
| Explanation fidelity | Compare AI statements to machine-generated reports; note omissions/overclaims |
| Operations | Setup requirements, dependencies, supporting services |
| Maintainability | Rule-change and regression-test workflow |
| Security and data boundaries | File access, transfer, approvals, enforcement, absence of SEC-001 |
| **Multi-user reusability and consistency** | Installation/distribution, shared version pinning, upgrade flow, identical findings across users, explanation differences |
| Reproducibility | Another user can follow documented setup and rerun identical synthetic cases |

**Fairness note:** Sharing a deterministic Python engine compares orchestration/integration rather than independent rule-engine correctness. Track exact sample versions and rule versions; do not equate similar AI wording with deterministic consistency. Do not claim a multi-user test was performed without evidence.
