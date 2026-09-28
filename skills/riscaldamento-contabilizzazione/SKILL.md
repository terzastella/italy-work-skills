---
name: riscaldamento-contabilizzazione
description: Explain heat metering splits with millesimi. Use when asked riscaldamento contabilizzazione, heat metering Italy, spese riscaldamento.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[bill]"
user-invocable: true
disable-model-invocation: false
---

# Riscaldamento Contabilizzazione

Heat bills split fairly: fixed vs variable shares, meter readings, disputes.

## When to use

- "riscaldamento contabilizzazione", "heat metering Italy", "spese riscaldamento".
- Do not use for plant works (technician matter).

## Workflow

1. System: centralized with meters/ripartitori vs millesimi-only (old plants flagged).
2. Split logic: fixed share (millesimi) + variable share (readings) — standard model explained.
3. Check a bill: readings vs estimate, season coherence, previous balances.
4. Output: split math + anomaly flags + administrator questions.

## Rules

- Metering obligation noted (where due, year-stated) with old-plant exceptions.
- Estimates vs readings: conguaglio logic explained plainly.
- No plant advice: accounting only.

## Examples

See `examples/riscaldamento-cases.md`. Split model in `references/riparto.md`.

## Edge cases

- Detached unit (distacco) → fixed-share duty usually remains, flag + verify regolamento.
- Broken meter → estimated period rules + replacement duty stated.
- Disputed season bill → readings history requested first, then contest path.
