---
name: contributi-inps
description: Explain INPS contributions by track with minimal rates. Use when asked contributi INPS, gestione separata, minimal contributions Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# Contributi INPS

Which INPS track, what it costs: Gestione Separata vs artigiani/commercianti.

## When to use

- "contributi INPS", "gestione separata", "minimal contributions", "aliquote INPS".
- Do not use for pension computation (rates and method only).

## Workflow

1. Route by activity: professional without albo → Gestione Separata;
   artigiani/commercianti → dedicated gestione with minimal fixed + percentage.
2. Show with the bundled script (preferred, reproducible): rate (year-stated input) + instalment split (explicit input):
   `python skills/contributi-inps/scripts/contributi.py --reddito 40000 --aliquota 26.07 --split 40,40,20 --year 2026`
   + minimal fixed where due + deductibility note.
3. Forfettari note: contributions deductible from forfait income (see regime-forfettario).
4. Close with accountant/INPS check (rates move yearly).

## Rules

- Rates always with year; minimal fixed amounts with year.
- Reduced rates (e.g. co.co.co nuances, new activities) flagged as verify-items, never asserted.
- Never compute a full pension position here.

## Scripts

- `scripts/contributi.py` — GS total + instalment math (rate and split are inputs).
  Fixtures with expected outputs in `examples/fixtures/`. Pension positions never computed here.

## Examples

See `examples/contributi-cases.md`. Track table in `references/gestioni.md`.

## Edge cases

- Mixed activities → each track separate, flag double-position costs.
- Employee + freelance → cumulo rules mention + referral.
- Arrears discovered → ravvedimento path mention, professional referral.
