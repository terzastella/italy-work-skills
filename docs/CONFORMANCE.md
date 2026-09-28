# Conformance corpus — frozen sample for real-agent runs (Level C)

Level A (structure) and Level B (install) already cover all 278 entries in
CI. This file freezes the Level C sample: the only honest way to claim
behavioral compatibility without running 278 × 9 cells.

## Corpus (69 skills × claude + codex local = 138 cells)

- **L3 delicate, all 36**: accertamento-info, adozioni-info, affido-familiare,
  appalti-pubblici-info, assicurazione-vita-info, cittadinanza,
  contratto-base-check, contratto-tipi, cooperative-info, criptovalute-fisco,
  donazioni-info, eredita-debiti, fallimento-crisi-info, franchising-info,
  giudice-di-pace, invalidita-104, irap-info, licenziamento-info,
  mantenimento-figli, marchi-info, maternita-congedi, mediazione-civile,
  multe-ricorso, pensione-guida, pensione-reversibilita, permesso-soggiorno,
  pignoramento-conto, salute-mentale-info, separazione-divorzio,
  successioni-info, testamento-biologico-dat, testamento-olografo,
  testamento-pubblico, unioni-convivenze, vaccini-obbligatori,
  whistleblowing-info.
- **L2 calculators, all 30**: acconti-calcolo, assegno-unico, buoni-fruttiferi,
  busta-paga-leggi, carte-revolving, cedolare-secca,
  collaborazioni-occasionali, compensazioni-f24, condominio-spese,
  conti-deposito, contributi-inps, ferie-permessi, fondo-emergenza,
  imposta-bollo, imu-calcolo, invoice-it, irpef-scaglioni, mutuo-tassi,
  plusvalenza-casa, plusvalenza-finanziaria, rateizzazione-debiti,
  ravvedimento-operoso, regime-forfettario, riscatto-laurea,
  ritenuta-acconto, spese-mediche-detrazioni, straordinari-info, tfr-fondo,
  tredicesima-info, xlsx-budget-it.
- **L1/L0 probes (3)**: hello-agent, email-formale-it, cv-europass.

Grok stays blocked (no local launcher, no subscription) — documented, not faked.

## Protocol (per wave, ~10-12 cells)

Same as `docs/TEST-PLAN-LOCAL-MATRIX.md`: one skill × one harness,
explicit file-read invocation, reply-only prompts, `qwen3:8b`
(never qwen3.8), tree clean after each run, honest ✅/❌ with notes.
Log waves in `docs/TEST-PLAN-LOCAL-MATRIX.md`.

## Waves completed

- Wave 1 (2026-09-28): hello-agent, invoice-it, frontend-design (vendor,
  outside corpus), tdd (vendor), brainstorming (vendor) × claude+codex —
  10/10 ✅ (see matrix log).
- Wave 2 (2026-09-28): imu-calcolo, irpef-scaglioni, acconti-calcolo,
  regime-forfettario, busta-paga-leggi × claude+codex — 4/10
  (memory-over-skill math failures, zero skill-file defects).
- Corpus coverage so far: 10/69 skills (14%). Next waves pick uncovered
  L3 first (highest risk), then remaining L2.
