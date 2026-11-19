---
name: new-product-planner
description: Given a bestseller or a trend, suggest new color/design/size/shape variants, decide which shop each should be listed in, and give a launch checklist. Use when the owner asks what new products or variants to make, or wants to expand a winning listing.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# New Product Planner

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Either **a bestseller** (listing title/ID/photo + what sells: sizes, colors) or **a trend/idea** (e.g. "checkered rugs", "scalloped edge", "mushroom kids rug"). Plus shop(s) in scope — default all primary shops.

Read: shop profiles (positioning — which shop owns what), latest shop-analysis / compare reports, keyword pools, `data/learnings.md`. If a bestseller is named and CSV data exists, pull its size/price/country mix via `python scripts/etsy_analyze.py --shop <shop>`.

## Step 1 — Why does it sell? (bestseller mode)

One line each: design hook · color story · size sweet spot · price band · keyword it ranks for · buyer/room. New variants must keep the hook and change **one thing at a time**.

## Step 2 — Variant ideas

Give 8–12 ideas across these levers, ranked by (demand evidence × ease to make × fit with shop):

| Lever | Examples |
|---|---|
| Colorway | neutral (ivory/beige/greige), earthy (rust, terracotta, olive, mustard), cool (sage, dusty blue, navy), soft (blush, lilac), bold (black/white, cobalt), seasonal (fall rust → spring pastel) |
| Size/format | missing standard sizes, runner version (2x6/2x8/2x10), round version (4/5/6/8 ft), EU cm sizes, oversized 9x12, bedside pair |
| Shape (tufted) | irregular/organic, scalloped, arch, wavy edge, oval, animal/flower shapes |
| Pile/texture | high-low carved, loop + cut mix, tassels/fringe, thicker "cozy" version, flat low-profile version |
| Material | wool → wool-cotton budget version, undyed natural wool, jute border |
| Room/buyer | nursery version (softer colors, round), kids version, kitchen runner, entryway 2x3/3x5 |
| Pattern sibling | same palette, new pattern (checkered ↔ stripes ↔ abstract ↔ geometric) → a "collection" |
| Personalization | custom name/initial (tufted), custom color match |

Trend mode: translate the trend into 3–5 concrete rug designs our artisans can make, with honest construction; note trend risk (fad vs lasting).

Output table: `# | Variant | What changes | Why (evidence) | Shop | Sizes to launch | Target price band | Effort (L/M/H) | Priority`.

Evidence must be labelled: `data` (from our exports) / `competitor` (owner-pasted) / `idea` (unverified — owner should check Etsy search/Pinterest).

## Step 3 — Which shop?

Use each profile's "Positioning" line + sales data:
- Match each idea to the connected shop whose niche, price band and proven categories fit best (generic mode / single shop: skip this step).
- One primary shop per product. Cross-list only with different photos + title angle + size set, and say why.
- Add to an existing listing as a new variation (keeps reviews/ranking) **vs** a new listing (new keywords/photo) — decide per variant: same design + new size → variation; new color with its own search demand ("sage green rug") → new listing.

## Step 4 — Launch checklist (per chosen variant — paste-ready)

```
PRE-LAUNCH
[ ] Sample / photo-ready piece made (or realistic mockup plan) — size: …
[ ] Costing → pricing-advisor → size-wise prices
[ ] Keywords → keyword-research (primary phrase: …)
[ ] Listing package → etsy-listing-seo
[ ] 10 photos + video → image-prompts / video-ad-prompts (hero = real photo)
[ ] SKU: [SHOP]-[CONSTR]-[DESIGN]-[COLOR]-[SIZE]

LAUNCH DAY
[ ] Publish Tue–Thu, US morning (evening IST)
[ ] All attributes filled, all sizes + custom option, free shipping profile
[ ] Add to correct shop section; feature it (top 4 featured listings)
[ ] Link from the parent bestseller's description ("Also available in …")
[ ] Favorite/share via Share & Save link to Pinterest (2–3 pins) + Instagram

FIRST 30 DAYS
[ ] Etsy Ads ON for the new listing (small budget) — judge after 30 clicks
[ ] Day 14: check impressions/CTR → if CTR <1% change photo 1; if no impressions change title start/tags
[ ] Day 30: send stats → decide scale / fix / retire → log in learnings.md
```

## Step 5 — Reply

In the owner's language: "Make these top 3 now" (with reason) → full table → checklist for #1 → ask which one to turn into a full listing package. Also add a seasonal note: which variants suit the next 90 days (Western calendar).

## Rules

- Original designs only — no copying a competitor's exact design, no licensed characters/brand logos.
- Don't recommend more than 3 launches at once (artisan capacity + clean testing).
- Honest construction/material for every idea.
