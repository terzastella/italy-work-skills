---
name: conti-deposito
description: Compare deposit accounts with net rates and guarantee. Use when asked conto deposito, deposit account Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[amount/horizon]"
user-invocable: true
disable-model-invocation: false
---

# Conti Deposito

Parked cash compared: tied vs free, gross vs net, guarantee cap.

## When to use

- "conto deposito", "deposit account Italy".
- Do not use for investment advice.

## Workflow

1. Types: free (svincolabile) vs tied (vincolato) with early-exit penalties.
2. Net math: gross rate − 26% withholding (year-stated) − stamp duty (year-stated).
3. Guarantee: FITD 100k per bank — split above it, stated plainly.
4. Output: net comparison + penalty check + questions for the bank.

## Rules

- Net, never gross, as verdict number.
- Promo rates: duration + post-promo rate checked (the classic trap).
- No bank endorsement; no investment pushes.

## Scripts

- `scripts/deposito.py` — net math (rate and duty are inputs).
  Fixtures with expected outputs in `examples/fixtures/`. Net as verdict, never gross.

## Examples

See `examples/deposito-cases.md`. Net math in `references/netto.md`.

## Edge cases

- Foreign online banks: FITD-equivalent schemes flagged, verify.
- Joint accounts: guarantee per depositor logic explained.
- Inflation vs return: honest framing, no fear tactics.
