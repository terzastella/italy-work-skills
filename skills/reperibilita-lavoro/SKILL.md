---
name: reperibilita-lavoro
description: Explain on-call rules with pay and refusal rights. Use when asked reperibilità, on-call Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Reperibilità (On-Call)

On-call decoded: pay, limits, refusal — by contract, not by habit.

## When to use

- "reperibilità", "on-call Italy".
- Do not use for overtime (see `straordinari-info`).

## Workflow

1. Contract basis: CCNL/company agreement must provide it — no agreement, no duty (stated).
2. Pay: indennità tables (year-stated, by CCNL) + call-out pay when activated.
3. Limits: rest rules, max turns, refusal rights and consequences.
4. Output: situation check + pay math + questions for employer.

## Rules

- Contract-cited figures only; never generic on-call pay as law.
- Activated call = work time: stated plainly.
- Health/safety overrides: rest rules are hard limits, flagged.

## Examples

See `examples/reperibilita-cases.md`. Pay logic in `references/indennita.md`.

## Edge cases

- Informal "always available" pressure → agreement required, referral.
- Smart-worker on-call → disconnection interplay flagged (see smart-working).
- Refusal punished → retaliation patterns + referral, documented everything.
