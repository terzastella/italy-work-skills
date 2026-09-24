---
name: orario-riposi
description: Explain work hours with daily and weekly rest. Use when asked orario lavoro, riposi settimanali Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Orario e Riposi

Hours with hard limits: 48h average, 11h daily rest, 24h weekly rest.

## When to use

- "orario lavoro", "riposi settimanali Italy".
- Do not use for overtime pay (see `straordinari-info`).

## Workflow

1. Limits: 48h weekly average (reference period) · 11h consecutive daily rest ·
   24h weekly rest (usually Sunday + daily share).
2. Night work: definition + limits + health checks where due.
3. Derogations by CCNL/agreement: where flexibility lives.
4. Output: situation check + violated-rule flags + referral.

## Rules

- Averages over reference periods: single-week spikes read correctly.
- Rest is a right, not a favor: systematic violations flagged + referral.
- Dirigenti: separate track, do not generalize.

## Examples

See `examples/orario-cases.md`. Limit table in `references/limiti.md`.

## Edge cases

- Multi-job total hours → summed across employers, flag + referral.
- On-call counted as work when activated (see `reperibilita-lavoro`).
- Smart workers: right-to-disconnect interplay flagged.
