---
name: percorso-apri-partita-iva
description: Guided path from idea to first invoice. Use when asked open partita IVA start to finish, avvio attività percorso, freelance from zero Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# Percorso: Aprire Partita IVA (Start to First Invoice)

One guided path across six skills: no duplicated questions, context handed off
at every step. Rules and figures verified for the year in course (year-stated everywhere).

## When to use

- "voglio aprire partita IVA", "start freelance from zero", whole-journey requests.
- Do not use for single questions (route to the specific skill instead).

## Workflow (tappe + handoff)

1. **Idea** (see `partita-iva-apri`): activity, employee vs freelance, expected revenue,
   prior employment. Handoff: activity + revenue + employment history.
2. **ATECO** (see `ateco-scelta`): code choice from the activity. Handoff: code + coefficient.
3. **Regime** (see `regime-forfettario`): gates check + tax math with the script
   (`forfettario.py --fatturato ... --coeff ... --year ...`). Handoff: regime + expected tax.
4. **INPS** (see `contributi-inps`): track by activity (Gestione Separata vs artigiani/commercianti).
   Handoff: track + first-year contribution estimate.
5. **Deadlines** (see `scadenze-fiscali`): calendar for year one (saldo + acconti + split
   from `acconti-calcolo`). Handoff: dated calendar.
6. **First invoice** (see `invoice-it` or `fattura-elettronica-it`): draft with verified
   totals. Close: accountant review before filing anything.

## Rules

- Ask once, reuse everywhere: never re-ask activity/revenue/employment at later tappe.
- No regime verdicts, no filing: guidance only (see `partita-iva-apri` rules).
- Amounts with year; ex-employee continuity flagged at tappa 1, never later as a surprise.
- If the user stops mid-path, summarize reached tappe + what's next.

## Examples

Two end-to-end runs in `examples/percorso-cases.md`. Stage detail in `references/tappe.md`.

## Edge cases

- Occasional work fits better → exit to ritenuta path early (see `collaborazioni-occasionali`), don't push VAT.
- Foreign resident → fiscal residence flag at tappa 1 + referral.
- Over 85k expected → threshold plan from tappa 3 (see `regime-forfettario` 85k/100k logic).
