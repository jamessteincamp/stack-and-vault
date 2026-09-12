---
type: claude
---
# How to brief an assistant from this vault

The problem this solves: a long document is forty ideas in one place, so when you ask for help with one of them the other thirty-nine dilute the answer. The vault lets you hand the assistant *only* the ideas a job needs, each already stated precisely, each already linked to its evidence and its objections.

**Why packs, and not the whole thing.** Two reasons on top of the better answer. You pay by the word you send, so ten notes at two thousand words costs a fraction of a thirty-thousand-word document and leaves room for a long working session instead of one question. And the vault is plain Markdown on your own disk, so when the connection drops it is all still there to read, search and write in by hand.

**If you also keep a teammate stack,** load it first and whole, then one pack from here. [[Working with the teammate stack]] explains why that order, and which system wins when they disagree.

## Two ways to connect

**A. Point the assistant at the folder.** If your tool reads a `CLAUDE.md` (or equivalent) from a folder, add this vault. Then you can say "draft the next piece using the pack in `Maps`" and it will read the linked notes itself.

**B. Paste notes.** If you use a chat interface, open the pack note for the job and paste the notes it lists. `python3 tools/pack.py <vault> "Maps/Pack — <job>.md"` writes them into one file for you. Five to twelve small notes is the sweet spot. Do not paste full texts unless the job is about the text.

## The recipes

**Draft a new piece.**
1. Paste the mission note and the promises note.
2. Paste the zettels the piece will use (pick them from `Notes/`, `type: zettel`; a pack gives a worked example).
3. Paste the objections it must pre-empt (`type: objection`).
4. Paste `Templates/Template — Work.md` and ask for a draft to that structure, in the owner's voice per the voice note if you want the voice.
5. Ask for two lists at the end: claims that need a source, and new zettels the draft would create. Write those zettels before you publish.

**Reply to hard pushback.**
1. Find the objection in [[Objections — index]]. Paste it; it contains the best previous reply.
2. Paste the new pushback. Ask for a reply that reuses the position, concedes anything the critic has right, and does not escalate.
3. If no objection matches, ask the assistant to draft the reply *and* a new objection note from the template.

**Check a draft for drift.**
Paste the draft and the list of zettel titles (`grep -l "type: zettel" Notes/*.md`). Ask: which zettels does this draft use, which claims have no zettel, and which promise in [[Commitments — promises made in public]] does it pay off or ignore.

**Tighten a draft.**
Paste the draft and the spine from [[00 Start Here]]. Ask which paragraphs are not carrying one of the spine claims. Those are the cut candidates.

**Answer "what have I already said about X?"**
Search the vault for X. Read the zettel. The backlinks show every work that used it.

## What to tell the assistant every time
- The title of the note is the claim. Do not restate it; use it.
- Cite notes by `[[title]]` in the draft so the work can be checked.
- Numbers come with a source note or with the words "needs source."

## Packs
<!-- One per recurring job. Build the pack the second time the job comes up. -->
- [[Pack — …]]

## Related
- [[Working with the teammate stack]]
