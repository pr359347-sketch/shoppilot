# Amazon — How to Export Your Data

ShopPilot is **advisor-only on Amazon** — you download these yourself in Seller Central and drop them in `data/exports/<shop>/` (private, git-ignored). Files are recognised by headers. Menu names vary by marketplace; search the report name in Seller Central if needed.

## 1. Business Report — sessions, conversion, Buy Box per ASIN
**Reports → Business Reports → By ASIN → Detail Page Sales and Traffic by Child Item** → set date range (last 30 d + previous 30 d as two files) → **Download (.csv)**.

## 2. Sponsored Products search term report — PPC harvesting
**Advertising → Campaign Manager → Measurement & Reporting → Sponsored ads reports → Create report** → Sponsored Products → **Search term** → last 60 days → Daily or Summary → download.

## 3. Search Query Performance — Brand Registry only
**Brands → Brand Analytics → Search Query Performance** → Brand view or ASIN view → last 3 months → **Download / Generate download**.

## 4. All Listings + suppressed check
- **Reports → Inventory Reports → All Listings Report** → Request → download.
- **Inventory → Manage All Inventory → filter "Search suppressed"** → screenshot or download the list.
- **Inventory → Fix stranded inventory** → download if any.

## 5. FBA inventory — replenishment
**Inventory → FBA Inventory** (or Inventory Planning → Restock) → **Download**.

## 6. Flat-file template — for bulk listing / edits
**Catalog → Add Products via Upload → Download an Inventory File** → choose your category/product type → download the `.xlsm` template. Keep it in `data/exports/<shop>/`; ShopPilot fills a CSV copy you paste into it.

## 7. Account Health
**Performance → Account Health** → screenshot (ODR, late shipment rate, valid tracking rate, policy compliance).

Order reports contain buyer details — ShopPilot uses aggregates only.
