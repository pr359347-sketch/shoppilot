# eBay module — coming soon 🔜

This folder is a placeholder. Until the module exists, ShopPilot's platform-agnostic `core/` skills still work for eBay sellers if you give the agent eBay's field limits yourself — it will not invent them.

## Module contract

To be considered complete, this module must contain:

| File | Purpose |
|---|---|
| `PLATFORM.md` | Single source of truth: listing field limits (title, item specifics, description, photos, video), fees, image specs, search-ranking factors (Cassini), benchmarks, export / report formats |
| `ebay-listing-seo/SKILL.md` | Full paste-ready listing package following `PLATFORM.md` |
| `ebay-shop-analysis/SKILL.md` | Sales analysis from Seller Hub reports in `data/exports/<shop>/` |
| `ebay-ads-optimizer/SKILL.md` | Promoted Listings analysis → pause / scale / fix list |
| `docs/ebay-csv-export-guide.md` | Exact steps to export each report |
| `scripts/ebay_analyze.py` | Report cruncher (aggregates only, no buyer PII) |

Plus routing rows in `CLAUDE.md` and a ✅ in the README platform table. Full guide: [docs/adding-a-platform.md](../../../docs/adding-a-platform.md).
