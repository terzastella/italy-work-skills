---
name: operazioni-estero
description: Guide Italy cross-border VAT ops and Intrastat basics. Use when asked esterometro abolished, Intrastat, reverse charge, operazioni estero.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[operation]"
user-invocable: true
disable-model-invocation: false
---

# Operazioni con l'Estero (VAT)

Cross-border without errors: esterometro gone (SdI data), Intrastat stays, reverse charge logic.

## When to use

- "esterometro", "Intrastat", "reverse charge", "fattura estero", "acquisti UE".
- Do not use for customs/duties (different matter).

## Workflow

1. Classify: EU goods (cessioni/acquisti intra) · EU services · extra-EU.
2. Route: esterometro abolished — cross-border invoice data via SdI formats (TD17-TD19 etc., verify current codes);
   Intrastat filings where still due; reverse charge on EU purchases.
3. VIES check note for EU counterparties.
4. Close with accountant verification (penalties are real here).

## Rules

- TD document codes change: cite current table, never from memory alone.
- Forfettari buying EU services → reverse charge applies to them too (flag it).
- Never guess Intrastat thresholds: current values only, with year.

## Examples

See `examples/estero-cases.md`. Code map in `references/codici.md`.

## Edge cases

- UK post-Brexit → extra-EU rules, flag it.
- Digital services B2C EU → OSS scheme mention, referral.
- Triangulations → do not DIY, professional referral with reasons.
