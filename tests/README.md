# tests/ — behavior harness (drill-style, deterministic)

No LLM, no network. Two layers:

1. **Static guards** (`scripts/eval-behavior.py`, CI step): every Golden skill
   has out-links, Good/Bad examples, and year markers; every delicate skill
   carries a referral and ships no code; banned verdict patterns
   (`patterns-ban.txt`) never appear affirmatively.
2. **Run protocols** (`golden/<skill>/input.md` + `expect.md`): the exact prompt
   and the traits a good answer must show. Executed by a human or an agent
   during real-agent test sessions (see `docs/TEST-PLAN.md`); the runner only
   verifies the protocol files exist and are non-trivial.

Conventions:

- `golden/<skill>/input.md`: one realistic user prompt with sample data.
- `golden/<skill>/expect.md`: checklist of MUST traits (numbers, questions,
  refusals, referrals) the answer must exhibit.
- Delicate skills have no run protocols by design (no simulated cases on
  sensitive matters) — they are covered by guards + `docs/AUDITS.md`.
