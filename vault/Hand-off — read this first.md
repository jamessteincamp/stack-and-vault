# Hand-off — read this first

<!-- Write this page for the person who will own the vault if it is not you, or for
     yourself in a year. One page. What it is, what it is for, the four rules, where to
     start, and how to get a copy. docs/handing-off.md in the toolkit explains the test
     this page has to pass. -->

This is a Zettelkasten built from [what], as of [date]. It exists to solve one specific problem: long documents are hard for a person to hold in their head and hard for an assistant to work from.

**Nothing in here is invented.** Every claim is [the owner's], quoted or closely paraphrased from [their own work]. Where a number needs a source and does not have one, the note says so. [If anyone else has written anything in the vault, say what and where, and mark it at the top of the file.]

## What it is for

[Two paragraphs. The problem in the owner's own terms, and what the vault does about it. The difference is granularity: a long document holds a thousand thoughts in one file, so when you ask for help with one of them the rest dilute the answer. The vault holds the same thinking as separate claims, each with its evidence, its limits, and links to everything it connects to.]

## The four rules

1. **One idea per note.** If a note needs a second heading, it is two notes.
2. **The title is the claim.** You should be able to read the file list and hear the argument.
3. **Say when it would be false.** Every idea note has a *Not true when* section. It is the most useful thing in the whole system, and the first thing worth rewriting in your own words.
4. **Link, and cite the source.** A note earns its place by what it connects to and where it came from.

## Where to start

Open the folder in [Obsidian](https://obsidian.md) and read [[00 Start Here]]. Then look at three notes in particular:

- [[ ]] — the thesis, with its boundary condition attached.
- [[ ]] — the best reply to the most common pushback, already written down.
- [[Commitments — promises made in public]] — the promises made in public, and which are delivered.

## Things worth knowing

[Three to five findings the vault makes visible that the works alone do not. Which idea travels furthest. Which critic wrote the most. How many promises are outstanding. Where the sourcing is thin, and what the real backlog is.]

## Using it with an assistant

[[How to brief an assistant from this vault]] has the recipes. The short version: stop pasting documents, paste notes. `CLAUDE.md` at the root is read automatically if you point a tool that reads such files at this folder.

**If you are also using a teammate stack**, the two divide cleanly: the stack answers *who is speaking and how*, this vault answers *what is true and where it came from*. Load the stack whole, because it is small; take one pack from here, because this is not. [[Working with the teammate stack]] is the contract between them.

## Where it lives, and how to get a copy

This folder is also a git repository. That means every version of every note is recoverable, and a copy exists somewhere other than your laptop.

```bash
git clone <URL>
```

To save your work after an editing session, three commands from inside the folder:

```bash
git add -A
git commit -m "a few words about what changed"
git push
```

**None of this is required to use the vault.** It is plain Markdown in folders; it works in Obsidian or any text editor on a machine that has never heard of git. The repository is insurance and history, not machinery you have to operate.

## Keeping it alive

Twenty minutes after each new piece of work, following [[Inbox — how to empty it]]: capture the text and the feedback, write the work note, write three to eight new zettels for what was new, read the feedback properly, and log anything you promised.

Then one hour a week, following [[Week — how to synthesise]]. That one is easy to skip and it is the one that makes the rest compound: without it the daily notes are expensive bookmarks. If only one habit survives, make it the weekly one.

Capture is never the problem. Draining is — an inbox that is never empty is the commonest way these systems die, which is why the drain has a bucket for *delete it, guilt-free* and a bucket for *this was never a note*.
