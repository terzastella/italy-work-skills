---
name: busta-paga-leggi
description: Read Italian payslips line by line with net-pay math. Use when asked busta paga, payslip Italy, read payslip, netto in busta.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
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
3. Recompute net from lines shown; flag mismatches as questions, not accusations.
4. Close with TFR accrual note (where it sits) + CU cross-check tip.

## Rules

- Math only on given figures; never invent CCNL tables from memory — cite level + source.
- Anomalies phrased as checks ("verify with payroll"), never fraud claims.
- Privacy: suggest redacting name/fiscal code before sharing.

## Examples

See `examples/busta-cases.md`.

## Edge cases

- 13a/14a months → separate reading, accrual logic explained.
- Part-time % → proportional checks flagged.
- Arretrati/tassazione separata → special section, do not mix with ordinary.
