---
name: percorso-assunzione-domestica
description: Guided hiring path for domestic workers. Use when asked assumere colf badante passo passo, hire domestic worker path Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Percorso: Assunzione Domestica (Hire to Payslip)

Hire a colf/badante in order: profile, contract, pay, contributions, permits.
Rules and figures verified for the year in course (year-stated everywhere).

## When to use

- Whole-journey domestic hiring requests ("devo assumere una badante, da dove parto?").
- Do not use for single questions (route to the specific skill instead).

## Workflow (tappe + handoff)

1. **Profile** (see `colf-badanti`): mansioni (colf vs badante vs baby-sitter), hours,
   convivente or not, level per CCNL domestico. Handoff: level + hours + convivente flag.
2. **Contract** (see `contratto-base-check`): read the clauses with the checklist
   (periodo prova, preavviso, vitto/alloggio counting for conviventi). Info-only, no verdicts.
3. **Pay** (CCNL minimum tables, year-stated): monthly pay + 13a + TFR accrual + ferie
   (see `ferie-permessi` ratei math). Handoff: full cost picture.
4. **Contributions** (see `colf-badanti` INPS quarterly F24 + INAIL): rates and minimal
   year-stated. Handoff: payment cadence.
5. **Permits** (non-EU workers): hiring-decree flows flagged + referral, never DIY on quotas.
6. **First payslip** (see `busta-paga-leggi`): verify lines with the script. Close: privacy
   (redact before sharing) + accountant/CAF check.

## Rules

- Levels and minimums with year + CCNL cited; never generic pay figures.
- Convivente rules differ at every tappa: carry the flag forward.
- Irregular work: risks stated plainly for both sides at tappa 1, not buried later.
- Permits are a referral track, never a DIY checklist.

## Examples

Two end-to-end runs in `examples/percorso-cases.md`. Stage detail in `references/tappe.md`.

## Edge cases

- Night-shift badante: presence vs active-hours rules at tappa 1 (see `colf-badanti`).
- Dismissal later: preavviso + TFR domestic terms (see `colf-badanti` edge cases), no generic mix.
- Bonus linked (asilo): cross-link at tappa 3, amounts with year.
