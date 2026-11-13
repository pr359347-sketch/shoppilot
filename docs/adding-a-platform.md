# Adding a Platform Module

ShopPilot is multi-platform by design. Etsy is the reference module — copy its shape.

## The module contract

A platform module is complete when all of this exists (replace `<p>` with the platform name, lowercase):

```
.claude/skills/<p>/
  PLATFORM.md                    limits, fees, image/video specs, ranking factors, benchmarks, export formats
  <p>-listing-seo/SKILL.md       paste-ready listing package
  <p>-shop-analysis/SKILL.md     sales analysis from exports
  <p>-ads-optimizer/SKILL.md     ad performance → pause / scale / fix
docs/<p>-csv-export-guide.md     exact export steps, shown to users when a file is missing
scripts/<p>_analyze.py           export cruncher
```

## Steps

1. **Write `PLATFORM.md` first.** Use the same headings as `.claude/skills/etsy/PLATFORM.md`: listing limits · graphics sizes · fees · shipping · search ranking · benchmarks · exports. Every number must come from the platform's official documentation — mark anything uncertain `[VERIFY]`.
2. **Write the three platform skills.** Start from the Etsy versions. Keep the same output order and the same rules (character counts shown, honest claims, placeholders for unknown facts, "Next steps" at the end). Each analysis skill must check `data/exports/<shop>/` first and point to the export guide when files are missing.
3. **Write the export guide** in `docs/` with click-by-click steps and the expected file names.
4. **Write the analysis script.** Standard library only if possible. It must detect file types by header, accept `--shop`, read from `data/exports/<shop>/`, and print **aggregates only** — never buyer names, emails or addresses.
5. **Wire it up:**
   - `CLAUDE.md` → architecture block (section 2) and routing table (section 6)
   - `.claude/commands/start.md` → platform list
   - `README.md` → platform support table and roadmap
   - `docs/skills-reference.md`
   - replace the placeholder `README.md` in `.claude/skills/<p>/`
6. **Don't fork the core skills.** `core/` skills read limits from the active `PLATFORM.md`. If a core skill needs platform-specific behaviour, add a short section to your `PLATFORM.md` and reference it, rather than copying the skill.
7. **Test in both modes:** generic (no shop) and connected (a test profile with `platform: <p>` and sample exports in `data/` — which stays untracked).

## Adding a product domain

Product knowledge lives in `.claude/skills/domain/`. Add `<domain>.md` with: standard sizes, materials + care lines, techniques and what can honestly be claimed, rooms / uses, styles, photo-set guidance, keyword patterns. Then mention it in `CLAUDE.md` section 2.

## Privacy checklist for every PR

- No real shop names, URLs, emails, cost figures or exports — examples use placeholders.
- `git config core.hooksPath .githooks` is set, and the pre-commit hook passes.
