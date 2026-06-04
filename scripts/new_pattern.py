#!/usr/bin/env python3
"""Create a new pattern file from the repository template."""
from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    raise SystemExit("PyYAML is required. Install with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ROOT / "config" / "subjects.yml"
PATTERNS = ROOT / "patterns"
SOURCES = ROOT / "sources" / "manifest.yml"


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def source_label(source_id: str) -> str:
    manifest = load_yaml(SOURCES)
    for src in manifest.get("sources", []):
        if src.get("id") == source_id:
            return f"{source_id}: {src.get('citation_label') or src.get('title')}"
    return f"{source_id}: source registered in sources/manifest.yml"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a new pattern markdown file.")
    parser.add_argument("--subject", required=True, help="Subject folder, e.g. reliability")
    parser.add_argument("--id", required=True, help="Pattern id, e.g. platform.high-availability")
    parser.add_argument("--title", required=True, help="Pattern title")
    parser.add_argument("--summary", default="TODO: summarize what this pattern helps an agent do.")
    parser.add_argument("--source", action="append", default=[], help="Source id from sources/manifest.yml; repeatable")
    parser.add_argument("--type", default="architecture-pattern")
    args = parser.parse_args()

    subjects = load_yaml(SUBJECTS).get("subjects", {})
    if args.subject not in subjects:
        known = ", ".join(sorted(subjects))
        raise SystemExit(f"Unknown subject {args.subject!r}. Known subjects: {known}")

    filename = slug(args.id.split(".")[-1]) + ".md"
    out = PATTERNS / args.subject / filename
    if out.exists():
        raise SystemExit(f"Refusing to overwrite existing pattern: {out.relative_to(ROOT)}")

    default_tags = subjects[args.subject].get("default_tags", [])
    fm = {
        "id": args.id,
        "title": args.title,
        "type": args.type,
        "status": "draft",
        "subject_area": args.subject,
        "summary": args.summary,
        "tags": default_tags,
        "aliases": [],
        "applies_when": ["TODO: add concrete applicability trigger."],
        "avoid_when": ["TODO: add concrete avoid condition."],
        "related": [],
        "sources": [source_label(s) for s in args.source] or ["TODO: add source id and citation label"],
        "source_confidence": "low",
        "last_reviewed": str(date.today()),
    }
    body = f"""# {args.title}

## Intent

TODO: State the durable design intention in one short paragraph.

## Use when

- TODO: Add practical triggers.

## Avoid when

- TODO: Add contexts where this pattern is wrong or risky.

## Context and problem

TODO: Describe the recurring situation this pattern solves.

## Forces

- TODO: Explain tradeoffs and tensions.

## Guidance

TODO: Give the core advice in original language.

## Implementation moves

- TODO: Provide concrete moves an agent can recommend or execute.

## Checks

- TODO: Provide review questions.

## Failure modes

- TODO: Describe ways this pattern is commonly misapplied.

## Agent trigger hints

Use this pattern when the user says or implies:

- TODO: Add trigger phrase.

## Source notes

TODO: Explain source lineage and confidence. Do not include long quotes or chapter recaps.
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n" + body, encoding="utf-8")
    print(f"Created {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
