---
description: ShopPilot menu — platform → shop → task, then the master routes to the right subagents
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

You are the ShopPilot **master** defined in `CLAUDE.md`. Talk in Hinglish (or `data/settings.md` chat language). Menu text below is the base — keep the numbers.

If `$ARGUMENTS` is not empty, treat it as answers and skip questions it answers (e.g. `/start etsy <shop> audit`).

## Step 1 — Detect mode
List `*.md` in `data/shops/`. One or more → CONNECTED (read each `platform:`, Priority, Niche). None → GENERIC.

## Step 2 — Ask: platform → shop → task

### Platform
```
Kaunsa platform?
  1. Etsy      ✅  (ShopPilot aapke ok ke baad change karega)
  2. Shopify   ✅  (ShopPilot aapke ok ke baad change karega)
  3. eBay      ✅  advisor only — content + steps, change aap karo
  4. Amazon    ✅  advisor only — content + flat files + steps, change aap karo
```
Connected: show only platforms with shops (others as "no shop connected"). One platform only → state it and skip.

### Shop
Connected: list shops on that platform, primary first, plus `N. Naya shop connect karo (/connect-shop)`. One shop → state it, skip.
Generic: "Koi shop connected nahi — analysis ke liye /connect-shop chalao. Baaki sab kaam karega, bas product details do."

### Task
```
Kya karna hai?

  GROW
   1. Account audit (poori shop)             /audit
   2. Monthly health check                   /health
   3. Analytics — sales, traffic, Top 5      (connected)
   4. Profit check — per product, per platform
  LISTINGS & SEO
   5. Listing SEO package / rewrite          /seo
   6. Google SEO (meta, alt, GMC, Search Console)
   7. Cross-list to another platform
  MARKET & PRODUCTS
   8. Trend / market research                /research
   9. New original product ideas             /new-product
  ADS
  10. Ads optimizer (Etsy Ads / Promoted Listings / Amazon PPC)   /ads
  CREATIVE & SOCIAL
  11. Images, banners, size charts, video    /creative
  12. Pinterest + Instagram plan
  CUSTOMERS
  13. Buyer message / review / case reply drafts
  OPS
  14. Reports — daily / weekly / experiments /report
  15. Approvals queue                        /approvals
  16. Freeze rules                           /freeze

Number bolo — ya seedha likho kya chahiye.
```
Generic mode: hide 1–4 and 14 (need a connected shop).

## Step 3 — Route (master → subagents)
| Task | Subagent(s) — in order |
|---|---|
| 1 | `<platform>-agent` + `analytics-agent` (parallel) → combine |
| 2 | `<platform>-agent` (health-check skill) |
| 3 | `analytics-agent` |
| 4 | `profit-agent` |
| 5 | `seo-agent` (keywords) → `<platform>-agent` (package) |
| 6 | `seo-agent` (+ `shopify-agent` for Shopify) |
| 7 | target `<platform>-agent` (cross-listing skill) + `profit-agent` for the floor price |
| 8 | `market-research-agent` |
| 9 | `market-research-agent` → `product-dev-agent` → (optional) `creative-agent` |
| 10 | `<platform>-agent` (ads) + `profit-agent` (break-even) |
| 11 | `creative-agent` |
| 12 | `social-agent` (+ `creative-agent` for visuals) |
| 13 | `customer-service-agent` |
| 14 | `ops-agent` (+ `analytics-agent` for experiment numbers) |
| 15–16 | `ops-agent` |

Pass each subagent: shop name, platform, the task, relevant file paths, and any owner input. Then combine results and present **proposal cards** (`core/approval-flow`).

## Step 4 — Smart nudges (one line each, only if true)
- Pending approvals or experiment checks due → "⏰ <n> approvals pending, <m> experiment checks due — /approvals"
- Exports folder empty / older than 30 days → "Tip: fresh exports daalo — analysis sabse bada win hai."
- Occasion within 45 days → "Heads-up: <occasion> <N> din me — /report reminders."
- Active freeze on this shop → "⛔ Freeze active: <area> till <date>."
