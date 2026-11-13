# Shopify module — coming soon 🔜

This folder is a placeholder. Until the module exists, ShopPilot's platform-agnostic `core/` skills still work for Shopify stores if you give the agent your theme's field limits yourself — it will not invent them.

## Module contract

To be considered complete, this module must contain:

| File | Purpose |
|---|---|
| `PLATFORM.md` | Single source of truth: product fields (title, description, SEO title / meta description, handles, tags, variants, metafields), image specs, fees, Google / Shop search factors, benchmarks, export formats |
| `shopify-listing-seo/SKILL.md` | Full paste-ready product page package following `PLATFORM.md` |
| `shopify-shop-analysis/SKILL.md` | Sales analysis from Shopify order / product / analytics exports in `data/exports/<shop>/` |
| `shopify-ads-optimizer/SKILL.md` | Ad performance analysis (Shop Campaigns / Google / Meta exports) → pause / scale / fix list |
| `docs/shopify-csv-export-guide.md` | Exact steps to export each report |
| `scripts/shopify_analyze.py` | Export cruncher (aggregates only, no buyer PII) |

Plus routing rows in `CLAUDE.md` and a ✅ in the README platform table. Full guide: [docs/adding-a-platform.md](../../../docs/adding-a-platform.md).
