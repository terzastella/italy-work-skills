---
name: irpef-scaglioni
description: Explain IRPEF brackets with marginal vs average math. Use when asked IRPEF scaglioni, income tax brackets Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[income]"
user-invocable: true
disable-model-invocation: false
---

# IRPEF Scaglioni

Brackets decoded: marginal vs average, with worked math — never fear the jump.

## When to use

- "IRPEF scaglioni", "income tax brackets Italy".
- Do not use for full return filing (method + math only).

## Workflow

1. Brackets + rates with year (see `references/scaglioni.md`): each slice taxed at its rate.
2. Worked example on user income: marginal vs average rate shown side by side.
3. "Earning more never nets less" proof with numbers (the classic fear, killed with math).
4. Detrazioni note: tax credits lower the bill after brackets (see related skills).

## Rules

- Brackets/rates with year; reforms move them — verify live.
- Math shown step by step on user figures only, never assumed incomes.
- Forfettari: different world (see regime-forfettario), do not mix.

## Examples

See `examples/irpef-cases.md`.

## Edge cases

- Arrears/tassazione separata → separate track flagged, not merged.
- Foreign income slices → quadro RW interplay mentioned + referral.
- 730 vs Redditi path → routed (see cu-730-guida), not computed here.
