# Skills Reference

All skills live in `.claude/skills/<module>/<skill>/SKILL.md`. The agent opens them by path (see the routing table in `CLAUDE.md`). You don't need to name a skill — describe what you want, or use a command.

## Commands

| Command | What it does |
|---|---|
| `/start` | Menu: platform → shop → task |
| `/connect-shop` | Creates your private shop profile + exports folder |
| `/analyze` | Shop analysis, ads analysis, or shop comparison from your exports |
| `/audit` | Audits a listing you paste |
| `/seo` | Keyword research + full listing package |
| `/prompts` | Photo, banner / social, and video prompts |

v1.0 commands (`/health`, `/research`, `/new-product`, `/creative`, `/ads`, `/report`, `/approvals`, `/freeze`): see [agents-reference.md](agents-reference.md).

## Core skills (platform-agnostic)

| Skill | Use it for | You provide | You get |
|---|---|---|---|
| `core/keyword-research` | Finding keywords | Product, color / style / room | Keyword pool by type (head, long-tail, room, style, size, occasion, buyer-intent) + a ready tag set |
| `core/listing-audit-framework` | "Why isn't this selling?" | Pasted listing (+ stats if you have them) | Funnel diagnosis, scores, exact replacement title / tags / fixes |
| `core/competitor-research` | Gap analysis | Pasted competitor titles, tags, prices, sizes | Missing keywords, sizes, price points, styles, tactics |
| `core/pricing-advisor` | Price ladders | Costs, shipping, target margin | Size-wise matrix with floor price, margin, sale headroom |
| `core/seasonal-planner` | Planning | Shop or product type | 13-week calendar: list / optimize / promote, with order cutoffs |
| `core/new-product-planner` | Expanding winners | A bestseller or a trend | Ranked variant ideas + launch checklist |
| `core/image-prompts` | Listing photos | Product details / real photo | 10-photo set of prompts + alt text |
| `core/banner-prompts` | Shop + social graphics | Asset type, occasion | Background prompts + exact text overlays |
| `core/video-ad-prompts` | Listing videos / reels | Product details / real photo | Per-clip prompts, edit plan, captions |
| `core/multilingual-seo` | Selling abroad | English title + tags | Localized title + tags in 9 languages with character counts |
| `core/multi-shop-compare` | Where to focus | 2+ connected shops with exports | Side-by-side metrics, product placement, focus split |

## Etsy module

| Skill | Use it for | You provide | You get |
|---|---|---|---|
| `etsy/etsy-listing-seo` | New / rewritten listings | Product facts | Title, 13 tags, attributes, materials, variations, description, alt text |
| `etsy/etsy-shop-analysis` | What sells, what doesn't | CSV exports in `data/exports/<shop>/` | Dated report + prioritized action list |
| `etsy/etsy-ads-optimizer` | Etsy Ads | Ads table (CSV / paste / screenshot) | Break-even ROAS, pause / scale / fix lists, budget advice |

Platform rules: `.claude/skills/etsy/PLATFORM.md`. Export steps: [etsy-csv-export-guide.md](etsy-csv-export-guide.md).

## Domain knowledge

| File | Covers |
|---|---|
| `domain/rugs.md` | Sizes (ft + cm), constructions, pile heights, materials + care, rooms, styles |
| `domain/home-textiles.md` | Pillows, throws, quilts, table linens, curtains, decor — sizes, materials, care, photo set |

## v1.0 core skills

| Skill | Use it for |
|---|---|
| `core/AGENT-RULES.md` | Shared rules every subagent reads first |
| `core/approval-flow` | Proposal cards, ok/no handling, safe execution, logging |
| `core/experiment-tracker` | +7/+14/+30 day before/after checks → learnings |
| `core/cross-listing` | One listing → Etsy / eBay / Shopify / Amazon formats + bulk files |
| `core/google-seo` | Meta, alt text, structured data, collections, blog, Merchant Center, Search Console, GA4, page speed |
| `core/trend-research` | Trend signals, price bands, scoring, fit |
| `core/creative-qa` | Tool choice, lock-line, drift check, text check, disclosure |
| `core/profit-check` | Profit per product/size/platform, price floor, break-even |
| `core/customer-replies` | Message / review / case reply templates and platform rules |
| `core/social-planner` | Pinterest + Instagram specs, cadence, calendar |
| `core/health-check` | Monthly health check method |
| `core/ops-routine` | Daily log, summaries, weekly report, freeze, reminders |

## Other platforms

`ebay/PLATFORM.md`, `shopify/PLATFORM.md`, `amazon/PLATFORM.md` — limits, fees (`[VERIFY]`), ranking, admin paths, exports, monthly health checklist. Agents: see [agents-reference.md](agents-reference.md). Export guides: [eBay](ebay-csv-export-guide.md) · [Shopify](shopify-csv-export-guide.md) · [Amazon](amazon-csv-export-guide.md).
