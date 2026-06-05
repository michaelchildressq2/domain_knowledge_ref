#!/usr/bin/env python3
"""Validate a generated folder of pattern markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## Intent",
    "## Use when",
    "## Avoid when",
    "## Context and problem",
    "## Forces",
    "## Guidance",
    "## Implementation moves",
    "## Checks",
    "## Failure modes",
    "## Agent trigger hints",
    "## Source notes",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pattern_dir", type=Path)
    args = parser.parse_args()

    pattern_dir = args.pattern_dir
    errors: list[str] = []

    if not pattern_dir.is_dir():
        fail(f"not a directory: {pattern_dir}")
        return 2

    pattern_files = sorted(
        path
        for path in pattern_dir.glob("*.md")
        if path.name.lower() not in {"readme.md", "index.md"}
    )
    if not pattern_files:
        errors.append("no pattern markdown files found")

    long_quote_re = re.compile(r'"[^"]{240,}"')
    for path in pattern_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path.name}: missing frontmatter")
        if "tags:" not in text.split("---", 2)[1]:
            errors.append(f"{path.name}: missing frontmatter tags")
        for heading in REQUIRED_HEADINGS:
            if heading not in text:
                errors.append(f"{path.name}: missing {heading}")
        if long_quote_re.search(text):
            errors.append(f"{path.name}: possible long quote")

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(f"Validation passed: {len(pattern_files)} pattern file(s) in {pattern_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
