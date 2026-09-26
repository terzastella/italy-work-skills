---
name: prima-casa-agevolazioni
description: Explain first-home tax breaks with residence rules. Use when asked prima casa, agevolazioni prima casa, first home Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[purchase]"
user-invocable: true
disable-model-invocation: false
---

# Prima Casa Agevolazioni

First-home perks without losing them: reduced taxes, residence timing, constraints.

## When to use

- "prima casa", "agevolazioni prima casa", "first home Italy".
- Do not use for generic purchase steps (see `compravendita-casa`).

## Workflow

1. Perks: reduced registration tax (vs ordinary), IVA reduced rate where due, cadastre/mortgage fixed taxes (year-stated).
2. Conditions: no exclusive ownership of another home in same comune, residenza transfer within 18 months.
3. Constraints: 5-year no-sale rule (decadenza + surcharge + interest if broken, exceptions listed).
4. Output: eligibility check + timeline + notary referral.

## Rules

- Residenza 18-month clock stated first — the classic killer.
- Under-36 special schemes: year-stated, verify live (they change).
- Never promise perks: conditions checked one by one.

## Examples

See `examples/primacasa-cases.md`. Conditions in `references/condizioni.md`.

## Edge cases

- Owned bare ownership elsewhere → rules nuance flagged, referral.
- Sale within 5 years + rebuy within 1 year → credito d'imposta path, explain + refer.
- Foreign resident buying → different track, do not generalize.
