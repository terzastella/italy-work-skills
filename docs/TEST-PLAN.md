# Real-agent test plan — 5 skills × 3 agents (your accounts needed)

Local gates are green (validate, security, evals). This file is the protocol
for the only thing machines can't do alone: installing on real agents and
recording dated ✅ in `docs/COMPATIBILITY.md`.

## Matrix (fill with ✅ date + agent version, or ❌ + issue link)

| Skill | Claude Code | Codex | Grok |
|---|---|---|---|
| hello-agent | ⬜ | ⬜ | ⬜ |
| invoice-it | ⬜ | ⬜ | ⬜ |
| frontend-design (vendor/anthropics) | ⬜ | ⬜ | ⬜ |
| tdd (vendor/pocock) | ⬜ | ⬜ | ⬜ |
| brainstorming (vendor/superpowers) | ⬜ | ⬜ | ⬜ |

## Install commands (run from repo root)

```bash
python scripts/install.py --skill hello-agent --agent claude
python scripts/install.py --skill invoice-it --agent claude
python scripts/install.py --skill frontend-design --source vendors --agent claude
python scripts/install.py --skill tdd --source vendors --agent claude
python scripts/install.py --skill brainstorming --source vendors --agent claude
# repeat with --agent codex, then --agent grok
```

## Per-cell protocol (same 4 steps everywhere)

1. Install with the command above (one skill, one agent).
2. `hello-agent`: ask the agent `hello skills`, check the reply table.
   Others: run the skill's smoke prompt —
   `invoice-it`: "draft an invoice: consulting 10h x €50, VAT 22%" (expect €610 table);
   `frontend-design`: "sketch a landing hero" (expect brand-aware draft);
   `tdd`: "add a trivial function test-first" (expect RED-GREEN cycle);
   `brainstorming`: "help me scope a tiny project" (expect questions before code).
3. Record `✅ YYYY-MM-DD <agent> <version>` or `❌ YYYY-MM-DD + issue link`.
4. After 15 cells: collapse this file's table into `docs/COMPATIBILITY.md`
   (replace the "all untested" note row by row) and delete this file or mark done.

## Rules

- One cell at a time; never batch-install before testing (isolation).
- Vendor skills are read-only tests: issues go upstream, not into `vendors/`.
- Failing cell → open issue (`.github/ISSUE_TEMPLATE/bug_report.md`) before retrying.
