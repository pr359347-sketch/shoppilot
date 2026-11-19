# Approval Flow — proposal → owner ok → execute → log

Used by the **master** for every live change. Subagents only list "PROPOSALS NEEDED"; the master turns them into cards.

## 1. Proposal card (show in chat, Hinglish labels, English content)

```
🟡 PROPOSAL <ID>  ·  <shop> · <platform> · <area>
KYA:      <exact change — field: old → new, or "new listing", "pause ad X">
KYUN:     <the data/reason in 1–2 lines, with source>
IMPACT:   <expected effect + how we'll measure it (metric, 7/14/30 d)>
RISK:     <what could go wrong — ranking reset, margin, policy> · Level: low / med / high
ROLLBACK: <how to undo — old values saved in the proposal file>
MODE:     ShopPilot karega (Etsy/Shopify)  |  Aap karo — steps neeche (eBay/Amazon)
→ Reply: "ok <ID>"  /  "no <ID>"  /  "change <ID>: …"
```

- **ID** = `P-YYMMDD-NN` (e.g. `P-260101-01`).
- Group related changes on one listing into one card; never bundle different listings into one "ok".
- Before showing: check `data/ops/freeze.md` — frozen → show the card as `⛔ FROZEN` with no ok option.

## 2. Save
Write `data/approvals/<ID>.md` from `templates/proposal.md` with status `pending`, the full **old values** (for rollback) and new values.

## 3. Owner reply
| Reply | Action |
|---|---|
| `ok <ID>` (or "ok" when exactly one card is open) | status → `approved` (+ date). Execute (Etsy/Shopify) or show owner steps (eBay/Amazon). |
| `no <ID>` | status → `declined` + the reason if given → append a one-line learning to `data/learnings.md` ("owner declined X because Y"). |
| `change <ID>: …` | revise, new version of the same ID, ask again. |
| "ok all" | only for cards shown in the same message; list the IDs back before executing. |

## 4. Execute (Etsy / Shopify only)
1. Connector available (e.g. Shopify) → use it. Else built-in browser, owner already logged in.
2. Safe speed from AGENT-RULES §5: one change, verify on the page, 45–90 s pause, next.
3. Stop on captcha / unusual activity / login prompt / unexpected page → tell the owner, mark `blocked`.
4. After saving: re-open the listing and confirm the new value is live. Screenshot path or "verified" note in the file.
5. status → `done` + timestamp. Start the experiment: fill **baseline** (last 30 d metrics from the latest export, or "baseline needed" if none) and the check dates (+7, +14, +30).

eBay / Amazon: status → `owner-to-do`; when the owner says done → `done` + baseline as above.

## 5. Report
One line per executed change: `✅ P-260101-01 done — Etsy listing <short name>: title updated, verified live.` Then the ops daily log gets the line.
