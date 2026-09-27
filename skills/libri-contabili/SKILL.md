---
name: libri-contabili
description: Explain mandatory books with retention. Use when asked libri contabili, accounting books Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[company]"
user-invocable: true
disable-model-invocation: false
---

# Libri Contabili

Books in order: which ones, how kept, 10-year retention.

## When to use

- "libri contabili", "accounting books Italy".
- Do not use for bookkeeping itself (accountant matter).

## Workflow

1. List by regime: libro giornale, inventari, IVA (vendite/acquisti/corrispettivi), cespiti, sociali where due.
2. Form: validly kept (vidimazione where required) + electronic conservation rules.
3. Retention 10 years + exhibition on control.
4. Output: checklist per company type + gaps to fix.

## Rules

- Forfettari/minimi simplifications stated (fewer books), never assumed exempt from all.
- Electronic conservation ≠ simple PDF dump: rules noted.
- Missing years: reconstruct with accountant now, stated as urgent (retention year-stated: 10 years).

## Examples

See `examples/libri-cases.md`. Book map in `references/libri.md`.

## Edge cases

- Lost/damaged books → denuncia + reconstruction path, urgent tone.
- Inspection announced → exhibit in order, professional present.
- Digital-only startup: conservation provider notes, no DIY archiving advice beyond basics.
