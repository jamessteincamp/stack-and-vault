# Working in this repository

This is a toolkit, not a body of work. It holds a template stack, a starter vault, an example vault, and the tools and documents that explain how they fit. If you are reading this because someone has copied the toolkit and started filling it in, the rules below still apply; the material will just be theirs instead of the example's.

## Read, in this order

1. `stack/`, whole. Eight short files plus the audit log. It says who you are working for and how they want to be worked with. Weight `04-context.md` most for *what to do today* and `05-rules.md` for *how to do it*.
2. `vault/CLAUDE.md`. The conventions for every note in the vault, and the routines for the recurring jobs: processing new material, researching a claim, drafting from notes, answering pushback.
3. One pack from `vault/20 Maps/`, never the vault whole. See `docs/briefing.md`.

## Precedence

When the stack and the vault disagree: the stack wins on voice, style and working method; the vault wins on facts, evidence, what has already been said, and what has been promised. The full contract is in `docs/the-contract.md`.

## Two rules that hold everywhere

- **Never invent a citation.** "Needs source" is an acceptable outcome; a plausible-looking reference that does not exist is the one unrecoverable mistake in a vault.
- **Propose, do not apply,** for anything that changes many notes at once: reclassifying evidence, merging notes, renaming. Give the list; the owner confirms.

## The tools

`tools/vault_check.py <vault>` finds broken links, invalid frontmatter and idea notes missing their *Not true when*. Run it before reporting a job finished. `tools/pack.py` assembles a briefing pack into one file. `tools/stats.py` counts what is in a vault. All three are Python 3 with no dependencies.
