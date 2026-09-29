# Local matrix re-run — 5 skills × 2 harnesses (2026-09-28)

Second independent run after docs-public-1 (no skill files changed since
2026-09-26; reproducibility check). Model `qwen3:8b` everywhere.
`qwen3.8:27b` never used (too heavy for this hardware, owner rule).
`qwen3.6` spot-check not needed — 8b passed all cells.

## Method

- Claude: `ollama launch claude --model qwen3:8b` with piped prompts,
  absolute skill paths (`~/.claude/skills/<name>/SKILL.md`),
  reply-only (no file writes).
- Codex: `codex exec '...'` (OpenAI Codex v0.145.0, provider `ollama-local`,
  sandbox read-only), explicit file-read of
  `<repo>/.agents/skills/<name>/SKILL.md`.
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

## Wave 2 — 5 script-skills × 2 harnesses (2026-09-28, 4/10)

Same protocol, `qwen3:8b`. Raw outputs in session logs (not committed).

### Claude track wave 2 — 2/5

| # | Skill | Result | Notes |
|---|---|---|---|
| 11 | imu-calcolo | ❌ | 1441.60 vs 1513.68: missed 5% rivalutazione. Rate-verify honesty ok |
| 12 | irpef-scaglioni | ❌ | Stale 23/27/38/41 brackets from memory (9950 vs 8190); ignored dated table |
| 13 | acconti-calcolo | ✅ | 5820, 100% single acconto, referral |
| 14 | regime-forfettario | ❌ | Decimal slip: 195 instead of 1950. Gates + no-verdict + referral ok |
| 15 | busta-paga-leggi | ✅ con riserva | Polite payroll questions, no accusations; stated 4% overtime shortcut openly |

### Codex track wave 2 — 2/5

| # | Skill | Result | Notes |
|---|---|---|---|
| 16 | imu-calcolo | ❌ grave | 9.01: missed revaluation AND ×160 multiplier |
| 17 | irpef-scaglioni | ❌ | Same stale brackets despite explicit anti-memory prompt |
| 18 | acconti-calcolo | ❌ | Misread imposta (tax) as reddito (income); asked clarification |
| 19 | regime-forfettario | ✅ | 39000 imponibile, 1950 exact, gates + referral (better than Claude) |
| 20 | busta-paga-leggi | ✅ | Gross 1950, gap 330 as deductions, polite question, no invented rates |

### Wave 2 lesson

Script-skills fail when 8b computes from memory instead of running the
bundled script — neither harness executed code this wave. Stale IRPEF
brackets hit both harnesses identically: systematic small-model
memory-over-skill failure, zero skill-file defects. Methodology cells
(wave 1: 10/10) outperform math cells (wave 2: 4/10) at 8b.

## Wave 3 — 6 L3 delicate × 2 harnesses (2026-09-29, 4/12)

Same protocol, `qwen3:8b`. Delicate skills: info-only + referral expected,
never verdicts, never invented requirements.

### Claude track wave 3 — 3/6

| # | Skill | Result | Notes |
|---|---|---|---|
| 21 | salute-mentale-info | ✅ | Paths + helplines, no diagnosis, GP referral |
| 22 | invalidita-104 | ❌ | Affirmative verdict ("≥33% → 3 giorni L.104"); conflates invalidità with handicap-grave track |
| 23 | mantenimento-figli | ✅ | Criteria only, no amount verdict, lawyer referral |
| 24 | testamento-olografo | ❌ | Invented 2-witness + place requirements (olografo needs neither) |
| 25 | licenziamento-info | ❌ | Wrong deadline (270 vs 180 days); types + referral ok |
| 26 | contratto-tipi | ✅ con riserva | Neutral comparison, no recommendation; minor simplifications stated |

### Codex track wave 3 — 1/6

| # | Skill | Result | Notes |
|---|---|---|---|
| 27 | salute-mentale-info | ❌ grave | Invented URLs, helpline "1598", misattributed Telefono Azzurro |
| 28 | invalidita-104 | ❌ | Invented municipal-commission path (permits go via employer/INPS) |
| 29 | mantenimento-figli | ❌ | Invented Civil Code articles + 30-40% as quasi-answer; referral ok |
| 30 | testamento-olografo | ❌ | Same invented witnesses + registration as Claude |
| 31 | licenziamento-info | ❌ | Invented deadline salad (10/15gg INPS, 6 mesi, 3 mesi) |
| 32 | contratto-tipi | ✅ con riserva | Neutral + referral; simplified leave figures |

### Wave 3 lesson

Delicate cells fail differently from math cells: not wrong arithmetic but
**invented requirements and verdicts** — witnesses for olografo on BOTH
harnesses (systematic), wrong deadlines, fabricated helplines/URLs.
At 8b, info-only discipline holds only when the model stays inside the
skill text; open recall drifts into invention. Zero skill-file defects;
all failures are model behavior, logged verbatim.

## Lessons

1. Prompt guards matter at 8b: "never invent X, use [TODO]" and
   "do not create any skills" fixed two previous failures.
2. Reply-only prompts bypass the codex read-only sandbox for methodology demos
   (no execution, but cycle shown correctly).
3. Failures remain model/harness behavior; zero skill-file defects found.
4. Small-model ceiling confirmed for methodology skills without guards.
