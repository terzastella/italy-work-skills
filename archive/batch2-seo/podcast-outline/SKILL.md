---
name: podcast-outline
description: Create podcast episode outlines with timing and questions. Use when asked podcast outline, podcast episode, episode structure.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[theme/duration]"
user-invocable: true
disable-model-invocation: false
---

# Podcast Outline

Episodes that hold: hook, 3 acts, closing with CTA.

## When to use

- "podcast outline", "podcast episode", "episode structure".
- Do not use for transcriptions.

## Workflow

1. Ask: duration (20/40/60min), guest yes/no, promised takeaway.
2. Outline with timings: Hook 2min → Act1 → Act2 → Act3 → Recap+CTA.
3. With guest: 5-7 real questions (not "tell us about you"), 1 politely tough question.
4. Output with cumulative timings + edit notes (`[cut if...]`).

## Rules

- 1 takeaway per episode, stated at open and repeated at close.
- Short questions, never double ("what and why and when...").
- Realistic timings: chatter = 150 wpm with pauses included.

## Examples

See `examples/podcast-cases.md`. Narrative arcs in `references/arcs.md`.

## Edge cases

- Vague guest → questions on concrete cases ("tell me the last time...").
- Long unstructured episode → split into 2 episodes, not 1 river.
- Solo monologue → rhythm shifts every 5 min (story, data, audience question).
