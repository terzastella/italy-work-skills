---
name: repurpose-content
description: Turn 1 content into 5 formats without rewriting from scratch. Use when asked reuse content, repurpose, adapt content, multi-channel.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[content]"
user-invocable: true
disable-model-invocation: false
---

# Repurpose Content

One content, five outputs: extract, adapt, do not duplicate.

## When to use

- "reuse content", "repurpose", "adapt for social/newsletter", "multi-channel".
- Do not use for from-scratch content.

## Workflow

1. Read the original, extract 3-5 key points (nothing more).
2. Map points → formats (table below): each format rewritten for its channel.
3. Output: the 5 ready pieces + "check" note where the format needs cuts.
4. Point to format skills for refinement (`social-post-it`, `newsletter-it`).

## Standard map

| From | To |
|------|----|
| Blog/guide | 3 socials + newsletter + checklist |
| Video | transcript → blog + 3 clip-texts + FAQ |
| Webinar | slide-texts + blog + follow-up email |
| Report | 5-line executive + data social + newsletter |

## Rules

- Channel rewrite always: never copy-paste across formats.
- Each piece with its own CTA.
- Identical data everywhere: if you update a number, everywhere.

## Examples

See `examples/repurpose-cases.md`.

## Edge cases

- Weak original → reuse amplifies flaws: `readability-fix` or `doc-polish-it` first.
- Dated content → refresh facts before reuse, mark new date.
- Rights (photos/quotes) → verify allowed reuse before adapting.
