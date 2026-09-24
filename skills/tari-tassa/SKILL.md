---
name: tari-tassa
description: Explain TARI waste tax with base and reductions. Use when asked TARI, tassa rifiuti, waste tax Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[municipality]"
user-invocable: true
disable-model-invocation: false
---

# TARI (Waste Tax)

Who pays, on what base, with which reductions — all municipal.

## When to use

- "TARI", "tassa rifiuti", "waste tax Italy".
- Do not use for IMU (see `imu-calcolo`).

## Workflow

1. Ask: municipality, property (sqm, use: home/business), occupants.
2. Base: sqm × rate (fixed + variable by occupants/use) — municipal tariff, year-stated.
3. Reductions: single occupant, seasonal, composting, out-of-town — check local regolamento.
4. Instalments per comune calendar + F24/pagoPA channels. Close with comune check.

## Rules

- Tariffs are municipal: comune + year always cited, never national numbers.
- Reductions must be requested (forms/deadlines) — state how, not just that they exist.
- Never compute without sqm + occupants + comune.

## Examples

See `examples/tari-cases.md`. Base logic in `references/base.md`.

## Edge cases

- Empty property → rules vary (some comuni charge anyway), flag + verify.
- Business premises → different class and rates, do not apply home math.
- Late payment → ravvedimento note + referral for messy arrears.
