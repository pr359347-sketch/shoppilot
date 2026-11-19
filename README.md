# ShopPilot v1.0

**Your AI co-pilot for marketplace growth — a master agent + 13 specialist subagents for Etsy, Shopify, eBay and Amazon sellers.**

ShopPilot is an open-source [Claude Code](https://claude.com/claude-code) agent for handmade and home-decor sellers. It audits your shop, researches what's selling, writes SEO for the marketplace **and** Google, plans original new products, makes creatives, drafts customer replies, checks profit and ads — and presents every change as a proposal **you approve**. Nothing goes live without your "ok".

## What it does

| Area | What you get |
|---|---|
| **Audit & health** | Full account audit, monthly health check per platform (🟢🟡🔴 + Top 5 actions) |
| **Analytics** | Sales, conversion, traffic sources, zero-sale listings, ads ROAS, before/after experiments, multi-shop compare (on request) |
| **Profit** | Per product × size × platform profit after fees + shipping + cost, price floor, break-even ROAS/ACoS, loss-makers |
| **SEO** | Titles/tags/specifics/bullets per platform + Google SEO: meta titles/descriptions, alt text, structured data, collections, blog, Merchant Center feed, Search Console fixes (Semrush when connected) |
| **Market research** | What's trending, why, demand, price bands, seasonality, competitor gaps, fit with your shop |
| **New products** | Original designs from trends — brief, colour variants, preview prompts, listing package, shop fit |
| **Creative** | Room shots from your real product photo (design locked), size charts, infographics, banners, icons, video ads — 2–3 options with drift + spelling QA |
| **Ads** | Etsy Ads · eBay Promoted Listings General vs Priority · Amazon PPC search-term harvesting · Google Shopping basics |
| **Cross-listing** | One listing → every other platform's format (limits respected, bulk files) |
| **Social** | Pinterest + Instagram plans, pins, captions linking to your listings |
| **Customers** | Drafts for buyer messages, reviews, returns and cases |
| **Ops** | Daily log, evening summary, weekly report, occasion reminders, freeze rules, approvals queue, experiment tracking → learnings |

## Platform support

| Platform | Mode | Module |
|---|---|---|
| Etsy | ✅ **Executes after your ok** (browser, safe speed) | PLATFORM.md + 3 skills + analysis script + `etsy-agent` |
| Shopify | ✅ **Executes after your ok** (connector or browser) | PLATFORM.md + `shopify-agent` |
| eBay | ✅ **Advisor only** — content, upload CSV, steps; you make changes | PLATFORM.md + `ebay-agent` |
| Amazon | ✅ **Advisor only** — content, flat files, bulk sheets, steps; you make changes | PLATFORM.md + `amazon-agent` |

eBay and Amazon are advisor-only on purpose: automated activity on those seller accounts risks suspension. Fees and limits for eBay, Shopify and Amazon are marked `[VERIFY]` where they change often — the agents check before any money decision.

## Architecture

```
                         YOU  (Hinglish chat)
                          │   /start /audit /health /seo /research /new-product
                          │   /creative /ads /report /approvals /freeze /connect-shop
                          ▼
   ┌──────────────────── MASTER  (CLAUDE.md) ─────────────────────┐
   │ understand → plan → delegate → combine → proposal cards      │
   │ → your "ok" → execute (Etsy/Shopify) or give steps (eBay/Amz) │
   │ → log + experiment tracking → learnings                      │
   └───────┬───────────────┬────────────────┬───────────────┬─────┘
           │               │                │               │
     PLATFORM          GROWTH             MAKE            RUN
     etsy-agent        market-research    creative        customer-service
     shopify-agent     seo                product-dev     ops
     ebay-agent  (adv) analytics          social
     amazon-agent(adv) profit
           │               │                │               │
           └──── each reads ─▶ core/AGENT-RULES.md → skills → PLATFORM.md → domain → data/
```

## Approval flow

Every live change comes as a card:

```
🟡 PROPOSAL P-261119-03 · <shop> · etsy · title
KYA:      Title: "…" → "…" (128/140)
KYUN:     12k impressions, 0.6% CTR — main keyword not in first 40 chars
IMPACT:   CTR 0.6% → 1.2%+ in 14 days (measured from Stats)
RISK:     low — short ranking wobble for 2–3 days
ROLLBACK: old title saved in the proposal file
→ "ok P-261119-03" / "no P-261119-03" / "change P-261119-03: …"
```

- One "ok" = one proposal. Freeze rules block execution during sensitive periods (e.g. Black Friday week).
- Executed changes are verified live, logged, and re-checked at **+7 / +14 / +30 days** (before vs after). Results go into `data/learnings.md`, and future suggestions follow those learnings.

## Setup on any PC

1. **Clone**
   ```bash
   git clone https://github.com/pr359347-sketch/shoppilot.git
   ```
2. **Enable the privacy hook** (once per clone)
   ```bash
   git config core.hooksPath .githooks
   ```
3. **Open the folder in Claude Code** (desktop app or CLI).
4. **`/connect-shop`** — platform, shop, products, market, costs → your private profile in `data/`. Repeat per shop (one or many shops on one PC; each shop gets its own folder, data never mixed).
5. Drop your exports in `data/exports/<shop>/` — guides: [Etsy](docs/etsy-csv-export-guide.md) · [Shopify](docs/shopify-csv-export-guide.md) · [eBay](docs/ebay-csv-export-guide.md) · [Amazon](docs/amazon-csv-export-guide.md).
6. **`/start`** — or just say what you need.

**Connectors** (optional, used automatically when present): Shopify, Canva, Semrush, Search Console / analytics. Without them ShopPilot uses the built-in browser (Google Trends, Gemini, Flow) or gives you a prompt pack.

**Generic mode** — no shop connected? Research, SEO, creatives, product ideas, cross-listing, customer replies and pricing still work; you give product details in the prompt.

## Privacy

- This repo contains **only the agent** — no shop data.
- Everything private lives in `data/` (git-ignored): profiles, brand, costs, exports, reports, keyword pools, approvals, logs, learnings. Only `data/.gitkeep` and `data/README.md` are tracked.
- The **pre-commit hook** blocks anything under `data/`, `reports/`, `exports/`, any `.env`/CSV/Excel file, personal emails, real shop URLs and every word in your private `data/.private-keywords`.
- Before every push ShopPilot shows `git status` and a keyword grep.
- Order exports contain buyer details — agents use aggregates only and never write buyer names or addresses anywhere.

## Commands

See [docs/agents-reference.md](docs/agents-reference.md) for every subagent and command.

| Command | Use |
|---|---|
| `/start` | Menu: platform → shop → task |
| `/connect-shop` | Add a shop (private profile + exports folder) |
| `/audit` | One listing you paste, or a full account audit |
| `/health` | Monthly health check |
| `/seo` | Keywords + listing package + Google SEO |
| `/research` | Trends, demand, price bands, fit |
| `/new-product` | Original product ideas with listing package |
| `/creative` | Images, banners, size charts, video (2–3 options) |
| `/ads` | Etsy Ads / Promoted Listings / Amazon PPC |
| `/report` | Daily, evening, weekly, reminders, experiments |
| `/approvals` | Pending proposals, owner to-dos, experiments due |
| `/freeze` | Pause live changes for a shop/area |
| `/analyze`, `/prompts` | v0.1 commands, still work |

## Project layout

```
CLAUDE.md                master agent: rules, modes, routing, privacy + git rules
.claude/agents/          13 subagents
.claude/commands/        14 slash commands
.claude/skills/
  core/                  AGENT-RULES.md + 22 platform-agnostic skills
  etsy/ ebay/ shopify/ amazon/   PLATFORM.md each (+ Etsy skills)
  domain/                rugs.md, home-textiles.md
scripts/                 etsy_analyze.py
templates/               shop, brand, settings, learnings, keyword pools, proposal, freeze, daily-log
docs/                    export guides ×4, agents-reference, skills-reference, adding-a-platform, faq
data/                    YOUR private workspace — git-ignored
```

## Roadmap

- [x] v0.1 — Etsy module, core skills, two modes, privacy guard
- [x] v1.0 — master + 13 subagents, Shopify/eBay/Amazon modules, approval flow, experiment tracking, ops
- [ ] Analysis scripts for eBay / Shopify / Amazon exports
- [ ] More product domains (jewelry, ceramics, wall art, furniture)

Contributing: [CONTRIBUTING.md](CONTRIBUTING.md) · [docs/adding-a-platform.md](docs/adding-a-platform.md) · [docs/faq.md](docs/faq.md)

## License

[MIT](LICENSE)

---

## Quickstart (Hinglish)

ShopPilot ek **master agent + 13 expert subagents** ka system hai. Aap kaam batao, master plan banata hai, sahi experts se kaam karwata hai, aur har change ko **proposal card** ki tarah dikhata hai (KYA / KYUN / IMPACT / RISK). Aapke "ok" ke bina kuch live nahi hota.

- **Etsy + Shopify:** "ok" ke baad ShopPilot khud change karta hai (insaan ki speed se).
- **eBay + Amazon:** sirf advisor. Content, CSV/flat file aur steps milenge, change aap karengi.

1. Repo clone karo, phir `git config core.hooksPath .githooks` chalao, phir folder Claude Code me kholo.
2. `/connect-shop` chalao (har shop ke liye ek baar).
3. Exports `data/exports/<shop>/` me daalo.
4. `/start` chalao, ya seedha likho kya chahiye.

Aapka saara data sirf `data/` me rehta hai. Wo git me kabhi nahi jaata.
