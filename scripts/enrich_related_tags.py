#!/usr/bin/env python3
"""Suggest or write tag and relationship enrichments across pattern files."""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    raise SystemExit("PyYAML is required. Install with: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = ROOT / "patterns"
CONFIG = ROOT / "config"
SUGGESTIONS = ROOT / "work" / "suggestions"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm) or {}, body


def write_frontmatter(path: Path, fm: dict[str, Any], body: str) -> None:
    path.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip() + "\n---" + body, encoding="utf-8")


def tokens(text: str) -> set[str]:
    raw = re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower())
    stop = {
        "the", "and", "for", "that", "with", "this", "from", "when", "into", "their", "there", "should",
        "pattern", "patterns", "source", "agent", "agents", "user", "users", "todo", "book", "chapter",
    }
    return {x for x in raw if x not in stop}


def phrase_present(phrase: str, text: str) -> bool:
    return phrase.lower() in text.lower()


def main() -> None:
    parser = argparse.ArgumentParser(description="Suggest or write related links and tags.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--suggest", action="store_true", help="Write markdown suggestions only")
    mode.add_argument("--write", action="store_true", help="Apply high-confidence tag and related-link updates")
    parser.add_argument("--min-score", type=float, default=0.18, help="Minimum similarity score for related suggestions")
    parser.add_argument("--max-related", type=int, default=5, help="Maximum related links to suggest per pattern")
    args = parser.parse_args()

    taxonomy = load_yaml(CONFIG / "taxonomy.yml")
    subjects = load_yaml(CONFIG / "subjects.yml").get("subjects", {})
    canonical_tags = set()
    for values in taxonomy.get("required_tag_families", {}).values():
        canonical_tags.update(values or [])

    items: list[dict[str, Any]] = []
    for path in sorted(PATTERNS.glob("*/*.md")):
        if path.name == "README.md":
            continue
        fm, body = split_frontmatter(path)
        text = "\n".join(
            [
                str(fm.get("title", "")),
                str(fm.get("summary", "")),
                " ".join(map(str, fm.get("tags", []) or [])),
                " ".join(map(str, fm.get("aliases", []) or [])),
                body,
            ]
        )
        items.append({"path": path, "fm": fm, "body": body, "text": text, "tokens": tokens(text)})

    suggestions: dict[str, list[str]] = defaultdict(list)
    changes = 0

    # Tag suggestions from canonical taxonomy and subject concept terms.
    for item in items:
        fm = item["fm"]
        tag_set = set(map(str, fm.get("tags", []) or []))
        new_tags = []
        for tag in sorted(canonical_tags):
            phrase = tag.replace("-", " ")
            if tag not in tag_set and (phrase_present(tag, item["text"]) or phrase_present(phrase, item["text"])):
                new_tags.append(tag)
        subject = fm.get("subject_area")
        if subject in subjects:
            for tag in subjects[subject].get("default_tags", []) or []:
                if tag not in tag_set and tag not in new_tags:
                    new_tags.append(tag)
        if new_tags:
            suggestions[str(item["path"].relative_to(ROOT))].append("suggest tags: " + ", ".join(new_tags[:8]))
            if args.write:
                fm["tags"] = list(dict.fromkeys(list(fm.get("tags", []) or []) + new_tags[:8]))
                changes += 1

    # Relationship suggestions by Jaccard similarity over tokens plus tag overlap.
    id_to_item = {i["fm"].get("id"): i for i in items}
    pair_scores: dict[tuple[str, str], float] = {}
    for i, a in enumerate(items):
        for b in items[i + 1 :]:
            aid = a["fm"].get("id")
            bid = b["fm"].get("id")
            if not aid or not bid:
                continue
            common = a["tokens"] & b["tokens"]
            union = a["tokens"] | b["tokens"]
            if not union:
                continue
            token_score = len(common) / len(union)
            tags_a = set(map(str, a["fm"].get("tags", []) or []))
            tags_b = set(map(str, b["fm"].get("tags", []) or []))
            tag_score = len(tags_a & tags_b) / max(1, len(tags_a | tags_b))
            same_subject = 0.05 if a["fm"].get("subject_area") == b["fm"].get("subject_area") else 0.0
            score = token_score * 0.65 + tag_score * 0.35 + same_subject
            pair_scores[(aid, bid)] = score

    related_candidates: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for (aid, bid), score in pair_scores.items():
        if score >= args.min_score:
            related_candidates[aid].append((bid, score))
            related_candidates[bid].append((aid, score))

    for pid, candidates in sorted(related_candidates.items()):
        item = id_to_item.get(pid)
        if not item:
            continue
        existing = set(map(str, item["fm"].get("related", []) or []))
        chosen = [(rid, score) for rid, score in sorted(candidates, key=lambda x: x[1], reverse=True) if rid not in existing]
        chosen = chosen[: args.max_related]
        if not chosen:
            continue
        relpath = str(item["path"].relative_to(ROOT))
        suggestions[relpath].append("suggest related: " + ", ".join(f"{rid} ({score:.2f})" for rid, score in chosen))
        if args.write:
            item["fm"]["related"] = list(dict.fromkeys(list(item["fm"].get("related", []) or []) + [rid for rid, _ in chosen]))
            changes += 1

    if args.write:
        for item in items:
            write_frontmatter(item["path"], item["fm"], item["body"])
        print(f"Applied updates to {changes} pattern metadata block(s).")
    else:
        SUGGESTIONS.mkdir(parents=True, exist_ok=True)
        out = SUGGESTIONS / "related-tags.md"
        lines = ["# Related Tag Suggestions", ""]
        if not suggestions:
            lines.append("No suggestions found.")
        for relpath in sorted(suggestions):
            lines.append(f"## `{relpath}`")
            lines.append("")
            for s in suggestions[relpath]:
                lines.append(f"- {s}")
            lines.append("")
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"Wrote suggestions to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
