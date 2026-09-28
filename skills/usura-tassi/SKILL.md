---
name: usura-tassi
description: Explain usury thresholds with verification paths. Use when asked usura, tassi soglia, usury Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[loan]"
user-invocable: true
disable-model-invocation: false
---

# Usura e Tassi Soglia

Rate legality checked: Bank of Italy thresholds, TAEG verification, victim paths.

## When to use

- "usura", "tassi soglia", "usury Italy".
- Do not use for legal action strategy (specialist referral).

## Workflow

1. Thresholds: Banca d'Italia quarterly tables by loan class (year-stated quarter).
2. TAEG recomputation: all costs in (fees, insurance tied) — the classic dodge.
3. Over-threshold: criminal matter + contract consequences overview, referral now.
4. Sovraindebitamento (L.3): composition paths named + OCC referral.

## Rules

- Tables with quarter + year; never generic thresholds as law.
- Tied insurance/fees counted in TAEG: stated as the check that matters.
- Victim tone: protection paths first, no shame framing.

## Examples

See `examples/usura-cases.md`. Threshold logic in `references/soglie.md`.

## Edge cases

- Loan sharks (non-bank) → criminal track + denuncia paths, urgent tone.
- Old loans: threshold at signing time applies — historical tables noted.
- Business loans: different classes flagged, not mixed.
