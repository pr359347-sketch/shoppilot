---
description: Reports — daily log, evening summary, weekly report, occasion reminders, experiment check-ins
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

Arguments (optional): `$ARGUMENTS` — `daily` · `evening` (default) · `weekly` · `reminders` · `experiments`.

1. Connected mode needed for numbers; reminders work in generic mode too.
2. Delegate to **ops-agent** with the type. For `weekly` and `experiments`, ops-agent asks the master for **analytics-agent** numbers (before/after windows per `core/experiment-tracker`).
3. Experiments at +30 d → learning appended to `data/learnings.md`.
4. Reply in Hinglish, short; reports saved in `data/reports/` or `data/ops/`.
