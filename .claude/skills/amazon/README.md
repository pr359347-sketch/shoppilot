# Amazon module — coming soon 🔜

This folder is a placeholder. Until the module exists, ShopPilot's platform-agnostic `core/` skills still work for Amazon sellers if you give the agent your category's field limits yourself — it will not invent them.

## Module contract

To be considered complete, this module must contain:

| File | Purpose |
|---|---|
| `PLATFORM.md` | Single source of truth: listing field limits (title, bullets, description / A+ content, backend search terms, images, video), fees (referral, FBA / FBM), image specs, ranking factors, benchmarks, report formats |
| `amazon-listing-seo/SKILL.md` | Full paste-ready listing package following `PLATFORM.md` |
| `amazon-shop-analysis/SKILL.md` | Sales analysis from Seller Central business reports in `data/exports/<shop>/` |
| `amazon-ads-optimizer/SKILL.md` | Sponsored Products / Brands analysis (ACoS, ROAS) → pause / scale / bid list |
| `docs/amazon-csv-export-guide.md` | Exact steps to export each report |
| `scripts/amazon_analyze.py` | Report cruncher (aggregates only, no buyer PII) |

Plus routing rows in `CLAUDE.md` and a ✅ in the README platform table. Full guide: [docs/adding-a-platform.md](../../../docs/adding-a-platform.md).
