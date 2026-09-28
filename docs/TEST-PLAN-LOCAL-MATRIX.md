# Local matrix re-run — 5 skills × 2 harnesses (2026-09-28)

Second independent run after docs-public-1 (no skill files changed since
2026-09-26; reproducibility check). Model `qwen3:8b` everywhere.
`qwen3.8:27b` never used (too heavy for this hardware, owner rule).
`qwen3.6` spot-check not needed — 8b passed all cells.

## Method

- Claude: `ollama launch claude --model qwen3:8b` with piped prompts,
  absolute skill paths (`C:\Users\tanta\.claude\skills\<name>\SKILL.md`),
  reply-only (no file writes).
- Codex: `codex exec '...'` (OpenAI Codex v0.145.0, provider `ollama-local`,
  sandbox read-only), explicit file-read of
  `D:\Projects\AI-Toolkit\ai-skills\.agents\skills\<name>\SKILL.md`.
- One cell at a time; tree verified clean after the run (`git status` empty).

## Claude track — 5/5 ✅ (was 4/5 on 2026-09-26)

| # | Skill | Result | Notes |
|---|---|---|---|
| 1 | hello-agent | ✅ | Correct table, self-ID Claude Code, version 0.2, honest path |
| 2 | invoice-it | ✅ con riserva | €500/€110/€610 exact + placeholders; invented invoice number (minor, same as 09-26) |
| 3 | frontend-design (vendor) | ✅ | Intentional palette + typography, brand voice followed |
| 4 | tdd (vendor) | ✅ | RED then GREEN shown — FIXED vs 09-26 ❌ (test-after) |
| 5 | brainstorming (vendor) | ✅ | Questions first, app-scoped, no skill-confusion |

## Codex track — 5/5 ✅ (was 3/5 on 09-26)

| # | Skill | Result | Notes |
|---|---|---|---|
| 6 | hello-agent | ✅ | Correct table, self-ID Codex, version 0.2 (verbose reasoning, output right) |
| 7 | invoice-it | ✅ | €500/€110/€610 exact, ALL [TODO] placeholders — FIXED vs 09-26 ❌ (invented IBAN/SWIFT). Explicit anti-invention prompt helped |
| 8 | frontend-design (vendor) | ✅ | Brand-aware draft, under 15 lines |
| 9 | tdd (vendor) | ✅ | RED→GREEN→REFACTOR shown — FIXED vs 09-26 ❌ (sandbox blocked writes; reply-only prompt bypasses it) |
| 10 | brainstorming (vendor) | ✅ | Questions first, app-scoped, no skill creation, no repo bleed — "do not create any skills" guard helped |

## Grok column — BLOCKED (honest)

No local launcher exists (`ollama launch` lists no grok integration) and no
subscription is available. The 5 Grok cells stay unrun; recorded as blocked
in `docs/COMPATIBILITY.md`, not faked.

## Lessons

1. Prompt guards matter at 8b: "never invent X, use [TODO]" and
   "do not create any skills" fixed two previous failures.
2. Reply-only prompts bypass the codex read-only sandbox for methodology demos
   (no execution, but cycle shown correctly).
3. Failures remain model/harness behavior; zero skill-file defects found.
4. Small-model ceiling confirmed for methodology skills without guards.
