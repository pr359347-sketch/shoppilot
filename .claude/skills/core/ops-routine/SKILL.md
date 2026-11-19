# Ops Routine — log, summaries, freeze, reminders

Files (all private, created from `templates/` if missing):
- `data/ops/daily-log.md` ← `templates/daily-log.md`
- `data/ops/freeze.md` ← `templates/freeze.md`
- `data/approvals/<ID>.md` ← `templates/proposal.md`

## Daily log entry
```
## YYYY-MM-DD
- Done: <ID / task, one line each>
- Proposals: new <IDs> · approved <IDs> · declined <IDs>
- Issues: <blocked items, platform warnings>
- Numbers (if new export): orders <n>, revenue <x> — per shop, never mixed
```

## Evening summary (chat, Hinglish, ≤ 8 lines)
Aaj kya hua · pending approvals (IDs) · experiment checks due · kal ke top 3 · active freezes · next occasion countdown.

## Weekly report (`/report weekly`)
`data/reports/YYYY-MM-DD_weekly.md` — per shop section: done changes, experiment verdicts, numbers vs last week, what's next. Plus one "Overall" line only if 2+ shops and the owner wants it.

## Freeze rules (`/freeze`)
`data/ops/freeze.md` table:
```
| Shop | Area (all / prices / listings / ads / photos / messages) | From | To | Reason |
```
Common reasons: peak sale running (don't touch titles during Black Friday week), vacation mode, platform review, new-listing settle period (no edits for 7 days after a big rewrite). While frozen: research + drafts allowed, no executable proposals. Expired rows → mark `ended`.

## Occasion reminders
From `data/settings.md` occasion calendar (buyers' market only). For each occasion within 60 days: peak date, last order date for delivery (processing + shipping time from the shop profile), list-by / optimize-by / promote-by dates using the timing rules in `core/seasonal-planner` (list D−10 wk, optimize D−8 wk, promote D−6 wk → last order date) — one rule, don't invent another. Black Friday / Cyber Week: also suggest a freeze on titles/tags during the sale week.
