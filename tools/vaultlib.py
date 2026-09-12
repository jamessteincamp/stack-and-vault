"""Shared helpers for the vault tools. Python 3.8+, standard library only.

A vault is a folder of Markdown files. A note's title is its file name without
the extension, and [[wikilinks]] resolve against titles anywhere in the vault,
case-insensitively, the way Obsidian does it.

Folders are identified by their STAGE, not their exact name: a leading numeric
prefix is stripped and the rest lower-cased, so "00 Inbox" and "Inbox" are both
the inbox. That means the tools work on a vault that numbers its folders for
sidebar order and on one that does not.
"""
import re
import pathlib

SKIP_DIRS = {".obsidian", ".git", "_tools", "node_modules", "__pycache__"}

# stage -> the folder name this repo ships. Only used for messages; detection
# goes through stage() below, so a vault may name these whatever it likes.
FOLDERS = {
    "inbox": "00 Inbox",
    "notes": "10 Notes",
    "maps": "20 Maps",
    "daily": "30 Daily",
    "sources": "40 Sources",
    "templates": "99 Templates",
}

TYPES = {
    "mission", "zettel", "vocab", "work", "feedback", "person", "objection",
    "source", "series", "map", "claude", "daily", "weekly", "template",
}
ZETTEL_STATUS = {"seedling", "growing", "evergreen"}
SOURCE_STATUS = {"sourced", "partial", "needs-source", "contested"}
EVIDENCE = {"external", "partial", "observed", "argument", "asserted"}
ZETTEL_SECTIONS = ["The idea", "Not true when", "Why it matters", "Related", "Sources"]

_FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)
_LINK = re.compile(r"\[\[([^\]\|#\^]*)(?:[#\^][^\]\|]*)?(?:\|[^\]]*)?\]\]")
_FENCE = re.compile(r"```.*?```", re.S)
_INLINE_CODE = re.compile(r"`[^`\n]*`")
_COMMENT = re.compile(r"<!--.*?-->", re.S)
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$", re.M)
_NUM_PREFIX = re.compile(r"\A\d+[\s._-]*")


def stage(folder):
    """"00 Inbox" -> "inbox"; "Daily Notes" -> "daily notes"; "" -> ""."""
    return _NUM_PREFIX.sub("", folder).strip().lower()


class Note:
    def __init__(self, path, root):
        self.path = pathlib.Path(path)
        self.rel = self.path.relative_to(root)
        self.title = self.path.stem
        self.folder = self.rel.parts[0] if len(self.rel.parts) > 1 else ""
        self.stage = stage(self.folder)
        self.text = self.path.read_text(encoding="utf-8", errors="replace")
        self.front, self.body = split_frontmatter(self.text)

    @property
    def type(self):
        return self.front.get("type")

    def links(self):
        """Wikilink targets in the body, with code and comments stripped.
        Placeholders like [[ ]] and [[…]] are dropped."""
        clean = _COMMENT.sub("", _FENCE.sub("", self.body))
        clean = _INLINE_CODE.sub("", clean)
        out = []
        for m in _LINK.finditer(clean):
            t = m.group(1).strip()
            if not t or "…" in t or "..." in t or t.startswith("<"):
                continue  # placeholder left by a template
            out.append(t)
        return out

    def sections(self):
        """Map of heading text -> content under it (comments stripped), for ## headings."""
        clean = _COMMENT.sub("", self.body)
        parts = _HEADING.split(clean)
        # parts: [pre, hashes, title, content, hashes, title, content, ...]
        out = {}
        for i in range(1, len(parts) - 2, 3):
            hashes, title, content = parts[i], parts[i + 1], parts[i + 2]
            if len(hashes) == 2:
                out[title.strip()] = content.strip()
        return out


def split_frontmatter(text):
    m = _FRONT.match(text)
    if not m:
        return {}, text
    front = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        k, v = line.split(":", 1)
        v = v.strip().strip('"').strip("'")
        front[k.strip()] = v
    return front, text[m.end():]


def load_vault(root):
    """Return (root_path, [Note]) for every .md file outside the skipped folders."""
    root = pathlib.Path(root).resolve()
    if not root.is_dir():
        raise SystemExit(f"not a folder: {root}")
    notes = []
    for p in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        notes.append(Note(p, root))
    return root, notes


def title_index(notes):
    """Lower-cased title -> Note. Obsidian resolves links case-insensitively."""
    return {n.title.lower(): n for n in notes}


def resolve(target, index):
    """Resolve a link target (possibly a path like 20 Maps/00 Start Here) to a Note."""
    t = target.strip()
    if t.lower().endswith(".md"):
        t = t[:-3]
    if "/" in t:
        t = t.rsplit("/", 1)[1]
    return index.get(t.lower())


def word_count(text):
    return len(text.split())
