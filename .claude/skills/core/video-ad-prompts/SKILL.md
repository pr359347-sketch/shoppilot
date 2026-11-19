---
name: video-ad-prompts
description: Write Veo (Google Flow) prompts for 8–15 second listing videos and Instagram/Pinterest reels for rugs — unroll, texture, pile, room reveal — with shot lists and on-screen text. Use when the owner asks for a listing video, reel or video ad prompt.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Video Prompts — Etsy listing videos & reels (Veo / Flow)

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs

Rug (real photo strongly preferred) · construction/material/pile · size · shop · purpose: **Etsy listing video** or **reel/ad** (Instagram, Pinterest, Etsy social). Read the shop profile + `.claude/skills/domain/rugs.md`.

## Specs

| Use | Length | Ratio | Audio | Text |
|---|---|---|---|---|
| Etsy listing video | 5–15 sec | 16:9 or 4:3 landscape (1:1 OK), ≥1080p | Etsy plays it **muted** — don't rely on sound | No text needed; never essential info in text |
| Instagram Reel / Pinterest Idea / Shorts | 8–15 sec | 9:16 vertical | Add trending/soft music in-app | 2–4 short captions |

Veo makes ~8-second clips. For 12–15 sec: generate **2 clips** (Shot A + Shot B) and join in Flow / CapCut. Always give prompts per clip.

## Product-truth rule (same as images)

- Use **image-to-video**: upload the real rug photo as the first frame / ingredient. Lock line in every prompt:
  `The rug must stay exactly as in the reference image — same pattern, colors, proportions and texture throughout the whole clip. No morphing, no pattern changes.`
- Best listing video is often a **real phone clip** (hand brushing pile, unrolling). Always include a "Shoot it on your phone" 3-step option next to the AI prompt.
- Text-to-video without a reference = `MOCKUP / social teaser only`. Reject clips where the pattern warps.

## Prompt formula

`[lock line] + [shot type + camera move] + [subject action] + [setting + style] + [light] + [pace] + [duration, aspect] + [negatives]`

Camera moves that work for rugs: slow push-in · slow top-down descend · low-angle slide along the pile · orbit 30° · static with action (unroll). One move per clip — keep it slow and smooth.
Negatives: `no text, no logos, no watermark, no people's faces, no warping, no flicker, no fast cuts, no color shift`.

## Shot library (pick by purpose; output paste-ready prompts)

1. **Unroll** — hands (no face) unroll the rug across a light wood floor, camera low at the far end, rug rolls toward camera and settles flat. *(Hook for reels; shows size.)*
2. **Texture glide** — macro, camera slides slowly 2 inches above the pile in raking window light; fibres catch the light. *(Tufted/knotted: plush depth; flatweave: weave detail.)*
3. **Hand touch** — a hand presses into and brushes across the pile, pile springs back; shallow depth of field. *(Softness + pile height.)*
4. **Room reveal** — slow push-in or pan from a doorway revealing the rug in a styled living room/bedroom/nursery, morning light, curtains moving slightly. *(Scale must be true to size.)*
5. **Edge & backing** — corner is lifted and folded over to show backing/finish, then laid back. *(Trust.)*
6. **Top-down settle** — overhead shot, rug laid flat, coffee table / bare feet / pet walks in. *(Lifestyle.)*
7. **Artisan craft** — close-up of hands tufting/weaving on a frame/loom, warm light, yarn in focus (no faces). *(Brand story; mockup unless real footage — prefer real workshop clips.)*
8. **Seasonal** — same room dressed for the upcoming Western occasion (holiday greenery and warm lights; spring flowers; nursery prep).

## Ready-made sequences

- **Etsy listing video (10–15s, muted, landscape):** Clip A = #2 Texture glide or #3 Hand touch (5–7s) → Clip B = #4 Room reveal (6–8s). First 2 seconds must show the rug clearly.
- **Reel (12–15s, 9:16):** #1 Unroll (hook, 0–4s) → #3 Hand touch (4–8s) → #4 Room reveal (8–14s) + captions.
- **Kids/nursery:** #6 with toy blocks/baby feet → #4 nursery reveal.
- **Runner:** unroll down a hallway (camera at the end, low) → walk-through feet shot.

## Output format

```
VIDEO: Etsy listing video — <rug> — 12 sec (2 clips)

CLIP A (6s) — TEXTURE GLIDE — image-to-video, 16:9
Prompt:
<paste-ready>

CLIP B (7s) — ROOM REVEAL — image-to-video, 16:9
Prompt:
<paste-ready>

Edit: join A→B, 0.3s cross-fade, export 1080p MP4, no audio needed.
Phone shoot (alternative): 1) … 2) … 3) …
```
For reels add: **On-screen captions** (English, ≤5 words each, with timing — e.g. 0–3s "Hand tufted, one loop at a time"), **caption + hashtags**, **music mood**.

End with **Next steps** (owner's language): upload real photo → generate each clip → check pattern didn't change → join → upload (Etsy: listing → Video; keep under 15s / 100MB).

## Rules

- Never show a size, thickness or color the real rug doesn't have. No fake "customer" faces/testimonials.
- Seasonal dressing must match the target market (default Western).
