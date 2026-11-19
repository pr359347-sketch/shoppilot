---
description: Audit — a single listing you paste, or a full account audit (platform agent + analytics agent)
---

Audit a listing. Arguments (optional): `$ARGUMENTS` — the pasted listing, or a shop name.

1. Detect mode (`data/shops/`). Connected: read the shop profile, `data/settings.md`, `data/learnings.md`. Generic: ask which platform (default Etsy) and continue without a profile.
2. If no listing content was given, ask the owner to paste: title, tags, price(s) and variations, description, photo list or screenshots, and stats if available (impressions, visits, favorites, orders + date range).
3. Follow `.claude/skills/core/listing-audit-framework/SKILL.md` using the limits in `.claude/skills/<platform>/PLATFORM.md` and the matching domain file.
4. For a bulk health check of all listings (connected mode, Etsy): check `data/exports/<shop>/` for the listings export — if missing show the steps from `docs/etsy-csv-export-guide.md` — then run `python scripts/etsy_analyze.py --shop <shop> --listing-health`.
5. **Full account audit** (`/audit <shop>` or "poori shop"): connected only. Run **<platform>-agent** (account audit) and **analytics-agent** (exports → funnel, buckets, Top 5) in parallel, then combine into one report in `data/reports/YYYY-MM-DD_<shop>_account-audit.md` and present fixes as proposal cards (`core/approval-flow`). eBay/Amazon: advisor only — owner steps.
