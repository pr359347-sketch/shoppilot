---
name: etsy-ads-optimizer
description: Analyze Etsy Ads data (CSV or pasted table/screenshot) — ROAS per listing — and produce a pause / scale / fix / watch list plus budget advice. Use when the owner shares Etsy Ads numbers or asks about ads, ROAS or ad budget.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Etsy Ads Optimizer

> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Step 0 — Data check

**Connected mode only.** No shop profile in `data/shops/` → stop and tell the owner to run `/connect-shop`. **Check `data/exports/<shop>/` for CSVs first.** If the files this task needs are missing, do not guess or continue on empty data — show the owner the exact export steps for the missing files from `docs/etsy-csv-export-guide.md` (print the relevant section in full, in the owner's language) and wait for them to drop the files. For this skill the needed data is the Etsy Ads listing table (CSV, pasted table or screenshot all work).

## Inputs

- Etsy Ads listing table: `data/exports/<shop>/ads*.csv` or pasted/screenshot. Expected columns (names vary — map flexibly): listing title/ID, views (impressions), clicks, click rate, orders, revenue, spend, ROAS. Date range must be known — ask if not stated.
- Shop profile pricing inputs (margin). If margin unknown, assume break-even ROAS = 3 and say so.
- Optional: daily budget, the ads "search terms"/keywords view per listing.

## Step 1 — Break-even

`Break-even ROAS = 1 ÷ margin before ads` (margin before ads = (price − making cost − shipping − Etsy fees) ÷ price).
Example: 35% margin → break-even ROAS 2.9. Target ROAS = break-even × 1.3.
Compute per shop (or per category if costs differ) and state it first.

## Step 2 — Classify every advertised listing

Need enough data before judging: **≥ 30 clicks** or spend ≥ 1× the listing's average profit per order. Rugs are high-ticket/slow — prefer a 30–90 day window.

| Bucket | Rule | Action |
|---|---|---|
| 🚀 SCALE | ROAS ≥ target, ≥2 orders | Keep on; raise shop daily budget; clone the listing into more sizes/colors; make sure it has video + all sizes |
| ✅ KEEP | ROAS between break-even and target | Keep; improve conversion (photos/price) to lift |
| 🔧 FIX | Clicks ≥30, CTR good (≥1.5%) but 0–1 orders | Listing page problem → `listing-audit-framework` (price, photos 2–10, shipping, sizes). Pause if not fixed in 2 weeks |
| 🖼 CTR PROBLEM | Views high, CTR <0.8% | Photo 1 / title start / starting price → fix, keep ad running at low cost meanwhile |
| ⛔ PAUSE | Spend ≥ 1.5× avg order profit and 0 orders, or ROAS < 0.5× break-even after ≥50 clicks | Turn ad off for this listing |
| 👀 WATCH | <30 clicks | Not enough data — leave |
| 🌱 ADD | Organic bestsellers not being advertised | Turn ads on |

## Step 3 — Budget & bids

- Etsy Ads has no manual keyword bidding for most shops — levers are: **which listings are on**, **daily budget**, and (if the shop sees it) the per-listing max bid/"prioritize" option. If the owner's dashboard shows bid controls, give per-listing suggestions: SCALE → +20–30%, KEEP → same, FIX → −30%.
- Budget rule: if total ROAS ≥ target and the budget is being fully spent most days → raise budget 25–50% and re-check in 2 weeks. If total ROAS < break-even → cut to SCALE+KEEP listings only before touching budget.
- Seasonal: raise budget 2–3 weeks before Western peaks (early Nov–mid Dec, Jan refresh, Mar–Apr spring); keep made-to-order + international shipping deadlines in mind — pause holiday-gift pushes when delivery before Christmas is no longer possible.
- Offsite Ads are separate (fee on attributed orders) — mention only if statement data shows the fee share.

## Output

1. Summary in the owner's language (3 lines): total spend, revenue, ROAS vs break-even, verdict.
2. Table: `Listing | Views | Clicks | CTR | Orders | Spend | Revenue | ROAS | Bucket | Action`.
3. **Pause list**, **Scale list**, **Fix list** as separate copyable lists (listing title short + ID).
4. Budget recommendation (current → suggested).
5. "Next steps" — 3–5 steps + when to re-check (date).

Save `data/reports/YYYY-MM-DD_<shop>_ads.md`. When the owner reports results after changes, log in `data/learnings.md`.

## Rules

- Never judge on <30 clicks. Never recommend turning off all ads in peak season without data.
- ROAS from Etsy counts all orders within 30 days of a click — mention it's slightly optimistic.
