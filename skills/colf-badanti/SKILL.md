---
name: colf-badanti
description: Guide domestic work contracts with levels and contributions. Use when asked colf badante, domestic worker Italy, contratto domestico.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Colf e Badanti

Domestic work in order: contract level, pay, contributions, permits.

## When to use

- "colf badante", "domestic worker Italy", "contratto domestico".
- Do not use for company employees (different CCNL).

## Workflow

1. Profile: mansioni (colf vs badante vs baby-sitter), hours (convivente or not), level per CCNL domestico.
2. Pay: minimum tables (year-stated) + 13a + TFR accrual + ferie.
3. Contributions: INPS quarterly (F24), rates + minimal (year-stated); INAIL for domestics.
4. Permits for non-EU workers: hiring-decreto flows flagged + referral, never DIY on quotas.

## Rules

- Levels and minimums with year + CCNL cited; never generic pay figures.
- Convivente vs non-convivente rules differ: vitto/alloggio counting stated.
- Irregular work: risks stated plainly for both sides, regularization path.

## Examples

See `examples/colf-cases.md`. Level table in `references/livelli.md`.

## Edge cases

- Badante night shifts: presence vs active hours rules flagged.
- Dismissal of domestic worker: preavviso + TFR + specific terms, no generic licenziamento mix.
- Bonus/assegni linked (e.g. asilo): cross-links stated, amounts with year.
- Reading their payslip → see `busta-paga-leggi`; their holidays → see `ferie-permessi`.
