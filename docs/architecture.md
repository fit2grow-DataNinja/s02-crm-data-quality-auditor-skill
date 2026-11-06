# Architecture — Variant 2

**Provisional target:** synthetic CRM CSV files → ChatGPT Skill instructions/orchestration → deterministic Python audit → structured report → AI explanation.

Python is authoritative for rule decisions and coverage. The model may explain but must not add findings. Skill instructions alone are not an enforcement mechanism for model faithfulness.

The skill runtime's script execution, file handling, and distribution constraints must be verified before treating this as implemented. Do not assume centrally managed distribution or uniform versions across users.

Contrast: Variant 1 exposes the same kind of deterministic audit through FastAPI and the Open WebUI Workspace Tool adapter; Variant 2 aims to avoid that separately running service, subject to runtime support.
