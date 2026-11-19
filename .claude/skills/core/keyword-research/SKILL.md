---
name: keyword-research
description: Build a keyword pool for a product (rug type or any home decor / textile item) + color/style/room — head, long-tail, room, style, size, occasion and buyer-intent keywords, tag-ready (≤20 chars) and title-ready. Checks data/keyword-pools first and the shop's own search-term data, then suggests new ones. Use when the owner asks for keywords or before writing a listing.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Keyword Research

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Rug type (construction) + any of: color, style, room, size focus, shop, season. Missing pieces → assume from the shop profile and say what you assumed in one line.

## Sources — in this order

1. **Proven data (strongest):**
   - `data/exports/<shop>/` search-terms files (`search_terms*.csv`) or anything the owner pasted from Stats → "Search terms".
   - Order-item titles of bestsellers (what already converts).
   - `## Proven` sections in keyword pools and `data/learnings.md`.
2. **Pool:** matching file(s) in `data/keyword-pools/` — always combine construction pool + style/shape pool (e.g. `rug-tufted.md` + `rug-moroccan.md` + `rug-runner.md`).
3. **New ideas:** generate by combining the grid below. Mark as `idea`.
4. **Optional live check** (only if the owner asks for a live check or a browser/search tool is available): Etsy search-bar autocomplete for the head terms, and the titles of the first-page bestseller/popular-now listings. Never present guessed volume as data.

Combination grid for ideas: `[color] + [style] + [construction/material] + rug` · `[room] + rug` · `[size] + [material/style] + rug` · `[shape] + rug + [room]` · `[occasion] + gift` · problem/intent phrases ("soft rug for baby", "low profile rug").
Add US vs UK variants where they differ (colour/color isn't needed — Etsy stems; but "hallway runner" US = "hall runner" UK; "nursery" both; "throw rug" US; "carpet" used in UK/EU/IN searches).

## Output format

Intro in the owner's language (1–2 lines), then English tables. Columns: `Keyword | Chars | Tag-ready (≤20)? | Use in | Confidence (proven/pool/idea)`.

Sections (8–12 keywords each, best first):
1. **Head** (broad, high competition — use 1–2 in title start)
2. **Long-tail** (3–5 words, the money phrases — title + split into tags)
3. **Room**
4. **Style / color**
5. **Size / shape**
6. **Material / construction**
7. **Occasion / season** — Western only; put the next 90 days' occasions first (check today's date)
8. **Buyer-intent** (gift, custom, problem-solving)

Then:
- **Top pick set** — a ready 13-tag set (with char counts, repeated-word rule applied) + the recommended first-40-chars title phrase.
- **Avoid list** — keywords that look tempting but are wrong: wrong construction, origin claims ("authentic moroccan"), trademarks, single-word tags, irrelevant high-volume terms.
- **Worth checking** — 5 `idea` keywords the owner should verify by typing into Etsy search (autocomplete shows = real demand).

## After

- Connected mode: ask whether to save to the pool — on yes (or if the owner already asked to save), append new keywords to the right section of the right pool file with `(idea, YYYY-MM-DD)` or `(proven: <source>, YYYY-MM-DD)`. Keep tag-ready sections ≤20 chars; longer phrases go under Long-tail.
- If a needed pool file doesn't exist (new product type), create it with the standard sections: Head / Long-tail / Room / Style / Size / Material / Occasion / Buyer-intent / Proven / Tested & dropped.
