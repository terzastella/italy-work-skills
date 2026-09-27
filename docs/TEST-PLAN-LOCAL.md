# Local-agent test log — OpenCode + Ollama (separate track)

Official 5×3 matrix (`docs/TEST-PLAN.md`, Claude/Codex/Grok) is untouched.
This file logs the local track: first real-agent runs anywhere in this repo.

## Environment

- Harness: OpenCode (repo `opencode.json` → Ollama provider, `localhost:11434`)
- Model: `qwen3:8b` via Ollama 0.32.13 (qwen3.6:23GB chosen first, infeasible here:
  >10 min/prompt on this hardware — recorded, retry on stronger iron)
- Skills installed: 254 ours + 3 vendors (frontend-design, tdd, brainstorming)
  in `.opencode/skills/` (gitignored) via `install.py --agent opencode`
- Date: 2026-09-26. One skill per run, explicit invocation
  (`Use the <skill> skill now...`).

## Results

| # | Skill | Prompt | Verdict | Notes |
|---|---|---|---|---|
| 1 | hello-agent | `hello skills` (implicit) | ❌ | Generic greeting, skill not triggered, emoji used |
| 2 | hello-agent | explicit invocation | ✅ | Correct table, path, next-test line; agent self-ID wrong ("Codex" instead of OpenCode) — model limit, not skill bug |
| 3 | invoice-it | invoice 10h×€50 VAT 22% | ✅ | Read fixture JSON, computed €610, missing-data honesty; wrote `draft-invoice.txt` into installed copy (cleaned) |
| 4 | frontend-design | bakery hero, <15 lines | ✅ | Brand-aware draft + read LICENSE; wrote `outputs/` into installed copy (cleaned) |
| 5 | tdd | add(a,b) test-first, <20 lines | ✅ | Test + minimal impl, edge cases; wrote `tests/test_add.py` into REPO (removed immediately) |
| 6 | brainstorming | scope shopping-list app, questions first | ❌ | No questions asked; tried to create skill, failed; hallucinated `budget-xlsx`; wrong cross-refs — model limit on methodology skills |
| 7 | imu-calcolo | seconda casa rendita 850 A/2, 2026 | ✅ | Ran `imu.py`: 142.800 / 1.513,68 / 756,84+756,84 exact; assumed 10.6 rate openly — asked to verify (minor caveat) |
| 8 | irpef-scaglioni | 35k gross 2025 | ✅ | Ran `irpef.py` with dated table: slices + 8190 + 23.4%/25% exact |
| 9 | acconti-calcolo | forfettario, prior 5.820 | ✅ | Ran `acconti.py`: threshold + split stated + dates pointer (minor: presented split as AdE rule rather than stated input) |

Score: **7/9 ✅** (2 model-limit ❌, 0 skill-content bugs).

## CPU-only run — llama3.2:3b, num_gpu:0 (2026-09-26, training-safe)

Same machine was training (RTX 3060 busy) → qwen runs suspended. Direct
Ollama API with `num_gpu: 0` (no server restart, no VRAM touched, ~20s/cell
on CPU). Skill text pasted in-prompt (harness auto-load already proven).
Weak signal by design: 3b models can't operationalize long instructions.

| # | Skill | Result | Notes |
|---|---|---|---|
| 1 | hello-agent | ✅ | Correct table, agent, path 0.2 — better than 8b run |
| 2 | invoice-it | ❌ | Structure followed, math failed (10×50=50, total 61 vs 610) — model limit |
| 3 | imu-calcolo | ❌ | Tappe echoed, zero computation — model limit, no numbers produced |

CPU-track: **1/3 ✅**, 0 skill-content bugs. Scripts only help inside agentic
harnesses (the model can't run them here) — qwen3:8b+opencode cells stay
the reference for script skills.

## Observations for skill design

1. Agents write outputs INTO installed skill dirs (and once into repo `tests/`).
   Harness hygiene matters: never keep editable state next to skills; check
   `git status` after every agent session in this repo.
2. Small models need explicit invocation; auto-trigger is unreliable at 8b.
   Skills with scripts performed best (tool call anchors the behavior).
3. Methodology skills (brainstorming) fail on small models — expected; retest
   on frontier models in the official matrix.
4. Fixed during session: `hello-agent` hardcoded `0.1` in output table → 0.2
   (keep paired with `metadata.version`).

## To collapse into COMPATIBILITY.md

Local-track section added (this run). Official matrix still pending (big-3 accounts).
