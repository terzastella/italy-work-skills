---
name: nota-credito
description: Issue Italian credit notes via SdI with correct references. Use when asked nota di credito, credit note Italy, storno fattura.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[original invoice]"
user-invocable: true
disable-model-invocation: false
---

# Nota di Credito

Fix invoicing errors the legal way: credit notes referencing the original, via SdI.

## When to use

- "nota di credito", "credit note Italy", "storno fattura", "invoice correction".
- Do not use for editing a transmitted invoice (never edit — credit note instead).

## Workflow

1. Identify: original invoice (number, date), what is wrong (amount, item, full cancel).
2. Draft TD04 credit note with mandatory reference to the original (section 2.1.6 linkage).
3. Partial vs total: partial corrects lines, total cancels all (state which).
4. VAT effect explained briefly + accountant check before transmitting.

## Rules

- Never modify an SdI-transmitted file: credit note only.
- Original reference always present (number + date, year-stated).
- Forfettari: no VAT involved — state it, simpler flow.

## Examples

See `examples/nota-cases.md`. TD04 notes in `references/td04.md`.

## Edge cases

- PA invoice error → credit note + new correct invoice, CIG/CUP repeated.
- Year closed → competence note, flag to accountant (no DIY on closed years).
- Foreign invoice error → same logic, currency note as in fattura-elettronica-it.
