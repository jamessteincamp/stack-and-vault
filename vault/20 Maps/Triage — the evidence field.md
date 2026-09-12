---
type: claude
kind: routine
---
# Triage — the evidence field

A vault built from existing work starts with almost every zettel marked `evidence: asserted`, because the notes record what was said without recording what is behind it. This note is the plan for fixing that, and the place to track it.

**Do not run a batch pass over the whole vault.** Asking an assistant to add sources to three hundred notes in one go is the fastest way to ruin a vault. A fabricated reference looks exactly like a real one until somebody opens it, and checking three hundred notes costs more than researching thirty. Work one claim at a time, and open every source.

## The backlog is smaller than it looks

Most `asserted` notes are not research tasks. Sort them into three piles:

| | What it is | Becomes |
|---|---|---|
| Contains a number, a year, or a reference to a study | An empirical claim with nothing behind it | stays `asserted` — the real backlog |
| Rests on the owner's own experience, and says so | Lived experience, labelled | `observed` |
| A framing, an aphorism, a way of seeing | Rhetoric, not a claim | `argument` |

*Money is the door, not the house* is not a claim missing a citation; it is rhetoric, and asking it for a source is a category error. In a vault of three hundred asserted notes, the genuine backlog is typically a tenth of that, and because several rest on the same citation note, the research is fewer pieces still.

## Step one: triage (one session, before any research)

Ask the assistant:

> Read `20 Maps/Triage — the evidence field.md`. Go through the zettels with `evidence: asserted` and propose a new value for each — `observed` where the note rests on the owner's own experience and says so, `argument` where it is a framing or an aphorism rather than an empirical claim, and leave `asserted` where a real citation is missing. Give me the proposal as a list, grouped by proposed value, with one line of reasoning each. Change nothing until I confirm.

The point of the proposal step is that the rule of thumb is fallible. A note can mention the owner's own kitchen and still make a general claim. The owner confirms; the assistant applies.

After this, searching `evidence: asserted` returns the genuine backlog and nothing else.

## Step two: the research, by source note rather than by zettel

Several zettels rest on one citation note. Upgrading the citation note upgrades all of them; working note by note repeats the same research. Ask the assistant:

> Take the top unticked row in the worklist in `20 Maps/Triage — the evidence field.md`. Follow the *When asked to research a claim* routine in `CLAUDE.md`. Find the actual paper, statute or dataset, write or rewrite the citation note in `40 Sources/`, fill in Sample and scope and the Gap between the claims and the source honestly, then update the zettel's `evidence:` field and its *Outside the work* line. Report any discrepancy you find, however small. If you cannot find the source, say so and write down where to look next — never invent a citation.

Then tick the row, note the date, and stop. One per session is the right pace.

## Step three: the toll, which matters more than the queue

Backlog projects die. This one will too, if it depends on finding a spare hour.

The mechanism that actually works is a toll on use: **any note going into a new piece of work gets its source checked before the work is published.** Effort then lands exactly on the notes that carry weight, and notes nobody ever uses stay unsourced, which is correct. The queue below is what to do on a quiet day, not the engine.

## The worklist

Ranked by how many other notes link to each one, which is the best available proxy for how much weight the claim carries (`python3 tools/stats.py <vault>` prints it). Tick the box and date it when the note has a real citation behind it.

| ✓ | Links in | Note | Citation note | Done |
|---|---|---|---|---|
| ☐ |  | [[ ]] | — |  |
