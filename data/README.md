# data/ — your private workspace

Everything in this folder stays on your computer. It is **git-ignored**; only this README and `.gitkeep` are tracked, and the pre-commit hook blocks anything else here from being committed.

Run `/connect-shop` in Claude Code and ShopPilot creates what it needs:

```
data/
  settings.md            your chat language, target market, occasion rules
  brand.md               brand voice, story, USPs, shipping / return policy
  learnings.md           what worked / didn't after your feedback
  .private-keywords      words that must never reach git (shop names, your name…), one per line
  shops/<shop>.md        one profile per shop — includes a `platform:` field (etsy / ebay / shopify / amazon)
  exports/<shop>/        marketplace exports you drop in (CSV files)
  keyword-pools/*.md     your working keyword pools
  reports/               dated analysis reports
```

- How to export your marketplace data: [docs/etsy-csv-export-guide.md](../docs/etsy-csv-export-guide.md)
- Order exports contain buyer names and addresses — never share this folder.
- Back it up yourself (it is not in git).
