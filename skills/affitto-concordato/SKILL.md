---
name: affitto-concordato
description: Explain agreed-rent leases with tax discounts. Use when asked canone concordato, agreed rent Italy, cedolare concordato.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[city/contract]"
user-invocable: true
disable-model-invocation: false
---

# Canone Concordato

Agreed rents: lower rent bands, bigger tax cuts — both sides win when done right.

## When to use

- "canone concordato", "agreed rent Italy".
- Do not use for free-market leases (see `affitto-check`).

## Workflow

1. Check: high-tension municipality? Local agreement bands (fasce) for the zone.
2. Contract 3+2 at agreed rent + union asseverazione (attestazione) — mandatory step.
3. Tax perks: reduced cedolare rate + IRPEF/IMU discounts (year-stated).
4. Output: eligibility + steps + math vs free rent + union referral.

## Rules

- Zone bands are municipal: comune + agreement year cited, never generic rents.
- Asseverazione mandatory: no perks without it — stated bluntly.
- Percentages with year; verify current before signing.

## Examples

See `examples/concordato-cases.md`. Perks table in `references/vantaggi.md`.

## Edge cases

- Non-tension comune → concordato unavailable, say it + free-rent path.
- Existing free contract → conversion mechanics + timing, referral.
- Student contracts in university cities → dedicated sub-track flagged.
