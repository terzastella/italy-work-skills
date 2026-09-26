---
name: bollette-energia
description: Read Italian energy bills and compare offers. Use when asked bolletta luce gas, read bill, energy offer Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[bill data]"
user-invocable: true
disable-model-invocation: false
---

# Bollette Energia

Bills decoded: fixed vs variable, kWh/Smc math, offer comparison that holds.

## When to use

- "bolletta luce/gas", "read bill", "energy offer", "cambio fornitore".
- Do not use for switching contracts (comparison only).

## Workflow

1. Take bill data: POD/PDR, kWh/Smc, price components (materia energia, trasporto, oneri, IVA/accise).
2. Recompute total from components; flag anomalies vs typical household.
3. Offer comparison: same annual consumption on both, total-year math, fixed fees included.
4. Output: verdict + yearly saving estimate + "verify on ARERA comparator" (offers year-stated).

## Rules

- Compare total yearly cost, never just €/kWh headline.
- Free-market vs tutelato notes where relevant (rules change — verify year).
- No provider endorsement: math only.

## Examples

See `examples/bollette-cases.md`. Bill anatomy in `references/anatomia.md`.

## Edge cases

- Conguaglio shock → estimated vs actual reads, rateizzazione mention.
- Second home rates → different tariff class, flag it.
- Bonus sociale → eligibility note (ISEE link), do not compute it.
