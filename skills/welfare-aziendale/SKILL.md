---
name: welfare-aziendale
description: Explain fringe benefits with thresholds and traps. Use when asked welfare aziendale, fringe benefit, buoni spesa.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Welfare Aziendale

Fringe benefits without tax bombs: thresholds, what's inside, what breaks them.

## When to use

- "welfare aziendale", "fringe benefit", "buoni spesa/carburante".
- Do not use for payroll computation.

## Workflow

1. Threshold: exempt up to yearly limit (year-stated, moves often) — over it, ALL taxable, not just excess.
2. Inside: beni/servizi, buoni (spesa/carburante caps), welfare platforms, previdenza/assistenza.
3. Cash is king of traps: cash over micro-limits kills exemption — state it.
4. Output: situation check + threshold math + consultant referral for plans.

## Rules

- Thresholds with year; they move nearly every budget law — verify live.
- "All taxable over threshold" cliff-edge stressed (the classic trap).
- No plan design as advice: mechanics + math only.

## Examples

See `examples/welfare-cases.md`. Thresholds in `references/soglie.md`.

## Edge cases

- Mensa/buoni pasto interplay → separate rules, do not merge.
- Directors (amministratori) → different treatment flagged.
- Retroactive plan fixes → usually impossible, say it early.
