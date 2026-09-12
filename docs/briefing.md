# Briefing: packs and recipes

The operational version is inside the vault at `vault/Maps/How to brief an assistant from this vault.md`. This page explains the idea of a pack and when to build one.

## What a pack is

A pack is a pre-assembled brief for a job that comes up more than once: drafting the next piece in a series, answering a recurring kind of pushback, working the research queue. It is a note in `Maps/` that lists the five to twelve vault notes to hand the assistant, in order, and the ask written out so it does not have to be re-invented.

`tools/pack.py` reads the wikilinks in a pack note and writes the bodies of those notes into one file for pasting. That is the whole mechanism. A pack is a query over the vault, saved.

## When to build one

The second time a job comes up. Not the first, because you do not yet know which notes the job needs, and not the fifth, because by then you have re-assembled the same brief four times. The teammate stack calls this the leverage ladder: session, then saved prompt, then template, then automation. A pack is the template rung.

## What goes in a pack

Four things, in this order.

A classification step, because most instances of a recurring job are one of a few kinds and each kind needs different notes. "Most critical feedback is one of three moves: it has always been so; she chose it; you have no standing." Each move points at the objection notes that handle it.

The notes to load, as wikilinks. The mission notes that set the frame, the zettels that do the work, the objections to pre-empt. Five to twelve. If the list is longer, the job is two jobs.

The ask, written out. What to reuse, what not to invent, how long, and what to report at the end. The reporting lists matter most: claims with no outside source, new zettels the output would create with their *Not true when*, and any promise it pays off or breaks.

An afterwards step, saying what to write back into the vault when the job is done. A pack that only reads from the vault is half a pack; the other half is the objection note, the person note, or the ledger row that the job produced.

## The recipes

Beyond packs, five jobs come up in almost every vault, and the vault's briefing note carries a recipe for each: draft a new piece; reply to hard pushback; check a draft for drift against the notes; tighten a draft against the spine; and answer "what have I already said about this". None of them involves pasting a whole document.

## What to say every time

Three lines belong at the top of every ask, and the stack's `05-rules.md` is a fine place to keep them so they are said once. The title of the note is the claim: use it, do not restate it. Cite notes by `[[title]]` in the output so the work can be checked. Numbers come with a source note or with the words "needs source."
