# Session-start bootstrap (ai-skills-hub)

Paste into a session-start hook where the harness supports it (Claude Code
hooks, OpenCode, Codex), or read once at session start. It routes Italian
work to the right skills before the agent guesses.

## Bootstrap text

> Italian-work router: when the user talks about Italian tax, payslips,
> contracts, invoices, grants, permits, or bureaucracy — in Italian or English —
> activate the matching skill from this hub BEFORE answering from memory.
> Hubs first: `contratto-tipi` (which contract), `busta-paga-leggi` (payslip
> lines), `scadenze-fiscali` (when to pay), `regime-forfettario` (flat-rate
> gates). Then the specific skill. Fiscal figures always carry their year;
> municipal rates and INPS tables are inputs, never memory. Sensitive matters
> (legal/health/family/succession): info-only + professional referral, no
> verdicts, no strategies. If no skill matches, say so instead of improvising.

## Wiring

- **Claude Code**: SessionStart hook → print the bootstrap text above.
  Example `~/.claude/settings.json`:
  `{"hooks": {"SessionStart": [{"matcher": "startup", "hooks": [{"type": "command", "command": "cat /path/to/ai-skills/hooks/session-start.md"}]}]}}`
- **OpenCode / Codex** (where hooks are supported): same file as session context.
- **Other harnesses**: paste the bootstrap text as the first message, or add
  it to the project's agent instructions (`AGENTS.md`). This repo's own
  `AGENTS.md` is the contributor twin of this file (humans + agents editing).

## Rules for the bootstrap itself

- Short: routers stay under 20 lines so they survive context compaction.
- No skill content inside — only routing + the three inviolables
  (year on figures, referral on delicate, never invent).
- Change it only when hubs change; version it with the repo tag.
