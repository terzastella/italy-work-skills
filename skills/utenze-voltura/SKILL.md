---
name: utenze-voltura
description: Guide utility takeover vs new connection with costs. Use when asked voltura utenze, subentro luce gas, new connection Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[move]"
user-invocable: true
disable-model-invocation: false
---

# Utenze: Voltura e Subentro

Take over utilities without gaps: voltura vs subentro vs allaccio, costs, timing.

## When to use

- "voltura utenze", "subentro luce/gas", "new connection Italy".
- Do not use for offer comparison (see `bollette-energia`).

## Workflow

1. Case: active supply (voltura: change holder) · closed supply (subentro: reopen) ·
   never connected (allaccio: works + costs).
2. Documents: ID, fiscal code, POD/PDR, address, (voltura: prior holder data if available).
3. Costs/timing ranges per case + deposit (deposito cauzionale) notes.
4. Output: path + documents + timing + cost estimate.

## Rules

- Debts of prior holder: voltura does NOT transfer them (state it); subentro clean start.
- Allaccio costs vary wildly by works needed: ranges + distributor quote, never fixed promises.
- Morosità pregresse on POD: flag + verify before subentro.

## Examples

See `examples/utenze-cases.md`. Case table in `references/casi.md`.

## Edge cases

- Rented home: tenant does voltura, landlord cooperation note.
- Deceased holder: heir voltura path with documents, flag + sensitivity.
- Urgent move-in: temporary solutions + realistic timings, no miracles.
