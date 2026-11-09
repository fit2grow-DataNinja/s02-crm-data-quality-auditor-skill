# ChatGPT Skill integration — Variant 2

**Status:** The installed Skill has been exercised with explicitly synthetic CSVs. Populated audit/parity results and a successful fresh-checkout 17-test regression execution have been reported by the project owner. Successful second-user Skill execution with matching audit results has been confirmed by the owner. Centrally controlled version updates and repeatable installation procedures have **not** been verified.

## Supported execution flow
1. Make sure the `s02-crm-auditor` Skill is available in the current ChatGPT environment. Availability and installation mechanisms vary; do not assume it is installed for other users.
2. Supply explicitly **synthetic** `contacts.csv` and `deals.csv`. A synthetic `associations.csv` may be supplied optionally. Repository header-only templates are under `skill/s02-crm-auditor/assets/templates/`.
3. Ask ChatGPT to run the S02 CRM audit on the attached synthetic files and identify which attachment is contacts, deals, and (if present) associations.
4. The Skill resolves the actual attachment paths, then runs deterministic Python, not prompt-only validation:
   ```bash
   python3 scripts/run_audit.py --contacts <contacts-path> --deals <deals-path> [--associations <associations-path>] --output <output-directory>
   ```
   This command is executed from the installed Skill directory; replace placeholders with paths discovered in the actual runtime. The Skill requires the command, exit code, stdout, and stderr to be reported.
5. Review `summary.json`, `issues.csv` and `report.md` from the output directory. The model may explain the Python-generated findings, but cannot add findings or claim checks that were not executed.

## Required inputs and known coverage
- Contacts required headers: `Record ID,Email`.
- Deals required headers: `Record ID,Deal Name,Deal Stage,Amount`; `Deal owner` is audited when present.
- Optional association headers: `Deal Record ID,Contact Record ID`.
- Associations check references **present** in the optional file only. A partial export cannot prove which deals lack links.
- Freshness and original close-date reconciliation are **not evaluated** without necessary source metadata.

The header-only three-file test is documented at [validation/header-only-input-test.md](validation/header-only-input-test.md). The reported populated synthetic parity case produced 202 contacts, 121 deals, and 92 medium-severity missing-owner findings; these findings reflect a provisional business rule rather than confirmed CRM mistakes.

## Errors and safe interpretation
- If either required attachment is missing, request only the missing **synthetic** file. Do not invent it.
- On missing/invalid CSV schema or execution failure, show the error and do not claim audit success.
- For zero findings, state that **implemented, evaluated checks** produced zero findings; never claim comprehensive CRM quality validation.
- If the Skill cannot run scripts or access files, report the environment limitation; do not simulate deterministic execution.
- Do not connect to a live CRM, send owner notifications, update records, or upload real customer data. SEC-001 is **not implemented**.

## Evidence boundaries
Observed or previously reported single-environment Skill audit execution is **not** proof of repeatable setup across users. Install/share/version procedures require independent testing. See [deployment](deployment.md), [validation](validation.md), and [comparison](variant-comparison.md).
