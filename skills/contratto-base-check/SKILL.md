---
name: contratto-base-check
description: Read base contracts with clause checklist. Use when asked check contratto lavoro, employment contract Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract type]"
user-invocable: true
disable-model-invocation: false
---

# Contratto Base Check (Info Only)

Read your contract guided: what each clause means, which red flags to spot.

## When to use

- "check contratto lavoro", "employment contract Italy".
- Do not use for validity verdicts or dispute strategy (lawyer/union matter).

## Workflow

1. Identify: CCNL applied, level (livello), duties (mansioni), workplace, hours, contract type (see `contratto-tipi`).
2. Read key clauses: probation (see `periodo-prova`), notice periods, fixed-term cause where due, non-compete terms flagged.
3. Pay check: stated salary vs CCNL minimums for that level (see `busta-paga-leggi`).
4. Output: clause map + red-flag list + questions for union/lawyer. No verdicts, ever.

## Rules

- Never declare a clause valid or void: mapping only, professionals decide.
- Blank resignations or under-CCNL pay patterns: illegality stated plainly + referral now.
- Figures only with CCNL cited; never generic thresholds.

## Examples

See `examples/contratto-cases.md`. Clause map in `references/clausole.md`.

## Edge cases

- No written contract: regularization path + referral, urgent tone.
- Non-compete signed: scope/limits overview, no validity calls.
- Fixed-term without requirements: formal check + referral, documented everything.
