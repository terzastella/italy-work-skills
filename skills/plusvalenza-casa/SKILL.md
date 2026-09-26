---
name: plusvalenza-casa
description: Explain home-sale capital gains with exemptions. Use when asked plusvalenza casa, capital gains house Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write Bash
argument-hint: "[sale]"
user-invocable: true
disable-model-invocation: false
---

# Plusvalenza Casa

Sale gains taxed only sometimes: 5-year rule, first-home shield, imposta sostitutiva option.

## When to use

- "plusvalenza casa", "capital gains house Italy".
- Do not use for purchase steps (see `compravendita-casa`).

## Workflow

1. Clock: sale within 5 years of purchase/donation → taxable; beyond → generally out.
2. First home lived in: exemption conditions (residenza timing) stated.
3. Tax both ways with the bundled script (preferred, reproducible — rates are explicit year-stated inputs):
   ordinary IRPEF on gain vs 26% imposta sostitutiva option at deed:
   `python skills/plusvalenza-casa/scripts/pluscasa.py --acquisto 2023 --vendita 2026 --gain 40000 --sostitutiva 26 --marginale 35 --year 2026`
4. Output: situation map + math both ways + notary referral.

## Rules

- Donated property: 5-year clock from original purchase — stated (classic trap).
- Inherited: different track flagged, referral.
- Never compute a final tax as verdict: method + ranges.

## Scripts

- `scripts/pluscasa.py` — 5-year clock + both tax paths (rates are inputs).
  Fixtures with expected outputs in `examples/fixtures/`. Notary computes final.

## Examples

See `examples/plusvalenza-cases.md`. Clock rules in `references/termini.md`.

## Edge cases

- Prima casa sold + rebuy within 1 year → credito d'imposta path (see prima-casa-agevolazioni).
- Lavori raising base cost → documented costs reduce gain, list what counts.
- Non-resident seller → separate track flagged + referral.
