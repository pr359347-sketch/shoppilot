---
name: listing-audit-framework
description: Audit a live listing the owner pastes (title, tags, description, price, variations, photos, stats) — find CTR and conversion problems and give exact paste-ready fixes. Use when the owner asks to check a listing, pastes listing text/screenshot, or asks why a listing isn't selling.
---

# Listing Audit Framework

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Owner pastes any of: title, tags, description, price(s), variations, photo list/screenshots, listing stats (impressions/visits/favorites/orders, date range), reviews count. Work with whatever is given — list what's missing at the end as "send these next time", don't block.

If a listings CSV exists in `data/exports/<shop>/`, you may pull the listing's title/tags/price from it (match by title). Run `python scripts/etsy_analyze.py --shop <shop> --listing-health` for bulk title/tag/photo checks across all listings.

Read first: shop profile, `.claude/skills/etsy/PLATFORM.md` (limits + benchmarks), `.claude/skills/domain/rugs.md`, `data/learnings.md`, relevant keyword pool.

## Step 1 — Diagnose the funnel (if stats given)

| Symptom | Problem area | Look at |
|---|---|---|
| Low impressions | **Findability** | title start, tags, attributes, category, too-niche or too-broad keywords |
| Impressions OK, CTR < 1% | **Click appeal** | photo 1, price shown in grid (lowest variation), first 40 chars of title, free shipping badge, sale badge |
| Visits OK, favorites OK, orders low | **Price / trust** | price vs competitors, shipping cost/time, reviews, return policy |
| Visits OK, favorites low, orders low | **Listing page** | photos 2–10, sizes confusion, description, no video |
| Sells only one size | **Variation pricing** | price ladder, missing sizes |

State the diagnosis in one line (owner's language): e.g. "This is a click problem, not an SEO problem — fix photo 1 and the starting price."

## Step 2 — Score (0–10 each, one-line reason)

| Area | Checks |
|---|---|
| Title | primary phrase in first 40 chars? readable? ≤140? stuffing/repeats? construction + material + style + room + size cue present? |
| Tags | all 13 used? each ≤20? multi-word? repeated words wasted? match title phrases? single-word or irrelevant tags? missing room/size/occasion angles? |
| Attributes/category | (if visible) all filled? correct shape/material/room? |
| Photos | hero clean + bright + shows whole rug + thumbnail-safe crop? room scene? scale reference? texture close-up? size chart image? 10 used? video? alt text? |
| Price & variations | entry price attractive in grid? ladder logical per sq ft (bigger = cheaper per sq ft)? all standard sizes + runners/round + custom? ft + cm labels? |
| Description | keyword in first 160 chars? scannable? sizes, pile, material, care, shipping time, custom CTA, FAQ, shedding/handmade notes? |
| Trust | processing time, shipping clarity, returns, duties note |
| Honesty | wrong construction/material/origin claims = flag as **RISK** (case/bad review risk) |

Give total /80 and a verdict: 🔴 rebuild · 🟡 fix top 3 · 🟢 minor polish.

## Step 3 — Exact fixes (paste-ready)

Order by impact. For each fix: **Current** → **New** (in a code block) → 1-line why.

Always provide when relevant:
- **New title** (with char count) — keep any phrase that is already bringing sales/search terms (don't destroy a ranking listing: if the listing has steady sales, change tags/photos first and title only lightly; say this).
- **New 13 tags** (with counts) — mark each `KEEP` / `NEW` / replaced-what.
- **Photo fixes** — slot-by-slot (1–10): keep / reshoot / add, with what the new shot should be (offer `image-prompts`).
- **Price/variation fixes** — table of size → current → suggested (or hand off to `pricing-advisor` if costs unknown).
- **Description patch** — only the missing/weak blocks, written out.
- **Attributes to fill.**

Follow all keyword placement rules from `etsy-listing-seo`.

## Step 4 — Next steps

Numbered list, max 6 steps, most impactful first. Add: "Don't change everything at once — title + tags + photo 1 today, send stats after 2–3 weeks, then the next round." Ask the owner to send before/after stats later → log to `data/learnings.md`.

## Rules

- Change-safety: for listings with sales history, recommend staged changes and never recommend deleting/relisting a listing that has reviews/sales; suggest "copy listing" for experiments instead.
- No invented numbers. If no stats, say the diagnosis is based on content only.
