---
name: voli-ritardi
description: Claim EU261 flight compensation with bands and letters. Use when asked volo ritardo, flight delay compensation, EU261 Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[flight]"
user-invocable: true
disable-model-invocation: false
---

# Voli Ritardi (EU261)

Delayed flight money: bands, exceptions, claim letter that works.

## When to use

- "volo ritardo", "flight delay compensation", "EU261", "cancellazione volo".
- Do not use for travel insurance claims (separate).

## Workflow

1. Check scope: EU departure OR EU carrier arrival; delay at arrival (3h+), cancellation, denied boarding.
2. Extraordinary circumstances test (weather/ATC vs technical — airline-proven, not claimed).
3. Band math: ≤1500km €250 · 1500-3500km €400 · >3500km €600 (verify current).
4. Output: eligibility verdict + claim letter draft + evidence list (boarding, receipts).

## Rules

- Bands with year; amounts fixed by regulation but cite it.
- Extraordinary circumstances: airline must prove — state the burden rule.
- No claim-fee services pushed: DIY letter first.

## Examples

See `examples/voli-cases.md`. Bands in `references/fasce.md`.

## Edge cases

- Airline voucher offered → cash right stated; voucher only if wanted.
- Connecting flights → delay measured at final destination.
- Non-EU carrier, non-EU departure → out of scope, say it + Montreal hint.
