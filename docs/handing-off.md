# Handing off

Most vaults are built by one person for themselves. Some are built by one person for another: a friend, a client, a collaborator who has the material but not the method. This page is about the second case, because it has a failure mode the first does not.

## The test

The person you hand the vault to should be able to keep it alive without you. Not "with a quick call when they get stuck" and not "as long as you keep running the script every week." If you were to disappear tomorrow, nothing in the vault should stop working, and no document in it should be one only you know how to read.

There is an old ladder of giving on which the highest rung is the gift that ends the need for the giver. That is the rung to aim for. It is also the only one that scales: a vault that needs its builder is a vault with one user.

## What passes the test

**Plain text.** Markdown in folders, readable in any editor, with `[[double brackets]]` that are just links. No database, no plugin the vault cannot survive without, no proprietary format. Obsidian is the nicest way to read it, and the vault does not need Obsidian.

**Conventions written down, in the vault, more than once.** The four rules in the hand-off page; the full conventions in `CLAUDE.md`; the rules for each kind of note written into its template as comments. A convention that lives only in the builder's head is a dependency.

**A drain, not just a capture habit.** The person receiving the vault will fill an inbox within a week; whether they ever empty it decides whether the vault survives. So the routine they get has to include permission to throw things away — the bucket for material that was never a note, and the bucket for *delete it, guilt-free* — and a weekly hour that connects what they wrote. A hand-off that teaches capture and not draining hands over a landfill in slow motion.

**Routines, not instructions.** `Inbox — how to empty it` is a twenty-minute procedure the owner can follow, not a description of what the builder used to do. The research routine, the triage routine and the briefing recipes are the same: written so the owner, or the owner's assistant, can run them.

**Tools with their prerequisites named.** If a script is part of the workflow, its README says what it needs (Python 3, say, and nothing else) and what each script does in one line. A script that needs the builder's machine is not a tool; it is a favour.

**A hand-off page.** One page at the vault root, written for the person receiving it: what the vault is, what it is for, the four rules, where to start, where it lives and how to get a copy, and how to keep it alive. The template is at `vault/Hand-off — read this first.md`.

**Version control the owner can ignore.** A git repository means every version of every note is recoverable and a copy exists somewhere other than one laptop. The hand-off page teaches three commands and says plainly that none of them is required to use the vault. The repository is insurance, not machinery.

## What fails the test

Anything the builder did by hand and did not write down. Anything that runs only from the builder's account. Any part of the routine the owner watched the builder do rather than did themselves. A repository under the builder's name rather than the owner's.

## Two rules for the builder

**Label your own contributions.** If you write a note into someone else's vault as a demonstration, say so at the top of the file. Otherwise it becomes indistinguishable from their thinking, and the next reader, human or assistant, will cite it as theirs.

**Propose, do not apply.** Especially for anything that touches many notes at once. Give the list, with a line of reasoning each, and let the owner confirm. The vault is theirs. The method is the only thing you are handing over.

## The order to do it in

Build the vault from their material and hand it over with the hand-off page. Move the repository to their account. Walk through the inbox routine once, with them driving. Then stop. The measure of a good hand-off is that the second month's daily notes are in their voice, not yours.
