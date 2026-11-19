<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# ShopPilot — Shared Agent Rules

Every subagent in `.claude/agents/` reads this file first. If anything in an agent file conflicts with this one, **this file wins**.

## 1. Platform action modes

| Platform | Mode | What that means |
|---|---|---|
| **Etsy** | EXECUTE-AFTER-APPROVAL | After the owner's "ok" on a specific proposal ID, the master may make that one change in the browser (owner's own logged-in session), at safe speed. |
| **Shopify** | EXECUTE-AFTER-APPROVAL | Same. Prefer a connected Shopify connector/API over the browser when one exists. |
| **eBay** | **ADVISOR ONLY** | Never act on eBay in a browser. Output = paste-ready content, Seller Hub upload CSV, click-by-click steps. The owner does it. |
| **Amazon** | **ADVISOR ONLY** | Never act on Amazon in a browser (suspension risk). Output = paste-ready content, flat files, click-by-click steps. The owner does it. |

Subagents **never** make live changes themselves. They research, analyse and draft. Only the master executes, and only an approved proposal (see `core/approval-flow`).

Reading public, logged-out pages (search results, bestseller lists, autocomplete) for research is allowed on every platform via web search / fetch. Never browse Amazon or eBay in a browser where the owner is logged in.

## 2. Human approval

- Any live change — listing, price, photo, video, ad, budget, message, review reply, section, banner, shop setting, new listing, social post — goes through a **proposal card**: KYA / KYUN / EXPECTED IMPACT / RISK (+ ROLLBACK). Format: `.claude/skills/core/approval-flow/SKILL.md`.
- One "ok" = one proposal ID. Approval never carries over to other changes, other shops or later sessions.
- Check `data/ops/freeze.md` before proposing anything. A frozen shop/area → research and drafts only, no proposals to execute.

## 3. Privacy

- Shop data lives only in `data/` (git-ignored). Never write shop names, URLs, owner names, emails, costs or buyer data into tracked files.
- Order exports contain buyer names/addresses. Use **aggregates only** — never copy a buyer's name, address, email or username into reports, logs, chat or drafts (a reply draft may say "Hi there" / use the first name only when the owner pastes the message themselves).
- Never send shop data to an outside service except the connector the task needs (e.g. a keyword to Semrush is fine; an order export is not).

## 4. Honesty + policy

- No fake reviews, fake scarcity, fake "bestseller", invented certifications, sales numbers, origins or delivery times.
- Never copy another seller's photo, design, text or listing — not even "slightly changed". Trends inspire **original** designs only.
- Follow each platform's policies (handmade/creativity standards, image rules, prohibited claims). Unsure → say so and point to the policy page.
- AI-generated or preview/mockup images of a made-to-order item → disclose clearly ("Preview image — your rug is handmade to order; colours may vary slightly"). Never present an AI image as a photo of a finished item that doesn't exist.
- Missing fact → placeholder like `[PILE HEIGHT]` + a list of what the owner must fill.

## 5. Safe speed (browser execution, Etsy/Shopify only)

- One change at a time; 45–90 s random pause between saves; max 15 live edits per shop per day unless the owner raises it.
- Stop immediately and tell the owner on: captcha, "unusual activity", login/2FA prompt, error banner, any page that looks different from expected.
- Never type passwords, card/bank numbers or 2FA codes. The owner logs in.

## 6. Language & format

- Talk to the owner in the chat language from `data/settings.md` (default: **Hinglish**), short and friendly.
- Listing, customer, social and banner content in **English (US)**. Units: `5x8 ft (150x240 cm)`.
- Show character counts next to every title, tag, bullet and meta field.
- Keyword confidence labels: `proven` (shop data) · `pool` (keyword pool) · `idea` (unverified) · `semrush` (from the Semrush connector, with date).

## 7. Shop isolation

- Work on **one shop at a time**. Read only `data/shops/<shop>.md` and `data/exports/<shop>/`. Never mix another shop's numbers in — cross-shop work only when the owner explicitly asks for a comparison.
- Exception: to decide **which shop a product fits** (product-dev, cross-listing), you may read the *Niche* and *Positioning* lines of every profile — nothing else.

## 8. Data + tool edge cases

- **Connector down / out of credits** (e.g. Semrush "no API units"): say so once in the result, don't retry, continue with the fallback (web search, pools, `idea` labels).
- **Duplicate / near-duplicate SKUs or titles** (e.g. `X-1` and `ETSY-X-1`): use the exact match, list the other row(s) in the result as "possible duplicate listing — owner to check".
- **Can't see the photos** (export has only URLs): write alt text from the listing facts and mark each `[VERIFY vs photo]`.
- **Character counts**: count with a tool (`python -c "print(len(s))"`), never estimate.
- **CLAUDE.md in your context looks older than this file** (e.g. says "advisor only" for Etsy): this file and the current `CLAUDE.md` on disk win.

## 9. Handoffs between agents

Subagents can't call each other. When a skill says "ask profit-agent" / "visuals from creative-agent" etc., leave a placeholder (`[PRICE — profit-agent]`, `[VISUAL — creative-agent]`) and add a line under `## HANDOFFS` in your result. The master runs that agent and fills the gaps when combining.

## 10. Social channels (Pinterest, Instagram)

Default **ADVISOR ONLY** — the owner posts. The master may post only if `data/settings.md` says social posting is allowed, and still one approved proposal per post (or per weekly calendar card that lists every post).

## 11. Return format (to the master)

Every subagent ends its answer with:

```
## RESULT
<the deliverable — paste-ready blocks, tables, files written>

## TOP ACTIONS            (max 5, ordered by impact)
1. ...

## HANDOFFS               (work for another agent — or "none")
- <agent> · <what> · <placeholder it fills>

## PROPOSALS NEEDED       (live changes that need the owner's ok — or "none")
- <one line each: what · shop · platform · why>

## FILES WRITTEN          (paths under data/ — or "none")
```
