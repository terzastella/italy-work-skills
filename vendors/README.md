# vendors/ — third-party skills (read-only copies)

Curated, byte-identical copies of other projects' skills, pinned to the commits in
`upstreams.lock.json`. **Never hand-edit files in here**: to update, re-copy from
upstream at a new pinned commit (see `scripts/sync-vendors.py`).

## What is here (24 skills)

- `anthropics-skills/` (10, Apache-2.0): Anthropic's official example skills.
  Each folder keeps its upstream `LICENSE.txt`.
- `mattpocock-skills/` (6, MIT): engineering skills, flattened from `skills/engineering/`.
  License: `third-party/LICENSE-mattpocock.txt`.
- `superpowers/` (8, MIT): obra's workflow core.
  License: `third-party/LICENSE-superpowers.txt`.

## What is NOT here (on purpose)

- `docx`, `pdf`, `pptx`, `xlsx` from `anthropics/skills`: **source-available,
  not open source**. Link only — see `../catalog/vendors-manifest.json`.
- Grok built-in skills and Codex skills: no public repo to copy; use our
  install guides in `../.grok/README.md` and `../.agents/skills/README.md`.

## Install (opt-in)

Our skills install by default; vendor skills only on request:

```bash
python ../scripts/install.py --all                          # ours only
python ../scripts/install.py --all --source vendors         # ours + vendors
python ../scripts/install.py --skill tdd --source vendors   # one vendor skill
```

## License texts

- `third-party/LICENSE-mattpocock.txt` (MIT, Matt Pocock)
- `third-party/LICENSE-superpowers.txt` (MIT, Jesse Vincent / obra)
- Anthropic: per-skill `LICENSE.txt` inside each `anthropics-skills/<skill>/`
  (`doc-coauthoring` covered by the repo README's Apache-2.0 statement).
- Full notices: `../docs/THIRD-PARTY-NOTICES.md`.
