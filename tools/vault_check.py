#!/usr/bin/env python3
"""Check a vault for the things that quietly go wrong.

    python3 tools/vault_check.py <vault> [--strict] [--quiet]

Reports, per note:
  ERROR  a note in Notes/ or Sources/ has no frontmatter, or no `type:`
  ERROR  `type:`, `status:` or `evidence:` holds a value the conventions do not know
  ERROR  a zettel is missing one of its five sections, or its "Not true when" is empty
  ERROR  a link points into Inbox/ (nothing in Inbox is settled)
  WARN   a link points at a note that does not exist (a "ghost" link; fine while
         drafting, an error with --strict)
  WARN   Inbox/ is not empty
  WARN   a source note has no citation line

Exits 1 if there were errors (or, with --strict, warnings), 0 otherwise. Templates,
.obsidian and _tools are skipped. Standard library only.
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from vaultlib import (load_vault, title_index, resolve, TYPES, ZETTEL_STATUS,
                      SOURCE_STATUS, EVIDENCE, ZETTEL_SECTIONS, TEMPLATE_DIR)


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    strict = "--strict" in argv
    quiet = "--quiet" in argv
    if len(args) != 1:
        sys.exit(__doc__)
    root, notes = load_vault(args[0])
    index = title_index(notes)
    errors, warnings = [], []

    def err(n, msg):
        errors.append(f"{n.rel}: {msg}")

    def warn(n, msg):
        warnings.append(f"{n.rel}: {msg}")

    inbox_items = [n for n in notes if n.folder == "Inbox" and n.title != "README"]
    inbox_titles = {n.title.lower() for n in inbox_items}

    for n in notes:
        if n.folder == TEMPLATE_DIR or n.title in {"README", "CLAUDE"}:
            continue
        must_have_front = n.folder in {"Notes", "Sources"}
        if not n.front:
            if must_have_front:
                err(n, "no frontmatter")
            continue
        t = n.type
        if t is None:
            if must_have_front:
                err(n, "frontmatter has no `type:`")
        elif t not in TYPES:
            err(n, f"unknown type `{t}` (expected one of {', '.join(sorted(TYPES))})")

        if t == "zettel":
            st = n.front.get("status")
            if st and st not in ZETTEL_STATUS:
                err(n, f"unknown zettel status `{st}`")
            ev = n.front.get("evidence")
            if ev is None:
                err(n, "zettel has no `evidence:` field")
            elif ev not in EVIDENCE:
                err(n, f"unknown evidence value `{ev}` (expected one of {', '.join(sorted(EVIDENCE))})")
            secs = n.sections()
            for s in ZETTEL_SECTIONS:
                if s not in secs:
                    err(n, f"missing section `## {s}`")
            ntw = secs.get("Not true when", "")
            if "Not true when" in secs and not ntw.strip("- \n"):
                err(n, "`## Not true when` is empty — every claim needs its boundary")
            if len(n.links()) < 2:
                warn(n, "fewer than two links; a zettel earns its place by what it connects to")

        if t == "source":
            st = n.front.get("status")
            if st and st not in SOURCE_STATUS:
                err(n, f"unknown source status `{st}`")
            if "**Citation.**" not in n.body:
                warn(n, "no `**Citation.**` line")

        # links
        for target in n.links():
            hit = resolve(target, index)
            if hit is None:
                warn(n, f"ghost link [[{target}]]")
            elif hit.title.lower() in inbox_titles and n.folder != "Inbox":
                err(n, f"links into Inbox: [[{target}]]")

    if inbox_items:
        warnings.append(f"Inbox/ holds {len(inbox_items)} unprocessed item(s); see Maps/Inbox — how to empty it.md")

    if not quiet:
        for e in errors:
            print("ERROR ", e)
        for w in warnings:
            print("WARN  ", w)
    ghost = sum(1 for w in warnings if "ghost link" in w)
    print(f"\n{len(notes)} notes checked: {len(errors)} error(s), {len(warnings)} warning(s)"
          + (f" ({ghost} ghost link(s))" if ghost else ""))
    if errors or (strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
