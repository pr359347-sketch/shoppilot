<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Google SEO — get listings and products found on Google

Applies to Shopify stores (main use), Etsy/eBay/Amazon listing pages (Google indexes them too) and blogs.

## 1. What Google reads on a listing/product page
| Element | Etsy | Shopify | Rule |
|---|---|---|---|
| Page title | listing title (first ~60 chars show) | SEO title (≤70) | Main keyword first, then material/size/style. No ALL CAPS. |
| Meta description | first ~160 chars of description | meta description (≤160) | Main keyword + key benefit + reason to click. Written for humans. |
| URL | auto from title | handle | Short, keyword, hyphens: `/products/hand-tufted-wool-rug-beige-5x8` |
| Images | alt text (≤500) | alt text (≤512) | Describe the photo + 1 natural keyword. File names descriptive before upload. |
| Structured data | Etsy adds it | theme JSON-LD (Product, Offer, AggregateRating) | Check with Google Rich Results Test. Ratings only if real reviews. |
| Content | description | description + collection text + blog | Unique, not copied across variants or from suppliers. |

## 2. Keyword choice for Google (vs marketplace)
Google searchers type longer, question-like queries ("best rug size for 10x12 living room", "wool vs jute rug"). Use Semrush (if connected) for volume/KD; prefer KD < 30 for small stores. Map: 1 primary keyword per page; collections for category terms; blog for questions.

## 3. Shopify specifics
- **Collections**: one per construction/room/style/size; 150–300 words of helpful text + FAQ; internal links.
- **Blog**: guides (rug size guide, care, room styling) linking to collections/products. One post = one question cluster.
- **Google Merchant Center + Shopping**: Google & YouTube app. Feed checklist: title formula `Brand + Type + Material + Size + Color`, google_product_category, condition=new, brand, identifier_exists=no for handmade (no GTIN), size/color/material, shipping + return policy set in GMC, product images without text/watermarks. Fix disapprovals from GMC → Products → Needs attention.
- **Search Console**: sitemap submitted; Pages report (indexing errors); Performance → queries with impressions but CTR < 1% → rewrite title/meta; pages ranking 8–20 → improve content.
- **GA4**: conversions by channel (Organic, Paid, Social, Email); landing pages with high exits.
- **Page speed basics**: compress images (WebP), ≤ 2048 px wide for content images, limit apps, remove unused app code, lazy-load below fold, check Core Web Vitals in GSC / PageSpeed Insights.
- **Abandoned checkout**: Marketing → Automations; recovered revenue is an SEO-traffic multiplier.

## 4. Data sources (order)
Owner exports in `data/exports/<shop>/` (GSC CSV, GA4 export) → connected analytics connector → Semrush → web search SERP check. Label each number with its source.

## 5. Output
Per page: current → proposed (title, meta, handle, alt texts, H1, content additions) with counts; GMC fix list; GSC fix list; blog/collection plan. Live changes → proposals.
