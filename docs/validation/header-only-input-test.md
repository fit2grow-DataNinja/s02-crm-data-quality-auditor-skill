# S02 Variant 2 — Header-only input validation

## Purpose

Validate that the installed S02 CRM Data Quality Auditor accepts the three explicitly synthetic, header-only CSV input templates without schema errors.

## Evidence provenance

Execution was performed in a separate ChatGPT conversation and its results were supplied by the project owner on 2026-11-08. This document records **reported execution evidence**, not an independently rerun test in this repository. The working installed Skill implementation is not yet committed to this repository.

## Inputs

- `contacts-template.csv`: `Record ID,Email`
- `deals-template.csv`: `Record ID,Deal Name,Deal Stage,Amount,Deal owner`
- `associations-template.csv`: `Deal Record ID,Contact Record ID`

All files were header-only and explicitly synthetic.

## Reported command

Working directory: `/home/oai/skills/s02-crm-auditor`

```bash
python3 scripts/run_audit.py \
  --contacts /mnt/data/contacts-template.csv \
  --deals /mnt/data/deals-template.csv \
  --associations /mnt/data/associations-template.csv \
  --output /mnt/data/s02-header-only-test
```

Standard output and error were captured separately by the shell.

## Expected and reported results

| Metric | Expected | Reported |
| --- | --- | --- |
| Exit code | 0 | 0 |
| Contacts checked | 0 | 0 |
| Deals checked | 0 | 0 |
| Issues total | 0 | 0 |
| Schema errors | None | None |
| Stderr | Empty | Empty |
| Known associations | 0 | 0 |

Reported `by_rule` and `by_severity` were both empty objects. All three templates were accepted. Generated outputs: `summary.json`, `issues.csv`, and `report.md`.

Reported run timestamp (UTC): `2026-11-08T18:27:02.366320+00:00`.

## Coverage reported

- `contact_associations`: `partial_reference_only_no_missing_association_inference`
- `known_associations_in_file`: `0`
- `freshness`: `not_evaluated_no_extract_timestamp`
- `close_date_source_reconciliation`: `not_evaluated_no_original_value_in_export`

The two association reference-validation checks were registered, but no populated associations were exercised.

## Limits and follow-up

This is an **empty-input schema baseline only**. It does not establish behavior for populated rows, malformed headers, invalid association references, or edge cases. Automated unit and integration tests are still missing from Variant 2. SEC-001 sensitivity and approval enforcement is not implemented; use only explicitly synthetic data. This evidence does not establish production readiness.

Suggested future test: automate this header-only baseline once the working Skill implementation is committed.
