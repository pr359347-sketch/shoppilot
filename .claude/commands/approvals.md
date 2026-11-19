---
description: Approvals queue — pending proposals, approved-not-done, owner to-dos (eBay/Amazon), experiment checks due
---

Arguments (optional): `$ARGUMENTS` — `ok <ID>` · `no <ID>` · a shop name · empty (= show queue).

1. Read `data/approvals/*.md` (create the folder if missing).
2. Show grouped: 🟡 pending · ✅ approved-not-done · 📝 owner-to-do · 🔬 experiment checks due today/overdue.
3. `ok <ID>` / `no <ID>` → follow `.claude/skills/core/approval-flow/SKILL.md` §3–4 (check freeze first).
4. Experiment checks due → `core/experiment-tracker` (ask for fresh exports if needed).
