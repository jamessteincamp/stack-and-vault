#!/usr/bin/env python3
"""Count what is in a vault, and rank notes by how much weight they carry.

    python3 tools/stats.py <vault> [--top N] [--queue]

Prints notes by type; zettels by status and by evidence; sources by status; the
Inbox count; ghost links; and the N most-linked notes (default 10), counting the
distinct notes that link to each. --queue restricts the ranking to zettels still
marked `evidence: asserted`, which is the research queue in priority order: the
unsourced claims that the most other notes depend on.

Standard library only.
"""
import sys
import pathlib
from collections import Counter, defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from vaultlib import load_vault, title_index, resolve, TEMPLATE_DIR, word_count


def main(argv):
    top = 10
    if "--top" in argv:
        i = argv.index("--top")
        top = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    queue = "--queue" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    root, notes = load_vault(args[0])
    notes = [n for n in notes if n.folder != TEMPLATE_DIR and n.title not in {"README", "CLAUDE"}]
    index = title_index(notes)

    by_type = Counter(n.type or "(none)" for n in notes)
    zettels = [n for n in notes if n.type == "zettel"]
    sources = [n for n in notes if n.type == "source"]
    inbox = [n for n in notes if n.folder == "Inbox"]
    words = sum(word_count(n.body) for n in notes)

    inbound = defaultdict(set)
    ghosts = Counter()
    for n in notes:
        for t in n.links():
            hit = resolve(t, index)
            if hit is None:
                ghosts[t] += 1
            elif hit is not n:
                inbound[hit.title].add(n.title)

    print(f"{len(notes)} notes, {words:,} words, in {root.name}/\n")
    print("By type")
    for t, c in by_type.most_common():
        print(f"  {c:5d}  {t}")
    if zettels:
        print("\nZettels by status")
        for s, c in Counter(n.front.get("status", "(none)") for n in zettels).most_common():
            print(f"  {c:5d}  {s}")
        print("\nZettels by evidence")
        for e, c in Counter(n.front.get("evidence", "(none)") for n in zettels).most_common():
            print(f"  {c:5d}  {e}")
    if sources:
        print("\nSources by status")
        for s, c in Counter(n.front.get("status", "(none)") for n in sources).most_common():
            print(f"  {c:5d}  {s}")
    print(f"\nInbox: {len(inbox)} item(s)")
    print(f"Ghost links: {sum(ghosts.values())} to {len(ghosts)} unwritten note(s)")
    if ghosts:
        for t, c in ghosts.most_common(5):
            print(f"  {c:5d}  [[{t}]]")

    pool = zettels if queue else notes
    if queue:
        pool = [n for n in pool if n.front.get("evidence") == "asserted"]
    ranked = sorted(pool, key=lambda n: (-len(inbound[n.title]), n.title))[:top]
    label = "Research queue (asserted zettels, by links in)" if queue else "Most linked"
    print(f"\n{label}")
    for n in ranked:
        print(f"  {len(inbound[n.title]):5d}  [[{n.title}]]")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
