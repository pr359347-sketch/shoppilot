# FAQ

**Does ShopPilot change anything in my shop?**
Only after your explicit "ok" on a specific proposal, and only on **Etsy and Shopify** (in your own logged-in browser session or a connected Shopify connector, one change at a time at human speed). On **eBay and Amazon** it is advisor-only: you get paste-ready text, upload files and step-by-step instructions, and you make every change yourself. It never types your passwords or payment details.

**What do I need to run it?**
[Claude Code](https://claude.com/claude-code) and this repo. Python 3 is needed only for the CSV analysis script (standard library, nothing to install).

**Do I have to connect a shop?**
No. Without a shop, ShopPilot runs in generic mode: listing SEO, audits, keyword research, competitor research, pricing, seasonal planning and creative prompts all work — you just give the product details in your message. Shop analysis, shop comparison and the ads optimizer need a connected shop and its exports.

**Where is my data stored? Is it uploaded anywhere?**
Everything about your shop stays in the `data/` folder on your computer. That folder is git-ignored, and a pre-commit hook blocks it from ever being committed. The files you ask the agent to read are processed by Claude Code like any other conversation content; nothing is sent to GitHub or any other service by this project.

**My order CSV has customer names and addresses. Is that a problem?**
The analysis script prints aggregates only, and the agent is instructed never to write buyer details into reports. Still: never share your `data/` folder.

**Can I connect more than one shop?**
Yes — run `/connect-shop` once per shop. Each profile has a `platform:` field, so shops on different marketplaces can sit side by side as modules are added.

**Which platforms are supported?**
Etsy today. eBay, Shopify and Amazon are planned as separate modules with the same structure. The platform-agnostic core skills can already be used for them if you supply the platform's field limits.

**I sell something other than rugs.**
The rug knowledge is the deepest, but there is a general home-textiles / decor module, and every skill falls back to asking for your product's sizes, materials and techniques. New product domains are easy to add (`.claude/skills/domain/`).

**How accurate are the keywords?**
ShopPilot has no live search-volume data. It labels keywords `proven` (from your own search-term or sales data), `pool` (curated starter lists) or `idea` (suggestions to verify in the marketplace search bar or a keyword tool).

**Are the fee numbers correct?**
Marketplace fees change and vary by seller country. Values that need checking are marked `[VERIFY]` in the platform file — compare with your own monthly statement.

**Can I use the AI image prompts for my listing photos?**
The prompts are written to place your **real product photo** into room scenes without changing the product. Listing photos must represent the actual item — keep the hero shot and close-ups as real camera photos and reject any generated image where the design or colors drifted.

**What does the pre-commit hook do, and how do I enable it?**
After cloning run `git config core.hooksPath .githooks`. The hook blocks commits that include anything under `data/`, `reports/` or `exports/`, any `.env` / CSV / Excel file, personal email addresses or real shop URLs, and any word you list in `data/.private-keywords`.

**How do I update ShopPilot?**
`git pull`. Your `data/` folder is untouched by updates.

**How do I contribute a platform?**
See [adding-a-platform.md](adding-a-platform.md) and `CONTRIBUTING.md`.
