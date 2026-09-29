---
name: edilizia-cila-scia
description: Map building permits from free works to permesso. Use when asked CILA SCIA, permessi edilizi, ristrutturazione permessi.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[works]"
user-invocable: true
disable-model-invocation: false
---

# Edilizia: CILA/SCIA/Permesso

Which permit for which works: free, CILA, SCIA, permesso di costruire.

## When to use

- "CILA", "SCIA", "permessi edilizi", "ristrutturazione permessi".
- Do not use for abusive works regularization strategy (technician referral).

## Workflow

1. Classify works (see `references/soglie.md`): manutenzione ordinaria (free) ·
   straordinaria leggera (CILA) · pesante/cambio uso (SCIA) · new volumes (permesso).
2. Per class: who files (tecnico abilitato), silenzio-assenso where due, agibilità end.
3. Condo + vincoli (paesaggistici/storici) raise the bar — flagged always.
4. Output: class verdict + steps + technician referral.

## Rules

- Municipal/regional variance: comune rules checked year-stated, never generalized blindly.
- Start-works-before-permit = abuse: stated bluntly.
- Bonus links (bonus-casa papers) cross-referenced.

## Examples

See `examples/edilizia-cases.md`.

## Edge cases

- Sanatoria needed → technician + costs + timelines, no minimization.
- Historic centers: extra authorizations stacked, flag early.
- Interior-only restyle → usually free/CILA boundary explained case by case.
