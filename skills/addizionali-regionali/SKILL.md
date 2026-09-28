---
name: addizionali-regionali
description: Explain regional and municipal surcharges with where-paid logic. Use when asked addizionali, regional surcharge Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.4", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[residence]"
user-invocable: true
disable-model-invocation: false
---

# Addizionali Regionali e Comunali

Surcharges mapped: who sets them, where you pay, advance vs balance.

## When to use

- "addizionali", "regional surcharge Italy", "addizionale comunale".
- Do not use for IRPEF brackets (see `irpef-scaglioni`).

## Workflow

1. Two layers: regionale (residence region rate, year-stated) + comunale (residence comune, acconto/saldo split).
2. Residence rule: 1st January domicile decides the year — stated first.
3. Withholding vs return: employer withholds, return settles differences.
4. Output: situation math + rates with year + region/comune check.

## Rules

- Rates per region/comune + year; never national figures as law.
- Moved mid-year: 1st-January rule applied, edge months explained.
- Exemption bands (some regions) flagged where due, verified live.

## Examples

See `examples/addizionali-cases.md`. Rate logic in `references/aliquote.md`.

## Edge cases

- AIRE abroad → generally out, flag + verify case.
- Two homes, one residenza → residenza decides, second home irrelevant here.
- Arrears years → old rates per year, no blending.
