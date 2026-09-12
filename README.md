# Stack and Vault

A plain-text toolkit for working with an AI assistant on a body of thinking that is too large to paste into a chat.

It has three layers, and the point of the repository is how they fit together:

| Layer | What it answers | Size | How it is loaded |
|---|---|---|---|
| **The stack** (`stack/`) | *Who is speaking, and how.* Who you are, how you sound, how you want to be worked with, what the assistant may touch. | Eight short files | Whole, at the start of every session |
| **The vault** (`vault/`) | *What is true, and where it came from.* One idea per note, the title is the claim, every claim carries its boundary and its evidence. | Grows without limit | Selectively: five to twelve notes chosen for the job |
| **The wiki layer** (`vault/Maps/`) | *How the ideas hang together.* Hub pages, indexes, ledgers and pre-assembled briefing packs. | A dozen pages | As the entry point to the vault |

The stack is a copy of the [teammate-stack](https://github.com/jamessteincamp/teammate-stack) template. The vault is a Zettelkasten with a wiki on top, built to be read by a person in [Obsidian](https://obsidian.md) and by an assistant through its own `CLAUDE.md`. The contract between the two, which one wins when they disagree and why, is in `docs/the-contract.md`.

## The problem it solves

Working from long documents makes an assistant worse, not better. Ask about one idea inside a twelve-thousand-word document and the other thirty-nine ideas dilute the answer. Ask it to hold your whole set of notes and you get the same failure at a larger scale, plus a bill for every word you sent.

The vault holds each idea as its own note, stated as a claim, with the condition under which it would be false, linked to its evidence and to the objections it has already drawn. A good brief is then a handful of notes chosen for the job. The stack means you never have to re-explain who you are or how you want to be worked with. The wiki layer means you can find the handful.

Two things this buys that a long document does not. The first is cost: a pack of ten notes is two thousand words; a long document is thirty thousand. The second is independence: everything here is plain Markdown on your own disk. It works in any text editor, with no database, nothing to log into, and no connection to anything.

## What is in here

```
stack-and-vault/
├── README.md            this file
├── CLAUDE.md            what an assistant should read, and in what order
├── LICENSE              CC BY 4.0 for the text, MIT for the scripts
├── docs/
│   ├── why.md           the argument for three layers, in more detail
│   ├── the-contract.md  stack versus vault: precedence, loading order, the collision points
│   ├── briefing.md      packs and recipes: how to hand the assistant the right notes
│   └── handing-off.md   how to give a vault to someone else without leaving them dependent on you
├── stack/               the teammate-stack template, eight files plus an audit log
├── vault/               the starter vault: open this folder in Obsidian
│   ├── CLAUDE.md        the assistant's standing instructions for working in the vault
│   ├── Templates/       one template per kind of note, with the rules written into it
│   ├── Maps/            Start Here, the indexes, the ledgers, the routines
│   └── Inbox/ Notes/ Sources/ Daily Notes/
├── tools/               three small Python scripts: check the vault, build a pack, count things
└── example/             a filled-in vault on a deliberately small subject, so the shape is visible
```

## Quick start

1. **Read `example/`** first, in Obsidian or any editor. It is a dozen notes about keeping a sourdough starter. The subject is unimportant; the shape is the point. Start at `example/Maps/00 Start Here.md`.
2. **Copy `vault/` to wherever you keep your notes** and open it as an Obsidian vault. Read `vault/CLAUDE.md` and the templates. Fill in the mission notes and the Start Here page.
3. **Build your stack** by following `stack/README.md`. Expect it to take an afternoon.
4. **Point your assistant at both.** The repository's own `CLAUDE.md` says what to read and in what order. If your assistant reads `CLAUDE.md` files automatically, that is all the setup there is. If you use a chat interface, paste the stack, then paste one pack from `vault/Maps/`.
5. **Run the checker** now and then: `python3 tools/vault_check.py vault/`. It finds broken links, invalid frontmatter, and claims that are missing their boundary.

## The four rules of the vault

1. **One idea per note.** If a note needs a second heading, it is two notes.
2. **The title is the claim.** Not "Money" but "Money is the door, not the house." You should be able to read the file list and hear the argument.
3. **Say when it would be false.** Every idea note has a *Not true when* section. It is the most useful thing in the system, because it is what stops an assistant applying an idea where it does not belong.
4. **Link, and cite the source.** A note earns its place by what it connects to and where it came from. Saying a thing three times is not three sources.

## Status

This is an early, working version, shared to get feedback. It was extracted from a vault in daily use and de-identified; the method is kept and the person is removed. Issues and pull requests are welcome, especially on the parts that only prove themselves in use: the evidence field, the triage routine, and the contract.

## License

The text (everything except `tools/`) is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The scripts in `tools/` are MIT. See `LICENSE`.
