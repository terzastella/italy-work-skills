# changelog-gen cases

## From commit list

Input (`git log v0.1..HEAD --oneline`):
```text
a1b2 feat(skills): add json-clean
c3d4 fix(installer): also copy assets
e5f6 wip docs work
```

Output:
```markdown
## [0.2.0] - 2026-09-23

### Added
- `json-clean` skill with validation and auto-fix

### Fixed
- Installer also copies `assets/` subfolders
```

Note: `wip` merged/dropped, not its own line.

## Empty range

Output: `No changes between v0.2 and HEAD.`
