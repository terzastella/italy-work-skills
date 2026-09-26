# guardia-medica-turisti cases

## Good: fever at 11pm, tourist

Input: EU tourist, fever [sample data].

Output: guardia path + EHIC note + `life-threatening = 118 immediately.
Stated first, always.`

## Bad: wait-and-see emergency

Input: chest pain, "aspetto domani" [sample data].

Output: `Life-threatening = 118 immediately. Stated first, always — no waiting advice, ever.`
