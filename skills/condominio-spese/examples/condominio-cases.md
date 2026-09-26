# condominio-spese cases

## Good: riparti mismatch (script)

Input: rendiconto €48.000, unit millesimi 85/1000, charged €4.500 [sample data].

Run: `python skills/condominio-spese/scripts/riparto.py --totale 48000 --millesimi 85 --addebitato 4500`

Output: `85/1000 × 48.000 = €4.080 expected vs €4.500 charged → €420 gap:
ask administrator for breakdown. Contest terms (year-stated) if delibera confirmed.`
Math first, accusations never.

## Bad: fraud claim

Input: any gap found [sample data].

Output: `Gap = question for the breakdown, never a fraud claim. Delibera first, contest terms second.`
