---
name: busta-paga-leggi
description: Read Italian payslips line by line with net-pay math. Use when asked busta paga, payslip Italy, read payslip, netto in busta.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.5", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[payslip data]"
user-invocable: true
disable-model-invocation: false
---

# Busta Paga Leggimi

Payslips decoded: gross → withholdings → net, every line explained.
Flagship skill: section-by-section walk, script verification, privacy-first.

## When to use

- "busta paga", "payslip Italy", "read payslip", "netto in busta".
- Do not use for payroll computation for employers (reading only).

## Workflow (tappe with formal in/out)

### Tappa 1 — Frame the document

Input: payslip data (user-provided, anonymizable — suggest redacting
name/fiscal code BEFORE sharing). Output: CCNL + level identified, month type
(ordinary / 13a / 14a / arrears section?).

### Tappa 2 — Walk the sections

Follow `references/sezioni.md` top to bottom: testata → competenza →
trattenute → netto → TFR/ferie footer. Every line gets: what it is, where
the figure comes from, what to compare it against. Overtime lines: see
`straordinari-info`; TFR line: see `tfr-fondo`.

### Tappa 3 — Recompute (script preferred, reproducible)

`python skills/busta-paga-leggi/scripts/payslip_check.py --lordo 1950 --inps 175.5 --irpef 280 --detrazioni 125.5 --netto 1620`
Flag mismatches as questions for payroll, not accusations. Tolerance €1 (rounding).

### Tappa 4 — Close the loop

TFR accrual note (where it sits) + CU cross-check tip at year end +
privacy reminder (redact first) + ordered payroll questions if gaps.

## Multi-turn protocol

Turn 1 (frame): CCNL + level + month type — anonymized first.
Turn 2 (walk): sections explained, no math yet. Turn 3 (verify): script run
+ gap verdict. Turn 4 (close): TFR/CU + questions list. Never accuse, at any turn.

## Rules

- Math only on given figures; never invent CCNL tables from memory — cite level + source.
- INPS/IRPEF figures year-stated; contribution rules move — verify yearly.
- Anomalies phrased as checks ("verify with payroll"), never fraud claims.
- Privacy: suggest redacting name/fiscal code before sharing.
- 13a/14a and arretrati run as separate readings, never merged into ordinary math.

## Scripts

- `scripts/payslip_check.py` — net verification: recompute vs stated net, gap verdict (5 fixtures).
  Fixtures with expected outputs in `examples/fixtures/`. Gaps are checks, never fraud claims.

## Examples

Good and bad cases in `examples/busta-cases.md`. Section walk in `references/sezioni.md`.
Line glossary in `references/voci.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Gap found | ordered payroll questions, conguaglio hypothesis, no accusations |
| 2 | 13a/14a months | separate reading, accrual logic explained |
| 3 | Part-time % | proportional checks flagged |
| 4 | Arretrati/tassazione separata | special section, do not mix with ordinary |
| 5 | Privacy refusal | respect it: explain with redacted structure, no data needed |
