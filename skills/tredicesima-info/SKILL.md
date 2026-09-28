---
name: tredicesima-info
description: Explain 13th salary with accrual and advances. Use when asked tredicesima, 13th salary Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Tredicesima

13th salary decoded: accrual, advances, who gets what.

## When to use

- "tredicesima", "13th salary Italy".
- Do not use for 14th month (separate CCNL benefit, flagged).

## Workflow

1. Accrual with the bundled script (preferred, reproducible): monthly twelfths on CCNL-cited pay items:
   `python skills/tredicesima-info/scripts/tredicesima.py --retribuzione 1800 --mesi 8`
2. Advances: December anticipation practices + employer policies vary — verify current-year rules (year-stated).
3. Exclusions: who does NOT accrue (some contracts/situations) — stated per case.
4. Output: accrual math + timing + CCNL check.

## Rules

- Items included vary by CCNL: cite contract, never generic lists as law.
- Part-time/pro-rata math shown plainly.
- Resigned mid-year: accrued share due — stated.

## Scripts

- `scripts/tredicesima.py` — accrual math (pay items are CCNL-cited inputs).
  Fixtures with expected outputs in `examples/fixtures/`.

## Examples

See `examples/tredicesima-cases.md`. Accrual logic in `references/ratei.md`.

## Edge cases

- 14a where due → separate benefit, do not merge.
- CIG months: accrual effects flagged generally.
- Forfettario/P.IVA: no tredicesima — stated to avoid confusion.
