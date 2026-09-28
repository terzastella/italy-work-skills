---
name: spid-cie-guida
description: Explain SPID/CIE levels and recovery without touching credentials. Use when asked SPID, CIE, identità digitale, access public services Italy.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[problem]"
user-invocable: true
disable-model-invocation: false
---

# SPID/CIE Guide

Digital identity without disasters: levels, where it works, recovery — credentials never handled.

## When to use

- "SPID", "CIE", "identità digitale", "access INPS/AdE" (Italy).
- Do not use for anything requiring passwords/OTPs (never ask for them).

## Workflow

1. Identify need: access service (AdE precompilata, INPS, INL) vs get identity vs recover.
2. Explain levels (SPID L1/L2/L3, CIE + PIN/PUK, requirements year-stated) and which service needs what.
3. Recovery path: official provider helpdesk steps, never "send me codes".
4. Close with security rules (see `references/sicurezza.md`).

## Rules

- NEVER ask for, receive, or use passwords, OTPs, PINs, PUKs. Refuse clearly if offered.
- Providers change procedures: link official help pages with verify-date.
- Minors/representatives (genitori, tutori, deleghe): mention the dedicated paths.

## Examples

See `examples/spid-cases.md`.

## Edge cases

- Locked account → provider recovery only, no workarounds.
- Abroad with Italian services → CIE + consulate paths, flag limitations.
- Phishing suspicion → stop, verify sender, official channels only.
