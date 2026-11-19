<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Experiment Tracker — every approved change is an experiment

Every `done` proposal in `data/approvals/` is tracked. Results feed `data/learnings.md`, and future suggestions must read those learnings first.

## When it runs
- `/report`, `/start` (nudge), `ops-agent` evening summary → list experiments with a check due today or overdue.
- Owner says "check experiments" / "kya kaam kiya".

## Check-in (at +7, +14, +30 days)
1. Need fresh exports/stats covering the after-window. Missing → ask with the exact export steps; don't guess.
2. Same-length windows: **before** = N days before `done` date, **after** = N days after. Same metrics as the baseline: impressions/views, visits/sessions, CTR, orders, conversion, revenue, ROAS/ACoS where relevant. Use `analytics-agent` for the numbers.
3. Seasonality guard: if the after-window includes an occasion peak (Black Friday, Christmas…) note it and compare with a control (similar listings not changed) when possible.
4. Verdict: **WORKED** (main metric +15% or more and not explained by seasonality/control) · **DIDN'T WORK** (flat or down) · **UNCLEAR** (< 30 visits or < 3 orders in either window, or confounded).
5. Write the check-in into the proposal file (table: metric · before · after · change %).

## At +30 days (final)
Append to `data/learnings.md` in its format:
```
### YYYY-MM-DD | <shop> | <area>
- Change: <ID> — <what>
- Result: <metric before → after, window>
- Verdict: WORKED / DIDN'T WORK / UNCLEAR
- Rule going forward: <one line>
```
Same verdict on the same kind of change 3+ times → promote to "Standing rules" in learnings.

## Rollback suggestion
DIDN'T WORK at +14 or +30 with a clear drop → create a new proposal to roll back (old values are in the file).

## Using learnings
Before proposing any change, agents check learnings: a standing rule against it → don't propose (or say why this case is different).
