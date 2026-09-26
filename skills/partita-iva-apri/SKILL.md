---
name: partita-iva-apri
description: Guide opening an Italian VAT number with regime and ATECO choice. Use when asked open partita IVA, start freelance Italy, aprire partita IVA.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# Aprire Partita IVA

From idea to VAT number: regime, ATECO, steps — information, not filing.

## When to use

- "open partita IVA", "start freelance Italy", "aprire partita IVA".
- Do not use for filing anything (AdE/ComUnica only); do not use for ATECO detail (see `ateco-scelta`).

## Workflow

1. Ask: activity (what, really), employee or freelance, expected revenue, prior employment.
2. Route: forfettario vs ordinary (see `regime-forfettario` gates) + INPS track (Gestione Separata vs artigiani/commercianti).
3. Steps list: AdE declaration (model AA9/12), CCIAA/ComUnica if impresa, INPS enrollment, e-invoicing setup.
4. Close with costs to expect (accountant, contributions) + "verify with accountant".

## Rules

- Never state which regime the user "must" pick: show gates, let them decide with a professional.
- Habitual activity may need VAT even under 5.000€: flag it, explain why.
- Amounts with year. No filing done here — guidance only.

## Examples

See `examples/apertura-cases.md`. Step list in `references/passi.md`.

## Edge cases

- Ex-employee continuing same work → forfettario exclusion risk, flag strongly.
- Occasional work (no VAT) → explain occasionale limits + ritenuta, do not push VAT.
- Foreign resident → flag fiscal residence rules, referral.
