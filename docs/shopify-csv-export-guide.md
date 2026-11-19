<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Shopify — How to Export Your Data

Drop files in `data/exports/<shop>/` (private, git-ignored). If a Shopify or analytics connector is connected, ShopPilot can read some of this directly and will tell you which files it still needs.

## 1. Products — SEO audit, cross-listing, collections
**Products → Export → All products → CSV for Excel, Numbers…** → `products_export.csv`.

## 2. Orders — sales analysis
**Orders → Export → choose date range → CSV for Excel…** → `orders_export.csv`. Contains customer details — ShopPilot uses aggregates only.

## 3. Analytics reports — funnel, channels
**Analytics → Reports** → open each report below → set date range → **Export**:
- Sessions over time / Sessions by referrer (traffic sources)
- Conversion rate breakdown (sessions → add to cart → reached checkout → completed)
- Sales by product

## 4. Google Search Console — Google SEO
search.google.com/search-console → your property → **Performance** → last 3 months → **Export → CSV** (queries + pages). Also **Pages** (indexing) → Export.

## 5. GA4 — channels and landing pages
analytics.google.com → **Reports → Acquisition → Traffic acquisition** and **Engagement → Landing page** → **Share → Download file → CSV**.

## 6. Google Merchant Center — Shopping feed health
merchants.google.com → **Products → Needs attention / Diagnostics** → **Download**.

## 7. Abandoned checkouts
**Orders → Abandoned checkouts** — take a screenshot of the count and recovery numbers (or Marketing → Automations → abandoned checkout performance).
