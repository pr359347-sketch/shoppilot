# ShopPilot

**Your AI co-pilot for marketplace growth.**

ShopPilot is an open-source [Claude Code](https://claude.com/claude-code) agent for handmade and home-decor sellers. It is an **advisor**: it never touches your shop. It analyzes your data, tells you exactly what to change, and hands you paste-ready titles, tags, descriptions, prices and creative prompts. You stay in control.

## Platform support

| Platform | Status | Module |
|---|---|---|
| Etsy | ✅ Ready | listing SEO · shop analysis · ads optimizer |
| eBay | 🔜 Planned | — |
| Shopify | 🔜 Planned | — |
| Amazon | 🔜 Planned | — |

Multi-platform from day one: platform-agnostic **core** skills + one **module** per marketplace + **domain** knowledge per product type (rugs, home textiles).

## Features

| | Feature | Needs a connected shop? |
|---|---|---|
| **SEO** | Full listing package — title, tags, description with size + price table, attributes, alt text | no |
| | Listing audit — CTR and conversion problems → exact fixes | no |
| | Keyword research — head, long-tail, room, style, size, occasion, buyer-intent | no |
| | Localized titles + tags in 9 languages | no |
| **Analytics** | Shop analysis from your exports — best / worst / zero-sale listings, sizes and price bands that sell, seasonality, countries, repeat buyers | **yes** |
| | Multi-shop comparison — where to focus, which product belongs where | **yes** (2+ shops) |
| | Ads optimizer — ROAS per listing → pause / scale / fix | **yes** |
| **Strategy** | Competitor gap analysis from listings you paste | no |
| | Size-wise pricing matrix (costs + fees + free shipping + sale headroom) | no |
| | 90-day seasonal calendar with order cutoffs | no |
| | New product / variant planner with launch checklist | no |
| **Creative** | 10-photo listing image prompts | no |
| | Shop banner, Pinterest and Instagram prompts with text overlays | no |
| | 8–15 second listing video and reel prompts | no |

Details: [docs/skills-reference.md](docs/skills-reference.md)

## Setup — 3 steps

1. **Clone**
   ```bash
   git clone https://github.com/pr359347-sketch/shoppilot.git
   ```
2. **Open the folder in Claude Code**
3. **Run `/connect-shop`** — a few questions (platform, shop, products, market, goals, costs) and your private shop profile is created. Repeat per shop.

Then `/start` for the menu (platform → shop → task), or just say what you need.

Other commands: `/analyze` · `/audit` · `/seo` · `/prompts`

## Two modes

| | Connected mode | Generic mode |
|---|---|---|
| When | you ran `/connect-shop` | no shop connected |
| What works | everything, personalized with your profile, keyword pools and past learnings | SEO, audits, keywords, competitor research, pricing, seasonal plans, creative prompts — you give product details in the prompt |
| Data features | shop analysis, shop comparison, ads optimizer | not available — "run `/connect-shop` for analysis features" |

The mode is detected automatically.

## Privacy

- This repo contains **only the agent** — instructions, skills, templates, docs and one script. No shop data.
- Everything about your business — shop profiles, brand, costs, exports, reports, keyword pools, learnings — lives in `data/`, which is **git-ignored**. Only `data/.gitkeep` and `data/README.md` are tracked.
- A **pre-commit hook** blocks commits containing anything under `data/`, `reports/` or `exports/`, any `.env` / CSV / Excel file, personal email addresses or real shop URLs, and any word you list in `data/.private-keywords`. Enable it once after cloning:
  ```bash
  git config core.hooksPath .githooks
  ```
- Order exports contain buyer names and addresses. The analysis script prints aggregates only and the agent never writes buyer details into reports.

## Getting your data in

Shop analysis needs your marketplace exports in `data/exports/<shop>/`. Step-by-step guide: **[docs/etsy-csv-export-guide.md](docs/etsy-csv-export-guide.md)**. If a file is missing when you ask for an analysis, ShopPilot shows you the exact steps.

## Example prompts

- `New listing: hand tufted wool rug, beige and black abstract, 0.5 in pile, sizes 3x5 to 9x12, custom sizes available.`
- `Audit this listing — it gets views but no sales:` *(paste title, tags, price, description)*
- `Keywords for a Moroccan-style cream wool rug for living rooms and bedrooms.`
- `Analyze my shop — the CSVs are in the exports folder. What sells and what doesn't?`
- `Compare my two shops. Where should I focus?`
- `Check my ads — what do I pause and what do I scale?`
- `Here are 5 competitor listings (title, price, sizes). What am I missing?`
- `Build a size-wise price matrix: making cost <X> per sq ft, shipping <Y> per kg, 30% margin, free shipping.`
- `90-day plan — what should I list, optimize and promote for the holidays?`
- `Suggest new color variants of my bestseller, then 10 photo prompts and a 12-second video prompt.`

## Project layout

```
CLAUDE.md                master context: role, platform routing, modes, privacy + git rules
.claude/commands/        start, connect-shop, analyze, audit, seo, prompts
.claude/skills/
  core/                  11 platform-agnostic skills
  etsy/                  Etsy module (PLATFORM.md + 3 skills)
  ebay/ shopify/ amazon/ placeholders with the module contract
  domain/                rugs.md, home-textiles.md
scripts/                 etsy_analyze.py (Python 3, standard library)
templates/               shop, brand, settings, learnings, keyword-pool + starter keyword pools
docs/                    export guide, skills reference, adding a platform, FAQ
data/                    YOUR private workspace — git-ignored
```

## Roadmap

- [x] v0.1 — Etsy module, core skills, rugs + home-textiles domains, two modes, privacy guard
- [ ] eBay module
- [ ] Shopify module
- [ ] Amazon module
- [ ] More product domains (jewelry, ceramics, wall art, furniture)
- [ ] Cross-platform comparison (same product, different marketplaces)

Want to help? See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/adding-a-platform.md](docs/adding-a-platform.md). Questions: [docs/faq.md](docs/faq.md).

## License

[MIT](LICENSE)

---

## Quickstart (Hinglish)

ShopPilot ek **advisor** agent hai — aapki shop me khud kuch nahi badalta, sirf batata hai kya karna hai aur paste-ready content deta hai.

1. Repo clone karo → folder Claude Code me kholo.
2. `/connect-shop` chalao — platform, shop ka naam, products, market, cost poochega aur aapki private profile bana dega.
3. `/start` chalao — platform → shop → task chuno. Ya seedha apni baat likh do.

Bina shop connect kiye bhi listing SEO, audit, keywords, pricing, seasonal plan aur photo / banner / video prompts chalte hain. Shop analysis, compare aur ads ke liye shop connect karke CSV `data/exports/<shop>/` me daalni hogi ([guide](docs/etsy-csv-export-guide.md)).

Aapka saara data sirf `data/` folder me rehta hai — wo git me kabhi nahi jaata.
