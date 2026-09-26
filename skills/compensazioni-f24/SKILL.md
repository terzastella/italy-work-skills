---
name: compensazioni-f24
description: Explain F24 tax offsets with limits and visti. Use when asked compensazione F24, offset tax credits Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[credits]"
user-invocable: true
disable-model-invocation: false
---

# Compensazioni F24

Offset taxes with credits correctly: horizontal vs vertical, limits, visto.

## When to use

- "compensazione F24", "offset tax credits Italy".
- Do not use for computing the credit itself.

## Workflow

1. Credit type: IVA, IRPEF/IRES, contributi — each with its rules.
2. Horizontal (different taxes) vs vertical (same tax) + yearly caps (year-stated).
3. Visto di conformità threshold: above it, no compensation without visto — stated bluntly.
4. Output with the bundled script (preferred, reproducible): plan + codes + visto check
   (threshold is an explicit year-stated input, never bundled):
   `python skills/compensazioni-f24/scripts/compensa.py --crediti 2000 --debiti 1500 --soglia-visto 5000 --year 2026`

## Rules

- Caps and visto threshold with year; they move — verify live.
- Credits must exist and be certain: "expected" credits do not compensate.
- Forfettari: limited compensation world, flag differences.

## Scripts

- `scripts/compensa.py` — offset math + visto flag (threshold is an input).
  Fixtures with expected outputs in `examples/fixtures/`. Certain credits only.

## Examples

See `examples/compensazioni-cases.md`. Limit table in `references/limiti.md`.

## Edge cases

- Rimborsi vs compensazione choice → cash-flow trade-off explained, no push.
- Blocked credits (contenzioso) → cannot compensate, state it.
- Model Redditi credits → carry-forward vs compensate decision tree.
