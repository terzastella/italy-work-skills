---
name: spese-mediche-detrazioni
description: Explain medical expense deductions with documents. Use when asked spese mediche detrazione, 19 percent health, scontrini farmacia.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[expenses]"
user-invocable: true
disable-model-invocation: false
---

# Spese Mediche Detrazioni

19% back on health costs: what counts, which papers, how to declare.

## When to use

- "spese mediche detrazione", "19% health", "scontrini farmacia".
- Do not use for full return filing (method + papers only).

## Workflow

1. Eligible: visits, exams, drugs (parlante receipts with fiscal code), devices — see `references/ammissibili.md`.
2. Papers: scontrini parlanti, fatture, quietanze; tracciabilità rules for the deduction.
3. Franchise (franchigia) math + 19% on the excess — shown, not just stated.
4. Output: eligible list + papers checklist + declaration line pointer.

## Rules

- Non-prescription cosmetics/parapharmacy generally out: say it.
- Tracciabilità: which payments need traceable means (year-stated).
- Veterinarian crossover: separate track flagged, not merged.

## Examples

See `examples/mediche-cases.md`.

## Edge cases

- Lost receipts → pharmacy ristampa path, not estimates.
- Family expenses → whose fiscal code on paper decides deductibility.
- Disabled persons' vehicles/aids: higher deductions flagged + referral.
