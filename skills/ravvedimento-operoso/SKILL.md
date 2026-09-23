---
name: ravvedimento-operoso
description: Fix late tax payments with reduced penalties by timing. Use when asked ravvedimento operoso, late payment fix Italy, sanzioni ridotte.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[tax/delay]"
user-invocable: true
disable-model-invocation: false
---

# Ravvedimento Operoso

Pay late, pay less penalty: timing bands decide the surcharge.

## When to use

- "ravvedimento operoso", "late payment fix", "sanzioni ridotte".
- Do not use if accertamento already started (different track — flag it).

## Workflow

1. Check: spontaneous fix? No audit/notice started? If audit started → different path, referral.
2. Timing band → reduced penalty % (year-stated) + legal interest days.
3. F24 codes for tax + penalty + interest (separate lines).
4. Output: amount math + codes + deadline "pay now, each day costs".

## Rules

- Bands with year; percentages move — verify current.
- Interest computed per day; show the math.
- Never advise hiding: spontaneous + fast is the whole point.

## Examples

See `examples/ravvedimento-cases.md`. Bands in `references/fasce.md`.

## Edge cases

- Avviso bonario received → special definition paths may apply, flag + compare.
- Multiple years late → per-year bands, do not average.
- Already in installment plan → ravvedimento off the table, say it.
