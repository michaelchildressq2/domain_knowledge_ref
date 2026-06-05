#!/usr/bin/env python3
"""Build a lightweight candidate index from chapter text files."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SIGNAL_RE = re.compile(
    r"\b(pattern|anti-pattern|antipattern|principle|practice|pitfall|avoid|should|must|trade-?off|"
    r"core practice|smell|risk|failure|guideline|consequence|applicability|motivation)\b",
    re.I,
)
HEADING_RE = re.compile(r"^[A-Z][A-Za-z0-9 ,:;()'\"/-]{3,100}$")


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for path in [current, *current.parents]:
        if (path / ".git").exists() or ((path / ".agents").is_dir() and (path / "patterns").exists()):
            return path
    return current


def clean(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def chapter_title(path: Path, lines: list[str]) -> str:
    for line in lines[:12]:
        value = clean(line)
        if value and not value.startswith("CHAPTER"):
            return value
    return path.stem


def candidates_for(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    headings: list[dict[str, object]] = []
    signals: list[dict[str, object]] = []

    for index, raw in enumerate(lines, start=1):
        line = clean(raw)
        if not line:
            continue
        if len(line) <= 110 and HEADING_RE.match(line):
            headings.append({"line": index, "text": line})
        if SIGNAL_RE.search(line):
            signals.append({"line": index, "text": line[:220]})

    return {
        "file": path.name,
        "title": chapter_title(path, lines),
        "headings": headings,
        "signals": signals,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chapter_dir", type=Path)
    parser.add_argument("--output", type=Path, help="Output folder, defaults to ./work at repo root")
    args = parser.parse_args()

    if not args.chapter_dir.is_dir():
        parser.error(f"not a directory: {args.chapter_dir}")

    chapters = sorted(args.chapter_dir.glob("chapter-*.txt"))
    if not chapters:
        parser.error(f"no chapter-*.txt files found in {args.chapter_dir}")

    output_dir = args.output or find_repo_root() / "work"
    output_dir.mkdir(parents=True, exist_ok=True)
    index = {
        "source_dir": str(args.chapter_dir),
        "chapters": [candidates_for(path) for path in chapters],
    }
    output_path = output_dir / "candidate-index.json"
    output_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")
    print(f"Chapters: {len(chapters)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
