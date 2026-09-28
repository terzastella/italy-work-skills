---
name: percorso-busta-controllo
description: Guided payslip audit path, contract to balances. Use when asked controllare busta paga percorso, payslip audit path Italy, stipendio verifiche.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Percorso: Busta Controllo (Contract to Balances)

Full payslip audit in order: contract, net verification, severance, holidays.
Rules and figures verified for the year in course (year-stated everywhere).

## When to use

- Whole-audit requests ("voglio controllare la mia busta paga e tutto il resto").
- Do not use for single questions (route to the specific skill instead).

## Workflow (tappe + handoff)

1. **Contract** (see `contratto-base-check`): level, duties, probation, notice — clause map.
   Info-only, no verdicts. Handoff: CCNL + level.
2. **Net check** (see `busta-paga-leggi` + script): recompute net from stated lines
   (`payslip_check.py --lordo ... --inps ... --irpef ... --netto ...`).
   Gaps are payroll questions, never accusations. Privacy: redact first.
3. **TFR** (see `tfr-fondo` + script): revaluation math on the accrued stock
   (`rivalutazione.py --accantonato ... --inflazione ... --year ...`). Mechanics only.
4. **Holidays** (see `ferie-permessi` + script): accrual vs taken balance
   (`ratei.py --spettanza ... --mese ... --fruiti ...`, CCNL-cited entitlement).
   Close: CU cross-check tip + payroll questions list.

## Rules

- Math only on given figures; CCNL tables cited, never from memory.
- Anomalies phrased as checks, never fraud claims — at every tappa.
- Privacy first: redact name/fiscal code before sharing anything.
- 13a/14a and arretrati: separate tracks, never merged into the ordinary math.

## Examples

Two end-to-end runs in `examples/percorso-cases.md`. Stage detail in `references/tappe.md`.

## Edge cases

- Part-time %: proportional checks flagged at tappe 2–4.
- Gap found: one question list for payroll, ordered by size, no accusations.
- TFR in fondo vs azienda: mechanics pointer (see `tfr-fondo`), no recommendations.
