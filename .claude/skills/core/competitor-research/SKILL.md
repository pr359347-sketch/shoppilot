---
name: competitor-research
description: Gap analysis from competitor data the owner pastes (titles, tags, prices, sizes, screenshots of listings or shops) — finds keywords, sizes, price points, styles and photo tactics the owner's shop is missing. Use when the owner shares competitor listings/shops or asks what competitors are doing.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Competitor Research

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Owner pastes any mix of: competitor listing titles, tags (bottom of listing page "Explore related searches"/tag list), prices per size, variation lists, review counts, "bestseller / popular now" badges, shop sales counts, screenshots. Also which of our shops + product this is for.

Read: our shop profile, relevant keyword pools, our listings CSV if present (`data/exports/<shop>/EtsyListingsDownload.csv`), `data/learnings.md`.

If the owner gives only a shop/listing URL and a browser tool is available, you may read the public page; otherwise ask them to paste title + price + sizes + tags. Don't guess a competitor's sales.

## Analysis

1. **Extract** into a table: `Competitor | Title (first 40 chars) | Entry price | Sizes offered | Price per sq ft (5x8 and 8x10) | Badges/reviews | Photo 1 type | Notable`.
2. **Keyword gap:** tokenize competitor titles/tags into phrases → compare with our titles/tags + pools:
   - `THEY USE, WE DON'T` (rank by how many competitors use it) ← main output
   - `BOTH`
   - `WE USE, THEY DON'T` (keep if proven, question if not)
3. **Size gap:** standard sizes (see `.claude/skills/domain/rugs.md`) they offer that we don't; EU cm sizes; runners/round/custom; how they label sizes.
4. **Price gap:** our price vs competitor median per size (per sq ft). Flag: we're >20% above without a reason, or >20% below (leaving money). Note their shipping (free vs paid) and sale % — compare **landed price**.
5. **Style/color gap:** designs, colorways, shapes (irregular, scalloped, checkered…) trending among them that we lack.
6. **Listing tactics:** photo 1 style (flat lay vs room vs angled), video, size-chart image, personalization, bundles, "custom" positioning, processing time, return policy.
7. **Where we can win:** things competitors do badly (few sizes, slow shipping, poor photos, no custom option) that match our USPs.

## Output

Summary in the owner's language (3–4 lines) → then:

1. **Missing keywords** — table `Keyword | Chars | Tag-ready? | Used by (n competitors) | Where to use (title/tag/desc) | Honest for our product?` — drop anything that would be a false claim (origin, construction, trademark).
2. **Missing sizes** — list with suggested labels (ft + cm).
3. **Price points** — table `Size | Ours | Competitor low / median / high | Suggestion` (send to `pricing-advisor` for the final matrix).
4. **Styles/colors to add** — 3–6 ideas (hand to `new-product-planner`).
5. **Tactics to copy / avoid.**
6. **Next steps** — top 5 actions with the skill for each.

## Rules

- Take inspiration from patterns, never copy a competitor's title, description text, photos or exact design. Suggest original wording/designs.
- Never put competitor shop names or brand names in our titles/tags.
- Save approved new keywords to the pool (`idea` or `proven` if they came with bestseller evidence — note "competitor bestseller, YYYY-MM-DD").
- Save the analysis to `data/reports/YYYY-MM-DD_<shop>_competitor-<topic>.md` if it's more than a quick look.
