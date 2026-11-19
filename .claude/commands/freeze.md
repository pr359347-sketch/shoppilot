---
description: Freeze rules — stop live changes for a shop/area for a period (e.g. Black Friday week), or list/lift freezes
---

Arguments: `$ARGUMENTS` — e.g. `/freeze <shop> titles-tags till 2026-12-02 black friday`, `/freeze list`, `/freeze lift <shop> all`.

1. Create `data/ops/freeze.md` from `templates/freeze.md` if missing.
2. Delegate to **ops-agent** (`core/ops-routine` → Freeze rules): add / list / lift. Ask once for anything missing (shop, area, end date, reason).
3. Confirm in one line: "⛔ Freeze set: <shop> · <area> · till <date>." While active, the master shows proposals for that area as FROZEN (no execution).
