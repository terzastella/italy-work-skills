---
name: rc-auto
description: Explain mandatory car insurance with coverage and claims. Use when asked RC auto, car insurance Italy, assicurazione auto.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[vehicle/driver]"
user-invocable: true
disable-model-invocation: false
---

# RC Auto

Mandatory insurance decoded: coverage, classes, claims, what voids.

## When to use

- "RC auto", "car insurance Italy", "assicurazione auto".
- Do not use for investment/insurance advice beyond motor.

## Workflow

1. Coverage: RCA mandatory (third-party damages) vs kasko/furto/incendio optional.
2. Price drivers: CU class (Bersani notes for family), km, box, driver age/history.
3. Claims: constatazione amichevole (CID) + denuncia timing + direct indemnity (indennizzo diretto) conditions.
4. Output: coverage check + comparison points + claims steps.

## Rules

- Driving uninsured: sanctions + seizure stated bluntly.
- CU class from attestato di rischio, never guessed.
- No insurer endorsement; comparison criteria only.

## Examples

See `examples/rcauto-cases.md`. Coverage map in `references/coperture.md`.

## Edge cases

- Historic cars: dedicated cheap policies + usage limits flagged.
- Foreign plates resident → regularization duty, referral.
- Accident with uninsured → Fondo vittime + lawyer referral, urgent tone.
