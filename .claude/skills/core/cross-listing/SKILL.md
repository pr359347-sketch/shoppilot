<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Cross-Listing — one listing → every other platform's format

Input: one source listing (pasted, or from an export in `data/exports/<shop>/`). Output: a paste-ready version per target platform, respecting each `PLATFORM.md`.

## Step 1 — Extract the product facts (platform-neutral)
Product type · construction · material (+%) · pile/thickness · sizes `ft (cm)` · colours · pattern/motif · style · room · care · made in · processing time · price per size · photos available · personalization.
Anything missing → `[PLACEHOLDER]`. Never carry over a claim the source can't support.

## Step 2 — Map per platform

| Field | Etsy | eBay | Shopify | Amazon |
|---|---|---|---|---|
| Title | ≤140, phrases | **≤80**, keyword-dense, no filler | ≤255 (keep ~70 for SEO title) | category limit (see PLATFORM.md), Brand + type + key attributes |
| Keywords | 13 tags ≤20 | item specifics (fill all) | tags + SEO title/meta | 5 bullets + backend terms <250 bytes |
| Variations | Size + Color | variation listing (Size/Color), each with own specifics | options/variants | parent-child (size_name / color_name) |
| Description | story + size table | mobile HTML, no active content | benefit-first + JSON-LD via theme | description + A+ (Brand Registry) |
| Photos | 10 + video | up to 24 | as many as useful | main = pure white bg + up to 8 more |
| Category | Etsy taxonomy | eBay category ID `[VERIFY in Seller Hub]` | product type + collection | browse node / product type from template |

## Step 3 — Price per platform
Subagents leave prices as `[PRICE — floor from profit-agent]`; the **master** runs `profit-agent` in parallel and fills them when combining. Fees differ — never just copy the Etsy price. Sample/swatch prices (e.g. a 1x1 sample) are not product prices: flag them and suggest a separate sample product.

## Step 4 — Policy check per platform
Amazon Handmade needs an approved artisan account; eBay requires accurate condition + item specifics; Etsy creativity standards; Shopify = own store (consumer law, clear returns).

## Output
For each target: a code block per field with character counts, plus the bulk file option:
- eBay → Seller Hub Reports listing template row (CSV)
- Shopify → product CSV rows (Handle, Title, Body (HTML), Vendor, Type, Tags, Option1 Name/Value, Variant Price, Image Src…)
- Amazon → flat-file row for the category template (owner downloads the template first)

Files go to `data/reports/` only. Creating the listing = live change → proposal (Etsy/Shopify) or owner steps (eBay/Amazon).
