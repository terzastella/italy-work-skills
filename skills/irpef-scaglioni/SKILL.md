---
name: irpef-scaglioni
description: Explain IRPEF brackets with marginal vs average math. Use when asked IRPEF scaglioni, income tax brackets Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.5", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write Bash
argument-hint: "[income]"
user-invocable: true
disable-model-invocation: false
---

# IRPEF Scaglioni

Brackets decoded: marginal vs average, with worked math — never fear the jump.
Flagship skill: dated tables, script-enforced year checks, detrazioni mapped after slices.

## When to use

- "IRPEF scaglioni", "income tax brackets Italy", "se aumento lo stipendio pago di più?".
- Do not use for full return filing (method + math only, see `cu-730-guida`).
- Do not use for flat-rate regimes (see `regime-forfettario`).

## Workflow (tappe with formal in/out)

### Tappa 1 — Take the figure + the year

Input: gross income + tax year. Both required; never assume either.
No-year requests stop here: ask first.

### Tappa 2 — Load the dated table

Table file `examples/scaglioni-YYYY.json` must equal the requested year
(verified live — reforms move brackets). The script enforces this and errors
on mismatch: surface that error, never bypass it.

### Tappa 3 — Run the slice math (script preferred, reproducible)

`python skills/irpef-scaglioni/scripts/irpef.py --reddito 35000 --scaglioni skills/irpef-scaglioni/examples/scaglioni-2025.json --year 2025`

### Tappa 4 — Show the statement

Slice table + total tax + average rate + marginal rate side by side.
Then kill the classic fear with numbers: only the slice above the threshold
pays the higher rate — earning more never nets less. Prove it with the
49k-vs-51k run (see examples), don't assert it.

### Tappa 5 — After slices: detrazioni + addizionali

Tax credits lower the bill AFTER brackets (see `references/detrazioni.md`,
separate step, not in the script). Regional/municipal addizionali stack on top
(see `addizionali-regionali`) — flag, don't compute here.

## Multi-turn protocol

Turn 1 (figure + year): "quanto e di che anno?" — both or nothing.
Turn 2 (fear check): if the user hesitates on a raise, run the two-figure proof.
Turn 3 (what's next): route to detrazioni, addizionali, or 730 path — never all at once.

## Rules

- Brackets/rates always with year; reforms move them — verify live, never timeless tables.
- The script refuses mismatched table/request years: that error is a feature, surface it.
- Math shown step by step on user figures only, never assumed incomes.
- Forfettari: different world (see `regime-forfettario`), do not mix.
- Tassazione separata (arrears, TFR): separate track flagged, not merged into slices.
- Detrazioni change the bill, never the slices: order stated every time.

## Scripts

- `scripts/irpef.py` — slice math from an explicit dated table (5 fixtures).
  Fixtures with expected outputs in `examples/fixtures/`. Run:
  `python skills/irpef-scaglioni/scripts/irpef.py --help`

## Examples

Good and bad cases in `examples/irpef-cases.md`. Bracket tables live next to
the cases (`examples/scaglioni-YYYY.json`), dated and year-checked.
After-slices logic in `references/detrazioni.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Year without a table | stop + verify live, never reuse last year's silently |
| 2 | Raise fear (49k vs 51k) | two-figure proof, proved not asserted |
| 3 | Arrears/tassazione separata | separate track flagged, not merged |
| 4 | Foreign income slices | quadro RW interplay + referral |
| 5 | 730 vs Redditi path | routed (see `cu-730-guida`), not computed |
| 6 | Zero/negative input | refused with error, never computed |
| 7 | Forfettario asking slices | stop: different world (see `regime-forfettario`) |
