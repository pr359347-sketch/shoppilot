---
description: SEO — marketplace keywords + listing package, and Google SEO (meta, alt text, Merchant Center, Search Console)
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

Create or improve listing SEO. Arguments (optional): `$ARGUMENTS` — the product description, e.g. `/seo hand tufted wool rug, beige abstract, 5x8 and 8x10`.

1. Detect mode (`data/shops/`). Connected: pick the shop (ask once if several), read its profile, `data/settings.md`, `data/learnings.md` and its keyword pools. Generic: ask which platform (default Etsy).
2. If product details are missing, ask once for the must-haves: product, technique/construction, material, sizes, colors/style, prices (or offer the pricing advisor), processing + shipping time.
3. Ask what's needed if unclear:
   - keywords only → `.claude/skills/core/keyword-research/SKILL.md`
   - full listing package (default) → keyword research first, then `.claude/skills/<platform>/<platform>-listing-seo/SKILL.md`
   - translation → `.claude/skills/core/multilingual-seo/SKILL.md`
4. Use the limits in `.claude/skills/<platform>/PLATFORM.md` and the matching domain file. Show character counts for every title and tag.
5. Offer the next step in one line: photo prompts (`/prompts`) or translation.
6. **v1.0 routing:** keywords + Google SEO → **seo-agent** (Semrush if connected); the listing package → **<platform>-agent**. Run seo-agent first, pass its keyword set on. Google-only tasks (Shopify meta, GMC feed, GSC fixes) → seo-agent + shopify-agent.
7. Applying the new title/tags/meta = proposal card (Etsy/Shopify: ShopPilot does it after "ok"; eBay/Amazon: owner steps).
