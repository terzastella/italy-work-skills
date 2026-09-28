---
name: assicurazione-casa
description: Explain home insurance with coverage and claims. Use when asked assicurazione casa, home insurance Italy, polizza casa.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.3", lang: "en", last_verified: "2026-09-28"}
allowed-tools: Read Write
argument-hint: "[home/needs]"
user-invocable: true
disable-model-invocation: false
---

# Assicurazione Casa

Home policies decoded: fire/theft/liability, deductibles, claim steps.

## When to use

- "assicurazione casa", "home insurance Italy", "polizza casa".
- Do not use for investment/insurance advice beyond home.

## Workflow

1. Needs: owner vs tenant, valuables, liability (RC capofamiglia) importance.
2. Coverage map (see `references/coperture.md`): incendio, furto, RC, eventi — deductibles (scoperti/franchigie) explained.
3. Claims: prompt notice + photos + list; deadlines in policy.
4. Output: needs-matched checklist + questions for agent + claim steps if active.

## Rules

- No insurer endorsement; comparison criteria only.
- Underinsurance (sottoassicurazione) proportional rule explained plainly.
- Mortgage-linked policies: check overlap before doubling (terms year-stated).

## Examples

See `examples/casa-cases.md`.

## Edge cases

- Claim denied → read motivo + IVASS complaint path mentioned.
- Rented home: tenant vs landlord cover split.
- Cat/natural events: standard exclusions flagged, extension options noted.
