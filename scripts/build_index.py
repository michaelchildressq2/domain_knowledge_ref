#!/usr/bin/env python3
"""Build a lightweight pattern index for agents."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    raise SystemExit("PyYAML is required. Install with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = ROOT / "patterns"
OUT = ROOT / "work" / "index"


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    items = []
    for path in sorted(PATTERNS.glob("*/*.md")):
        if path.name == "README.md":
            continue
        fm, _ = split_frontmatter(path)
        items.append(
            {
                "id": fm.get("id"),
                "title": fm.get("title"),
                "subject_area": fm.get("subject_area"),
                "summary": fm.get("summary"),
                "tags": fm.get("tags", []),
                "aliases": fm.get("aliases", []),
                "applies_when": fm.get("applies_when", []),
                "avoid_when": fm.get("avoid_when", []),
                "related": fm.get("related", []),
                "sources": fm.get("sources", []),
                "path": str(path.relative_to(ROOT)),
            }
        )

    by_subject: dict[str, list[dict[str, Any]]] = {}
    by_tag: dict[str, list[str]] = {}
    for item in items:
        by_subject.setdefault(item.get("subject_area") or "unknown", []).append(item)
        for tag in item.get("tags") or []:
            by_tag.setdefault(str(tag), []).append(item.get("id"))

    index = {"patterns": items, "by_subject": by_subject, "by_tag": by_tag}
    (OUT / "pattern-index.json").write_text(json.dumps(index, indent=2, sort_keys=True), encoding="utf-8")

    lines = ["# Pattern Index", ""]
    for subject in sorted(by_subject):
        lines.append(f"## {subject}")
        lines.append("")
        for item in sorted(by_subject[subject], key=lambda x: x.get("id") or ""):
            tags = ", ".join(item.get("tags") or [])
            lines.append(f"- `{item.get('id')}` - **{item.get('title')}**: {item.get('summary')} (`{item.get('path')}`) [{tags}]")
        lines.append("")
    (OUT / "PATTERN_INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT / 'pattern-index.json'} and {OUT / 'PATTERN_INDEX.md'}")


if __name__ == "__main__":
    main()
