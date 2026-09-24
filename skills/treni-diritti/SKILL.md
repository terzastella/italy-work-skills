---
name: treni-diritti
description: Explain train delay refunds with bands. Use when asked treno ritardo, train refund Italy, Trenitalia rimborso.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[trip]"
user-invocable: true
disable-model-invocation: false
---

# Treni Diritti

Late trains pay back: bands, bonus vs cash, claim paths.

## When to use

- "treno ritardo", "train refund Italy", "Trenitalia rimborso".
- Do not use for flights (see `voli-ritardi`).

## Workflow

1. Delay at arrival: 60-119 min vs 120+ min bands (year-stated) → 25%/50% of ticket.
2. Bonus vs cash choice where offered; claim channels (app/counter/online).
3. Cancellation/suppression: full refund or rerouting rights.
4. Output: band math + claim steps.

## Rules

- Bands with year; regional vs AV nuances flagged.
- Strike days: guarantee bands (fasce garantite) noted, claims differ.
- Season tickets: separate compensation logic, flagged.

## Examples

See `examples/treni-cases.md`. Bands in `references/fasce.md`.

## Edge cases

- Missed connection (same ticket) → arrival-delay logic on final destination.
- Strike with guarantees → check fascia first, then claim path.
- International legs → carrier split rules flagged.
