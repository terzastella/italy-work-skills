---
name: successioni-info
description: Explain Italian inheritance with allowances and deadlines. Use when asked successione, eredità, inheritance Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Successioni (Info Only)

Inheritance mapped: declaration, allowances, rates — information, notary decides.
Flagship delicate skill: debts-first order, allowance map, volture chain.

## When to use

- "successione", "eredità", "inheritance Italy".
- Do not use for legal advice or disputes (notary/lawyer referral).

## Workflow (tappe with formal in/out)

### Tappa 0 — Debts before assets (always first)

See `eredita-debiti`: accept/renounce mechanics. Touch nothing before deciding.
This tappa is never skipped, even when the user asks only about taxes.

### Tappa 1 — Timeline

Dichiarazione di successione within 12 months (filing path: AdE online/professional).
Missed deadline → ravvedimento path + sanctions note, professional now.

### Tappa 2 — Allowance map

Allowances by degree, year-stated (see `references/franchigie.md`): spouse/children
high, siblings lower, others minimal. Rates above allowance + prima-casa perks
for heirs (conditions). Method + ranges: no "you owe X" verdicts, ever.

### Tappa 3 — After filing

Volture (catasto) after filing (see `volture-catastali`). Will exists →
pubblicazione + legitima shares flagged, notary owns it. Close with notary referral.

## Multi-turn protocol

Turn 0 (debts): accept/renounce mechanics first. Turn 1 (timeline + map):
deadline + allowances. Turn 2 (after): volture + will + close. Notary referral
closes every turn.

## Rules

- Allowances/rates with year; never timeless figures.
- No "you owe X" verdicts: method + ranges, notary computes.
- Debts of the deceased: accettazione con beneficio d'inventario mentioned, never DIY.
- Foreign assets/heirs: cross-border layer, specialist referral.

## Examples

Good and bad cases in `examples/successioni-cases.md`.
Allowance logic in `references/franchigie.md`. Debts-first in `references/debiti-prima.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Possible debts | tappa 0 first, touch nothing |
| 2 | Missed 12 months | ravvedimento + sanctions + professional now |
| 3 | Will exists | pubblicazione + legitima flagged, notary owns |
| 4 | Foreign assets/heirs | cross-border layer + specialist referral |
| 5 | Minor heirs | court paths flagged + extra care |
