---
name: domicilio-digitale-inad
description: Register digital domicile in INAD with effects. Use when asked domicilio digitale, INAD, PEC address registry Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[subject]"
user-invocable: true
disable-model-invocation: false
---

# Domicilio Digitale (INAD)

One certified address for all PA mail: register, effects, keep it alive.

## When to use

- "domicilio digitale", "INAD".
- Do not use for PEC drafting (see `pec-bozza`).

## Workflow

1. Who must have it: firms/professionals (mandatory) vs citizens (voluntary, effects explained).
2. Register: INAD portal with SPID/CIE + PEC address + verification.
3. Effects: PA notifications legally valid there — mailbox monitoring duty stressed.
4. Change/revoke paths + dead-PEC risks (bounces = missed deadlines).

## Rules

- Monitoring duty stated bluntly: registered = deemed delivered.
- Never handle anyone's SPID/PEC credentials.
- Professionals: albo-linked obligations flagged (rules year-stated).

## Examples

See `examples/domicilio-cases.md`. Effects in `references/effetti.md`.

## Edge cases

- Expired/dead PEC in INAD → update urgently, missed-notice risks listed.
- Multiple roles (person + firm) → separate domiciles logic explained.
- Abroad resident → INAD access paths + limits flagged.
