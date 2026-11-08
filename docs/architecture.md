# Architecture — S02 Variant 2

**Implemented synthetic workflow:** explicitly synthetic CRM CSV attachments → ChatGPT Skill instructions/orchestration → deterministic Python audit → structured artifacts → AI explanation.

```text
Synthetic contacts.csv + deals.csv [+ associations.csv]
                      |
           ChatGPT Skill s02-crm-auditor
                      |
     scripts/run_audit.py -> scripts/audit.py
                      |
        Deterministic Python rule engine
                      |
    summary.json + issues.csv + report.md
                      |
         Explanation in ChatGPT chat
```

## Ownership and trust boundaries
- **Python is authoritative:** rules, record-level issues, severities, counts and evaluated/unevaluated coverage derive from the script, not the model.
- **ChatGPT orchestrates/explains:** it resolves attachments, invokes the script and explains produced evidence. Instructions requesting faithful explanation are **not** a software-enforced guarantee of model fidelity.
- **Read only:** no live CRM connection or record-write interface is implemented; outputs are local report artifacts.
- **Data exposure:** Skill access to attachments and hosted model handling do not constitute an implemented sensitivity/approval gate. **SEC-001 is absent; synthetic data only.**

## Scope and coverage limits
Contacts and deals CSVs are required; associations are optional and provide reference validation only. Incomplete relationship exports cannot establish missing associations. Freshness and original close-date reconciliation require source metadata not available in the shared sample. Stage and missing-owner rules are provisional pending business-owner sign-off.

## Validation status
Single-environment runtime/audit exercises, populated synthetic 202/121/92 parity and header-only execution have been previously reported. The owner confirms that a fresh-checkout 17-test regression run succeeded; raw run logs were not supplied. Multi-user installation, version consistency and explanation-faithfulness verification remain untested.

## Variant 1 distinction
Variant 1 uses a standalone FastAPI service, multipart `POST /audit`, and Open WebUI Workspace Tool; Variant 2 executes the Python auditor inside the Skill runtime without operating that service. These are intentionally different integrations for equivalent synthetic business-rule scope. See [comparison](variant-comparison.md).

Commercial release, CI and production controls are deferred; see [future-improvements and commercial-readiness backlog](future-improvements-and-commercial-readiness.md).
