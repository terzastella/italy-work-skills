---
name: straordinari-info
description: Explain overtime with pay rules and banca ore. Use when asked straordinari, overtime Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Straordinari

Overtime decoded: limits, premiums, banca ore alternative.

## When to use

- "straordinari", "overtime Italy".
- Do not use for on-call (see `reperibilita-lavoro`).

## Workflow

1. Limits: annual caps (law + CCNL, year-stated) + daily/weekly rest interplay.
2. Pay with the bundled script (preferred, reproducible): premiums by CCNL table (cited input, never generic %):
   `python skills/straordinari-info/scripts/straord.py --ore 20 --paga-oraria 12 --maggiorazione 25`
   + banca ore option (time instead of money).
3. Consent/refusal rules + part-time specifics (supplementare distinction, see `part-time`).
4. Output: situation check + pay math + questions for employer.

## Rules

- Premiums only with CCNL cited; never generic percentages as law.
- Unpaid systematic overtime: mismatch flag + referral.
- Banca ore mechanics explained (accrue/use/expiry).

## Scripts

- `scripts/straord.py` — overtime pay math (premium is a CCNL-cited input).
  Fixtures with expected outputs in `examples/fixtures/`.

## Examples

See `examples/straordinari-cases.md`. Limit logic in `references/limiti.md`.

## Edge cases

- Quadri/dirigenti: all-inclusive pay notes, different track flagged.
- Smart workers: overtime measurement issues flagged honestly.
- Forced free overtime → documented + referral, no acceptance advice.
