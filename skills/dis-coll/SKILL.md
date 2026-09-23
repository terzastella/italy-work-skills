---
name: dis-coll
description: Explain DIS-COLL benefit for collaborators with math. Use when asked DIS-COLL, disoccupazione collaboratori Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# DIS-COLL

Unemployment benefit for co.co.co/dottorandi: requirements, math, application.

## When to use

- "DIS-COLL", "disoccupazione collaboratori".
- Do not use for NASpI (see `naspi-guida`).

## Workflow

1. Requirements: contribution months minimum (year-stated), involuntary end, exclusivity notes.
2. Math: reference income → % → monthly cap (year-stated) → duration rule.
3. Apply: INPS online/patronato + documents + timing.
4. Output: eligibility check + amount range + steps. No approval promises.

## Rules

- Distinct from NASpI: state differences first (who, how much, how long).
- Amounts/duration with year; INPS decides on records.
- PhD/borsisti tracks: separate rules flagged, referral.

## Examples

See `examples/discoll-cases.md`. Gates in `references/requisiti.md`.

## Edge cases

- Mixed co.co.co + employee periods → which benefit applies, INPS verification.
- New contract signed → decadenza rules stated plainly.
- Pensioners with co.co.co → exclusion noted.
