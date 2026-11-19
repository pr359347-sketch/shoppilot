---
name: image-prompts
description: Generate a 10-photo listing image set as paste-ready prompts for Google Flow / Nano Banana / Gemini — hero flat and angled, living room, bedroom, nursery, texture close-up, pile/edge detail, size comparison, folded/rolled, packaging, lifestyle — tailored to the rug type and shop. Use when the owner asks for photo prompts or listing images.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Image Prompts — 10-photo Etsy listing set

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Rug description (or the owner's real product photo) · construction · material · pile height · colors · pattern · shape · size shown · shop · target room/style. Read the shop profile for visual positioning and `.claude/skills/domain/rugs.md`.

## Non-negotiable: the rug in the image must be the real rug

Etsy requires photos to represent the actual item. So:
- **Preferred workflow = image-to-image.** Owner uploads the real rug photo (flat, top-down, good light) into Nano Banana / Gemini / Flow and uses our prompt to place *that exact rug* in a scene. Every prompt starts with a lock line:
  `Use the uploaded rug photo as the exact product. Keep its pattern, colors, proportions, pile texture and edges 100% unchanged. Do not redesign, recolor or restyle the rug.`
- **Photo 1 (hero), texture close-up and pile/edge detail should be real camera photos** whenever possible — give shooting instructions for these (plus an AI clean-up prompt: straighten, even light, remove background clutter — no design change).
- Text-to-image (no reference photo) only for **concept mockups before the rug exists** — label those prompts `MOCKUP ONLY — not for the live listing`.
- After generating, the owner must reject any image where pattern/color/size ratio drifted. Remind them in "Next steps".

## Prompt building blocks

`[lock line] + [scene/room + style] + [rug placement + true scale] + [camera angle + lens] + [light] + [props, minimal] + [mood/palette that complements the rug] + [quality tags] + [negatives]`

- **Scale truth:** state real size and anchor furniture — 5x8 under a 3-seat sofa's front legs; 8x10 holds all sofa legs; 2x3 at a door/bedside; 4 ft round under a nursery chair; runner in an 3 ft-wide hallway. Never make a small rug look room-size.
- **Light:** soft natural daylight from a side window, no harsh shadows, true-to-life color, neutral white balance.
- **Rooms for US/EU buyers:** light oak/wood floors, white or warm-neutral walls, linen sofa, plants, minimal clutter; Scandinavian / modern / boho / farmhouse per rug style. Decor must look native to the buyers' market, no text, no logos, no people's faces (hands/feet OK).
- **Texture by construction:** tufted = dense plush cut pile, visible carved high-low lines; knotted = fine knots, slight sheen, fringe; flatweave/kilim = flat woven surface, visible weft, crisp geometric edges; dhurrie = thin cotton weave; jute = chunky braided natural fibre.
- **Format:** `4:3 landscape, 2000px+` for Etsy (thumbnail crops centre — keep the rug centred, full rug visible in photo 1). Add 1:1 variant on request.
- **Negatives (append):** `no text, no watermark, no logo, no extra rugs, no warped pattern, no changed colors, no distorted furniture, no people's faces, no oversaturation`.

## The 10-photo set (output one block per photo)

| # | Shot | Purpose | Notes |
|---|---|---|---|
| 1 | **Hero** — flat top-down *or* slight 30° angle, full rug, clean light floor | CTR | Real photo preferred. Give both flat and angled versions; recommend one (pattern-heavy → flat; plush texture → angled) |
| 2 | Living room | "see it in my home" | Sofa + coffee table, correct scale |
| 3 | Bedroom | second use case | Under bed, 2/3 visible, bare feet optional |
| 4 | Nursery / kids room (or entryway/kitchen/dining if not kid-suitable) | room keyword match | Crib/armchair; soft palette |
| 5 | Texture close-up (macro) | quality proof | Real photo preferred; 45° raking light |
| 6 | Pile height / edge / backing detail | trust | Hand pressing pile, corner folded to show backing, ruler optional |
| 7 | Size comparison / size chart | fewer returns | Top-down outlines of 2x3…9x12 with furniture silhouettes; text overlay list added by owner in Canva: sizes in ft + cm |
| 8 | Folded / rolled | thickness, giftable | Rolled rug tied with jute string / neatly folded stack |
| 9 | Packaging | shipping trust | Rolled in protective wrap + kraft box/bag, "handmade with care" card (blank — text added later) |
| 10 | Lifestyle | emotion | Coffee cup, book, pet or child's feet, morning light — seasonal version if within 60 days of an occasion (Christmas tree corner, spring flowers) |

Adapt automatically: runner → hallway + kitchen + bedside instead of living room/bedroom; round → nursery, reading nook, under round table; kids rug → playroom, floor-level angle; flatweave → dining under table, kitchen, door clearance shot; visual style from the shop profile / brand file when a shop is connected.

## Output format

For each photo:
```
PHOTO 3 — BEDROOM
Tool: Nano Banana / Gemini (image-to-image, upload real rug photo)
Prompt:
<full paste-ready prompt>
Aspect: 4:3
```
For real-photo slots (1, 5, 6) give **How to shoot** instructions (3 bullets: angle, light, setup) + an AI clean-up prompt.

Then: **Alt text** for each of the 10 (English, ≤500 chars, 1 natural keyword) · **Canva overlay text** for #7 (sizes list) and optional icons row (Handmade · Wool · Custom Size · Free Shipping — only true ones) · **Next steps** (owner's language): generate → reject drifted ones → upload order 1–10.

## Rules

- Never generate fake review screenshots, fake badges, "bestseller" stamps, or certification logos.
- No copyrighted characters, brand furniture logos, or real people.
- Seasonal props must match the target market (default Western: Christmas greenery, pumpkins in fall).
