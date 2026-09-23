---
name: ditta-vs-srl
description: Compare Italian business forms with costs and liability. Use when asked ditta individuale vs SRL, business form Italy, open company Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[activity/size]"
user-invocable: true
disable-model-invocation: false
---

# Ditta vs SRL (and Friends)

Choose the vehicle with eyes open: liability, costs, taxes, admin load.

## When to use

- "ditta individuale vs SRL", "business form Italy", "open company", "SRLS".
- Do not use for incorporation filing (information + comparison only).

## Workflow

1. Ask: activity, solo/team, expected revenue, risk level, growth plans.
2. Compare (see `references/forme.md`): ditta individuale, SRL ordinaria, SRLS,
   SAS/SNC briefly — liability, setup/running costs, accounting, INPS track.
3. Recommend a shortlist (2 max) with reasons + accountant/notary referral.
4. Forfettario compatibility note per form (see regime-forfettario).

## Rules

- Liability differences stated plainly (unlimited vs limited, with standard caveats).
- Costs as ranges with year, never exact promises.
- No "open it tomorrow" pushes on SRLs: notary + capital realities stated.

## Examples

See `examples/forme-cases.md`.

## Edge cases

- Freelancer with employees coming → ditta limits flagged early.
- Foreign founder → fiscal residence + visa issues flagged, referral.
- Innovative startup variant → dedicated incentives mentioned, specialist referral.
