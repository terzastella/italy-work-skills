# git-status-express output format

Fixed lines, max 15 total:

1. `Repo: <name> | Branch: <branch> | Clean/Dirty`
2. `Staged: <n> | Unstaged: <n> | Untracked: <n>`
3. `Areas touched: <area> (<n>), ...`
4. `Main files: <max 3 with +/-lines>`
5. `Next step: <1 suggestion>`

Tags: `[large]` for >1MB or binary files. `[new]` for untracked.
If `git diff --stat` is empty but status dirty → untracked only, say so.
