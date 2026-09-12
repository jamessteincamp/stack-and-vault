#!/usr/bin/env python3
"""Assemble a briefing pack into one file for pasting.

    python3 tools/pack.py <vault> "Maps/Pack — <job>.md" [-o brief.md]
    python3 tools/pack.py <vault> --titles "Title one" "Title two" ... [-o brief.md]

Reads the [[wikilinks]] under the pack note's "notes to load" heading (or every link
in the note if it has no such heading; or titles from the command line), and writes
the body of each linked note — frontmatter and HTML comments stripped, headings
demoted one level — into a single Markdown file.
Each note is included once, and the pack note itself is not included. Unresolved
links are reported on stderr and skipped. The word count goes to stderr too, because
that is the number you are about to pay for.

Standard library only.
"""
import sys
import re
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from vaultlib import load_vault, title_index, resolve, word_count, Note

_COMMENT = re.compile(r"<!--.*?-->", re.S)
_HEADING = re.compile(r"^(#{1,5})(\s)", re.M)


def render(note):
    body = _COMMENT.sub("", note.body).strip()
    body = _HEADING.sub(lambda m: "#" + m.group(1) + m.group(2), body)
    # Drop a leading H1 that repeats the title; the pack supplies its own heading.
    body = re.sub(r"\A##\s+" + re.escape(note.title) + r"\s*\n", "", body)
    meta = []
    for k in ("type", "status", "evidence"):
        if k in note.front:
            meta.append(f"{k}: {note.front[k]}")
    head = f"## {note.title}\n" + (f"*{' · '.join(meta)}*\n" if meta else "")
    return head + "\n" + body.strip() + "\n"


def main(argv):
    out_path = None
    if "-o" in argv:
        i = argv.index("-o")
        out_path = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if len(argv) < 2:
        sys.exit(__doc__)
    root, notes = load_vault(argv[0])
    index = title_index(notes)

    if argv[1] == "--titles":
        targets = argv[2:]
        pack_title = "Brief"
        intro = ""
    else:
        p = pathlib.Path(argv[1])
        if not p.is_absolute():
            p = root / p
        if not p.is_file():
            sys.exit(f"pack note not found: {p}")
        pack = Note(p, root)
        pack_title = pack.title
        # Prefer the links under a "notes to load" heading, if the pack has one;
        # otherwise every link in the note, in order.
        load = [c for h, c in pack.sections().items() if "load" in h.lower()]
        if load:
            probe = Note.__new__(Note)
            probe.body = "\n".join(load)
            targets = Note.links(probe)
        else:
            targets = pack.links()
        intro = _COMMENT.sub("", pack.body).strip()
        intro = re.sub(r"\A#\s+[^\n]*\n", "", intro).strip()

    seen, parts, missing = set(), [], []
    for t in targets:
        n = resolve(t, index)
        if n is None:
            missing.append(t)
            continue
        if n.title == pack_title or n.title.lower() in seen:
            continue
        seen.add(n.title.lower())
        parts.append(render(n))

    text = f"# {pack_title}\n\n"
    if intro:
        text += intro + "\n\n---\n\n"
    text += "\n---\n\n".join(parts)

    for m in missing:
        print(f"unresolved: [[{m}]]", file=sys.stderr)
    print(f"{len(parts)} note(s), {word_count(text)} words", file=sys.stderr)

    if out_path:
        pathlib.Path(out_path).write_text(text, encoding="utf-8")
        print(f"-> {out_path}", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
