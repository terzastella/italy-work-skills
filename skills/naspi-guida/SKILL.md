---
name: naspi-guida
description: Explain NASpI unemployment benefit requirements and math. Use when asked NASpI, disoccupazione, unemployment benefit Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# NASpI Guide

Unemployment benefit without myths: who gets it, how much, how long, how to ask.

## When to use

- "NASpI", "disoccupazione", "unemployment benefit Italy".
- Do not use for appeals or disputes (patronato/lawyer referral).

## Workflow

1. Requirements check: involuntary termination (voluntary quit excluded, just-cause excepted),
   contribution weeks,Declaratory: state each gate pass/fail from user data.
2. Math: reference salary → % brackets → monthly cap (current values with year) → duration rule.
3. How to apply: INPS online (SPID/CIE) or patronato; documents list.
4. Obligations while receiving: DID, servizio pact, suitable job offers, mandatory communications.

## Rules

- Voluntary resignation = no NASpI (say it first when relevant).
- Amounts/duration with year; INPS circulars change details.
- Never promise approval: INPS decides on records.

## Examples

See `examples/naspi-cases.md`. Gates in `references/requisiti.md`.

## Edge cases

- Fixed-term expiry → eligible (involuntary end), explain.
- Just-cause resignation → eligible path but evidence-heavy, professional referral.
- Work while on NASpI → compatibility rules + обязат? No — communications duty, explain simply.
