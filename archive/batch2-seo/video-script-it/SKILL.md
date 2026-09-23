---
name: video-script-it
description: Write video scripts with hook, timing and CTA. Use when asked video script, video text, reel, video tutorial.
license: MIT
compatibility: Claude Code, Codex, Grok, Cursor, Copilot
metadata: {author: ai-skills-hub, version: "0.1", lang: "en"}
allowed-tools: Read Write
argument-hint: "[topic/duration]"
user-invocable: true
disable-model-invocation: false
---

# Video Script

Scripts that are spoken, not read: 3-second hook, blocks, CTA.

## When to use

- "video script", "video text", "reel", "video tutorial", "youtube".
- Do not use for articles.

## Workflow

1. Ask: duration (reel ≤60s, youtube 5-10min), topic, CTA, tone.
2. Pace: ~150 words/minute English. Compute words per duration.
3. Structure: Hook (3s) → Promise → Numbered blocks → Recap → CTA.
4. Visual column: per block note what shows (`[show screen]`).

## Output format

```text
Hook (0:00): <1 sentence>
Block 1 (0:05): <spoken text> [visual: ...]
...
Total: <n> words ≈ <duration>
CTA: <one>
```

## Rules

- Short sentences, natural speech, no long subordinate clauses.
- Cumulative timings consistent with asked duration.
- B-roll/on-screen text suggested, never mandatory-expensive.

## Examples

See `examples/video-cases.md`. Pacing in `references/pacing.md`.

## Edge cases

- Unrealistic duration (10 min of thin content) → propose honest duration.
- No face/camera → voiceover script + stock/screen visuals.
- Series → recurring template (same hook/CTA) for recognition.
