---
name: pricing-advisor
description: Build a size-wise pricing matrix per rug type from the owner's costs, competitor prices, fees and free-shipping absorption — with margin per size and sale headroom. Use when the owner asks what price to set, wants size-wise pricing, or pricing looks wrong in an audit/analysis.
---
<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->

# Pricing Advisor

> **Platform:** this is a platform-agnostic core skill. The active platform comes from the shop profile's `platform:` field (generic mode: ask; default `etsy`). Field limits, fees, image specs, ranking factors and export formats come from that module's `.claude/skills/<platform>/PLATFORM.md`. Etsy numbers used below (140-char title, 13 tags × 20 chars, Etsy Ads, Shop Manager paths) are the worked example — substitute the active platform's values.
>
> **Mode & category (see CLAUDE.md):** in GENERIC mode (no shop connected) skip the shop-profile / learnings / private keyword-pool reads and ask the owner for the product details instead (starter pools live in `templates/keyword-pools/`). For non-rug products use `.claude/skills/domain/home-textiles.md` in place of `.claude/skills/domain/rugs.md`.

## Inputs (from shop profile → "Pricing inputs"; ask once for what's missing)

Must-have: making cost per sq ft for this construction — or per piece for non-rug items (any currency) · shipping cost by size or per kg to US (and EU) · target net margin % · free shipping yes/no.
Nice: packing cost, competitor prices per size, always-on sale %, real payment fee from statement, Offsite Ads rate, exchange rate (if costs aren't in the listing currency).
If the owner gives only 2–3 size costs, derive per-sq-ft cost and interpolate; mark estimated cells with `~`.
Save any new cost facts to the shop profile.

## Formula (show it once, briefly)

Fee rates from `.claude/skills/etsy/PLATFORM.md` (use shop profile values when verified):

```
t  = transaction fee              6.5%
p  = payment processing %         shop profile (default 4%)
c  = currency conversion          2.5% (if payout ≠ listing currency)
o  = Offsite Ads reserve          3–5% blended (or 12/15% × share of offsite orders)
a  = Etsy Ads reserve             0–8% (from ads data: spend ÷ revenue)
m  = target net margin
F  = fixed per order              $0.20 listing + payment fixed fee

Landed cost  L = making + packing + shipping (if free shipping) 
Sell price   S = (L + F) ÷ (1 − t − p − c − o − a − m)
List price     = S ÷ (1 − sale%)      ← if the shop runs an always-on sale
Floor price    = (L + F) ÷ (1 − t − p − c − o − a)     ← zero profit; never discount below this
```
Shipping: use volumetric weight (L×W×H cm ÷ 5000) vs actual — whichever is higher (see `.claude/skills/domain/rugs.md` for weight per sq ft).

## Shaping the ladder (after the math)

1. **Per-sq-ft price should fall as size rises** (small rugs carry fixed costs; large rugs need a per-sq-ft discount to feel fair). Check the ladder has no size where the next size up is <15% more expensive (nobody buys the smaller one) or jumps >2× per step.
2. **Entry size = the price shown in search grid** ("$X+"). Keep the smallest size as low as margin allows — it drives CTR. If 2x3 margin is thin, that's acceptable as a traffic size (say so), never below floor.
3. **Anchor to competitors:** place each size at competitor median ±10% unless we have a clear reason (wool quality, custom, reviews). If cost-based price is >25% above competitor median → flag "cost problem or positioning problem" and give options (cheaper shipping method, thinner pile, different size focus, premium positioning with better photos).
4. **Charm rounding:** <$100 → end in 9 (e.g. $79); $100–$500 → end in 9 or 5 ($249, $395); >$500 → round to $10/$25 less 1 ($849, $1,199).
5. **Runners & rounds:** price by sq ft using the nearest rectangle's per-sq-ft rate + 10–15% (more wastage/finishing) for rounds and irregular shapes.
6. **Custom size rule** for the description/messages: `$[rate] per sq ft` (L ft × W ft), minimum charge = 2x3 price.
7. **EU:** Etsy shows VAT-inclusive prices to EU/UK buyers; don't add VAT yourself. If EU shipping costs more and shipping isn't free there, give the EU flat shipping rate per size band.

## Output

2-line summary in the owner's language, then the matrix (English):

| Size | Sq ft | Making | Shipping | Landed cost | Floor price | **Suggested price** | **List price (if X% sale)** | Net profit $ | Net margin % | $/sq ft | Competitor median | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Rows: 2x3, 3x5, 4x6, 5x8, 6x9, 8x10, 9x12, runners 2x6 / 2x8 / 2x10, round 4 / 5 / 6 / 8 ft (only sizes the shop offers + suggest missing ones).

Then:
- **Paste-ready variation prices** — a clean `Size label — $price` list in Etsy variation order.
- **Custom quote rate** — $/sq ft.
- **Sale plan** — max safe discount % (stays above floor + min margin), suggested always-on sale %, and holiday sale % (Black Friday/Cyber Week, Christmas, New Year).
- **Warnings** — sizes below target margin, assumptions used (`~`), fees needing verification.
- **Next steps.**

## Rules

- Show both currencies when the owner gave costs in a currency other than the listing currency (state the rate used).
- Never present assumed fees as verified; mark `[VERIFY]`.
- Verify arithmetic (compute with a quick Python one-off if more than a few rows).
- Don't recommend raising prices on a bestseller by >10% in one step — stage it and watch conversion.
