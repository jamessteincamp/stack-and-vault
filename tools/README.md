# Tools

Three small scripts. Python 3.8 or later, standard library only, nothing to install. Each takes the vault folder as its first argument and works on any folder of Markdown files that follows the conventions in `vault/CLAUDE.md`.

- **`vault_check.py <vault> [--strict]`** — finds what quietly goes wrong: notes with no frontmatter or an unknown `type:`, invalid `status:` or `evidence:` values, zettels missing one of their five sections or with an empty *Not true when*, links into `00 Inbox/`, ghost links to notes not yet written, and an Inbox that is not empty. Exits 1 on errors. Run it before reporting a job finished.
- **`pack.py <vault> "20 Maps/Pack — <job>.md" [-o brief.md]`** — assembles a briefing pack into one file for pasting: follows the wikilinks under the pack note's *notes to load* heading (or every link in the note, if it has no such heading) and writes each note's body, stripped of frontmatter and comments, into a single Markdown file. Prints the word count, which is what you are about to pay for. `--titles "A" "B"` builds an ad-hoc brief without a pack note.
- **`stats.py <vault> [--top N] [--queue]`** — counts notes by type, zettels by status and evidence, sources by status, Inbox items and ghost links, and ranks notes by how many others link to them. `--queue` restricts the ranking to zettels still marked `asserted`: that is the research queue in priority order.

`vaultlib.py` is the shared parser the three import; keep it beside them. It identifies folders by **stage** rather than by exact name — a leading number is stripped and the rest lower-cased — so `00 Inbox` and `Inbox` are both the inbox, and the tools run on a vault that numbers its folders for sidebar order and on one that does not.

## What a saved query does better

The checker is a gate: run it before you commit and it tells you what is broken. It is not a dashboard. If you work in Obsidian, its Bases can build the standing views from the frontmatter this vault already writes, and three of them earn their keep: the inbox sorted by age, everything missing a `status:` or `type:`, and everything older than a fortnight. That is strictly better than a hand-maintained table of what needs attention, which goes stale the first week you are busy. The tools stay useful for the things a query cannot do — resolving wikilinks, checking that a zettel has its boundary section, assembling a pack.

## Keeping the tools inside a vault

If you want a vault to be self-contained, copy this folder into it as `_tools/` and call the scripts from there: `python3 _tools/vault_check.py .`. The checker skips `_tools/` when it walks the vault, and the vault's `CLAUDE.md` tells an assistant never to treat anything in `_tools/` as source material.

## What is deliberately not here

Ingest scripts. How a work and its feedback get from wherever they live into `00 Inbox/` depends entirely on where they live: a transcript tool for talks, an export for a mailing list, a comment fetcher for a video platform. Those belong beside the vault that uses them, with their own README naming what they need. Two rules from experience with one such pipeline, whatever yours turns out to be: make it check its own completeness against a count the source reports, and refuse to say it succeeded until they match; and keep the raw input it produced in an archive folder that no note links to.
