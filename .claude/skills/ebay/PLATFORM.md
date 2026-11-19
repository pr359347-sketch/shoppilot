<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# eBay — Platform Rules (single source of truth)

Last reviewed: 2026-11-19 (from general knowledge — **values marked [VERIFY] must be checked in Seller Hub / eBay fee pages before a pricing or fee decision**). If Seller Hub shows something different, Seller Hub wins; update this file.

**ShopPilot mode on eBay: ADVISOR ONLY.** Never act on eBay in a browser. Owner does every change.

## Listing limits

| Field | Limit | How we use it |
|---|---|---|
| Title | 80 characters | Use 75–80. Keyword-dense, no filler words ("L@@K", "wow"), no ALL CAPS. Order: type + construction + material + size + colour + style. |
| Subtitle | 55 characters (paid add-on) [VERIFY fee] | Only for high-ticket items. Not indexed in search. |
| Item specifics | Required + recommended + optional per category; value ≤ 65 chars [VERIFY] | Fill **every** relevant specific — they power filters and Cassini relevance. Score = filled ÷ (required + recommended). |
| Condition | Required | Handmade new → "New". |
| Description | No hard limit; no active content (JavaScript, Flash, forms) | Mobile-first: short paragraphs, size table, care, shipping, returns. First ~250 chars show as mobile summary. |
| Photos | Up to 24, min 500 px longest side, 1600 px+ recommended | Photo 1 white/neutral or clean room shot; show back side + size reference. |
| Video | 1 per listing, ≤ 1 min [VERIFY] | Product first 2 s. |
| Variations | Multi-variation listings (Size, Colour…) each with own photos and specifics | Rugs: Size × Colour. |
| Store categories | Up to 300 in eBay Store [VERIFY] | By construction / room / size. |

## Rugs category + item specifics [VERIFY in Seller Hub's listing form for the chosen category]
- Category: Home & Garden > Rugs & Carpets > Area Rugs (ID 45510) [VERIFY]; runners and round rugs share the category, use Shape.
- Usually required/recommended: Brand (Unbranded / own brand), Type, Size, Shape, Material, Color, Construction (Hand-Knotted / Hand-Tufted / Flatweave…), Style, Pattern, Room, Pile Height, Features, Country/Region of Manufacture, Rug Size (ft), Length, Width, Theme, Handmade (Yes), Department.
- **Score** = filled ÷ (required + recommended) shown in the form. Also fill optional specifics, but they don't count in the score.

## Fees [VERIFY all on eBay's "Selling fees" page for the seller's country]

| Fee | Typical value (US) |
|---|---|
| Insertion | 250 free listings/month for non-store sellers, then $0.35 each; Store plans include more |
| Final value fee | ~13.6% of total sale (item + shipping + tax) for most categories incl. Home & Garden, lower % above $7,500 per item; + per-order fee $0.30 (≤ $10) / $0.40 (> $10) |
| Promoted Listings General | ad rate % (2–100%) of sale, charged only if sale within 30 days of a click on the ad |
| Promoted Listings Priority | cost per click, daily budget, keyword/manual targeting |
| International fee | ~1.65% on international buyers (US sellers) |
| Below-standard surcharge | extra % on final value fee if seller level = Below Standard |

## Search ranking (Cassini) — in practice
1. Title + item-specifics relevance (exact phrase in title).
2. Sales history / sell-through and recent sales velocity of the listing.
3. Price competitiveness incl. shipping (free shipping helps).
4. Seller performance level (Top Rated / Above Standard / Below Standard) and returns policy (free 30-day returns help).
5. Listing quality: photos, complete specifics, item location, handling time.
6. Promoted Listings add placement on top of organic.

## Benchmarks (home decor, rough)
| Metric | Weak | OK | Good |
|---|---|---|---|
| Impression → click (CTR) | < 0.5% | 0.8–1.5% | 2%+ |
| Sales conversion (views → sale) | < 0.5% | 1–2% | 3%+ |
| Sell-through (Terapeak, sold ÷ listed) | < 20% | 30–60% | 60%+ |
| Item specifics score | < 70% | 80–90% | 100% |

## Key Seller Hub paths
- Performance → Seller level · Service metrics · Traffic (impressions, CTR, page views, conversion)
- Research → Product research (Terapeak): sold data up to 3 years, avg sold price, sell-through, top listings
- Marketing → Promoted Listings (General / Priority / Offsite) · Promotions → Sale event + markdown (Markdown Manager), Coded coupons, Order discounts
- Listings → Active / Unsold / Drafts · Reports → Downloads / Uploads (bulk templates)

## Promoted Listings — decision rule
- **General** (cost per sale): default for most listings. Ad rate ≤ (margin after fees − target profit). Start at eBay's suggested rate only if margin allows.
- **Priority** (cost per click): only listings with proven conversion (≥ 2% and ≥ 5 sales/90 d) and margin ≥ 25%; build exact/phrase keyword groups + negatives.

## Markdown Manager
Sale event + markdown: % off for a date range; time to occasions; never below `profit-agent` floor price; avoid permanent sales (buyers learn to wait).

## Policy notes
On-platform communication only; no off-eBay payments or contact info; accurate condition + specifics; VeRO (no brand names you don't own, e.g. "like Pottery Barn"); handling time honoured; returns per policy.

## Exports / reports (detected by header)
| Data | Where | Detect by |
|---|---|---|
| Orders | Seller Hub → Orders → Download report (CSV) | `Order Number`, `Item Number`, `Sold For` |
| Active listings | Reports → Downloads → Active listings | `Item number`, `Title`, `Current price` |
| Traffic | Performance → Traffic → Download | `Total impressions on eBay site`, `Click-through rate` |
| Promoted Listings | Marketing → Advertising dashboard → Download report | `Ad fees`, `Sales`, `Clicks` |
| Terapeak | Research → Product research (copy table or screenshot) | owner paste |

Full steps: `docs/ebay-csv-export-guide.md`.

## Analysis (no script yet — analytics-agent uses a scratch pandas/stdlib script, aggregates only)
Funnel from Traffic report · zero-impression and zero-sale listings · item specifics score per listing · ROAS per promoted listing vs break-even · sell-through vs Terapeak.

## Monthly health check
- [ ] Seller level + defect rate, late shipment rate, cases closed without resolution, tracking uploaded on time
- [ ] Traffic MoM: impressions, CTR, conversion
- [ ] Listings with 0 impressions (30 d) and 0 sales (90 d)
- [ ] Item specifics score < 80% listings
- [ ] Promoted Listings ROAS vs break-even; ad rate drift
- [ ] Prices vs Terapeak average sold price
- [ ] Returns policy (free 30-day?) + handling time
- [ ] Active promotions / Markdown events + upcoming occasions
- [ ] Policy/VeRO warnings in Messages from eBay
