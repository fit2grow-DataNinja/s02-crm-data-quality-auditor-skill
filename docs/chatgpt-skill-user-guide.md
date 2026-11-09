# ChatGPT Skill user guide — S02 Variant 2 (synthetic data only)

**Audience:** Person running the S02 CRM auditor in an eligible ChatGPT environment.  
**Status:** Documented from the version-controlled Skill instructions and previously reported synthetic executions. Exact installation/sharing UI steps and multi-user version management are **not yet verified**.

## 1. What the Skill does
The `s02-crm-auditor` Skill checks explicitly synthetic CRM CSV exports using executable deterministic Python rules. ChatGPT can explain the generated findings, but **Python—not the model—determines issue IDs, severity, counts and coverage**. No live CRM connection, record updates, or email notifications are provided.

Use **synthetic files only**. The SEC-001 sensitivity and manual-approval gate has not been implemented. **Do not upload real customer or sensitive CRM data.**

## 2. Prepare the synthetic inputs
You need two CSV files and may add a third:

| File | Required? | Required header fields |
| --- | --- | --- |
| Contacts | Yes | `Record ID`, `Email` |
| Deals | Yes | `Record ID`, `Deal Name`, `Deal Stage`, `Amount` |
| Associations | No | `Deal Record ID`, `Contact Record ID` |

The `Deal owner` deal column is optional in the input schema but is used to evaluate missing owners according to the provisional rule. For an empty-input trial, download or copy the repository's [synthetic header-only templates](../skill/s02-crm-auditor/assets/templates/). Header-only files produce no record-level findings; that does **not** validate populated CRM data quality.

Preserve CSV headers exactly. Never replace missing user inputs with model-generated records.

## 3. Access the Skill
Use a ChatGPT environment in which `s02-crm-auditor` has already been installed or otherwise made available and can execute its Python scripts and read attachments. **The exact ChatGPT installation, publishing, sharing, workspace permission and version-pinning steps have not been established by a documented multi-user test.** If the Skill is unavailable, request access through the supported Skill installation/distribution path for your environment; do not assume a repository URL alone installs it.

For developers, the version-controlled implementation is [`skill/s02-crm-auditor/`](../skill/s02-crm-auditor/). The developer prerequisites and unverified distribution areas are in [deployment.md](deployment.md).

## 4. Run an audit in ChatGPT
1. Start a conversation in the environment that has the installed Skill.
2. Attach **explicitly synthetic** contacts and deals CSVs. Optionally attach synthetic associations.
3. Use a request such as:

   > Run the S02 CRM Data Quality Auditor Skill on my attached **synthetic** contacts and deals CSV files. The association CSV is optional. Execute the deterministic Python audit, report the command, exit code, stdout/stderr, and show the summary, findings and coverage limits. Do not invent findings.

4. Confirm that the Skill actually executed `scripts/run_audit.py`. If file paths or execution support are missing, the assistant should report the limitation rather than silently simulating a result.
5. Read the produced structured findings and ask for an explanation of the **computed** issues if useful.

The Skill's execution contract is:
```bash
python3 scripts/run_audit.py --contacts <contacts-path> --deals <deals-path> [--associations <associations-path>] --output <output-directory>
```
The actual paths are resolved from the runtime's uploaded files; placeholders are not literal paths.

## 5. Understand the results
- **`summary.json`**: record counts, finding totals, counts by rule/severity, evaluated checks and coverage limitations.
- **`issues.csv`**: issue-level rows identifying the rule, severity, affected CRM object/record/field, observed value and explanation.
- **`report.md`**: human-readable audit summary and rule/coverage interpretation.

A missing deal owner from the relevant stage may be flagged under a **provisional owner-policy hypothesis**, not proof of a business error. A result of **zero findings** means no violations were found among the implemented checks on the supplied synthetic data; it does **not** mean the CRM is clean under every possible rule.

If an associations file is supplied, the Skill checks reference IDs that **appear in that file**; it cannot infer missing relationships from a partial list. Freshness and original close-date reconciliation are **not evaluated** without the required source metadata.

## 6. Troubleshooting and safe behavior

| Situation | What to do or expect |
| --- | --- |
| Contacts or deals attachment missing | Supply the missing **synthetic** CSV; never invent it |
| Incorrect/missing header | Check header spelling against section 2; script should reject invalid schema |
| Python script cannot run or file is inaccessible | Report the execution error and environment limitation; do not present fabricated findings |
| Nonzero exit code or stderr error | Treat as failed execution until corrected, even if AI offers a plausible explanation |
| No findings | Review `evaluated_checks` and unavailable checks; do not infer comprehensive coverage |
| Association export incomplete | Validate references present only; do not infer missing links |
| ChatGPT explanation conflicts with `issues.csv` | Treat Python output as authoritative and flag the explanation for review |
| Real customer or sensitive CRM data | **Do not process** with this MVP; SEC-001 is absent |

## 7. Repeating and comparing runs
Use exactly the same explicitly synthetic input versions and Python rule version; compare rule IDs, record-level issues, severity and coverage. Run timestamps can legitimately differ. AI explanations may vary between conversations even when the deterministic result is identical.

Previously reported evidence: 202 contacts, 121 deals, 92 medium missing-owner findings in the shared synthetic scenario, with issue-level parity against Variant 1; header-only three-file execution produced zero issues; the owner also confirmed successful execution of a 17-test suite from a fresh repository checkout. **Second-user Skill execution with matching audit results has been confirmed by the owner; centrally managed version updates and documented installation procedures have not been verified.** See [validation.md](validation.md).

## 8. Scope and related documentation
This is a **synthetic portfolio MVP**, not a production service. GitHub CI, commercial security, full freshness/close-date logic, scheduled jobs, notification workflows and CRM write-back are intentionally deferred. Do not claim SEC-001 protection or real-customer-data clearance.

- [ChatGPT integration and command details](integration.md)
- [Skill installation and distribution limits](deployment.md)
- [Rule scope and artifacts](service-specification.md)
- [Validation and evidence limitations](validation.md)
- [Variant 1 versus Variant 2 comparison](variant-comparison.md)
- [Single S02 business use-case and two-variant case study](https://github.com/fit2grow-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md)

**Documentation ownership:** This user guide is source-controlled in GitHub. ChatGPT-side guidance should be based on this file; avoid creating an unversioned, conflicting copy.
