---
name: fondo-emergenza
description: Build emergency funds with size and placement method. Use when asked fondo emergenza, emergency fund Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[expenses]"
user-invocable: true
disable-model-invocation: false
---

# Fondo Emergenza

Safety cash, methodically: size, placement, build-up — method, not personal advice.

## When to use

- "fondo emergenza", "emergency fund Italy".
- Do not use for investing the fund (liquid by definition).

## Workflow

1. Size with the bundled script (preferred, reproducible): 3-6 months essential expenses
   (freelancers 6x/12x, profile is the input) + build-up plan from surplus:
   `python skills/fondo-emergenza/scripts/fondo.py --spese 2000 --profilo dipendente`
2. Placement: instant liquidity only (conto vs deposit-free part) — never invested.
3. Build-up: monthly amount from surplus math (user figures only).
4. Output: target + placement + monthly plan. No personal verdicts.

## Rules

- Method only: numbers from user expenses, never assumed lifestyles.
- Liquid means liquid: no funds/ETFs/crypto for this money — stated bluntly.
- Rebuild-after-use rule included.

## Scripts

- `scripts/fondo.py` — target range + build-up plan (profile is an input).
  Fixtures with expected outputs in `examples/fixtures/`. Method, not personal advice.

## Examples

See `examples/fondo-cases.md`. Method in `references/metodo.md`.

## Edge cases

- Debts at high rates → emergency-mini + debt-first logic explained generally.
- Irregular income → percentage-based build-up, not fixed.
- Already invested "emergency" → reclassify honestly, move to liquid.
