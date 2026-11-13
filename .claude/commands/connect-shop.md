---
description: Connect a shop — creates a private shop profile and exports folder in data/ from templates
---

Connect a shop to ShopPilot. Everything you create goes in the private, git-ignored `data/` folder — never in tracked files. Talk in the owner's language (`data/settings.md` if it exists; otherwise the language they write in).

If `$ARGUMENTS` is given, treat it as answers already provided (e.g. `/connect-shop etsy <shop-name> handmade rugs`) and only ask for what's still missing.

## Step 1 — First-time workspace setup (only if missing)

Create from templates, without overwriting anything that exists:
- `data/settings.md` ← `templates/settings.md`
- `data/brand.md` ← `templates/brand.md`
- `data/learnings.md` ← `templates/learnings.md`
- `data/shops/`, `data/exports/`, `data/reports/`, `data/keyword-pools/`
- `data/.private-keywords` (empty list with a `#` comment line) — used by the pre-commit hook

## Step 2 — Ask (two short rounds, not one long form)

**Round 1 — must-haves** (one message):
1. Platform: Etsy ✅ (eBay / Shopify / Amazon 🔜 — a profile can be created now, platform skills arrive later)
2. Shop name
3. Shop URL
4. Category (rugs / home textiles / home decor / other) and main products — techniques, materials, sizes
5. Target market (default: US + Europe)
6. Primary or secondary shop? (only ask if another shop is already connected)

**Round 2 — helpful, all skippable** (one message; say "skip" is fine):
7. Goals for the next 90 days
8. Brand voice (3 words) + one-line story + where it's made / shipped from
9. Costs: making cost (per sq ft or per piece), packing, shipping cost to the main market
10. Processing time, delivery time, free shipping (where), return policy
11. Custom orders — what can be customized
12. (first shop only) Preferred chat language, and any occasions to avoid

Never invent answers. Skipped fields stay `[TODO]`.

## Step 3 — Create

1. `name` = shop name lowercased, letters/digits/hyphens only.
2. If `data/shops/<name>.md` already exists → don't overwrite; offer to update fields instead.
3. Copy `templates/shop.md` → `data/shops/<name>.md`, fill it with the answers. The `platform:` field is mandatory (`etsy` / `ebay` / `shopify` / `amazon`).
4. Create `data/exports/<name>/`.
5. Keyword pools: for each product type, if no matching pool exists in `data/keyword-pools/`, copy the matching starter from `templates/keyword-pools/` or create one from `templates/keyword-pool.md`. List the pool files in the profile.
6. Update `data/settings.md` / `data/brand.md` with new answers (first shop: fill them; later shops: put differences in the shop profile's brand-voice section).
7. If other shops are connected, fill "Positioning vs the owner's other shops" — ask one question if unclear.
8. **Privacy list:** append the shop name, the owner's name / business name and any other private identifiers the owner gave to `data/.private-keywords` (one per line) so the pre-commit hook blocks them from ever being committed.

## Step 4 — Confirm + next step

Show:
- What was created (file paths) and which fields are still `[TODO]`.
- The exact export steps for the two most useful files — **Order Items** and **Listings** — copied from `docs/<platform>-csv-export-guide.md`, with the destination folder `data/exports/<name>/`.
- "Connect another shop? Run `/connect-shop` again." and "Run `/start` for the menu."

## Rules

- Do not git-commit anything from this command — `data/` is private.
- Do not write the shop's name or details into any tracked file.
