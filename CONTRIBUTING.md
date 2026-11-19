# Contributing to ShopPilot

Thanks for helping. ShopPilot is a set of instructions, skills and small scripts for Claude Code — most contributions are Markdown.

## Ground rules

1. **No private data, ever.** No real shop names, shop URLs, emails, cost figures, customer data or exports — in files, examples, commit messages or issues. Use placeholders like `<your-shop>` and `[TODO]`.
2. **Enable the privacy hook** right after cloning:
   ```bash
   git config core.hooksPath .githooks
   ```
   It blocks commits touching `data/`, `reports/`, `exports/`, `.env` / CSV / Excel files, personal emails, real shop URLs, and any word in your local `data/.private-keywords`. Don't bypass it with `--no-verify`.
3. **Approval first.** Skills and agents never make live changes on their own. Every change goes through `core/approval-flow` (proposal → owner "ok" → master executes on Etsy/Shopify only). eBay and Amazon stay advisor-only. Agents never log in, never type credentials, never message buyers without approval.
4. **Honest by default.** Skills must not invent platform limits, fees, search volumes or product claims. Uncertain numbers are marked `[VERIFY]`.
5. **Paste-ready output.** Every skill ends with concrete, copyable output and a short "Next steps" list.

## What to contribute

- Fixes to platform limits / fees when a marketplace changes them (`.claude/skills/<platform>/PLATFORM.md`)
- Better keyword starter pools (`templates/keyword-pools/`)
- New product domains (`.claude/skills/domain/<domain>.md`)
- New platform modules (below)
- Docs and FAQ improvements

## How to add a new platform module

Short version — full guide in [docs/adding-a-platform.md](docs/adding-a-platform.md):

1. Create `.claude/skills/<platform>/PLATFORM.md` with the same headings as the Etsy one (limits, fees, image specs, ranking factors, benchmarks, exports). Official sources only.
2. Add three skills: `<platform>-listing-seo`, `<platform>-shop-analysis`, `<platform>-ads-optimizer` (copy the Etsy ones as a starting point).
3. Add `docs/<platform>-csv-export-guide.md` and `scripts/<platform>_analyze.py` (aggregates only — no buyer PII in output).
4. Wire it into `CLAUDE.md` (architecture + routing), `.claude/commands/start.md`, `README.md` and `docs/skills-reference.md`.
5. Don't copy core skills — they read limits from the active `PLATFORM.md`.

## Pull requests

- One topic per PR, conventional commit messages (`feat:`, `fix:`, `docs:`).
- Test your change in Claude Code in both generic mode (no shop) and connected mode (a local test profile under `data/`, which stays untracked).
- Keep skills concise: instructions the agent needs, not essays.

By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).
