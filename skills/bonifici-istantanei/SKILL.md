---
name: bonifici-istantanei
description: Explain instant transfers with costs and errors. Use when asked bonifico istantaneo, instant transfer Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Bonifici Istantanei

Seconds, not days: instant vs ordinary, costs, wrong-IBAN recovery.

## When to use

- "bonifico istantaneo", "instant transfer Italy".
- Do not use for scams already happened without urgency (see below).

## Workflow

1. Instant vs ordinary: seconds 24/7 vs cut-off times; fees compared (instant often costs).
2. Wrong IBAN: recall (richiamo fondi) path + timelines + beneficiary-bank cooperation.
3. Scam received-funds ("refund this overpayment"): classic pattern, refuse + report.
4. Output: choice logic + error paths.

## Rules

- Verify-beneficiary services where offered: use them, stated as habit.
- Instant = irrevocable in practice: think-first rule stressed.
- No bank endorsement.

## Examples

See `examples/bonifici-cases.md`. Timing/fees in `references/tempi.md`.

## Edge cases

- Authorized-push-payment fraud → bank + denuncia immediately, urgent tone.
- Salary/rent via instant monthly → cost math vs ordinary shown plainly.
- Cross-border instant: availability limits flagged.
