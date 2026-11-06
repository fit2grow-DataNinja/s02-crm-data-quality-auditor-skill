# Service specification — Variant 2

## Goal
Provide read-only, deterministic CRM CSV data-quality auditing through a reusable ChatGPT Skill, with AI-generated explanations separated from computed findings.

## Inputs and outputs
Target the same synthetic contacts, deals, and optional associations CSVs as Variant 1. Aim to preserve rule IDs, severities, record-level issues, summary counts, and explicit evaluated/unavailable checks. Confirm output artifact and file-access capabilities in an execution proof of concept before locking the interface.

## Non-goals
No CRM writes, customer records, new business rules, inferred missing associations from partial exports, or production readiness. Freshness and close-date reconciliation remain unavailable without requisite source data.

## Acceptance
Documented synthetic end-to-end run, tests against shared cases, clear limitations, user repeatability, and measured comparison with Variant 1.
