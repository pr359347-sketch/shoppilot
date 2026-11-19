---
description: Creative — product images, room shots, size charts, banners, icons, video ads (2–3 options, upload only after ok)
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

Arguments (optional): `$ARGUMENTS` — e.g. `/creative banner christmas`, `/creative room shots <listing>`, `/creative video`.

1. Detect mode; connected → pick shop, read `data/brand.md`.
2. Ask (once) for missing must-haves: asset type, the real product photo path (if exists), occasion/text for banners.
3. Delegate to **creative-agent**. It checks tools first (Canva / Gemini-Nano Banana / Flow-Veo), makes 2–3 options, runs creative QA (lock-line + drift + spelling).
4. Show options with QA results + recommended one. Uploading = proposal card (`core/approval-flow`) — Etsy/Shopify ShopPilot uploads after "ok"; eBay/Amazon owner uploads.
5. Old prompt-only mode still works: `/prompts`.
