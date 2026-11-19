---
description: Ads optimizer — Etsy Ads, eBay Promoted Listings (General/Priority), Amazon PPC harvesting, Shopify/Google ads basics
---

Arguments (optional): `$ARGUMENTS` — shop name.

1. Connected only (else: "Koi shop connected nahi — /connect-shop chalao").
2. Pick the shop; `platform:` decides the agent.
3. Exports first: check `data/exports/<shop>/` for the ads report (see the platform's export guide). Missing → steps, wait.
4. Run in parallel: **profit-agent** (break-even ROAS/ACoS per product) and **<platform>-agent** (ads analysis).
   - Etsy → `etsy/etsy-ads-optimizer`
   - eBay → Promoted Listings General vs Priority rules in `ebay/PLATFORM.md`
   - Amazon → PPC search-term harvesting in `amazon/PLATFORM.md` (bulk-sheet rows)
   - Shopify → Google Shopping / PMax basics via `shopify-agent` + `seo-agent`
5. Combine → pause / scale / fix lists → proposal cards (Etsy/Shopify executable; eBay/Amazon owner steps).
