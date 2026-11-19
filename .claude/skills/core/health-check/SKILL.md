# Monthly Health Check (`/health`)

Run once a month per shop, by that shop's platform agent. Uses the **"Monthly health check"** section of the platform's `PLATFORM.md` as the checklist.

## Steps
1. Exports needed: last 30 days + previous 30 days (stats/traffic, orders, listings; ads if running). Missing → export steps, wait.
2. Go through every checklist item in the platform's section. Each gets 🟢 / 🟡 / 🔴 with the number behind it.
3. Month-over-month: traffic, CTR, conversion, orders, revenue, AOV, ads ROAS/ACoS, account-health metrics.
4. Experiments: list `done` proposals from the month with their latest verdict (`core/experiment-tracker`).
5. Learnings check: anything that contradicts a standing rule?

## Output
Save `data/reports/YYYY-MM-DD_<shop>_health.md`:
```
HEALTH: <shop> · <platform> · <month>     Score: <🟢 count>/<total>
| Area | Status | Number | Fix |
TOP 5 ACTIONS
```
Reply with the score, the 🔴 items, and TOP 5 ACTIONS. Fixes that change the shop → proposals.
