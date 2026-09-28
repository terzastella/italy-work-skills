---
name: assegni-bancari
description: Explain checks with protest and deadlines. Use when asked assegno, check Italy, protesto.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[situation]"
user-invocable: true
disable-model-invocation: false
---

# Assegni Bancari

Checks decoded: filling, cashing, protest for uncovered ones.

## When to use

- "assegno", "check Italy", "protesto".
- Do not use for cashier's checks specifics only (covered within).

## Workflow

1. Fill correctly: amount in figures + letters, date, place, signature match.
2. Cashing: timelines + bank verification holds.
3. Uncovered: protesto mechanics + CAI registration consequences + late payment fix paths.
4. Output: steps + deadlines + referral for disputes.

## Rules

- Post-dating games: explained as risky, never advised.
- Bounced-check criminal edge flagged + referral, urgent tone where due (rules year-stated).
- Circolari vs bancari differences stated.

## Examples

See `examples/assegni-cases.md`. Protest logic in `references/protesto.md`.

## Edge cases

- Lost/stolen checkbook: denuncia + stop paths immediately.
- Received dubious check: verification before goods handover, stated as rule.
- Old check found: prescription terms stated plainly.
