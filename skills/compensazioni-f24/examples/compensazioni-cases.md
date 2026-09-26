# compensazioni-f24 cases

## Good: IRPEF credit vs IMU due (script)

Input: €2.000 IRPEF credit, €1.500 IMU due [sample data].

Run: `python skills/compensazioni-f24/scripts/compensa.py --crediti 2000 --debiti 1500 --soglia-visto 5000 --year 2026`

Output: compensato €1.500, residuo credito €500 + codes + visto check (threshold year-stated) +
`credits exist and certain — verified first.`

## Good: visto triggered

Input: €8.000 credit, €3.000 due, same threshold [sample data].

Output: compensato €3.000 + `Visto di conformità NECESSARIO sopra soglia — no compensation without it.`

## Bad: expected credits

Input: "mi aspetto un credito il prossimo anno, compenso ora?" [sample data].

Output: stop. `"Expected" credits do not compensate — certain and existing only, stated bluntly.`
