# Working in this vault

This folder is a Zettelkasten with a wiki layer on top. It holds one person's thinking on [subject], one idea per note, with the evidence for each idea and the pushback it has drawn. It is meant to be read selectively, never whole.

<!-- Fill in the bracketed parts. Keep this file short: it is read at the start of
     every session, so every line here costs every session. Anything that is only
     true of one job belongs in a routine note in 20 Maps/, not here. -->

## State
<!-- Two or three lines, kept current: how much is processed, whether the Inbox is
     empty, when the last big pass happened. An assistant reads this to know whether
     it is looking at a finished vault or a half-built one. -->
[N] works processed. `00 Inbox/` is [empty / holds N items]. About [N] notes. The vault is self-contained; nothing outside this folder is required.

## Layout
Six folders by stage of work, not by subject, numbered so they sort in the order the work happens: `00 Inbox` (raw, unprocessed), `10 Notes` (permanent: ideas, vocabulary, people, objections, mission), `20 Maps` (hubs, indexes, ledgers, routines, briefing packs), `30 Daily` (the daily log and the weekly synthesis), `40 Sources` (the works themselves, feedback captures, citation notes), `99 Templates`. The *kind* of a note is its frontmatter `type:`; to list all objections, search `type: objection` in `10 Notes/`, not a folder.

Material that is not thinking — product links, reference lists, resources — does not belong in these six at all. Give it a folder of its own outside the slip-box (`98 Resources`, say). The inbox drain has a bucket for exactly this.

## If the owner also keeps a teammate stack
The stack answers *who is speaking and how*; this vault answers *what is true and where it came from*. Load the stack whole at the start of a session, because it is small. Never load this vault whole; take one pack from `20 Maps/`. Precedence when they conflict: the stack wins on voice, style and working method; the vault wins on facts, evidence, what has already been said, and what has been promised. The contract is in `20 Maps/Working with the teammate stack.md`.

## Read first
- `20 Maps/00 Start Here.md` for the map.
- The mission notes in `10 Notes/` (`type: mission`): why the work exists, who it is for, the promises made in public, and the voice. Every draft must honour the promises note.
- Never build on anything in `00 Inbox/`; it is unprocessed. Process it first (see `20 Maps/Inbox — how to empty it.md`).

## Conventions
- **One idea per note. The title is the claim.** When you draft, cite the notes you used by `[[title]]`. When a draft makes a claim that has no note, say so.
- Frontmatter `type:` is one of `mission | zettel | vocab | work | feedback | person | objection | source | series | map | claude | daily | weekly | template`.
- Frontmatter `status:` on zettels: `seedling` (captured, unverified), `growing` (used once, has links), `evergreen` (used across works, sourced). On sources: `sourced | partial | needs-source | contested`.
- Frontmatter `evidence:` on zettels: `external` (an outside source is cited and it says what the note says), `partial` (some sourced, some not, gap written down), `observed` (rests on the owner's own experience and says so), `argument` (a framing or aphorism, not an empirical claim; nothing to cite), `asserted` (an empirical claim made with nothing behind it yet). See `20 Maps/Triage — the evidence field.md` before treating the count of `asserted` notes as a backlog.
- **Every zettel has five sections: The idea, Not true when, Why it matters, Related, Sources.** The *Not true when* section is the boundary of the claim. Read it before applying the idea; never draft a line that falls inside it. When you propose a new zettel, you must supply its *Not true when*.
- **The Sources section holds two different things and they are not interchangeable.** *In the work* is where the idea was said: provenance, not evidence. Saying it in three places is not three sources. *Outside the work* is what would make a stranger believe it: a study, a dataset, a statute, a report, a named expert on the record. See `99 Templates/Template — Zettel.md` for the three tests.
- **Source notes are about the source, not the claim.** One note per source, named after the source, because one source can back several zettels. Two fields are required: the citation, and the source's own words or figures, verbatim and short, that the zettels get checked against. The other fields in `99 Templates/Template — Source.md` are for when the source and the claim do not quite match.
- **Maturity lives in `status:`, topics live in `tags:`.** One to five topic tags, for querying. A tag is not a second title and never records status, which would then be recorded in two places and agree in neither.
- **A link is a claim.** Every link owes an answer to *what would make this connection false?*, and a word or two after it saying what it is for. Surprising edges are the valuable ones; edges reached for to confirm a hunch are cheap, and a vault full of them is a well-cross-referenced echo chamber.
- **The graduation rule.** A restatement inside a source note moves to `10 Notes/` only when it says something the author did not: a disagreement, a generalization, or a connection that surprised you. Most restatements never graduate, and that is the correct outcome rather than a backlog.
- Numbers, dates and quotations carry their origin. Where datasets conflict, prefer the more conservative figure. Personal observations are labelled as the owner's, not as research.
- Terms of art are kept as the owner uses them, with a plain gloss on first use, in a `type: vocab` note.
- Do not imitate the owner's voice unless asked; analysis can be plain. The voice note in `10 Notes/` is the observed baseline; the stack's `02-voice.md`, if there is one, is the rule.

## The three cadences
Daily notes log what happened (`30 Daily`, one per working day). **The weekly synthesis connects them** — one hour, `20 Maps/Week — how to synthesise.md`, and it is where a week of separate notes becomes thinking rather than expensive bookmarks. If the owner also keeps a teammate stack, its audit is quarterly and asks whether any of this is still working. The weekly one is the most often skipped and does the most compounding.

## When asked to process new material
Follow `20 Maps/Inbox — how to empty it.md`. In short: read the work, mark what is new (search `10 Notes/` first, because ideas recur), write the work note, write three to eight zettels with real *Not true when* sections, read the feedback properly, source one claim, update the hub and the ledgers, write the daily note.

## When asked to research a claim
1. Start from `20 Maps/Sources — index.md`. It ranks what is unsourced by how much weight it carries.
2. Find the actual paper, statute or dataset. A journal name and a year is not a citation. If the claim says "a study found", tracking down the study *is* the task.
3. Write or rewrite the citation note in `40 Sources/` to `99 Templates/Template — Source.md`. Fill in **Sample and scope** and **Gap between the claims and the source** honestly. A gap you name is worth more than an overreach.
4. Update the zettels that rest on it: the `evidence:` field, and the *Outside the work* line.
5. **Report every discrepancy you find, even a small one.**
6. **Never invent a citation.** If you cannot find the source, say so and write down where to look next. `needs-source` is an acceptable outcome; a plausible-looking reference that does not exist is the one unrecoverable mistake in this vault.

## When asked to draft something
1. Ask which zettels the draft should use, or propose a set from `10 Notes/` (zettels and objections).
2. Draft to the structure in `99 Templates/Template — Work.md`, or to whatever structure the owner names.
3. Finish with three lists: claims in the draft with no outside source, ranked by how much weight they carry; new zettels the draft would create, each with its *Not true when*; and any claim whose citation note records a gap.
4. If the draft would pay off or break a promise in `20 Maps/Commitments — promises made in public.md`, say which.

## When asked to answer pushback
1. Find the matching note via `20 Maps/Objections — index.md`. Reuse the owner's own reply; do not invent a new position.
2. If no objection matches, draft a reply *and* a new objection note from the template.

## When asked to triage or upgrade notes in bulk
Read `20 Maps/Triage — the evidence field.md` first. Two rules override anything else: **never run a batch pass that adds sources across many notes at once**, and **propose reclassifications as a list for the owner to confirm rather than applying them**.

## Do not
- Do not merge notes into long documents. Split, link, and keep titles as claims.
- Do not treat anything in `00 Inbox/` as settled, or anything in `_tools/` (if present) as source material.
- [Any editorial commitment the owner has made that survives every other instruction goes here, so it is visible from both the stack and the vault.]
