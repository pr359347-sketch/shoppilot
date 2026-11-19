---
name: etsy-shop-analysis
description: Analyze a shop's exported Etsy CSVs (orders, order items, listings, statements, stats, search terms) from data/exports/<shop>/ — category/SKU-wise sales, best/worst and zero-sale listings, size and price bands that sell, seasonality, country split, repeat buyers — then save a dated report with a prioritized action list. Use when the owner asks for shop analysis or drops new CSVs.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Etsy Shop Analysis

> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Step 1 — Find the data

1. **Connected mode only.** No shop profile in `data/shops/` → stop and tell the owner to run `/connect-shop`. **Check `data/exports/<shop>/` for CSVs first.** If the files this task needs are missing, do not guess or continue on empty data — show the owner the exact export steps for the missing files from `docs/etsy-csv-export-guide.md` (print the relevant section in full, in the owner's language) and wait for them to drop the files. Shop = from the owner; folder = `data/exports/<shop-lowercase>/` (create it if missing).
2. Run the cruncher (handles big files, column detection, and keeps buyer PII out):

```
python scripts/etsy_analyze.py --shop <shop>
```
   It auto-detects file types by header (order items / orders / listings / statement) and prints a markdown summary. Unrecognized CSVs (stats, search terms, ads) are listed with their headers — read those directly with the Read tool.
3. If Python fails, fall back to reading CSVs directly (sample big files; say so).
4. If only some files exist, analyze what's there and list what's missing + what it would unlock:
   - Order Items → what sells (needed for almost everything)
   - Listings → zero-sale listings, listing health
   - Statement → true fees / net margin
   - Stats + search terms (pasted or CSV) → CTR/conversion per listing, proven keywords

## Step 2 — Analysis checklist

Cover each, skip silently if data isn't there:

1. **Topline:** orders, units, revenue, AOV, date range covered, discount/coupon share.
2. **Category/construction split:** tufted / knotted / kilim-flatweave / dhurrie / jute / runner / round / kids / style buckets — revenue, units, share. (Script buckets by title keywords; sanity-check the "other" bucket.)
3. **Best listings:** top 10 by revenue and by units — note what they share (style, color, size, price).
4. **Worst / zero-sale listings:** active listings with 0 sales in the data window → for each bucket decide: `FIX` (good product, bad SEO/photos), `REPRICE`, `MERGE` (duplicate of a better listing), `RETIRE` (let it expire — never mass-delete).
5. **Sizes that sell:** units + revenue by size (from variations). Which standard sizes are missing from bestsellers? Runner/round demand?
6. **Price bands:** <$50, 50–100, 100–200, 200–400, 400–800, 800+ → where orders and revenue concentrate; the "sweet spot".
7. **Seasonality:** month-wise revenue/units; peak months; compare to the Western calendar (Q4 gifting, Jan refresh, spring, Aug back-to-school).
8. **Country split:** US vs UK/DE/FR/NL/CA/AU — any country over-performing → translation / shipping-profile action.
9. **Repeat buyers:** count and revenue share only (no names). If >5% → suggest thank-you coupon / follow-up.
10. **Listing health:** titles >140 or <60 chars, <13 tags, tags >20 chars, <8 photos, duplicate titles/tags, missing SKUs.
11. **Fees (statement):** total fees % of sales, Etsy Ads spend, Offsite Ads fees → real net.
12. **Search terms / stats (if provided):** top converting queries → mark as `proven` in keyword pools; high-impression/low-CTR listings → audit list.

## Step 3 — Report

Save to `data/reports/YYYY-MM-DD_<shop>_shop-analysis.md` (today's date) and show a short version in chat.

Report structure:
```
# <Shop> — Shop Analysis (YYYY-MM-DD)
Data used: files + date range · What's missing
## 1. Summary (5 bullets, owner's language)
## 2. Numbers (tables — English headers)
## 3. What sells / what doesn't (insights)
## 4. Action list — prioritized
| # | Action | Listing(s) | Impact (H/M/L) | Effort (H/M/L) | Skill to use |
## 5. Next data to export
```

Action list rules: max 10 actions; top 3 must be doable this week; each action names specific listings (title short + Listing ID) and the skill that produces the paste-ready fix (`listing-audit-framework`, `pricing-advisor`, `new-product-planner`, …). Typical high-value actions: clone the bestseller into missing sizes/colors, audit high-traffic zero-sale listings, add runner/round versions of winning designs, fix listing-health gaps in bulk.

## Step 4 — Update memory files

- Shop profile: update "Bestsellers & problem listings" and "Current numbers" + latest report path.
- Keyword pools: add proven search terms.
- Do **not** write any buyer names/addresses anywhere.

## Chat reply

In the owner's language, short: 5-bullet summary → top 5 actions → link to the report file → ask which action to start with.
