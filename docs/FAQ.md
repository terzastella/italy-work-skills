# Frequently asked questions

## Do I need a subscription?

No. Installing and the skill calculators run fully offline on your PC.
(Repo maintenance checks like upstream validator installs or vendor HEAD
lookups may use the network.) You only need
whatever account your chosen agent itself requires.

## Does it work offline?

Yes. Installed skills are text files plus small local calculators. Nothing
in them calls the internet — except the agent's own model, which is its
business, not this repo's.

## Where do my data go?

Nowhere. You type figures into your agent; the skill text never leaves your
machine. Redact names and fiscal codes before sharing payslips or contracts.

## Why won't it give me a verdict?

By design. On legal, tax, health, family, and inheritance matters the skills
map the procedure and refer you to a professional (accountant, notary,
patronato, lawyer, doctor). A wrong verdict costs money; a map doesn't.

## How fresh are the figures?

Every amount states its year (look for it next to each number). Italian rules
change yearly — if a figure's year is old, ask for the current one or check
the official source cited next to it.

## Which agent should I use?

Any of the 9 supported ones (see `INSTALL.md`). Skills share the same format
and core logic everywhere, but discovery, invocation, and tool permissions
vary by host (see `COMPATIBILITY.md`); only the agent's own smarts differ.

## What are "vendors"?

24 skills by other authors (Anthropic, Matt Pocock, Superpowers team),
copied byte-for-byte and pinned to a version. They are opt-in and read-only:
issues about them go to their authors, not here.

## What if the agent invents data?

Tell it the skill's rule back: never invent VAT IDs, names, dates, or codes —
`[TODO]` placeholders instead. Small models invent more; bigger ones less.
Report systematic cases as bugs (see `CONTRIBUTING.md`).

## Can I suggest a new skill?

Yes — open an issue with the `new-skill` template (`.github/ISSUE_TEMPLATE/`),
or follow `CONTRIBUTING.md` and send a pull request.

## Who maintains this?

A small team — issues and pull requests welcome. Every change passes automated gates
(validation, security, coherence, install dry-run, example checks) before merge.
