---
name: multi-shop-compare
description: Compare 2 or more shops side by side using their exported CSVs — sales, conversion, AOV, top categories, listings vs sales efficiency — and decide which shop deserves which product and where the owner should focus. Use when the owner asks to compare shops or asks which shop to focus on.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Multi-Shop Compare

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Step 1 — Data

1. Shops: the ones the owner names; default = all shops marked primary in `data/shops/`. **Connected mode only.** No shop profile in `data/shops/` → stop and tell the owner to run `/connect-shop`. **Check `data/exports/<shop>/` for CSVs first.** If the files this task needs are missing, do not guess or continue on empty data — show the owner the exact export steps for the missing files from `docs/etsy-csv-export-guide.md` (print the relevant section in full, in the owner's language) and wait for them to drop the files. Needs at least 2 connected shops with Order Items exports. Any shop with a profile in `data/shops/` can be included.
2. Run for all at once:

```
python scripts/etsy_analyze.py --shop <shop1> --shop <shop2>
```
   (prints one summary per shop + a side-by-side table). Read each shop's profile and latest report in `data/reports/` too.
3. **Compare the same date window.** If shops have different export ranges, restrict to the overlapping period (`--from YYYY-MM-DD --to YYYY-MM-DD`) and say so.
4. Visits/conversion need Stats numbers (not in the CSV downloads). If missing, ask the owner to paste from each shop's Stats page for the same range: visits, orders, conversion rate, revenue — continue without them if not given.

## Step 2 — Side-by-side table

| Metric | Shop A | Shop B | … | Winner |
|---|---|---|---|---|
| Revenue · Orders · Units | | | | |
| AOV | | | | |
| Active listings | | | | |
| **Revenue per active listing** (efficiency) | | | | |
| % listings with ≥1 sale | | | | |
| Top 3 categories (share) | | | | |
| Best-selling sizes | | | | |
| Price sweet spot | | | | |
| US share / top EU countries | | | | |
| Repeat buyer share | | | | |
| Visits · Conversion (if given) | | | | |
| Fees % / Ads spend (if statements) | | | | |
| Peak months | | | | |

## Step 3 — Decisions

1. **Shop roles** — one line each: what this shop is *winning* at (category × price band × size).
2. **Product placement matrix** — which product type goes to which shop:

| Product type / style | Best shop | Why (data) | Also list in |
|---|---|---|---|

   Rules: a product goes where the same category already converts and matches the shop's niche + price band. Avoid listing the identical product with identical photos/title in two shops (cannibalization + Etsy duplicate-shop policy risk) — if cross-listing, use different photos, title angle and sizes.
3. **Overlap check** — same/similar listings across shops competing for the same keywords → pick the owner shop for each.
4. **Focus recommendation** — split of the owner's weekly effort (e.g. "70% Shop A, 30% Shop B") with the reason, and top 3 actions per shop.
5. **Transfer learnings** — what works in shop A that shop B should copy (sizes, price points, photo style, keywords).

## Step 4 — Save + reply

- Save `data/reports/YYYY-MM-DD_<shopA>-vs-<shopB>_compare.md`.
- Chat (owner's language): verdict in 3 lines → table → focus split → top actions.
- No buyer PII anywhere. No invented numbers — blank cell + "data needed" instead.
