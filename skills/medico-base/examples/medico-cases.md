# medico-base cases

## Good: moved to Bologna

Input: residenza moved, need new GP [sample data].

Output: residenza-first order + ASL change steps + availability note +
`tourist rules do not apply — resident path used.`

## Bad: tourist shortcut

Input: resident asking the tourist path "per fare prima" [sample data].

Output: `Tourist rules do not apply to residents — residenza-first order, ASL steps. Shortcuts refused plainly.`
