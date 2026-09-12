"""Shared helpers for the vault tools. Python 3.8+, standard library only.

A vault is a folder of Markdown files. A note's title is its file name without
the extension, and [[wikilinks]] resolve against titles anywhere in the vault,
case-insensitively, the way Obsidian does it.
"""
import re
import pathlib

SKIP_DIRS = {".obsidian", ".git", "_tools", "node_modules", "__pycache__"}
TEMPLATE_DIR = "Templates"

TYPES = {
    "mission", "zettel", "vocab", "work", "feedback", "person", "objection",
    "source", "series", "map", "claude", "daily", "template",
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


class Note:
    def __init__(self, path, root):
        self.path = pathlib.Path(path)
        self.rel = self.path.relative_to(root)
        self.title = self.path.stem
        self.folder = self.rel.parts[0] if len(self.rel.parts) > 1 else ""
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
    """Resolve a link target (possibly a path like Maps/00 Start Here) to a Note."""
    t = target.strip()
    if t.lower().endswith(".md"):
        t = t[:-3]
    if "/" in t:
        t = t.rsplit("/", 1)[1]
    return index.get(t.lower())


def word_count(text):
    return len(text.split())
