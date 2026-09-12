---
type: map
kind: routine
---
# Inbox — how to empty it

Everything that lands in `00 Inbox/` is raw material that has not been turned into notes yet. The goal is an empty inbox, not a tidy one. Nothing in there should be linked to from a permanent note until it has been processed.

**Capture stays dumb and fast — that is the whole point of an inbox.** The thinking happens when you *drain* it, not when you fill it. One nudge at capture, then a sort when you process.

## At capture: one nudge, zero forms

Write a sentence with a verb, not a topic word. The shape of the title already tells you what you caught.

- ✗ "Compounding" · "Beekeeping" — a topic. That is a bookmark, not a thought.
- ✓ "Compounding needs consistent low effort, not rare high effort" — a claim. It promotes itself into a note.

Nothing else is required. No frontmatter, no template, no structure: a title and a sentence of context.

## When you drain: four buckets

Sort each item into one of four, and be willing to use the last one.

- **Seed** — a claim, or a question with a claim inside it → promote it to a note, or feed it to a map.
- **Resource** — links, products, courses, reference material → move it *out* of the slip-box, to wherever you keep resources. These were never notes.
- **Question** — something you want to chew on but cannot yet state → keep it as a question note, or hang it on a map under *Tensions*.
- **Did its job** — it was only there to clear your head → delete it, guilt-free.

**One question per seed:** *can I state this as a single sentence?* Yes → it is ready to become a note. No → it is not a failed note, it is a question that needs more oblique looking.

An inbox that is never empty is the same disease as a pile of unread highlights, and it is the most common reason these systems collapse. The drain is what keeps it a workbench instead of a landfill.

## To process one new work (twenty to thirty minutes)

1. **Capture the material.** The full text of the work, and whatever came back: comments, reviews, replies. Drop both in `00 Inbox/`. If a script produced them, keep the raw input somewhere labelled *archive, not source material*, so timestamps or original formatting survive.

2. **Read the work and mark what is new.** Three to eight claims per work is typical. Search `10 Notes/` for a few words of each first: ideas recur, and a restatement belongs in the existing note rather than in a new one. If the new work restates a claim in better words, add the better words to the existing zettel.

3. **Write the work note** from `99 Templates/Template — Work.md`, move it and the full text to `40 Sources/`, name the text `Text — <identifier>` (or `Transcript — <identifier>`), and set `status: processed`.

4. **Write the new zettels** in `10 Notes/`. One claim per note, title as the claim, `source:` pointing at the work note, and a real **Not true when** for each. Link each to at least two existing notes.

5. **Read the feedback properly.** This is where half the value is. For each response that matters: a new objection note if the pushback is new, a person note if they are substantive or recurring, a line in [[Commitments — promises made in public]] if anything was promised.

6. **Source one claim before you move on.** Pick the heaviest number or borrowed frame in the work and find what is actually behind it, following *When asked to research a claim* in `CLAUDE.md`. One per work is enough; the backlog only shrinks if the new material stops adding to it. Set `evidence:` on each new zettel honestly, and write the *Outside the work* line even when it says *Needs source*.

7. **Update the series hub** and any index the work changes.

8. **Write the daily note** saying what you processed and what you noticed. If you skipped the day, write why — the pattern in your own skipping is data.

## Three cautions

- **Do not skip the feedback.** The objection notes are the most reusable thing in the vault, and the audience commissions more of the work than it looks.
- **A claim repeated is not a claim sourced.** A number that appears in five works and has never been traced to a paper reads like corroboration and is not. Only the *Outside the work* line counts.
- **Check for a collision before naming a zettel.** The vault is more useful with one note and two sources than with two near-identical notes.

## Let a query do the triage

Hand-maintained lists of what needs attention go stale; a saved query does not. `python3 tools/vault_check.py <vault>` warns when the inbox is not empty. If you work in Obsidian, its Bases can build three views from the frontmatter this vault already writes, and they are the three worth having: everything in the inbox sorted by age, everything missing a `status:` or `type:`, and everything older than a fortnight. The third one is the one that stings, which is the point.

## Related
- [[00 Start Here]]
- [[Triage — the evidence field]]
- [[Week — how to synthesise]]
