# eBay — How to Export Your Data

ShopPilot is **advisor-only on eBay** — you download these yourself and drop them in `data/exports/<shop>/` (private, git-ignored). Files are recognised by their column headers; no renaming needed. eBay menus move around — if a step looks different, look for the same report name in Seller Hub.

## 1. Orders — sales analysis
1. **Seller Hub → Orders → All orders**.
2. Set the period (last 90 days / 1 year) → **Download report** (CSV).
3. Contains buyer names/addresses — ShopPilot only uses aggregates.

## 2. Active listings — item specifics score, zero-sale listings
1. **Seller Hub → Reports → Downloads → Create a report**.
2. Listing type: **Active listings** (choose the format with item specifics if offered) → Create → download when ready.

## 3. Traffic — impressions, CTR, conversion
1. **Seller Hub → Performance → Traffic**.
2. Choose the date range → **Download** (listing-level traffic report).

## 4. Promoted Listings — ROAS / ad rate decisions
1. **Seller Hub → Marketing → Advertising dashboard** (or Promoted Listings).
2. Pick campaign(s) and date range → **Download report** (listing-level; for Priority also the keyword/search-query report).

## 5. Terapeak — sold-data research
1. **Seller Hub → Research → Product research**.
2. Search the keyword ShopPilot gives you; set **Last 90 days** (or 1 year), filters as asked (Sold, Fixed price, category).
3. Copy the summary numbers (avg sold price, total sold, sell-through, total sellers) and the top 10 listings table → paste in chat or save as a text file in the exports folder. No CSV button? A screenshot works.

## 6. Seller performance
**Seller Hub → Performance → Seller level** and **Service metrics** → screenshot or copy the numbers (defect rate, late shipment rate, cases closed without seller resolution).
