---
name: code-review-it
description: English code reviews with severity, file line and proposed fix. Use when asked review code, code review, pull request review.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: "[file or diff]"
user-invocable: true
disable-model-invocation: false
---

# Code Review

Concrete reviews: issues ordered by severity, each with location and fix.

## When to use

- "review", "code review", "review code/pull request", "check this code".
- Do not use for guided debugging (see `systematic-debug`) or planned refactors (see `refactor-plan`).

## Workflow

1. Read files or diff (max ~400 lines per pass; beyond that, per file).
2. Look in order: correctness, security/secrets, error handling, readability, obvious performance.
3. Output: verdict (1 line) + issue table + top-3 fixes. Format below.

## Output format

```text
Verdict: ACCEPTABLE / NEEDS WORK / BLOCKED (1 line why)
[SEVERE] <file>:<line> — <issue>. Fix: <1 line>
[MEDIUM] <file>:<line> — <issue>. Fix: <1 line>
[MINOR] <file>:<line> — <issue>. Fix: <1 line>
Top-3 fixes in impact order.
```

## Rules

- Max 10 issues: the most impactful, not an endless style list.
- Every issue has an exact location: never "there is a bug somewhere".
- No full rewrites unless asked: targeted fixes.
- Secrets/tokens found → always `[SEVERE]` + point to `security-check`.

## Examples

See `examples/review-cases.md`. Severity scale in `references/severity.md`.

## Edge cases

- No issues → "No significant issues." + 1 optional suggestion, stop.
- Huge diff → review per file with priority (security first).
- Unknown language → review logic/structure, declare the limit.
