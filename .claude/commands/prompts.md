---
description: Creative prompts — listing photos, banners / social graphics, and listing videos / reels
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

Generate creative prompts. Arguments (optional): `$ARGUMENTS` — e.g. `/prompts photos beige abstract tufted rug 5x8`, `/prompts banner holiday`, `/prompts video`.

1. Detect mode (`data/shops/`). Connected: pick the shop, read its profile and `data/brand.md` for the look and voice. Generic: ask for the product details.
2. Pick the type from the arguments or ask:
   - **photos** — 10-photo listing set → `.claude/skills/core/image-prompts/SKILL.md`
   - **banner / social** — shop banner, featured graphics, Pinterest pins, Instagram posts → `.claude/skills/core/banner-prompts/SKILL.md`
   - **video** — 8–15 s listing videos and reels → `.claude/skills/core/video-ad-prompts/SKILL.md`
3. Image sizes and video specs come from `.claude/skills/<platform>/PLATFORM.md`; product details from the matching domain file.
4. Remind the owner: prompts are written to place their **real product photo** into scenes — the product itself must stay unchanged.
5. Prompt-only mode. To have ShopPilot generate and QA the images/videos itself, use `/creative` (creative-agent).
