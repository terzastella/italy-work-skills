# Bisection technique (isolate the bug)

1. Find one working case and one failing case.
2. Halve the difference (input, file, commits with `git bisect`, lines).
3. Repeat until 1 culprit remains.
4. Rules: change 1 variable at a time, log every attempt (command + outcome).

Useful commands: `git bisect start/good/bad`, `git stash` to isolate changes,
`python -X dev` for warnings, timestamped logs for flaky bugs.
