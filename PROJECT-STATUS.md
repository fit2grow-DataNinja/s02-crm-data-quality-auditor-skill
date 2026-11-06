# S02 Variant 2 — Project status

**Stage:** Repository and documentation baseline. **Implementation:** not started. **Data boundary:** synthetic CRM CSVs only.

## Goal
Build a ChatGPT Skill that orchestrates deterministic Python CRM data-quality checks and uses AI to explain the resulting report. Compare it with the accepted Variant 1 FastAPI/Open WebUI implementation using shared synthetic inputs.

## Decisions
- Separate private repository for Variant 2. The AI Services Portfolio remains the home of the S02 case study and eventual comparison.
- Approach B: executable Python owns validation; model text does not determine rule outcomes.
- Match Variant 1 rule IDs, provisional policy, optional association checks, and explicit evaluated/unavailable coverage.
- Compare multi-user reusability: sharing/access, version alignment, update management, same findings for identical synthetic inputs and rule versions, and explanation variability.
- Synthetic-only. SEC-001 sensitivity/approval gate remains unimplemented.

## Evidence
- GitHub repository initialized with Python `.gitignore` and README.
- No skill execution, tests, installation, or multi-user sharing verified.

## Next tiny action
Verify the target ChatGPT Skill runtime's ability to read synthetic attachments and execute a minimal deterministic Python script before porting audit rules.

## Reference
- [Variant 1 baseline](https://github.com/bb-DataNinja/s02-crm-data-quality-auditor)
- [Portfolio case study](https://github.com/bb-DataNinja/ai-services-portfolio/blob/main/case-studies/S02-crm-data-quality-auditor.md)
