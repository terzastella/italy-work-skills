---
name: verbale-riunione-it
description: Write Italian meeting minutes with decisions and owners. Use when asked verbale, meeting minutes, riunione notes.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[meeting notes]"
user-invocable: true
disable-model-invocation: false
---

# Verbale di Riunione

Minutes that work: who decided what, who does what, by when.

## When to use

- "verbale", "meeting minutes", "riunione notes".
- Do not use for transcripts (minutes, not dictation).

## Workflow

1. Ask or take: date, attendees/absent, agenda, raw notes.
2. Structure: header → decisions (numbered) → actions (owner + date each) → next meeting.
3. Every action has exactly one owner and one date. No ownerless actions.
4. Output ready minutes (Italian body) + English 3-line recap on top.

## Rules

- Decisions quoted with who proposed/seconded when relevant (condominio/assemblies).
- Opinions attributed, facts plain. Never invent attendees or decisions.
- Dates in DD/MM/YYYY, times with timezone if remote.

## Examples

See `examples/verbale-cases.md`. Template in `references/template.md`.

## Edge cases

- Messy notes → draft + `[da confermare]` on unclear points, never guess decisions.
- Formal assemblies (condominio/CdA) → add call/constitutive notes, suggest bylaws check.
- No decisions taken → state it plainly + next step proposed.
