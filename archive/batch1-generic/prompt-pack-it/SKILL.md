---
name: prompt-pack-it
description: Create reusable prompt packs with variables and tests. Use when asked prompt template, reusable prompt, prompt library, system prompt.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[purpose]"
user-invocable: true
disable-model-invocation: false
---

# Prompt Pack

Prompts that work twice: with variables, example and usage test.

## When to use

- "prompt template", "reusable prompt", "prompt library", "system prompt".
- Do not use for full skills (see `skill-creator-it`).

## Workflow

1. Ask: role, variable input, expected output, 1 real example.
2. Fixed structure: Role → Context (`{{variables}}`) → Numbered instructions → Output format → Example.
3. Mental test: apply it to the example, show simulated output, fix ambiguities.
4. Deliver pack + 3-line guide (when to use it, what to pass, what to check).

## Pack format

```text
# <Name>
Role: <who you are>
Input: {{var1}}, {{var2}}
Instructions:
1. ...
Output: <format>
Example: <input→output>
```

## Rules

- Variables in `{{double braces}}`, never real values as defaults (no PII).
- Max 1 task per prompt: if two, two prompts.
- Every prompt has a real usage example, never theory only.

## Examples

See `examples/prompt-cases.md`. Patterns in `references/patterns.md`.

## Edge cases

- Vague prompt ("improve text") → ask expected output + example before writing.
- Sensitive data in example → anonymize, mark `[sample data]`.
- Multi-step chain → numbered prompt pack with input/output between steps.
