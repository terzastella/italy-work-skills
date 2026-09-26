---
name: busta-paga-leggi
description: Read Italian payslips line by line with net-pay math. Use when asked busta paga, payslip Italy, read payslip, netto in busta.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[payslip data]"
user-invocable: true
disable-model-invocation: false
---

# Busta Paga Leggimi

Payslips decoded: gross → withholdings → net, every line explained.

## When to use

- "busta paga", "payslip Italy", "read payslip", "netto in busta".
- Do not use for payroll computation for employers (reading only).

## Workflow

1. Take payslip data (user-provided, anonymizable). Identify CCNL + level.
2. Walk sections (see `references/voci.md`): paga base, contingenza/EDR, superminimo,
   straordinari, ferie/permessi residue, INPS worker share, IRPEF + detrazioni, netto.
3. Recompute net with the bundled script (preferred, reproducible):
   `python skills/busta-paga-leggi/scripts/payslip_check.py --lordo 1950 --inps 175.5 --irpef 280 --detrazioni 125.5 --netto 1620`
   Flag mismatches as questions for payroll, not accusations.
4. Close with TFR accrual note (where it sits) + CU cross-check tip + privacy reminder (redact first).

## Rules

- Math only on given figures; never invent CCNL tables from memory — cite level + source.
- Anomalies phrased as checks ("verify with payroll"), never fraud claims.
- Privacy: suggest redacting name/fiscal code before sharing.

## Scripts

- `scripts/payslip_check.py` — net verification: recompute vs stated net, gap verdict.
  Fixtures with expected outputs in `examples/fixtures/`. Gaps are checks, never fraud claims.

## Examples

See `examples/busta-cases.md`.

## Edge cases

- 13a/14a months → separate reading, accrual logic explained.
- Part-time % → proportional checks flagged.
- Arretrati/tassazione separata → special section, do not mix with ordinary.
