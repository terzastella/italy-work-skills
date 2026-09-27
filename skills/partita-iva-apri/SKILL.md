---
name: partita-iva-apri
description: Guide opening an Italian VAT number with regime and ATECO choice. Use when asked open partita IVA, start freelance Italy, aprire partita IVA.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en"}
allowed-tools: Read Write
argument-hint: "[activity]"
user-invocable: true
disable-model-invocation: false
---

# Aprire Partita IVA

From idea to VAT number: regime, ATECO, steps — information, not filing.
Flagship skill: profiling funnel, cost preview with scripts, no-filing boundary.

## When to use

- "open partita IVA", "start freelance Italy", "aprire partita IVA".
- Do not use for filing anything (AdE/ComUnica only); do not use for ATECO detail (see `ateco-scelta`).

## Workflow (tappe with formal in/out)

### Tappa 1 — Profile the idea

Input: activity (what, really), employee or freelance, expected revenue,
prior employment. Output: profile + two flags computed immediately —
ex-employee continuity risk, occasional-vs-VAT test (see `collaborazioni-occasionali`).
Habitual activity may need VAT even under 5.000€: flag it, explain why.

### Tappa 2 — Route regime + INPS

Forfettario vs ordinary via `regime-forfettario` gates (run the script for a
first tax sketch: `forfettario.py --fatturato ... --coeff ... --year ...`) +
INPS track (Gestione Separata vs artigiani/commercianti — estimate with
`contributi.py --reddito ... --aliquota ... --year ...`). No verdicts:
gates shown, professional decides.

### Tappa 3 — Steps + costs preview

AdE declaration (model AA9/12), CCIAA/ComUnica if impresa, INPS enrollment,
e-invoicing setup (see `references/passi.md`). Costs to expect: accountant fee,
contributions from month one, Chamber fees if impresa. Amounts with year.

### Tappa 4 — Close with the boundary

"Verify with accountant." No filing done here — guidance only, stated as the
last line every time.

## Multi-turn protocol

Turn 1 (profile): the four facts in one batch. Turn 2 (route): regime + INPS
with script sketches. Turn 3 (steps): filing list + costs. Turn 4 (close):
boundary line. Ex-employee flag never waits past turn 1.

## Rules

- Never state which regime the user "must" pick: show gates, let them decide with a professional.
- Limits year-stated (e.g. employee-income ceiling for forfettario access, verify current law).
- Habitual activity may need VAT even under 5.000€: flag it, explain why.
- Amounts with year. No filing done here — guidance only.
- Foreign resident → flag fiscal residence rules, referral.

## Examples

Good and bad cases in `examples/apertura-cases.md`. Step list in `references/passi.md`.
Cost preview patterns in `references/costi-primo-anno.md`.

## Edge cases (priority order)

| # | Case | Action |
|---|---|---|
| 1 | Ex-employee same work | forfettario exclusion risk, flag strongly at tappa 1 |
| 2 | Occasional fits better | explain limits + ritenuta, do not push VAT |
| 3 | Foreign resident | fiscal residence rules flagged + referral |
| 4 | Second activity later | ATECO add + coefficient split, revenue summed for gates |
