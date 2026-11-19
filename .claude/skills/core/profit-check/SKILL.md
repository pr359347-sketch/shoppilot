<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Profit Check — real profit per product, size and platform

## Inputs
- Costs (owner's, from `data/shops/<shop>.md` → Pricing inputs): making cost (per sq ft / piece), packing, shipping per size/market, payment fee %, ads reserve %, exchange rate.
- Fees: platform `PLATFORM.md`; **real fees from statements in `data/exports/<shop>/` override defaults**.
- Prices: listings export or pasted.

Missing input → placeholder and skip that row. Never guess costs.

Notes:
- "Best-selling" = by units, ties broken by revenue (say which).
- Etsy orders CSV "Card Processing Fees" = payment processing only (often in payout currency and on a total incl. sales tax); transaction, listing, ads fees come only from the monthly statement — use PLATFORM.md defaults until it exists and say so.
- Standing coupons/sales: price floor is computed on the **net price after the usual discount**; list price floor = floor ÷ (1 − standing discount %).

## Formulas (per unit, in listing currency)
```
revenue        = item price + shipping charged
platform_fees  = listing fee + transaction/referral/final-value % × (revenue) + per-order fixed + payment % × revenue + payment fixed
ads_reserve    = blended ads % × revenue          (Etsy offsite ads, Promoted Listings rate, PPC ACoS share)
cost           = making + packing + shipping actual + (currency conversion % if applicable)
net_profit     = revenue − platform_fees − ads_reserve − cost
margin %       = net_profit ÷ revenue
price_floor    = price where net_profit = target margin
break-even ROAS = 1 ÷ (margin before ads)       ·   break-even ACoS = margin before ads %
```

## Output table
| Product | Size | Platform | Price | Fees | Shipping | Cost | Ads | Net | Margin | Floor | BE ROAS |
Flags: 🔴 net < 0 · ⚠️ margin < target · ✅ ok.

Then: best platform per product, loss-makers, price/shipping/ads actions (TOP 5). Save to `data/reports/YYYY-MM-DD_<shop>_profit.md` (private — contains costs).
