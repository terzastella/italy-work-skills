---
name: assegno-unico
description: Explain assegno unico with ISEE bands and application. Use when asked assegno unico, family allowance Italy, bonus bebè.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[household]"
user-invocable: true
disable-model-invocation: false
---

# Assegno Unico

Family allowance mapped: who gets it, how ISEE sets it, how to apply.

## When to use

- "assegno unico", "family allowance Italy", "bonus bebè".
- Do not use for exact entitlement without the current INPS circular (lookup + verify).

## Workflow

1. Who: dependent children (age/study/disability rules, year-stated).
2. ISEE link: look up the monthly amount in the dated band table (preferred, reproducible):
   `python skills/assegno-unico/scripts/fasce.py --isee 25000 --minori 2 --tabella skills/assegno-unico/examples/importi-2025.json --year 2025`
   Tables move yearly — the script refuses mismatched table/request years.
3. Apply: INPS online/patronato + DSU link (see `isee-guida`) + timing (arrears rules).
4. Output: eligibility check + amount range + application steps.

## Rules

- Amounts with year; tables move — verify current INPS circular.
- No-DSU = minimum: state it (the classic loss).
- Separated parents/shared custody: split rules flagged, not assumed.

## Scripts

- `scripts/fasce.py` — band lookup from a dated table (tables are inputs, never bundled truth).
  Dated tables in `examples/importi-YYYY.json`, fixtures in `examples/fixtures/`.

## Examples

See `examples/assegno-cases.md`. Band logic in `references/fasce.md`.

## Edge cases

- Late application → arrears limits stated plainly.
- Disabled children → higher bands + extra rules, flag + patronato.
- ISEE expired mid-year → renewal timing to avoid minimums.
