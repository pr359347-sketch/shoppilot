---
name: etsy-listing-seo
description: Build a complete paste-ready Etsy listing package for a rug or textile — title, 13 tags, description with size + price table, alt text for 10 photos, attributes, category, materials. Use when the owner asks for a new listing, or to rewrite title/tags/description for a product.
---

# Etsy Listing SEO — full listing package

> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Before writing

1. Read: shop profile (`data/shops/<shop>.md`), `.claude/skills/etsy/PLATFORM.md`, `.claude/skills/domain/rugs.md`, `data/brand.md`, `data/learnings.md`, and the matching pool(s) in `data/keyword-pools/`.
2. Needed inputs — take from the owner's message/photo; ask **once, in one message** only for must-haves that are missing:
   - shop · construction · material (+ blend %) · pile height · colors · design/style · sizes offered · prices per size (or offer to run the pricing advisor) · processing + shipping time · custom options
   - Nice-to-have: target room, backing, weight, SKU.
   - Anything still unknown → use `[PLACEHOLDER]` and list it under "You need to fill in". Never invent facts.
3. If no keyword set was given, run the `keyword-research` logic first (pool → pick). Choose **1 primary phrase** (highest intent, e.g. "hand tufted wool rug"), **2–3 secondary** (style/room/color), and long-tails for tags.

## Keyword placement rules

- **Title first 40 chars = primary phrase + strongest modifier** (this is what shows in search grid/mobile and carries most weight). Example: `Hand Tufted Wool Rug, Modern Abstract Area Rug` …
- Title order: primary phrase → style/color → room → size cue ("5x8 8x10 Custom Size") → gift/occasion (only if seasonal fit). 70–120 chars ideal, hard max 140. Title Case, commas or ` - ` separators, no word used more than twice, no ALL CAPS, no symbols/emoji.
- **Tags:** exactly 13, each ≤20 chars, all multi-word long-tail (2–3 words). Rules:
  - Exact-match the title's key phrases in 3–4 tags (title + tag match = strongest relevance).
  - **No word repeated across tags** beyond what is unavoidable — "rug" will repeat; every *other* word (wool, boho, living…) should appear in max 2 tags. More unique words = more query combinations covered.
  - Don't spend tags on words already covered by category/attributes (e.g. color attribute "Beige" already indexes "beige") — unless it's a core phrase like "beige wool rug".
  - Mix: 3 head/product · 3 style/color · 2 room · 2 size/shape · 1 material/construction · 1–2 occasion/gift/buyer-intent.
  - No misspellings, no singular+plural duplicates, no brand names, English only.
- **Description first 160 chars**: natural sentence containing the primary phrase (Google snippet).
- Seasonal fit: check today's date; if within 60 days of a major Western occasion, 1 tag + 1 description line may target it (flag it as "remove after the season").

## Output format (always this order, each block in its own code fence so it's copy-paste)

**1. TITLE** — give 2 options (A = recommended, B = alternative angle) with character counts.

**2. TAGS** — numbered 1–13, each with char count, comma-separated copy line at the end.

**3. CATEGORY + ATTRIBUTES** — category path, then a table: Attribute → Value (primary color, secondary color, material, shape, length, width, style, room, pattern, pile, occasion/holiday only if real).

**4. MATERIALS** (≤13) — comma-separated.

**5. VARIATIONS** — Variation 1 "Size" with every option labelled `5x8 ft (150x240 cm)`; Variation 2 (color / backing / shape) if needed; note "price varies by size = ON".

**6. DESCRIPTION** — plain text (Etsy has no formatting; use CAPS section headers and `•` bullets, short lines):

```
[HOOK — 2 lines: feeling + primary keyword]

[1 short paragraph — the product: design, feel, who it's for, handmade story line from brand.md]

DETAILS
• Construction: …
• Material: …
• Pile height: …
• Backing: …
• Colors: …
• Best for: living room, bedroom, …

SIZES & PRICES
2x3 ft (60x90 cm) — $…
3x5 ft (90x150 cm) — $…
…runners… round…
Need a different size? See CUSTOM SIZE below.

WHY YOU'LL LOVE IT
• 3–5 USPs (true ones, from brand.md)

CARE
• …(by material, from `.claude/skills/domain/rugs.md`)

SHIPPING
• Made to order in … days • ships via … with tracking • delivery … • free shipping …

CUSTOM SIZE & COLOR
Message us with your size (in feet, inches or cm) — we reply within 24 hours with a quote. [custom line]

GOOD TO KNOW
• handmade variation / screen color / shedding (wool) / fold lines / rug pad

FAQ
Q: … A: …   (5 questions: size help, shedding, pets/kids, custom, delivery time/duties)
```
Sizes table lists only sizes the shop actually offers. Prices only from the owner or the pricing skill — otherwise `$[PRICE]`.

**7. ALT TEXT — 10 photos** (≤500 chars each, aim 100–200; describe the image + one natural keyword; no "image of"): 1 hero, 2 living room, 3 bedroom, 4 nursery/other room, 5 texture close-up, 6 pile/edge detail, 7 size chart/comparison, 8 folded/rolled, 9 packaging, 10 lifestyle. If the owner's real photo order differs, follow theirs.

**8. You need to fill in** — placeholders list. **9. Next steps** — 3–5 numbered steps (owner's language), incl. offering photo prompts / translation as an optional next step.

## Self-check before sending (silently fix, don't narrate)

- [ ] Title ≤140, primary phrase inside first 40 chars, no word 3×.
- [ ] Exactly 13 tags, each ≤20 chars (count spaces), no duplicate tags, repeated-word rule followed.
- [ ] Construction/material claims match what the owner said. "Moroccan/Persian" → "style".
- [ ] Sizes in ft + cm. Wool → shedding line present. Occasions match the target market. No brand names.
- [ ] Customer-facing text English; chat to the owner in the owner's language.

## After

- If the owner approves new keywords, append them to the pool file under the right section.
- If the owner later reports results, log in `data/learnings.md`.
