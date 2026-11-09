# Installation, execution prerequisites and distribution — Variant 2

**Status:** An installed ChatGPT Skill has executed synthetic CRM audits and the GitHub source is version-controlled. Fresh-checkout Python tests were **user-confirmed successful**. Execution by a second ChatGPT user with matching deterministic results is **user-confirmed**. Documented installation steps, packaging/distribution procedures and shared version governance remain **untested or unrecorded**.

## Source layout
- `skill/s02-crm-auditor/SKILL.md` — invocation and safe-execution instructions.
- `skill/s02-crm-auditor/scripts/audit.py` — deterministic audit checks and reporting.
- `skill/s02-crm-auditor/scripts/run_audit.py` — CLI entry point.
- `skill/s02-crm-auditor/assets/templates/` — header-only synthetic CSV templates.
- `tests/` — synthetic Python regression suite.

## Prerequisites and locally reproducible checks
- A ChatGPT execution environment that can access the installed Skill and explicitly synthetic CSV attachments, and can invoke Python scripts.
- Python 3 capable of running the standard-library-only auditor.
- For a repository checkout, run from repository root:
  ```bash
  python3 -m unittest discover -s tests -v
  ```
  Successful fresh-checkout execution of the 17-case suite was **confirmed by the user**, but raw logs, exact Python version, and tested checkout SHA were not provided. CI is deliberately deferred.

## ChatGPT installation/distribution — unverified
The project does **not** claim a universal ChatGPT UI installation procedure, centrally enforced version pin, organization rollout mechanism, or simultaneous availability to multiple users. Actual installation controls depend on the supported ChatGPT Skill environment and account. Do not publish guessed UI steps.

A future distribution acceptance exercise should record: installation method, Skill code/version identifier, initial execution from another account/environment using explicitly synthetic files, output parity (excluding timestamps), updates and rollback. These are **comparison/evaluation items**, not a requirement to operate a production deployment for the portfolio MVP.

## Architecture boundary
Variant 2 invokes Python from the Skill runtime. It does not require the separate FastAPI server, multipart HTTP adapter, Open WebUI setup, or Podman network steps used in Variant 1.

**Synthetic only:** No real customer CRM data. SEC-001 sensitivity classification and approval enforcement are not implemented. No production-readiness claim.
