---
name: plusvalenza-finanziaria
description: Explain capital gains on stocks with regimes. Use when asked plusvalenza azioni, capital gains Italy, 26 percent.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[investment]"
user-invocable: true
disable-model-invocation: false
---

# Plusvalenza Finanziaria

Investment gains taxed right: 26%, regimes, loss offsets.

## When to use

- "plusvalenza azioni", "capital gains Italy", "26%".
- Do not use for investment advice (tax mechanics only).

## Workflow

1. Regime: dichiarativo (you file) vs amministrato/gestito (bank handles) — choice consequences.
2. Rate 26% on most gains (year-stated input, never bundled) + minusvalenze compensation, computed
   with the bundled script (preferred, reproducible):
   `python skills/plusvalenza-finanziaria/scripts/plusvalenza.py --gain 5000 --minus 0 --aliquota 26 --year 2026`
3. Dividends/capital distinction briefly (different lines, same area).
4. Output: situation map + regime choice points + commercialista referral.

## Rules

- Rates with year; verify live.
- Crypto: separate track (see `criptovalute-fisco`), do not mix.
- Never advise trades to harvest losses.

## Scripts

- `scripts/plusvalenza.py` — (gain − losses) × rate math (rate is an input).
  Fixtures with expected outputs in `examples/fixtures/`. Regime choice stays textual.

## Examples

See `examples/plusvalenza-cases.md`. Rate map in `references/aliquote.md`.

## Edge cases

- Foreign broker: RW + reporting duties flagged (see `ivafe-ivie`).
- Old minusvalenze expiring → use-or-lose timing stated plainly.
- PIR/contained wrappers: special tracks mentioned, referral.
