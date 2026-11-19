---
name: seasonal-planner
description: Build a 90-day calendar per shop of what to list, optimize and promote for upcoming US/EU occasions and seasons (Christmas, holiday gifting, New Year home refresh, spring, wedding, housewarming, nursery, back-to-school) — with made-to-order / international shipping cutoffs. Use when the owner asks for a plan for the next months or an upcoming occasion.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Seasonal Planner (90 days)

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Step 1 — Anchor

- Start = today's date (from the environment). Window = next 90 days, plus "prep now" items for occasions up to 120 days out.
- Shops = named shop(s), default all shops marked primary in `data/shops/` (generic mode: ask for product type, processing days and transit days). Read each shop profile (niche, processing + delivery time), latest report in `data/reports/` (seasonality, bestsellers), `data/learnings.md`.
- Use only occasions the **target market** celebrates (`data/settings.md`; default = the US/EU Western calendar below). Never the seller's own local festivals unless the buyers' market celebrates them.

## Western occasion calendar (compute exact dates for the current year)

| Occasion | When | Rug angle | Best fits |
|---|---|---|---|
| New Year home refresh | Jan 1 – mid Feb | "new year, new room", neutral/modern, bedroom + office rugs | tufted modern, moroccan style |
| Valentine's | Feb 14 | blush/pink/red accents, gift for her, small rugs | tufted small, kids |
| Spring refresh / spring cleaning | Mar – Apr | light colors, florals, cotton/flatweave, entryway + kitchen | dhurrie, kilim, pastel tufted |
| Easter | Mar/Apr (movable) | pastel, bunny/nursery, hosting | kids, cotton |
| Mother's Day | US: 2nd Sun May · UK: 4th Sun of Lent (Mar) | gift for mom, bedside/kitchen runners | runners, small rugs |
| Wedding season | Apr – Oct (peak May–Jun, Sep–Oct) | wedding gift, registry, first home | 5x8+, neutral classics |
| Graduation / moving season | May – Aug | first apartment, housewarming | 4x6, 5x8 budget |
| Nursery / baby shower | all year (peaks spring + late summer) | nursery rug, baby shower gift | kids, round |
| Summer | Jun – Aug | lightweight, cotton, jute, porch | dhurrie, jute, kilim |
| Back-to-school / dorm | Jul – early Sep | dorm rug, kids room refresh, playroom | 3x5, 4x6, kids, cotton |
| Fall decor | Sep – Nov | rust, terracotta, mustard, cozy wool | boho, kilim, tufted |
| Halloween | Oct 31 | skip unless a design truly fits | — |
| Thanksgiving hosting | 4th Thu Nov (US) | dining room rug, hosting refresh, runner | 8x10, runners |
| Black Friday → Cyber Monday | Fri after Thanksgiving → Mon | biggest sale window | all bestsellers |
| Christmas / holiday gifting | Dec 25 (shopping from early Nov) | gift for home, cozy, new home gift | small rugs, runners, kids |
| Winter cozy | Dec – Feb | thick wool, high pile, hygge | tufted, moroccan style |
| Housewarming / new home | all year | evergreen gift angle | all |

## Lead-time rules (made to order / international shipping)

For each occasion date **D**, using the shop's processing days **P** and transit days **T** (from the profile; if unknown assume P=14, T=7 and flag it):

- **Last order date** = D − (P + T + 4 buffer days). After this, stop "arrives by" messaging; switch to ready-to-ship items (if any) or the next occasion.
- **List new seasonal products** by D − 10 weeks (Etsy needs time to index and rank; buyers browse 4–8 weeks ahead).
- **Optimize existing listings** (tags/title/photos for the occasion) by D − 8 weeks.
- **Promote** (sale, Etsy Ads budget up, Pinterest/Instagram) D − 6 weeks → last order date.
- **Clean up** seasonal tags/photos within 1 week after D; swap to the next occasion.

If today is already past an ideal date, say so plainly and give the "what can still be done" version (e.g. ready-stock items, gift-card-style "made for your new home" angle, pivot to New Year refresh).

## Output

Intro in the owner's language (2–3 lines: what's coming, what's already late). Then per shop:

**A. Key dates table** — `Occasion | Date | Last order date | Status (on time / late / prep now)`.

**B. Week-by-week calendar (13 weeks)**

| Week (dates) | LIST (new) | OPTIMIZE (existing) | PROMOTE (sale / ads / social) | Occasion focus |
|---|---|---|---|---|

Each cell = specific and small (1–3 tasks): which rug type/size/color, which listings (use bestsellers from the profile/report), which keywords to add (from pools' Occasion sections — tag-ready), sale % (within pricing floor), ads budget direction, 1 social idea.

**C. Paste-ready seasonal kit** for the nearest 1–2 occasions:
- 6–8 seasonal tags (≤20 chars, with counts)
- 2 title add-on phrases
- 1 description line + 1 shop announcement (English)
- Sale name + dates + % suggestion
- 1 hero photo idea (→ `image-prompts`) and 1 banner idea (→ `banner-prompts`)

**D. Next steps — this week** (top 5).

## Save

Save to `data/reports/YYYY-MM-DD_<shop>_seasonal-plan.md`. One file per shop, or one combined file if the owner asked for both together.
