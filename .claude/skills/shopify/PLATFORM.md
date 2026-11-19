<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Shopify — Platform Rules (single source of truth)

Last reviewed: 2026-11-19 (from general knowledge — **[VERIFY] values against the store's admin / plan before pricing decisions**). Admin wins; update this file.

**ShopPilot mode on Shopify: EXECUTE-AFTER-APPROVAL.** Prefer a connected Shopify connector; otherwise Shopify admin in the built-in browser at safe speed.

## Product fields

| Field | Limit | How we use it |
|---|---|---|
| Title | 255 chars | 50–70 chars, readable: `Hand Tufted Wool Rug — Beige Abstract` |
| SEO title (page title) | ~70 chars shown by Google | Main keyword + material/size + brand at end if room |
| Meta description | ~160 chars shown (admin allows more) | Keyword + benefit + reason to click |
| URL handle | keep < 60 chars | lowercase-hyphen keyword slug; changing a live handle → set a redirect |
| Description | rich text/HTML | benefit-first intro, size table `ft (cm)`, material/care, story, shipping/returns, FAQ |
| Images | many per product; ≤ 20 MB, ≤ 5000×5000 px [VERIFY] | 2048×2048 square recommended; alt text each (≤ 512) |
| Variants | 3 options; up to 2048 variants [VERIFY] | Size / Colour / Shape |
| Tags | up to 250 per product | internal filtering + smart collections (not a Google ranking factor) |
| Metafields | custom | material, pile height, construction, care — shown in theme + filters |
| Collections | smart (rules) or manual | per construction, room, style, size; each with SEO text |

## Google Merchant Center feed limits

| Attribute | Limit |
|---|---|
| title | 150 chars (first ~70 show) |
| description | 5000 chars |
| google_product_category | Rugs: "Home & Garden > Decor > Rugs" (ID 598) [VERIFY in Google taxonomy] |
| identifier_exists | `no` for handmade items without GTIN/MPN |

## Fees [VERIFY on the store's plan page]
| Fee | Typical (US) |
|---|---|
| Plan | Basic / Shopify / Advanced monthly subscription |
| Shopify Payments online card rate | ~2.9% + 30¢ (Basic), lower on higher plans |
| Third-party gateway fee | extra ~2% / 1% / 0.6% by plan if not using Shopify Payments |
| Apps | monthly per app — check Settings → Apps |
| Currency conversion | ~1.5–2% when selling in other currencies [VERIFY] |
No marketplace commission — traffic is your job (Google, social, email, ads).

## Traffic & ranking (Google is the "search engine" here)
See `.claude/skills/core/google-seo/SKILL.md`. Key levers: unique product + collection content, structured data (theme JSON-LD), Merchant Center feed (free listings + Shopping ads), page speed, internal linking, backlinks/PR, email capture + abandoned checkout.

## Benchmarks (home decor, rough)
| Metric | Weak | OK | Good |
|---|---|---|---|
| Online store conversion | < 0.8% | 1–2% | 2.5%+ |
| Add-to-cart rate | < 3% | 4–7% | 8%+ |
| Checkout completion (reached → completed) | < 40% | 45–55% | 60%+ |
| Abandoned checkout recovery | < 3% | 5–10% | 10%+ |

## Key admin paths
- Products → All products → (product) → Search engine listing (SEO title, meta, handle)
- Products → Collections · Online Store → Navigation · Online Store → Blog posts
- Marketing → Automations (abandoned checkout, welcome series) · Marketing → Campaigns
- Sales channels → Google & YouTube (Merchant Center feed) · Settings → Apps
- Analytics → Reports (sessions, conversion, sales by product, by traffic source)
- Online Store → Themes → (web performance / theme speed)

## Exports (detected by header)
| Data | Where | Detect by |
|---|---|---|
| Products | Products → Export → CSV for Excel/Numbers | `Handle`, `Title`, `Variant Price` |
| Orders | Orders → Export | `Name`, `Financial Status`, `Lineitem name` |
| Analytics | Analytics → Reports → (report) → Export | `Sessions`, `Conversion rate` etc. |
| Search Console | GSC → Performance → Export | `Top queries`, `Clicks`, `Impressions` |
| GA4 | Reports → (report) → Share → Download CSV | `Session default channel group` |
| Merchant Center | Products → Diagnostics → Download | `Issue`, `Item ID` |

Full steps: `docs/shopify-csv-export-guide.md`.

## Analysis (analytics-agent, scratch script, aggregates only)
Sessions → add to cart → reached checkout → orders funnel · product conversion · channel conversion · zero-sale products · GSC low-CTR pages · GMC disapprovals.

## Policy notes
Own store = owner's legal policies (refund, privacy, terms, shipping) must exist and be accurate; consumer-law compliant claims; Google Merchant Center policies (no misrepresentation, accurate prices/shipping, contact info visible).

## Monthly health check
- [ ] Sessions, conversion, AOV MoM; funnel drop-off step
- [ ] Top 10 products: CR + stock + price vs competitors
- [ ] Zero-sale products 90 d
- [ ] GSC: clicks/impressions MoM, indexing errors, low-CTR pages, Core Web Vitals
- [ ] GMC: disapproved / limited products, feed errors
- [ ] Abandoned checkout recovery rate; email list growth
- [ ] Page speed: theme score, heavy apps, image sizes
- [ ] Policies pages present + up to date; contact info visible
- [ ] Apps cost vs use (remove unused)
- [ ] Upcoming occasions: collections + banners + discount codes ready
