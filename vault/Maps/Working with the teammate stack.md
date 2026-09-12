---
type: claude
---
# Working with the teammate stack

Two plain-text systems, and they are not competitors. This note is the contract between them, so neither drifts into being a worse copy of the other.

- **The teammate stack** is eight short files: who you are, how you sound, how you want to be worked with, what the assistant may touch. It is small, it is always loaded, and it changes slowly.
- **This vault** is the notes: what is true, where it came from, what you have already said, and who said it back. It is large, it is loaded *selectively*, and it changes every working day.

In one line: **the stack answers *who is speaking and how*; the vault answers *what is true and where it came from*.** Almost every question about which file something belongs in resolves against that sentence.

## Precedence, when they disagree

| Question | Winner | Why |
|---|---|---|
| How should this sound? | **Stack** (`02-voice`, `03-anti-style`) | Voice is a decision, not an observation. |
| How should we work today? | **Stack** (`04-context`, `05-rules`) | The stack is the standing brief; the vault is the material. |
| Is this claim true, and what backs it? | **Vault** (`Sources/`, the `evidence:` field) | Nothing else in either system tracks evidence per claim. |
| Have I said this before, and where? | **Vault** (backlinks) | The stack has no memory of the works. |
| Did I promise this? | **Vault** ([[Commitments — promises made in public]]) | The ledger is the record. |
| What may the assistant touch? | **Stack** (`07-connectors`) | Except any hard rule the vault's `CLAUDE.md` keeps under *Do not*. |

**Hard rules the vault keeps regardless of the stack** are editorial commitments made in public: things the owner has said on the record they will never do. They live in `CLAUDE.md` under *Do not* and survive any instruction elsewhere. Copy each into `07-connectors` under *Off-limits* as well, so it is visible from both sides.

## The three places they will actually collide

**1. Voice.** The vault holds a voice note (`type: mission`), which is *observed*: the openers, the recurring phrases, the sign-offs, all quoted from the works. The stack's `02-voice` and `03-anti-style` are *declared*: how the owner wants to sound.

Do not copy one into the other. Keep the vault note as the evidence and the stack file as the rule, and have `02-voice` open with a pointer:

> The observed baseline is `Notes/Voice — how the owner sounds.md` in the vault, derived from every published work. This file records the rule; that note records the practice.

When the two disagree, that is a finding rather than an error. It means the voice has drifted, or the owner has decided to change it. Either way it goes in the audit log, not quietly into one file.

**2. `04-context` versus the vault's ledgers.** `04-context` is the file weighted most heavily for *what to do today*, and it is the one most likely to swell into a second, staler copy of the commitments ledger. It should hold pointers and deltas, never lists:

> **Current work.** Current series: […]; next deliverable is […] (pack: `Maps/Pack — ….md`). Live backlog is `Maps/Commitments — promises made in public.md` and the research queue is `Maps/Sources — index.md`. Do not restate either here; read them.

Anything that changes weekly lives in the vault. `04` records what changed since the last audit and what it means.

**3. `05-rules` versus the vault's `CLAUDE.md`.** The test: *would this rule still apply if the owner were writing about a completely different subject?* If yes, it is a stack rule. If it is only true of this body of work, it stays in `CLAUDE.md`. So "lead with the critique" and "corrections come as proposals" are stack; "the title of a note is the claim" and "every zettel needs a *Not true when*" are vault. If a rule ends up in both, delete the vault copy and leave a pointer, because the stack is the one that gets read at the start of every session.

## The rule that already runs through both

`03-anti-style` names **false certainty and false specificity** — numbers without provenance, confidence without evidence — as an offence against the writing. The vault enforces exactly that rule one claim at a time, through the `evidence:` field and the *Outside the work* line in every zettel. They are the same principle at two scales: the stack states it, the vault holds the work to it, claim by claim.

That is the strongest argument for running both. The stack alone would leave the principle as an aspiration. The vault alone would be a filing system with no standard to file against.

## Loading order for a session

1. **Stack first, always, whole.** Eight short files is a few thousand words. That is the cost of the assistant knowing who it is working with.
2. **Then one pack from the vault, never the vault.** Five to twelve notes, chosen for the job. See [[How to brief an assistant from this vault]].
3. **Open with a move from `06-opening-move.md`.** Draft mode and build mode map to the recipes in the briefing note; spar mode is the right one for testing whether an argument holds before publishing it.

**The failure this prevents is the one that starts most of these projects.** Handing an assistant a twelve-thousand-word document means asking about one idea while thirty-nine others dilute the answer. Handing it the whole vault is the same mistake at a larger scale. The stack is loaded whole *because* it is small; the vault is queried *because* it is not.

## Where the two systems meet on the calendar

The stack audits quarterly (`AUDIT-LOG.md`); the vault logs daily (`Daily Notes/`). They meet at the audit. Three questions worth adding to the stack's standing audit prompts:

- **Did the sourcing backlog shrink?** Count `evidence: asserted` against last quarter.
- **Did the promises ledger shrink?**
- **Did the vault reduce inboxes or become one?** The stack's own test, applied to the vault. An `Inbox/` that is never empty is the warning sign.

## Two blocks to paste into the stack

Into `07-connectors`, under *Connected now*:

> **The vault** (Obsidian, local). The owner's Zettelkasten: every published work as a full text, feedback capture and work note; idea notes titled as claims; objections carrying the owner's own replies; citation notes. The assistant may read it, propose notes and draft from it. It may not merge notes into long documents, and it may not invent a citation — `needs-source` is an acceptable outcome and a fabricated reference is not. Conventions are in the vault's own `CLAUDE.md`.

Into `08-leverage`, under *Context loaded once*:

> **Briefing packs, not the folder.** `Maps/Pack — ….md` files are pre-assembled contexts for the recurring jobs. Building the next pack — for whichever job has now come up twice — is the next piece of leverage worth having.

## Related
- [[How to brief an assistant from this vault]]
- [[Sources — index]]
- [[00 Start Here]]
