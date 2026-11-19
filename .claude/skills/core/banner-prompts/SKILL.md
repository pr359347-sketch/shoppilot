---
name: banner-prompts
description: Create prompts and text overlays for shop graphics — big shop banner 1200x300, mini banner, shop icon, featured/sale graphics — plus Pinterest pins and Instagram posts, per shop and season. Use when the owner asks for a banner, shop graphics, pins or social posts.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Banner & Social Graphic Prompts

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Shop · asset type(s) · purpose (evergreen brand / seasonal / sale / new collection) · featured product(s) · any brand colors/fonts. Read shop profile, `data/brand.md`, `.claude/skills/etsy/PLATFORM.md` (sizes). Check today's date → if a Western occasion is within 60 days, offer a seasonal version alongside the evergreen one.

## Specs

| Asset | Size / ratio | Safe zone |
|---|---|---|
| Etsy big banner | 1200×300 min (4:1) — generate at 2400×600+ | Text in centre 60%; nothing important in outer 20% each side (mobile crop) or bottom-left (shop icon overlap) |
| Etsy mini banner | 1200×160 min (7.5:1) | Text centred, one line |
| Shop icon | 500×500 | Simple mark/monogram, readable at 50px |
| Featured / sale graphic (listing photo slot or update) | 2000×1500 (4:3) or 1:1 | |
| Pinterest pin | 1000×1500 (2:3) | Title in top third, big; logo/shop name bottom |
| Instagram post | 1080×1350 (4:5) | |
| Instagram story / reel cover | 1080×1920 (9:16) | Keep text out of top 250px / bottom 350px |

Most AI image tools don't output 4:1 natively: prompt for a **wide 21:9 or 16:9 scene with empty space top and bottom**, then crop to 4:1 in Canva. Say this in the steps.

## Method

- **Generate the background image without text**, then add text in Canva (AI text is unreliable). Each output = `Background prompt` + `Text overlay` (exact words, placement, font suggestion, color hex).
- If the tool handles text well (Nano Banana / Gemini), also give an optional "with text" prompt with the exact words in quotes.
- Real product in graphics: use image-to-image with the real rug photo and the same lock line as `image-prompts` (keep pattern/colors unchanged).
- Brand look (default until the shop profile defines one): warm neutrals (ivory #F5F0E8, sand #D9C7A8, terracotta #B5654A, charcoal #2F2A26), serif headline (Playfair Display / Cormorant) + clean sans subline (Montserrat / Lato). Calm, artisan, uncluttered. When a shop is connected, follow its look and voice from the shop profile and `data/brand.md`.
- Text rules: English, ≤7 words headline, ≤10 words subline. Only true claims (free shipping, custom sizes — check profile). No fake urgency, no "#1", no competitor names.

## Output format (per asset)

```
ASSET: Etsy Big Banner — <Shop> — <Evergreen / Christmas / Spring…>
Size: 1200×300 (generate 21:9, crop to 4:1)

Background prompt:
<paste-ready prompt: scene, composition with empty centre/side for text, light, palette, style, negatives: no text, no logo, no watermark>

Text overlay (add in Canva):
Headline: "Handmade Wool Rugs"            — centre, Playfair Display, #2F2A26
Subline:  "Hand tufted by artisans · Custom sizes · Free shipping"
Small tag (optional): "Made to order"

Optional one-shot prompt (text baked in): <…>
```

Give **2 concept options** per asset (e.g. A: artisan hands at work close-up + text right; B: styled room with rug + text centre).

### Idea bank

- **Banner concepts:** artisan hands tufting/weaving (no faces) · stack of rolled rugs in warm light · wide living room with hero rug · flat-lay of yarn balls + tools + rug corner · row of 3 bestsellers (collage, real photos).
- **Seasonal headlines (Western):** "Cozy Up for the Holidays" · "Gifts for the Home" · "New Year, New Room" · "Spring Refresh" · "Wedding & Housewarming Gifts" · "Nursery Rugs, Made by Hand" · "Back to School, Dorm Ready" · "Fall Layers".
- **Sale graphics:** "Holiday Sale — 20% Off" + dates; "Cyber Week"; always add real dates and % from the pricing skill's safe range.
- **Pinterest pins (5 types):** styled room + keyword title ("Boho Living Room Rug Ideas") · before/after room · size guide infographic · close-up texture + "Hand Tufted Wool" · color palette pin (rug + 5 swatches). Give pin **title (≤100 chars)** + **description (≤500 chars, 3–5 keywords natural)** + board suggestion + link = listing URL via Etsy Share & Save.
- **Instagram:** caption (hook line, 2–3 lines story, CTA "Link in bio / DM for custom size") + 8–12 hashtags (mix: #handmaderug #woolrug #bohodecor #nurserydecor #etsyfinds …) + reel cover text.

End with **Next steps** (owner's language): generate → crop → add text in Canva → upload path in Etsy (Shop Manager → Sales Channels → edit shop → banner).
