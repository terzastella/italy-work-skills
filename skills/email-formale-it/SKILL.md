---
name: email-formale-it
description: Write formal Italian business emails with right subject, structure and tone. Use when asked formal email, write email, work email, payment reminder.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[recipient/purpose]"
user-invocable: true
disable-model-invocation: false
---

# Formal Italian Email

Italian business emails: clear subject, 3 paragraphs, correct closing. Replies in English explain the choices; the email itself stays in Italian.

## When to use

- "formal email", "write email", "work email", "payment reminder" (Italian).
- Do not use for informal/friendly messages. Need certified legal value? See `pec-bozza`.

## Workflow

1. Ask (if missing): recipient, purpose in 1 sentence, what you want, deadline.
2. Fixed structure: Subject → Greeting → Context (2 lines) → Request (1 sentence) → Closing.
3. Tone: formal `Lei`, no abbreviations, no emoji, no exclamation marks.
4. Output: subject + copy-ready body + 1 short alternative subject.

## Output format

```text
Subject: <clear, max 60 chars>
Egregio/a <name>,
<2-line context>
<1-sentence request with deadline if any>
Cordiali saluti,
<name>
```

## Rules

- Max 12 body lines. One request per email.
- Sensitive data only if provided: never invent names, amounts, dates.

## Examples

See `examples/email-cases.md`. Openings/closings in `references/formule.md`.

## Edge cases

- Complaint/reminder → firm but neutral tone, facts + request, never threats.
- Multiple recipients → plural greeting or company form.
- Mentioned attachments → final `Attachments: ...` list, check they exist if local.
