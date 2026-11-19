<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Agents & Commands Reference

The **master** (`CLAUDE.md`) talks to you, plans, delegates to subagents, combines results and asks for your approval. Subagents live in `.claude/agents/` and never make live changes themselves.

## Subagents

| Agent | Does | Live changes |
|---|---|---|
| `etsy-agent` | Etsy audit, listing SEO, Etsy Ads, policies, Shop Manager steps, monthly health | master executes after "ok" |
| `shopify-agent` | Store audit, product pages, collections, SEO fields, Merchant Center feed, Search Console/GA4, abandoned checkout emails, blog, page speed | master executes after "ok" |
| `ebay-agent` | 80-char titles, item specifics score, Terapeak research, Promoted Listings General vs Priority, Markdown Manager, Seller Hub CSVs | **advisor only** — you do it |
| `amazon-agent` | Titles/bullets/backend terms, flat files, A+ content, Brand Analytics + SQP, Business Reports, PPC harvesting, FBA replenishment, suppressed/stranded | **advisor only** — you do it |
| `market-research-agent` | Trends, demand, bestsellers, price bands, seasonality, gaps, shop fit | none (research) |
| `seo-agent` | Marketplace keywords + Google SEO (meta, alt, JSON-LD, collections, blog, GMC, GSC); Semrush | proposals |
| `analytics-agent` | Sales, funnel, traffic sources, zero-sale, ROAS, experiments, compare | none (analysis) |
| `profit-agent` | Profit per product/size/platform, price floor, break-even ROAS/ACoS | none (analysis) |
| `creative-agent` | Room shots (design locked), size charts, infographics, banners, icons, video; 2–3 options + QA | upload = proposal |
| `product-dev-agent` | Original product ideas: brief, colours, prompts, listing package, shop fit | new listing = proposal |
| `social-agent` | Pinterest + Instagram plans, pins, captions | posting = proposal |
| `customer-service-agent` | Drafts for messages, reviews, returns, cases | sending = proposal |
| `ops-agent` | Daily log, evening summary, weekly report, reminders, freeze, approvals queue, experiments due | none |

## Commands

| Command | One-line use |
|---|---|
| `/start` | Menu: platform → shop → task; the master routes to agents |
| `/connect-shop` | Add a shop → private profile + exports folder (one per shop) |
| `/audit` | Paste one listing for fixes, or `/audit <shop>` for a full account audit |
| `/health` | Monthly health check with 🟢🟡🔴 and Top 5 actions |
| `/seo` | Keywords + listing package + Google SEO |
| `/research` | What's selling, why, demand, price bands, fit |
| `/new-product` | Original product ideas → listing package |
| `/creative` | Images, banners, size charts, video — 2–3 options |
| `/ads` | Etsy Ads / eBay Promoted Listings / Amazon PPC / Google Shopping |
| `/report` | `daily` · `evening` · `weekly` · `reminders` · `experiments` |
| `/approvals` | Queue; `ok <ID>` / `no <ID>` |
| `/freeze` | Freeze / list / lift live changes for a shop or area |
| `/analyze` | (v0.1) analysis — now runs analytics-agent |
| `/prompts` | (v0.1) prompt-only creative packs |

## Shared rules
`.claude/skills/core/AGENT-RULES.md` — modes, approval, privacy, honesty, safe speed, language, shop isolation, return format.
