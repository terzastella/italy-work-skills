---
name: systematic-debug
description: Guided 4-phase debugging with root cause before fix. Use when asked debug, error, bug, not working, traceback.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Bash
argument-hint: "[error or file]"
user-invocable: true
disable-model-invocation: false
---

# Systematic Debug

Four mandatory phases: reproduce → isolate → root cause → fix. Never fix blind.

## When to use

- "debug", "error", "bug", "not working", traceback, failing test.
- Do not use for general reviews (see `code-review-it`).

## Workflow

1. **Reproduce**: minimal command showing the error + full message. No reproduction, no progress.
2. **Isolate**: narrow down (file, function, input) halving the search space each time.
3. **Root cause**: 1 sentence "it happens because ...". Separate cause from symptom.
4. **Fix**: minimal patch + how to verify it (test command). Max 2 alternatives.
5. Output in the format below.

## Output format

```text
Reproduction: <command> → <short error>
Isolation: <guilty file/function/input>
Root cause: <1 sentence>
Fix: <patch or steps> | Verify: <command>
```

## Rules

- No fix proposals before the root cause.
- One cause at a time: if multiple hypotheses, order by likelihood and test the first.
- Never delete data/logs to "clean up": logs are evidence.
- If intermittent error: say so, propose how to capture it (logs, retry, seed).

## Examples

See `examples/debug-cases.md`. Isolation techniques in `references/bisect.md`.

## Edge cases

- Not reproducible → environment checklist (versions, env, cache) + how to log next occurrence.
- Error in external dependency → local fix (pin/workaround) + upstream issue link, do not patch the library.
- Multiple bugs together → one at a time, blocking one first.
