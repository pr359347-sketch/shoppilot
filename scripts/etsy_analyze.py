#!/usr/bin/env python3
"""Etsy CSV cruncher for the growth-advisor skills (stdlib only).

Reads every CSV in data/exports/<shop>/, detects the file type from its header,
and prints an aggregated markdown summary. Buyer names/addresses are never printed.

Usage:
  python scripts/etsy_analyze.py --shop myshop
  python scripts/etsy_analyze.py --shop shop-a --shop shop-b        (side-by-side)
  python scripts/etsy_analyze.py --shop myshop --from 2026-01-01 --to 2026-06-30
  python scripts/etsy_analyze.py --shop myshop --listing-health           (per-listing issues)
  python scripts/etsy_analyze.py --shop myshop --out data/reports/raw.md
"""
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATE_FORMATS = ("%m/%d/%y", "%m/%d/%Y", "%Y-%m-%d", "%B %d, %Y", "%b %d, %Y", "%d %B, %Y", "%d %b, %Y")
PRICE_BANDS = [(0, 50), (50, 100), (100, 200), (200, 400), (400, 800), (800, 10**9)]
CONSTRUCTION = [  # first match wins
    ("hand knotted", r"knott"),
    ("hand tufted", r"tuft"),
    ("kilim / flatweave", r"kilim|flat\s?weave|flat woven|handwoven|hand woven"),
    ("dhurrie / cotton", r"dhurrie|durrie|dhurry|cotton rug|cotton area"),
    ("jute", r"jute|hemp|sisal|braided"),
    ("block print", r"block\s?print"),
]
TAGS_MULTI = [  # a listing can hit several
    ("kids / nursery", r"kid|nursery|child|baby|playroom|toddler"),
    ("runner", r"runner"),
    ("round", r"\bround\b|circle|circular"),
    ("moroccan style", r"morocc|beni|berber"),
    ("boho", r"boho|bohemian"),
    ("modern / abstract", r"modern|abstract|contemporary|minimal"),
    ("vintage / oriental", r"vintage|persian|oriental|oushak|antique"),
    ("scandinavian", r"scandi|nordic"),
    ("geometric / tribal", r"geometric|tribal|aztec|southwest"),
    ("wool", r"\bwool"),
    ("cotton", r"cotton"),
]


def read_csv(path):
    for enc in ("utf-8-sig", "cp1252"):
        try:
            with open(path, newline="", encoding=enc) as f:
                rows = list(csv.DictReader(f))
            header = list(rows[0].keys()) if rows else next(csv.reader(open(path, encoding=enc)), [])
            return header, rows
        except UnicodeDecodeError:
            continue
    return [], []


def classify(header):
    h = {(c or "").strip().lower() for c in header}
    if "item name" in h and "transaction id" in h:
        return "items"
    if "order id" in h and ("order value" in h or "order total" in h):
        return "orders"
    if "title" in h and "tags" in h:
        return "listings"
    if "fees & taxes" in h:
        return "statement"
    return "other"


def col(row, *names):
    """Case-insensitive column lookup; returns '' if missing."""
    low = {(k or "").strip().lower(): v for k, v in row.items()}
    for n in names:
        if n.lower() in low and low[n.lower()] is not None:
            return str(low[n.lower()]).strip()
    return ""


def money(s):
    s = re.sub(r"[^0-9.\-]", "", (s or "").replace(",", ""))
    try:
        return float(s) if s not in ("", "-", ".", "--") else 0.0
    except ValueError:
        return 0.0


def parse_date(s):
    s = (s or "").strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    return None


def size_from(text):
    """Normalize a size out of a variation/title string -> '5x8', 'runner 2x8', 'round 6', or ''."""
    t = (text or "").lower().replace("×", "x").replace("&quot;", '"')
    is_round = bool(re.search(r"round|diameter|circle", t))
    m = re.search(r"(\d+(?:\.\d+)?)\s*(?:'|ft\.?|feet|foot)?\s*x\s*(\d+(?:\.\d+)?)\s*(cm|ft|feet|'|in|inch|\")?", t)
    if m:
        a, b = float(m.group(1)), float(m.group(2))
        unit = m.group(3) or ""
        if unit == "cm" or (a >= 30 and b >= 30):
            a, b = round(a / 30), round(b / 30)
        elif unit in ("in", "inch", '"'):
            a, b = round(a / 12), round(b / 12)
        a, b = sorted((a, b))
        if a <= 0:
            return ""
        if "sample" in t or "swatch" in t:
            return f"sample {a:g}x{b:g}"
        if is_round:
            return f"round {a:g}"
        label = f"{a:g}x{b:g}"
        return f"runner {label}" if a <= 3 and b / a >= 2.5 else label
    if is_round:
        m = re.search(r"(\d+(?:\.\d+)?)\s*(cm|ft|feet|')", t)
        if m:
            v = float(m.group(1))
            return f"round {round(v / 30) if m.group(2) == 'cm' else v:g}"
        return "round ?"
    return ""


def construction_of(title):
    t = title.lower()
    for name, pat in CONSTRUCTION:
        if re.search(pat, t):
            return name
    return "other / unclear"


def band_of(price):
    for lo, hi in PRICE_BANDS:
        if lo <= price < hi:
            return f"${lo}-{hi}" if hi < 10**9 else f"${lo}+"
    return "?"


def norm_title(t):
    return re.sub(r"\s+", " ", (t or "").strip().lower())


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "-"


def analyze(shop, folder, dfrom, dto, listing_health):
    out, summary = [], {"shop": shop}
    files = sorted(folder.glob("*.csv")) if folder.exists() else []
    out.append(f"# {shop} — raw summary\n")
    if not files:
        out.append(f"No CSV files in `{folder}`.\n")
        out.append("Export them from Etsy and drop them in that folder:")
        out.append("1. Shop Manager → Settings → Options → Download Data")
        out.append("2. Orders → CSV Type 'Order Items' → pick the year (leave month empty) → Download CSV")
        out.append("3. 'Currently for Sale Listings' → Download CSV")
        out.append("Full guide: docs/etsy-csv-export-guide.md\n")
        return "\n".join(out), summary

    items, orders, listings, statements, others = [], [], [], [], []
    out.append("## Files found")
    frows = []
    for p in files:
        header, rows = read_csv(p)
        kind = classify(header)
        frows.append((p.name, kind, len(rows)))
        {"items": items, "orders": orders, "listings": listings, "statement": statements}.get(kind, []).extend(rows)
        if kind == "other":
            others.append((p.name, header, len(rows)))
    out.append(table(["File", "Detected as", "Rows"], frows) + "\n")

    # ---------- order items ----------
    seen, clean = set(), []
    for r in items:
        tid = col(r, "Transaction ID")
        if tid and tid in seen:
            continue
        seen.add(tid)
        d = parse_date(col(r, "Sale Date"))
        if d and ((dfrom and d < dfrom) or (dto and d > dto)):
            continue
        qty = int(money(col(r, "Quantity")) or 1)
        price = money(col(r, "Price"))
        # Etsy's "Item Total" / "Price" are BEFORE the coupon, so real revenue = price*qty - discount.
        gross = price * qty
        net = gross - money(col(r, "Discount Amount"))
        title = col(r, "Item Name")
        clean.append({
            "date": d, "qty": qty, "price": price, "gross": gross, "rev": net, "title": title,
            "lid": col(r, "Listing ID") or norm_title(title)[:40], "oid": col(r, "Order ID"),
            "buyer": col(r, "Buyer"), "country": col(r, "Ship Country") or "?",
            "size": size_from(col(r, "Variations")) or size_from(title) or "no size",
            "coupon": col(r, "Coupon Code"), "disc": money(col(r, "Discount Amount")),
            "cur": col(r, "Currency"), "sku": col(r, "SKU"),
        })

    if clean:
        rev = sum(x["rev"] for x in clean)
        units = sum(x["qty"] for x in clean)
        n_orders = len({x["oid"] for x in clean if x["oid"]}) or len(clean)
        dates = [x["date"] for x in clean if x["date"]]
        curs = Counter(x["cur"] for x in clean if x["cur"])
        summary.update(revenue=rev, units=units, orders=n_orders, aov=rev / n_orders if n_orders else 0)
        out.append("## Topline (order items)")
        out.append(f"- Date range: {min(dates) if dates else '?'} → {max(dates) if dates else '?'}")
        gross_total = sum(x["gross"] for x in clean)
        out.append(f"- Orders: {n_orders} · Units: {units} · Net revenue (after coupons): {rev:,.0f} · AOV (net): {rev / n_orders:,.0f}")
        out.append(f"- List value before coupons: {gross_total:,.0f} · Discounts: {gross_total - rev:,.0f} ({pct(gross_total - rev, gross_total)})")
        out.append(f"- Currency: {', '.join(f'{c} ({n})' for c, n in curs.most_common()) or '?'}"
                   + ("  ⚠ mixed currencies — totals are not comparable" if len(curs) > 1 else ""))
        cp = sum(1 for x in clean if x["coupon"])
        out.append(f"- Rows with coupon: {cp} ({pct(cp, len(clean))}) · Total discounts: {sum(x['disc'] for x in clean):,.0f}\n")

        def group(keyfn, multi=False):
            g = defaultdict(lambda: [0, 0.0, set()])
            for x in clean:
                keys = keyfn(x)
                for k in (keys if multi else [keys]):
                    g[k][0] += x["qty"]; g[k][1] += x["rev"]; g[k][2].add(x["oid"])
            return g

        def section(title, g, first, sort_key=None, limit=None):
            rows = sorted(g.items(), key=sort_key or (lambda kv: -kv[1][1]))[:limit]
            out.append(f"## {title}")
            out.append(table([first, "Units", "Revenue", "Rev share", "Orders"],
                             [(k, v[0], f"{v[1]:,.0f}", pct(v[1], rev), len(v[2])) for k, v in rows]) + "\n")
            return rows

        cons = section("Construction buckets (by title keywords)", group(lambda x: construction_of(x["title"])), "Construction")
        summary["top_categories"] = ", ".join(f"{k} {pct(v[1], rev)}" for k, v in cons[:3])
        section("Style / format tags (a sale can count in several)",
                group(lambda x: [n for n, p in TAGS_MULTI if re.search(p, x["title"].lower())] or ["(none)"], multi=True), "Tag")
        sizes = section("Sizes sold", group(lambda x: x["size"]), "Size")
        summary["top_sizes"] = ", ".join(k for k, _ in sizes[:3])
        bands = group(lambda x: band_of(x["price"]))
        order_b = {band_of(lo): i for i, (lo, hi) in enumerate(PRICE_BANDS)}
        section("Price bands (unit price)", bands, "Band", sort_key=lambda kv: order_b.get(kv[0], 99))
        summary["sweet_spot"] = max(bands.items(), key=lambda kv: kv[1][1])[0]
        months = section("Monthly", group(lambda x: x["date"].strftime("%Y-%m") if x["date"] else "?"), "Month",
                         sort_key=lambda kv: kv[0])
        summary["peak_months"] = ", ".join(k for k, _ in sorted(months, key=lambda kv: -kv[1][1])[:3])
        countries = section("Countries", group(lambda x: x["country"]), "Country", limit=12)
        us = sum(v[1] for k, v in countries if k.lower() in ("united states", "us", "usa"))
        summary["us_share"] = pct(us, rev)

        # top listings
        L = defaultdict(lambda: {"u": 0, "r": 0.0, "t": "", "s": Counter()})
        for x in clean:
            e = L[x["lid"]]
            e["u"] += x["qty"]; e["r"] += x["rev"]; e["t"] = x["title"]; e["s"][x["size"]] += x["qty"]
        out.append(f"## Top listings by revenue ({len(L)} listings had sales)")
        out.append(table(["Listing ID", "Title", "Units", "Revenue", "Rev share", "Top sizes"],
                         [(k, e["t"][:70], e["u"], f"{e['r']:,.0f}", pct(e["r"], rev),
                           ", ".join(f"{s}×{n}" for s, n in e["s"].most_common(3)))
                          for k, e in sorted(L.items(), key=lambda kv: -kv[1]["r"])[:15]]) + "\n")
        top3 = sum(e["r"] for e in sorted(L.values(), key=lambda e: -e["r"])[:3])
        out.append(f"- Top 3 listings = {pct(top3, rev)} of revenue · listings with exactly 1 sale: "
                   f"{sum(1 for e in L.values() if e['u'] == 1)}\n")

        # repeat buyers (counts only, no identities)
        B = defaultdict(lambda: [set(), 0.0])
        for x in clean:
            if x["buyer"]:
                B[x["buyer"]][0].add(x["oid"]); B[x["buyer"]][1] += x["rev"]
        if B:
            rep = [v for v in B.values() if len(v[0]) >= 2]
            summary["repeat_share"] = pct(sum(v[1] for v in rep), rev)
            out.append("## Repeat buyers (aggregates only)")
            out.append(f"- Buyers: {len(B)} · Repeat buyers (2+ orders): {len(rep)} ({pct(len(rep), len(B))}) · "
                       f"their revenue share: {summary['repeat_share']}\n")
    elif orders:
        tot = sum(money(col(r, "Order Value", "Order Total")) for r in orders)
        summary.update(revenue=tot, orders=len(orders), aov=tot / len(orders) if orders else 0)
        out.append("## Topline (orders file only — export 'Order Items' for product-level analysis)")
        out.append(f"- Orders: {len(orders)} · Order value: {tot:,.0f} · AOV: {tot / len(orders):,.0f}\n")
        c = Counter(col(r, "Ship Country") or "?" for r in orders)
        out.append(table(["Country", "Orders"], c.most_common(12)) + "\n")
    else:
        out.append("## No order data found — export 'Order Items' CSV (see README)\n")

    # ---------- listings ----------
    if listings:
        # Titles change after a sale (Item Name = title at sale time), so match by SKU first, title as fallback.
        sold = {norm_title(x["title"]) for x in clean}
        sold_skus = {s.strip().lower() for x in clean for s in x["sku"].split(",") if s.strip()}
        summary["active_listings"] = len(listings)
        if clean:
            summary["rev_per_listing"] = summary["revenue"] / len(listings)
        issues, zero = [], []
        agg = Counter()
        for r in listings:
            title = col(r, "TITLE")
            tags = [t.strip() for t in col(r, "TAGS").split(",") if t.strip()]
            photos = sum(1 for k, v in r.items() if (k or "").upper().startswith("IMAGE") and (v or "").strip())
            long_tags = [t for t in tags if len(t) > 20]
            one_word = [t for t in tags if " " not in t and "_" not in t]
            probs = []
            if len(title) > 140: probs.append("title>140")
            if len(title) < 60: probs.append("title<60")
            if len(tags) < 13: probs.append(f"tags<13 ({len(tags)})")
            if long_tags: probs.append(f"tag>20ch ({len(long_tags)})")
            if len(one_word) >= 4: probs.append(f"one-word tags ({len(one_word)})")
            if photos < 8: probs.append(f"photos<8 ({photos})")
            if not col(r, "SKU"): probs.append("no SKU")
            for p in probs:
                agg[re.sub(r" \(\d+\)$", "", p)] += 1
            if probs:
                issues.append((title[:60], len(title), len(tags), photos, money(col(r, "PRICE")), "; ".join(probs)))
            has_sale = norm_title(title) in sold or col(r, "SKU").lower() in sold_skus
            if clean and not has_sale:
                zero.append((title[:70], money(col(r, "PRICE")), construction_of(title), len(tags), photos))
        out.append(f"## Active listings: {len(listings)}")
        cc = Counter(construction_of(col(r, "TITLE")) for r in listings)
        out.append(table(["Construction", "Listings"], cc.most_common()) + "\n")
        dup = [t for t, n in Counter(norm_title(col(r, "TITLE")) for r in listings).items() if n > 1]
        out.append(f"## Listing health — {len(issues)} of {len(listings)} listings have issues · duplicate titles: {len(dup)}")
        out.append(table(["Issue type", "Listings"], agg.most_common()) + "\n")
        if listing_health:
            out.append(table(["Title", "Title len", "Tags", "Photos", "Price", "Issues"], issues) + "\n")
        else:
            out.append("_(run with --listing-health for the per-listing table)_\n")
        if clean:
            summary["pct_with_sale"] = pct(len(listings) - len(zero), len(listings))
            out.append(f"## Zero-sale active listings in this data window: {len(zero)} of {len(listings)}")
            out.append("_Matched by SKU, then by title. Listings whose SKU and title both changed since the sale may still appear here._")
            out.append(table(["Title", "Price", "Construction", "Tags", "Photos"], zero[:60]) + "\n")
            if len(zero) > 60:
                out.append(f"_…and {len(zero) - 60} more_\n")

    # ---------- statements ----------
    if statements:
        S = defaultdict(lambda: [0, 0.0, 0.0, 0.0])
        for r in statements:
            t = col(r, "Type") or "?"
            S[t][0] += 1; S[t][1] += money(col(r, "Amount")); S[t][2] += money(col(r, "Fees & Taxes")); S[t][3] += money(col(r, "Net"))
        out.append("## Statement lines by type")
        out.append(table(["Type", "Lines", "Amount", "Fees & Taxes", "Net"],
                         [(k, v[0], f"{v[1]:,.2f}", f"{v[2]:,.2f}", f"{v[3]:,.2f}") for k, v in sorted(S.items())]) + "\n")
        fee_titles = Counter()
        for r in statements:
            if (col(r, "Type") or "").lower() in ("fee", "marketing", "tax", "vat"):
                key = re.sub(r"[:#].*$", "", col(r, "Title")).strip()[:40]
                fee_titles[key] += abs(money(col(r, "Fees & Taxes")) or money(col(r, "Amount")) or money(col(r, "Net")))
        if fee_titles:
            out.append(table(["Fee line", "Total"], [(k, f"{v:,.2f}") for k, v in fee_titles.most_common(12)]) + "\n")

    # ---------- unrecognized ----------
    if others:
        out.append("## Other CSVs (stats / search terms / ads — read these directly)")
        for name, header, n in others:
            out.append(f"- `{name}` — {n} rows — columns: {', '.join(h for h in header if h)}")
        out.append("")
    return "\n".join(out), summary


def main():
    ap = argparse.ArgumentParser(description="Summarize Etsy CSV exports per shop.")
    ap.add_argument("--shop", action="append", required=True, help="shop folder name under data/exports (repeatable)")
    ap.add_argument("--dir", help="override the exports folder (single shop only; for testing)")
    ap.add_argument("--from", dest="dfrom", help="YYYY-MM-DD")
    ap.add_argument("--to", dest="dto", help="YYYY-MM-DD")
    ap.add_argument("--listing-health", action="store_true", help="print per-listing issue table")
    ap.add_argument("--out", help="also write the markdown to this file")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    dfrom = datetime.strptime(a.dfrom, "%Y-%m-%d").date() if a.dfrom else None
    dto = datetime.strptime(a.dto, "%Y-%m-%d").date() if a.dto else None

    parts, sums = [], []
    for shop in a.shop:
        folder = Path(a.dir) if a.dir and len(a.shop) == 1 else ROOT / "data" / "exports" / shop.lower()
        folder.mkdir(parents=True, exist_ok=True)
        text, s = analyze(shop, folder, dfrom, dto, a.listing_health)
        parts.append(text); sums.append(s)

    if len(sums) > 1:
        fmt = lambda v: f"{v:,.0f}" if isinstance(v, (int, float)) else (v or "-")
        metrics = [("Revenue", "revenue"), ("Orders", "orders"), ("Units", "units"), ("AOV", "aov"),
                   ("Active listings", "active_listings"), ("Revenue per active listing", "rev_per_listing"),
                   ("% listings with a sale", "pct_with_sale"), ("Top categories", "top_categories"),
                   ("Top sizes", "top_sizes"), ("Price sweet spot", "sweet_spot"), ("US share", "us_share"),
                   ("Repeat-buyer revenue share", "repeat_share"), ("Peak months", "peak_months")]
        parts.append("# Side by side\n" + table(["Metric"] + [s["shop"] for s in sums],
                                               [[m] + [fmt(s.get(k)) for s in sums] for m, k in metrics]) + "\n")
    result = "\n\n".join(parts)
    print(result)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(result, encoding="utf-8")


if __name__ == "__main__":
    main()
