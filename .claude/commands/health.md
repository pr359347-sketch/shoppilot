---
description: Monthly health check for a shop — platform checklist with green/amber/red and Top 5 actions
---

Arguments (optional): `$ARGUMENTS` — shop name.

1. Connected only. Pick the shop; `platform:` decides the agent.
2. Exports first: last 30 d + previous 30 d. Missing → steps from `docs/<platform>-csv-export-guide.md`, wait.
3. Delegate to **<platform>-agent** with `.claude/skills/core/health-check/SKILL.md` (checklist = "Monthly health check" in its `PLATFORM.md`). Run **analytics-agent** in parallel for the MoM numbers and **ops-agent** for experiments due.
4. Combine → score, 🔴 items, Top 5 actions → proposal cards for fixes.
