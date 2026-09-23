---
name: collaborazioni-occasionali
description: Explain occasional work with limits and withholding. Use when asked prestazione occasionale, occasional work Italy, ritenuta occasionali.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Prestazioni Occasionali

Occasional work without VAT: limits, withholding, when VAT becomes mandatory.

## When to use

- "prestazione occasionale", "occasional work Italy".
- Do not use for continuous freelance (see `partita-iva-apri`).

## Workflow

1. Test: occasional, non-coordinated, non-continuous? If continuous → VAT track, flag strongly.
2. Rules: no VAT invoice (ricevuta with marca da bollo over threshold), 20% ritenuta, INPS Gestione Separata over yearly threshold (year-stated).
3. Libretto famiglia for small domestic gigs: alternative path explained.
4. Output: verdict (occasional ok / VAT needed) + documents + thresholds.

## Rules

- Habitual = VAT needed even under 5.000€: the key test, stated first.
- Thresholds with year (INPS franchise, bollo limit).
- Same client repeatedly → coordination red flag + referral.

## Examples

See `examples/occasionali-cases.md`. Thresholds in `references/soglie.md`.

## Edge cases

- Ex-employee occasional for ex-employer → forfettario-style continuity risk, flag.
- Occasional + employee job → cumulo INPS notes, referral.
- Online platforms gigs → each case tested against habituality, no blanket answers.
