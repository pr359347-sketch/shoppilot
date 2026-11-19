# Trend Research — what's selling, why, how much, does it fit

## 1. Define the scope (one line)
Product family · market (US default) · time window (next 90 days) · shop it's for.

## 2. Collect signals (note source + date for each)
| Signal | Where | What to record |
|---|---|---|
| Search interest over time | Google Trends (trends.google.com, US, 12 mo / 5 yr) | rising / stable / falling, peak months, rising related queries |
| Search volume | Semrush connector (keyword overview, US) | volume, KD, trend line — small calls only |
| Marketplace demand words | Autocomplete on Etsy / eBay / Amazon / Pinterest (logged-out fetch) | the suggestion list for the seed term + a–z modifiers |
| What sells | Bestseller / "popular now" / "most sold" pages; eBay sold listings (Terapeak via owner) | recurring motifs, palettes, sizes, prices, review counts as a demand proxy |
| Style direction | Design-press trend pieces, Pinterest Predicts, home-decor brand new arrivals | named trends (e.g. colour of the year, "quiet luxury", "vintage-washed") |
| Owner data | `data/exports/<shop>/`, past reports | what already sells for them (`proven`) |

Never save competitor images. Describe, don't copy.

## 3. Price bands
From 15–30 comparable listings: low / mid / premium per main size, and where the shop's prices sit.

## 4. Score (1–5 each)
- **Demand**: 1 = falling/no signal · 3 = stable, several sources · 5 = rising on 2+ independent sources (Trends/Semrush + marketplace)
- **Competition** (5 = easy): 1 = page 1 full of strong established listings · 3 = mixed · 5 = few good listings for the exact phrase
- **Fit**: 1 = new technique/material needed · 3 = small change · 5 = shop already makes it
- **Margin room**: 1 = market price below likely floor · 3 = mid band · 5 = premium band accepted. Costs unknown → score from price band and mark `est.`
Total /20 → **≥14 go ✅ · 10–13 test small ⚠️ · <10 skip ❌** (this is the fit verdict shown to the owner).

Demand source fallback: no Semrush → open trends.google.com in the built-in browser (public, no login); still nothing → label demand `idea` and say so. Price bands: aim for 15–30 comparables; with a small search budget, report how many you used.

## 5. Output
Opportunity table → price bands → seasonality window (list-by / peak) → 3 competitor gaps → fit verdict per shop → handoff line: "→ product-dev-agent for original designs" / "→ seo-agent for keywords".
