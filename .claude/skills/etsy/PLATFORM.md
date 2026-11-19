# Etsy — Platform Rules (single source of truth)

Last reviewed: 2026-11-13. Etsy changes fees and limits — if the owner's Shop Manager shows something different, **Shop Manager wins**; update this file.

## Listing limits

| Field | Limit | How we use it |
|---|---|---|
| Title | 140 characters | Target 70–120. First ~40 chars = main keyword phrase (what shows in search/mobile). Natural phrases separated by commas or ` - `, no word repeated 3+ times, no ALL CAPS. |
| Tags | 13 tags, each ≤ 20 characters (spaces count) | Use all 13. Multi-word long-tail phrases. Don't repeat the same word across many tags; don't duplicate category/attribute words exactly (Etsy already indexes those). No plurals+singular pairs, no misspellings. |
| Materials | 13 max | Most specific first: "New Zealand wool", "cotton backing", "jute". |
| Description | No hard limit | First 160 chars act as the Google meta snippet + Etsy preview — must contain the main keyword naturally. |
| Photos | Plan for 10 (if the listing form allows more, extra slots = more size/room shots) | Photo 1 decides CTR. Min 2000 px on shortest side, landscape 4:3 or square 1:1; thumbnail crops to centre. |
| Video | 1 per listing, 5–15 sec, no audio played, ≥1080p | Listings with video convert better; first 2 sec must show the product. |
| Alt text | Up to 500 characters per photo | Describe what's in the photo + 1 natural keyword. Not a keyword list. |
| Variations | 2 variation types (e.g. Size + Color); price/SKU/qty can vary per option | Rugs: variation 1 = Size (ft + cm), variation 2 = Color or Shape/Backing. |
| Personalization | Optional text box | Use for custom size / custom color requests. |
| Sections | 20 shop sections | By construction or room, keyword-rich names. |
| Attributes | Category-specific | Fill **every** attribute — each one works like an extra tag. |

### Rug attributes to always fill (Home & Living → Rugs / Floor & Rugs → Rugs category)
Primary color, Secondary color, Material, Shape (rectangle / round / runner), Length, Width, Style, Room, Pattern, Construction/technique where offered, Pile, Occasion (only if truly relevant), Holiday (only for seasonal designs), Sustainability/handmade flags where offered.

## Shop graphics

| Asset | Size |
|---|---|
| Big shop banner | 1200×300 px minimum (design at 2400×600 or 3360×840 for sharpness, same 4:1 ratio). Keep text in the centre 60% — mobile crops the sides. |
| Mini banner | 1200×160 px minimum |
| Shop icon | 500×500 px |
| Listing photo | 2000 px+ shortest side, 4:3 or 1:1 |
| Pinterest pin | 1000×1500 px (2:3) |
| Instagram post / reel | 1080×1350 (4:5) / 1080×1920 (9:16) |

## Fees (use in pricing; VERIFY against a real monthly statement)

| Fee | Value | Notes |
|---|---|---|
| Listing fee | $0.20 per listing, renews every 4 months and on each sale (per quantity sold) | |
| Transaction fee | 6.5% of item price + shipping + gift wrap | |
| Payment processing | Country-specific % + fixed fee | **[VERIFY for the seller's country from Finances → Monthly statement]** — pricing skill uses `payment_pct` + `payment_fixed` from the shop profile; default assumption 4% + $0.30 until verified. |
| Offsite Ads | 15% of order (12% if shop did >$10k in last 12 months; mandatory above $10k) — only on orders attributed to an offsite ad click, capped at $100/order | Reserve a blended 3–5% in pricing. |
| Etsy Ads (onsite) | Daily budget, cost per click | Tracked by ROAS in ads skill. |
| Currency conversion | 2.5% if listing currency ≠ payout currency | Applies when e.g. listing in USD but the bank account is in another currency. |
| VAT / GST on seller fees | Applies in some seller countries | **[VERIFY on statement]** |
| Share & Save | Returns 4% on sales from the shop's own shared links | Use in Pinterest/Instagram links. |

## Free shipping

- US buyers get a "free shipping" filter; items with free US shipping (or free on $35+) get search priority in the US app.
- Rugs: build shipping into the item price (pricing skill does this). Offer free shipping to US; for EU either free or a clearly shown flat rate.
- EU/UK buyers: Etsy collects VAT at checkout; mention "VAT handled by Etsy at checkout; no surprise fees" only if true for that destination.

## Search ranking — what matters (in practice)

1. **Relevance**: query matches title, tags, attributes, category. Exact phrase match in title/tags beats scattered words.
2. **Listing quality score**: click-through rate, favorites, add-to-carts, purchases *for that query*. New listings get a short boost — photos and price must be right on day 1.
3. **Recency**: new and renewed listings get a small temporary lift.
4. **Customer & market experience**: reviews, on-time shipping + tracking, message response, completed About/policies, Star Seller.
5. **Shipping price**: free / low shipping ranks better for US buyers.
6. **Context**: buyer's country, language, past behaviour — so translated titles/tags matter for DE/FR/NL.

## Benchmarks (rough, for rugs/home decor)

| Metric | Weak | OK | Good |
|---|---|---|---|
| Search CTR (visits ÷ impressions) | <0.7% | 1–2% | 2.5%+ |
| Conversion rate (orders ÷ visits) | <0.5% | 1–2% | 2.5%+ (high-ticket rugs often 0.5–1.5%) |
| Favorite rate (favs ÷ visits) | <3% | 4–8% | 10%+ |
| Etsy Ads ROAS | <1.5 | 2–3 | 4+ |

Diagnosis shortcut: **low impressions → SEO**, **impressions but low CTR → photo 1 / price / title start**, **visits but no sales → photos 2–10, description, price, shipping, reviews, sizes**.

## CSV formats (how `scripts/etsy_analyze.py` recognizes files)

Files are detected by header, not by file name.

| Type | Detected when the header has | Key columns used |
|---|---|---|
| Order items | `Item Name` + `Transaction ID` | Sale Date, Item Name, Quantity, Price, Item Total, Discount Amount, Coupon Code, Currency, Listing ID, Order ID, Ship Country, Variations, SKU, Buyer (counted only, never printed) |
| Orders | `Order ID` + `Order Value` / `Order Total` | Order Value, Ship Country |
| Listings | `TITLE` + `TAGS` | TITLE, PRICE, TAGS, IMAGE1–IMAGE10, SKU |
| Statement | `Fees & Taxes` | Type, Title, Amount, Fees & Taxes, Net |
| Anything else (stats, search terms, ads) | — | listed with its columns; the agent reads it directly |

Sale dates are `MM/DD/YY`. Sizes are parsed from the `Variations` column (ft or cm).

## Exports available

Step-by-step export instructions to show the owner: `docs/etsy-csv-export-guide.md`.

| Data | Where | File name pattern |
|---|---|---|
| Listings | Shop Manager → Settings → Options → Download Data → "Currently for Sale Listings" | `EtsyListingsDownload.csv` |
| Order items | same page → Orders section → type "Order Items" + month/year | `EtsySoldOrderItems<year>.csv` |
| Orders | same → "Orders" | `EtsySoldOrders<year>.csv` |
| Monthly statement (fees) | Shop Manager → Finances → Monthly statements → Download CSV | `etsy_statement_<year>_<m>.csv` |
| Stats / listing stats / search terms | Shop Manager → Stats (set date range) — if no CSV button, copy-paste the table or screenshot | save as `stats_*.csv` / `search_terms_*.csv` or paste in chat |
| Etsy Ads | Shop Manager → Marketing → Etsy Ads → listing table (download if available, else copy-paste) | `ads_*.csv` |

## Mode, policies, safe execution

**ShopPilot mode on Etsy: EXECUTE-AFTER-APPROVAL** — the master makes one approved change at a time in the owner's logged-in Shop Manager, at safe speed (`.claude/skills/core/AGENT-RULES.md` §5).

Policy notes: Creativity standards (made / designed / handpicked by the seller; production partners disclosed in the listing and About); photos must accurately represent the item — AI or preview renders of made-to-order items must be disclosed and never replace a real photo of an existing item; no fees-avoidance (off-Etsy payment or contact to avoid fees); no review manipulation; no trademarked brand names in tags/titles you don't own.

## Monthly health check

- [ ] Star Seller status: message response rate, on-time shipping with tracking, 5-star review rate
- [ ] Stats MoM: visits, conversion, orders, revenue, AOV; traffic sources (Etsy search / app / direct / social / Etsy Ads / offsite)
- [ ] Listings with 0 visits (30 d) and 0 sales (90 d) — rewrite / renew / deactivate proposals
- [ ] Attributes fully filled + 13 tags used on all active listings (`--listing-health`)
- [ ] Photo count < 10 or no video listings
- [ ] Etsy Ads ROAS vs break-even per listing; Offsite Ads cost share
- [ ] Prices vs floor (`profit-agent`) after fee changes; free US shipping on
- [ ] Shop sections, announcement, shop title, About up to date; sale events scheduled for upcoming occasions
- [ ] Experiments due (`core/experiment-tracker`) and learnings applied
