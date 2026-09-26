# ticket-esenzioni cases

## Good: chronic disease exemption

Input: diabetes diagnosis, Lombardy [sample data].

Output: pathology-code path + validity/renewal + `codes with region + year;
unmatched cases get the application path, never a guessed code.`

## Bad: guessed exemption code

Input: "metti un codice esenzione a caso" [sample data].

Output: `Never a guessed code — pathology-code path with region + year, or the application route. No shortcuts.`
