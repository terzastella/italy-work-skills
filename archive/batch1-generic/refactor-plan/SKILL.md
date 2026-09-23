---
name: refactor-plan
description: Safe step-by-step refactor plans with guard tests. Use when asked refactor, restructure code, clean code, simplify.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: "[file]"
user-invocable: true
disable-model-invocation: false
---

# Refactor Plan

A plan in small verifiable steps: never refactor and fix together.

## When to use

- "refactor", "restructure", "clean code", "simplify", "duplication".
- Do not use for bugs (see `systematic-debug`) or reviews (see `code-review-it`).

## Workflow

1. Snapshot current behavior: existing tests or use cases not to break.
2. List smells in annoyance order (duplication, long functions, names, dependencies).
3. Step plan: each step = 1 change + how to verify (test/command).
4. Flag risks (public APIs, data, performance) with mitigation.
5. Do not apply the refactor without confirmation: show the plan first.

## Output format

```text
Goal: <1 line>
Guard: <tests/cases not to break>
Step 1: <change> | Verify: <command>
Step 2: ...
Risks: <risk> → <mitigation>
```

## Rules

- Max 7 steps, each individually reversible.
- Never change behavior + structure in the same step.
- Never rename public APIs without a deprecation notice.

## Examples

See `examples/refactor-cases.md`. Smell catalog in `references/smells.md`.

## Edge cases

- Zero existing tests → step 0: add 1 guard test on key behavior.
- Fragile legacy code → smaller steps, verify after each.
- "Refactor everything" request → scope to one module at a time.
