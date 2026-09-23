# archive/ — pre-restart generic skills (NOT installed)

Kept for reference after the 2026-09-23 Italy restart. These skills are
complete and validated, but out of positioning (generic dev/SEO/content).
Nothing here is installed, validated, or listed in indexes:
`scripts/install.py`, `validate.py` and `security-check.py` only scan `skills/`.

- `batch1-generic/` (17): smart-commit, git-status-express, changelog-gen,
  release-notes, code-review-it, systematic-debug, refactor-plan, test-gen-it,
  api-docs-it, readme-gen, commit-scope, pdf-extract-it, csv-clean,
  web-research, source-cite, json-clean, prompt-pack-it
- `batch2-seo/` (18): seo-audit, meta-tags, headline-it, content-calendar,
  keyword-map, content-gap, blog-outline, social-post-it, newsletter-it,
  landing-copy, product-desc-it, faq-gen, video-script-it, podcast-outline,
  infographic-brief, cta-optimize, readability-fix, repurpose-content

To reuse one: `cp -r archive/<batch>/<name> skills/<name>` then update
`catalog/skills.json`, `llms.txt`, `.claude-plugin/plugin.json`,
`README.md`, `docs/COMPATIBILITY.md` and re-run the gates.
Full backup: `../ai-skills-backup-2026-09-23.zip`.
