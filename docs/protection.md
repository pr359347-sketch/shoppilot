<!-- ShopPilot © 2026 Priya Rani — proprietary, see LICENSE. -->
# Protecting ShopPilot — owner's playbook

ShopPilot is public for portfolio and evaluation only (see [LICENSE](../LICENSE)). This page is for the owner: how to spot copies and what to do about them.

## What's already in place
- **Proprietary license** — viewing only; any use, copy, modification or redistribution needs written permission.
- **Ownership headers** in CLAUDE.md, every agent, every skill and the scripts.
- **CODEOWNERS** (`.github/CODEOWNERS`) — every PR needs the owner's review.
- **Branch protection on `main`** — PRs need an approving review, force-push and branch deletion are disabled.
- Note: copies people made while the repo was MIT-licensed (before this change) keep the MIT terms for that old version. Everything from this commit on is under the new license.

## 1. Find forks and copies

| Where | How |
|---|---|
| Forks | Repo → **Insights → Forks** (or `https://github.com/pr359347-sketch/shoppilot/forks`) |
| Traffic | Repo → **Insights → Traffic**: clones, referring sites, popular content |
| Copied code on GitHub | GitHub search (code tab) for distinctive strings, e.g. `"ShopPilot © 2026 Priya Rani"`, `"AGENT-RULES.md"`, `"EXECUTE-AFTER-APPROVAL"`, `"KYA · KYUN"` |
| Renamed copies | Search for unique phrases from skill files in quotes on GitHub and Google, e.g. `"Lock-line"`, `"PROPOSALS NEEDED"` |
| Marketplaces / sites | Google the README tagline and unique headings in quotes |

Keep a dated note of each finding: URL, screenshot, what was copied, and whether the header or license was removed.

## 2. Ask first (often enough)
Open an issue on the copying repo or message the owner: point to the LICENSE, ask them to take it down or contact you for a licence. Give them 7 days.

## 3. GitHub DMCA takedown
1. Read GitHub's guide: <https://docs.github.com/en/site-policy/content-removal-policies/guide-to-submitting-a-dmca-takedown-notice>
2. Submit the form: <https://support.github.com/contact/dmca-takedown>
3. Include:
   - Your contact details and that you are the copyright owner (Priya Rani, @pr359347-sketch)
   - The original work: `https://github.com/pr359347-sketch/shoppilot` (link to specific files/commits)
   - Each infringing URL (repo + specific files), and for a fork network say whether all forks are infringing
   - What was copied and that it was used without permission under the proprietary license
   - The required good-faith and accuracy statements (from GitHub's guide) and your signature (typed full name)
4. GitHub usually gives the other party time to make changes; reply quickly to any follow-up.

Outside GitHub (websites, marketplaces): use that host's copyright / DMCA form with the same evidence.

## 4. Keep evidence strong
- Keep the ownership headers in every file.
- Don't rewrite git history — the commit dates prove authorship.
- Optional: GitHub Releases with tags (dated snapshots).
