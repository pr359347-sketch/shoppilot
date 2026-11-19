<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Creative QA — tool choice, lock-line, drift check, text check

## 1. Tool choice
| Need | Best tool | Fallback |
|---|---|---|
| Anything with text (banner, size chart, infographic, A+ module) | Canva connector (exact fonts, brand kit, spell-safe) | prompt pack + text spec for the owner |
| Room/lifestyle shot with the REAL product | Gemini / Nano Banana image edit (image-to-image) | prompt pack (`core/image-prompts`) |
| Video ad / reel | Google Flow / Veo (image-to-video from the real photo) | Canva video from stills; prompt pack |
| Preview of a NEW design (not made yet) | Gemini / Canva generate | prompt pack — always labelled "preview" |

Say which tools are available in one line before starting.

## 2. Lock-line (paste at the end of every image-to-image / image-to-video prompt)
```
LOCK: Keep the product in the reference image 100% identical — same design, motif placement, colours, border, fringe, texture, pile, shape and proportions. Do not redraw, recolour, simplify, mirror or crop the product. Change ONLY the room, lighting, camera angle and props around it.
```

## 3. Drift check (every output, before showing the owner)
Compare side by side with the original photo:
- [ ] Pattern/motif identical (count repeats, check corners)
- [ ] Colours match (no hue shift, no extra colour)
- [ ] Border / fringe / edges same
- [ ] Shape + proportions same (a 5x8 must look 5x8, not square)
- [ ] Texture/pile plausible for the construction
- [ ] Scale realistic vs furniture (sofa ~7 ft, bed width per size)
Any fail → reject, note what drifted, regenerate (max 3 tries, then tell the owner).

## 4. Text check
Every word in a graphic: spell-check, brand name exact, prices/dates correct, sizes `ft (cm)`. AI-rendered text is never trusted — put text in Canva.

## 5. Spec check
Pixel size, ratio and safe zones from the platform's `PLATFORM.md` (e.g. Etsy banner text in centre 60%).

## 6. Disclosure
Preview/AI images of made-to-order items → disclosure line in the listing description and, if the platform requires, on the image. Never as photo 1 if a real photo exists.

## 7. Options
2–3 options per asset, each passing QA, plus the recommended one with one line why.
