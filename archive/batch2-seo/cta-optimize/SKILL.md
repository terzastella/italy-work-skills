---
name: cta-optimize
description: Improve calls-to-action with verbs, proof and A/B tests. Use when asked improve CTA, call to action, button conversion.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[page/text]"
user-invocable: true
disable-model-invocation: false
---

# CTA Optimize

Buttons people press: verb + benefit + proof, then A/B test.

## When to use

- "improve CTA", "call to action", "button conversion", "A/B test".
- Do not use for whole landings (see `landing-copy`).

## Workflow

1. Analyze current CTA: verb, benefit, friction (what it asks in return).
2. Propose 3 variants: direct, benefit, proof (format below).
3. Per variant: where to place it + what to measure (clicks, not "engagement").
4. Mini A/B plan: minimum traffic, duration, winner = 1 metric.

## Output format

```text
Current: <text> — problem: <vague/no benefit/too much ask>
A (direct): <text>
B (benefit): <text>
C (proof): <text with real number>
Test: 50/50 for 2 weeks, metric: CTA clicks
```

## Rules

- Imperative verb + object ("Book the check", not "Submit").
- Benefit or proof always: never a bare "Click here" button.
- Numbers only real/provided. Friction declared ("free, 2 minutes").

## Examples

See `examples/cta-cases.md`. Strong verbs in `references/verbs.md`.

## Edge cases

- Low traffic → no A/B (won't converge): pick B and compare before/after.
- Multiple CTAs on page → one primary, rest secondary text links.
- Deceptive CTA requested ("free" when paid) → refuse, propose honest one.
