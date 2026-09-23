---
name: test-gen-it
description: Generate essential test cases from a function with input-outcome table. Use when asked generate tests, test cases, unit tests, coverage.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[file or function]"
user-invocable: true
disable-model-invocation: false
---

# Test Gen

Test cases that matter: happy paths, edges, errors. No tautological tests.

## When to use

- "generate tests", "test cases", "unit tests", "coverage".
- Do not use for exploratory manual test plans.

## Workflow

1. Read signature + body. Find branches (if/loops/errors).
2. Case table: normal, edges (empty, zero, max, None), errors (exceptions).
3. Generate tests in the repo's framework (if unknown, ask: pytest/unittest/other).
4. Each test: name `test_<function>_<case>`, assert on behavior not implementation.

## Output format

```text
Function: <name> (<n> branches)
Cases: normal (1), edges (3), errors (2)
Tests generated in <file>, run with <command>
```

Then the complete test code.

## Rules

- Max 8 tests per function: the most significant.
- No mocking of what you test; mock only external I/O.
- Every test must really fail if the code is broken (no assert True).

## Examples

See `examples/test-cases.md`. Framework reference in `references/frameworks.md`.

## Edge cases

- Function with I/O or network → tests with tmp/fakes, never real network.
- Code without separation → flag it and test observable behavior.
- Repo without framework → propose minimal pytest, do not impose it.
