---
name: faq-gen
description: Generate FAQs with real questions and 2-line answers. Use when asked FAQ, frequently asked questions, help section.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[topic]"
user-invocable: true
disable-model-invocation: false
---

# FAQ Gen

FAQs people really ask: 5-8 questions, 2-line answers with links.

## When to use

- "FAQ", "frequently asked questions", "help section".
- Do not use for 1-to-1 support.

## Workflow

1. Ask topic + audience. Collect real questions (clients, reviews, search) if available.
2. 5-8 questions ordered by likely frequency. Answers max 2 lines + deep link.
3. Close with "No answer? → <contact>".

## Rules

- Questions as people ask them ("how much?" not "pricing policy").
- Answers with fact + action, never bare "it depends" without follow-up.
- Prices/dates only if provided, else point to contact.
- No invented questions about nonexistent problems (no FUD).

## Examples

See `examples/faq-cases.md`. Question sources in `references/sources.md`.

## Edge cases

- Sensitive topic (health, tax) → cautious answers + "check with a professional".
- Zero info provided → skeleton FAQ with `[TODO]`, no fake answers.
- Existing ones → integrate and dedupe, do not append.
