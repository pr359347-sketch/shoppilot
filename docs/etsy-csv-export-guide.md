<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Etsy — How to Export Your Data

Skills show the relevant section of this file to the owner whenever a needed file is missing from `data/exports/<shop>/`. Export while logged in to the shop the data belongs to.

## Where files go

```
data/exports/<shop>/     ← every CSV for that shop (folder name = shop name in lowercase)
```
- No need to rename files — the agent recognizes them by their column headers.
- Keep old files and add new ones; duplicate orders are removed automatically.
- Everything in `data/` is private and git-ignored. Order files contain buyer names and addresses — never share this folder.

## 1. Listings — needed for: zero-sale listings, listing health, audits

1. Etsy → **Shop Manager → Settings → Options → Download Data** tab.
2. Under **Currently for Sale Listings** click **Download CSV**.
3. File: `EtsyListingsDownload.csv` → put in `data/exports/<shop>/`.

## 2. Order Items — needed for: almost all sales analysis (most important file)

1. Same page: **Shop Manager → Settings → Options → Download Data**.
2. Under **Orders**: CSV Type = **Order Items**, choose the **Year**, leave **Month** empty (= full year).
3. Click **Download CSV** → `EtsySoldOrderItems<year>.csv`.
4. Repeat for the previous year too (two years are needed to see seasonality).

## 3. Orders — optional (order totals, shipping, coupons)

Same as above with CSV Type = **Orders** → `EtsySoldOrders<year>.csv`.

## 4. Monthly statement — needed for: real fees, net margin, pricing accuracy

1. **Shop Manager → Finances → Monthly statements**.
2. Open a month → **Download CSV** → `etsy_statement_<year>_<month>.csv`.
3. The last 3 months are enough.

## 5. Stats — needed for: visits, conversion rate, CTR per listing

1. **Shop Manager → Stats** → set the date range (e.g. Last 12 months / This year).
2. Note the top numbers: Visits, Orders, Conversion rate, Revenue.
3. Scroll to the **Listings** table (views, visits, favorites, orders per listing).
4. If a download button is shown, save as `stats_<range>.csv`. Otherwise select the table and paste it into the chat, or send a screenshot.

## 6. Search terms — needed for: proven keywords

1. **Shop Manager → Stats → How shoppers found you → Etsy search** (or open a single listing's stats) → **Search terms**.
2. Copy-paste the table into the chat, send a screenshot, or save as `search_terms_<range>.csv`.

## 7. Etsy Ads — needed for: ads optimizer

1. **Shop Manager → Marketing → Etsy Ads** → set the date range (30–90 days).
2. Scroll to the listing table: Views, Clicks, Orders, Revenue, Spend, ROAS.
3. Download if available (save as `ads_<range>.csv`), otherwise copy-paste the table or send a screenshot.

## Which skill needs what

| Skill | Must have | Nice to have |
|---|---|---|
| etsy-shop-analysis | Order Items | Listings, Statement, Stats, Search terms |
| multi-shop-compare | Order Items for each shop (same period) | Listings, Stats numbers |
| etsy-ads-optimizer | Etsy Ads table | Statement (margin), Order Items |
| listing-audit-framework (bulk) | Listings | Stats per listing |
| keyword-research (proven) | — | Search terms |
