---
description: Analyze a connected shop from its exports — sales, listings, ads, or compare shops
---

Run a data analysis for a connected shop. Arguments (optional): `$ARGUMENTS` — e.g. `/analyze <shop>`, `/analyze <shop> ads`, `/analyze compare`.

1. **Mode check.** No profile in `data/shops/` → reply "No shop connected — run `/connect-shop` for analysis features." and stop.
2. **Pick the shop.** From the arguments; if missing and several shops are connected, ask once (platform → shop). Read its profile; `platform:` decides the module.
3. **Pick the analysis** from the arguments or ask:
   - sales / shop (default) → `.claude/skills/<platform>/<platform>-shop-analysis/SKILL.md`
   - ads / ROAS → `.claude/skills/<platform>/<platform>-ads-optimizer/SKILL.md`
   - compare (2+ shops) → `.claude/skills/core/multi-shop-compare/SKILL.md`
4. **Exports first.** Check `data/exports/<shop>/`. List which files are present. If a file the analysis needs is missing, show the exact export steps from `docs/<platform>-csv-export-guide.md` and wait.
5. Follow the skill. Save the report to `data/reports/` (private) and reply with the short summary + prioritized actions.
6. **v1.0 routing:** this command runs **analytics-agent** (sales/compare) or the ads flow (`/ads`). Kept for backwards compatibility.
