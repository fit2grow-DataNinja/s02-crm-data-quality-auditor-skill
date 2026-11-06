# Decisions — Variant 2

## V2-001 — Separate repository
Keep Variant 2 in its own private repository; maintain a single S02 case study in AI Services Portfolio.

## V2-002 — Deterministic Python Skill (Approach B)
Prefer a ChatGPT Skill that runs deterministic Python validation over prompt-only rule execution. Verify file and script capability before committing implementation.

## V2-003 — Comparison fairness
Use matching synthetic inputs and rule criteria. If Variant 2 reuses Variant 1's rule engine, distinguish orchestration comparison from independent rule-engine accuracy comparison.

## V2-004 — Multi-user reuse and consistency
Compare installation and access, same rule/version distribution, update governance, deterministic output parity across users, and variability of AI explanations. Never infer uniform version control from simple shareability.

## V2-005 — Scope boundary
SEC-001 deferred; synthetic-only until security design, enforcement, and testing support another decision.
