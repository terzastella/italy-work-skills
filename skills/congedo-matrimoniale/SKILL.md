---
name: congedo-matrimoniale
description: Explain wedding leave with length and papers. Use when asked congedo matrimoniale, wedding leave Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[contract]"
user-invocable: true
disable-model-invocation: false
---

# Congedo Matrimoniale

Wedding leave decoded: paid days, papers, timing.

## When to use

- "congedo matrimoniale", "wedding leave Italy".
- Do not use for honeymoon planning.

## Workflow

1. Length by CCNL (commonly 15 days, verify contract) + paid status.
2. Papers: marriage certificate to employer + timing (around the date).
3. Unioni civili: same treatment flagged.
4. Output: duration check + papers + request draft points.

## Rules

- Days only with CCNL cited; never generic "2 weeks" as law.
- Timing windows (before/after wedding) per contract, stated.
- No advice beyond procedure.

## Examples

See `examples/congedo-cases.md`. Duration logic in `references/durate.md`.

## Edge cases

- Fixed-term ending soon → use-it-or-lose-it math shown plainly.
- Religious-only wedding → civil validity first, flag it.
- Denied leave → written request trail + referral.
