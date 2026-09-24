---
name: case-study
description: Write case studies with problem, solution and real results. Use when asked case study, client story, customer success.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[client/project]"
user-invocable: true
disable-model-invocation: false
---

# Case Study

Stories that convince: real problem, concrete solution, real numbers.

## When to use

- "case study", "client story", "customer success".
- Do not use for 2-line testimonials.

## Workflow

1. Collect: client (anonymizable?), initial problem, solution, measured results, quote.
2. Structure: Result title → Context (3 lines) → Problem → Solution (3 steps) → Results (numbers) → Quote.
3. Max 400 words. Numbers only as provided, never estimated as real.
4. Propose anonymized version if data is sensitive.

## Rules

- Results with real numbers or `[number to confirm]`: never invented metrics.
- Quotes only real or `[quote to collect]`.
- Named client only with permission: default sector + size ("5-person firm").

## Examples

See `examples/case-cases.md`. Structure in `references/structure.md`.

## Edge cases

- Zero measured results → "process" case (what changed in the method), no fake numbers.
- Client forbids name → fully anonymous but real sector.
- Partial failure → selective honesty: what worked + what did not, no fiction.
