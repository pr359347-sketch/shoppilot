---
description: Audit a live listing you paste — CTR and conversion problems with exact fixes
---

Audit a listing. Arguments (optional): `$ARGUMENTS` — the pasted listing, or a shop name.

1. Detect mode (`data/shops/`). Connected: read the shop profile, `data/settings.md`, `data/learnings.md`. Generic: ask which platform (default Etsy) and continue without a profile.
2. If no listing content was given, ask the owner to paste: title, tags, price(s) and variations, description, photo list or screenshots, and stats if available (impressions, visits, favorites, orders + date range).
3. Follow `.claude/skills/core/listing-audit-framework/SKILL.md` using the limits in `.claude/skills/<platform>/PLATFORM.md` and the matching domain file.
4. For a bulk health check of all listings (connected mode, Etsy): check `data/exports/<shop>/` for the listings export — if missing show the steps from `docs/etsy-csv-export-guide.md` — then run `python scripts/etsy_analyze.py --shop <shop> --listing-health`.
