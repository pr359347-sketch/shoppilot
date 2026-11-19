# Amazon — Platform Rules (single source of truth)

Last reviewed: 2026-11-19 (from general knowledge — **Amazon changes limits per category; every [VERIFY] value must be checked in the category style guide / Seller Central before use**). Seller Central wins; update this file.

**ShopPilot mode on Amazon: ADVISOR ONLY.** Never act on Amazon in a browser (suspension risk). Owner does every change; ShopPilot provides content, flat files and steps.

## Listing limits

| Field | Limit | How we use it |
|---|---|---|
| Title | up to 200 chars incl. spaces in most categories; Amazon recommends shorter and may enforce lower per category [VERIFY in style guide] | Brand + product type + key attribute (material, construction) + size + colour. No promo words, no ALL CAPS, no special chars like ! $ ? _ { } ^ ¬ ¦, no word repeated more than twice. |
| Bullet points | 5 bullets, keep ≤ 250 chars each [VERIFY max] | One benefit per bullet, starting with a short CAPS-free label. Size, material, construction, care, gift/room use. |
| Description | ~2000 chars | Replaced by A+ when present (still indexed). |
| Backend search terms | < 250 bytes (not characters) | No brand names, no ASINs, no repeats from title, no commas needed, singular OR plural. Show byte count. |
| Images | main + up to 8 more; ≥ 1000 px longest side for zoom (1600–2000 recommended) | **Main: pure white RGB 255,255,255, product fills ~85%, no text/props/watermark.** Others: room, detail, size chart, back, infographic. |
| Video | Brand Registry sellers can upload | product first 2 s |
| A+ content | Brand Registry only; up to 5 modules basic (7 on some accounts), Premium A+ extra [VERIFY] | hero, comparison chart, size guide, story, care |
| Variations | parent-child, theme e.g. SizeColor | each child own price, images, SKU |

## Fees [VERIFY on the Seller Central fee schedule]
| Fee | Typical (US) |
|---|---|
| Selling plan | Professional $39.99/month (waived for approved Amazon Handmade sellers) / Individual $0.99 per item |
| Referral fee | Home & Kitchen ~15%; **Amazon Handmade 15%** (min $1.00) |
| FBA fulfilment | by size tier + weight; rugs are often large/bulky — check the FBA revenue calculator |
| FBA storage | monthly per cubic foot (higher Oct–Dec); aged-inventory surcharge |
| Sponsored Products | cost per click |
| Returns processing / refund admin | per category |

## Search ranking (A10) — in practice
1. Relevance: title, bullets, backend terms, attributes, browse node.
2. Conversion rate + sales velocity for the query (incl. PPC sales).
3. Featured Offer (Buy Box), price, Prime/FBA eligibility, stock availability.
4. Reviews and rating; return rate.
5. Listing quality (complete attributes, images, A+).
6. External traffic and click-through.

## Benchmarks (home decor, rough)
| Metric | Weak | OK | Good |
|---|---|---|---|
| Unit session percentage (CR) | < 5% | 8–12% | 15%+ |
| Featured Offer % | < 90% | 95% | 98%+ |
| Sponsored Products ACoS | > break-even | ≈ break-even − 5 pts | ≤ target |
| Search-term CTR (SQP) | below market click share | ≈ market | above market |

## Key Seller Central paths
- Reports → Business Reports → Detail Page Sales and Traffic by Child Item (sessions, unit session %, Featured Offer %)
- Brands → Brand Analytics → Search Query Performance / Top Search Terms (Brand Registry)
- Advertising → Campaign Manager → Sponsored Products → Reports → Search term report; Bulk operations
- Inventory → Manage All Inventory (filter: Search suppressed) · Fix stranded inventory · Inventory Planning → Restock / FBA Inventory
- Catalog → Add Products via Upload → Download inventory file (flat-file template for the category)
- Performance → Account Health · Brands → A+ Content Manager

## PPC search-term harvesting rules
- Source: auto + broad/phrase campaigns, last 30–60 days.
- **Winners**: ≥ 2 orders and ACoS ≤ target → add as EXACT in a manual campaign (bid = current CPC × target ACoS ÷ actual ACoS) and as NEGATIVE EXACT in the source campaign.
- **Wasters**: ≥ 10–15 clicks and 0 orders, or ACoS > 2× target with ≥ 20 clicks → NEGATIVE EXACT (or phrase for a bad root word).
- Target ACoS = break-even ACoS from `profit-agent` minus desired profit.
- Output as bulk-sheet rows the owner uploads.

## FBA replenishment
Days of cover = available + inbound ÷ avg daily units (30 d). Reorder point = (lead time days + safety days) × avg daily units. Q4: storage fees higher — don't overstock slow sizes.

## Amazon Handmade specifics [VERIFY all in Seller Central Handmade help]
- Artisan application must be approved before listing; items must be made by hand by the artisan / small team (≤ 20 people), no mass-produced items.
- Production time ("handling time") is set per listing — must match reality (hand-knotted rugs often 6–12 weeks per `domain/rugs.md`).
- Customization: "Customize now" options for size/colour; custom orders must stay on Amazon.
- Returns: Amazon's return policy for the marketplace applies; customized items may have exceptions.
- Maker profile (Artisan page) replaces brand page if no Brand Registry.

## Policy notes
Amazon Handmade requires an approved artisan application and items actually handmade by the artisan/small team. No reviews manipulation (no incentives, no asking only happy buyers), no off-Amazon contact, no medical/eco claims without proof, main image rules strict, accurate variations (no unrelated items as variations).

## Exports (detected by header)
| Data | Where | Detect by |
|---|---|---|
| Business Report (child ASIN) | Reports → Business Reports → Detail Page Sales and Traffic by Child Item → Download CSV | `(Child) ASIN`, `Sessions - Total`, `Unit Session Percentage` |
| Search term report | Campaign Manager → Reports → Sponsored Products → Search term | `Customer Search Term`, `Clicks`, `7 Day Total Sales` |
| Search Query Performance | Brand Analytics → SQP → Download | `Search Query`, `Impressions: Brand Share` |
| All listings | Reports → Inventory Reports → All Listings Report | `seller-sku`, `asin1`, `item-name` |
| FBA inventory | Inventory → FBA Inventory → Download | `afn-fulfillable-quantity` |
| Orders | Reports → Fulfillment / Order reports | `amazon-order-id` (never print buyer fields) |

Full steps: `docs/amazon-csv-export-guide.md`.

## Analysis (analytics-agent, scratch script, aggregates only)
ASIN funnel (sessions → unit session %), Featured Offer %, SQP share gaps, PPC harvest lists, ACoS vs break-even, FBA days of cover, suppressed/stranded list.

## Monthly health check
- [ ] Account Health: ODR, late shipment, valid tracking, policy violations (all green?)
- [ ] Suppressed / stranded / inactive listings
- [ ] Business Reports MoM per ASIN: sessions, unit session %, Featured Offer %
- [ ] SQP: queries with impression share but low click/purchase share (Brand Registry)
- [ ] PPC: harvested winners + negatives done, ACoS vs target, budget caps hit
- [ ] FBA: days of cover, aged inventory, storage fee risk
- [ ] Reviews + rating trend, return reasons
- [ ] Listing quality dashboard suggestions
- [ ] A+ content live on all main ASINs (Brand Registry)
- [ ] Upcoming occasions: deals/coupons scheduled (Prime Day, Black Friday, Christmas)
