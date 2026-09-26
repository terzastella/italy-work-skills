---
name: cassetto-fiscale
description: Navigate AdE tax drawer with delegations. Use when asked cassetto fiscale, AdE reserved area, tax drawer Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.2", lang: "en"}
allowed-tools: Read Write
argument-hint: "[need]"
user-invocable: true
disable-model-invocation: false
---

# Cassetto Fiscale

Your tax drawer decoded: returns, payments, refunds, deeds — and delegations.

## When to use

- "cassetto fiscale", "AdE reserved area".
- Do not use for filing (consultation only).

## Workflow

1. Access: SPID/CIE/CNS + Entratel/Fisconline legacy paths.
2. Sections map (see `references/sezioni.md`): dichiarazioni, versamenti F24, rimborsi status, atti/contratti registrati.
3. Delegations: conferring/revoking intermediario access, what they see.
4. Output: where-to-click map + what each section proves.

## Rules

- Never handle anyone's credentials.
- Refund statuses read as states, never promised dates.
- Discrepancies found → professional referral, not DIY corrections.

## Examples

See `examples/cassetto-cases.md`.

## Edge cases

- Mismatched data (payments missing) → quietanza collection + referral.
- Deceased person's drawer → heir access paths, flag + sensitivity.
- Fatture e corrispettivi vs cassetto: different portals, routed correctly.
