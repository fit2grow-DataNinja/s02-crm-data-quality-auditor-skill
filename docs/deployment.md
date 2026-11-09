# Installation, execution prerequisites and distribution — Variant 2

**Status:** An installed ChatGPT Skill has executed synthetic CRM audits and the GitHub source is version-controlled. Fresh-checkout Python tests were **user-confirmed successful**. Execution by a second ChatGPT user with matching deterministic results is **user-confirmed**. Documented installation steps, packaging/distribution procedures and shared version governance remain **untested or unrecorded**.

## Source layout
- `skill/s02-crm-auditor/SKILL.md` — invocation and safe-execution instructions.
- `skill/s02-crm-auditor/references/user-guide.md` — packaged copy of the approved GitHub user guide (authoritative source: `docs/chatgpt-skill-user-guide.md`).
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

## Manual documentation update (user-reported, 2026-11-09)
The updated Skill package includes `references/user-guide.md` and a reference from `SKILL.md`. The owner manually uploaded the guide into the existing ChatGPT Skill. In the observed editor behavior, uploading a folder flattened its contents, leaving `user-guide.md` at the Skill's top level; the owner therefore updated and saved the installed `SKILL.md` to refer to `user-guide.md`. This is a **user-confirmed manual workaround**, not a verified general installation or publishing procedure.

A subsequent documentation-only prompt returned the correct synthetic CSV requirements, cited the installed `user-guide.md`, and reported no audit execution. This supports documentation accessibility for that installed setup; it does not establish centrally governed updates or automated distribution. The version-controlled package retains the conventional `references/` layout.

## Architecture boundary
Variant 2 invokes Python from the Skill runtime. It does not require the separate FastAPI server, multipart HTTP adapter, Open WebUI setup, or Podman network steps used in Variant 1.

**Synthetic only:** No real customer CRM data. SEC-001 sensitivity classification and approval enforcement are not implemented. No production-readiness claim.

## Deferred improvement: GitHub-to-ChatGPT publishing (Approach B)
Future enhancement only; **not a Variant 2 MVP acceptance criterion** and not required for Variant 1 parity. Maintain the approved user guide in `docs/chatgpt-skill-user-guide.md` as the single authoritative source. On an approved change merged to `main` (or a manually invoked release trigger), a proposed GitHub Actions workflow would copy it into `skill/s02-crm-auditor/references/user-guide.md`, verify identical content, and build a complete Skill ZIP. Publishing that ZIP or updating the existing ChatGPT Skill remains a manual step unless a supported authenticated update interface is established. No CI workflow, automatic publication, or cross-user update propagation has been implemented or tested.
