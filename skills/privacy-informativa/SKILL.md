---
name: privacy-informativa
description: Draft GDPR privacy notices with mandatory items and template. Use when asked privacy, GDPR, informativa, data notice Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[activity/data]"
user-invocable: true
disable-model-invocation: false
---

# Privacy Informativa (GDPR, Italy)

Notices that inform: controller, purposes, rights — template, not legal advice.

## When to use

- "privacy", "GDPR", "informativa", "data notice" (Italy).
- Do not use for DPO opinions or DPIAs (refer to professionals).

## Workflow

1. Ask: controller data, what data collected, purposes, legal bases, retention, recipients, rights contact.
2. Fill template in `assets/informativa-template.md`. Missing items stay `[TODO]`.
3. Plain-language pass (see `readability-fix` spirit): rights section must be understandable.
4. Close with: DPO/consultant review recommended before publishing.

## Rules

- Mandatory items always present (see `references/voci.md`): never ship without rights + controller.
- Legal bases named per purpose; no invented bases.
- Cookie/tracking mention if website; separate cookie policy flagged (rules year-stated).
- Minors data → reinforced note + parental consent path.

## Examples

See `examples/privacy-cases.md`.

## Edge cases

- No DPO and unsure → draft + strong review recommendation, list open questions.
- Extra-EU transfers → dedicated section, never omitted silently.
- Existing notice → gap review vs checklist, not full rewrite by default.
