---
name: naspi-guida
description: Explain NASpI unemployment benefit requirements and math. Use when asked NASpI, disoccupazione, unemployment benefit Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# NASpI Guide

Unemployment benefit without myths: who gets it, how much, how long, how to ask.
Flagship skill: gates table, amount method with circular values, duties while receiving.

## When to use

- "NASpI", "disoccupazione", "unemployment benefit Italy".
- Do not use for appeals or disputes (patronato/lawyer referral).

## Workflow (tappe with formal in/out)

### Tappa 1 — Gate check (pass/fail each, from user data)

Involuntary termination? (voluntary quit excluded — say it first when relevant;
just-cause excepted, evidence-heavy.) Contribution weeks? Type covered?
See `references/requisiti.md`. One failed gate → stop with the reason, no math.

### Tappa 2 — Amount method (INPS computes, we map)

Reference salary → % brackets → monthly cap (year-stated, INPS circular cited)
→ duration = half the contribution weeks of the last 4 years.
No script by design: brackets and caps live in circulars, not here.
Show the formula with the user's salary plugged as variables, never invented values.

### Tappa 3 — File it

INPS online (SPID/CIE) or patronato; documents list; deadline runs from
termination — file promptly. DID registration in parallel.

### Tappa 4 — While receiving

DID, servizio/personalized pact, suitable job offers regime, communications
duty (new work, address, availability). Work-while-on-NASpI compatibility
rules + communications, explained simply.

## Multi-turn protocol

Turn 1 (gates): termination type + weeks — pass/fail table.
Turn 2 (amount): method with circular values, INPS computes.
Turn 3 (file + duties): documents, deadline, obligations. Never promise approval, any turn.

## Rules

- Voluntary resignation = no NASpI (say it first when relevant).
- Amounts/duration with year; INPS circulars change details.
- Never promise approval: INPS decides on records.
- Seasonal workers: recall + NASpI chain (see `stagionali-turismo`).

## Examples

Good and bad cases in `examples/naspi-cases.md`. Gates in `references/requisiti.md`.
Duties detail in `references/durante.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Voluntary quit | excluded — say first, just-cause exception + lawyer |
| 2 | Fixed-term expiry | eligible (involuntary end), explain |
| 3 | Seasonal gaps | recall + NASpI chain (see `stagionali-turismo`) |
| 4 | Just-cause resignation | eligible path, evidence-heavy, professional referral |
| 5 | Work while on NASpI | compatibility + communications duty, simply |
| 6 | DIS-COLL confusion | boundary stated: NASpI does not apply (see dedicated track) |
