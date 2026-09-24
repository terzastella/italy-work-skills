---
name: cedolare-secca
description: Compare flat rental tax vs IRPEF with break-even. Use when asked cedolare secca, flat rental tax Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[rent]"
user-invocable: true
disable-model-invocation: false
---

# Cedolare Secca

Flat rental tax math: 21%/26% vs IRPEF — break-even decides.

## When to use

- "cedolare secca", "flat rental tax Italy".
- Do not use for contract choice (see `affitto-check`, `affitto-concordato`).

## Workflow

1. Take annual rent + landlord marginal IRPEF rate (asked, not assumed).
2. Math: 21% flat (26% additional units, year-stated) vs IRPEF marginal + addizionali.
3. Option mechanics: where/when chosen (contract/extension/yearly), effects on increases (no ISTAT update under cedolare).
4. Output: both totals + winner + option steps.

## Rules

- Rates with year; second-unit 26% stated with year.
- Marginal rate asked: never assume 23/25/35/43%.
- Commercial use excluded: say it when relevant.

## Examples

See `examples/cedolare-cases.md`. Break-even table in `references/confronto.md`.

## Edge cases

- Concordato + cedolare → combined perks (see affitto-concordato), compute together.
- Mid-year switch → pro-rata logic + option timing, referral for edge months.
- Co-owners split → per-owner choice independence explained.
