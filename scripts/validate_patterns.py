#!/usr/bin/env python3
"""Validate knowledge-base pattern files."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML is required. Install with: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = ROOT / "patterns"
CONFIG = ROOT / "config"

DEFAULT_REQUIRED_FM = [
    "id",
    "title",
    "type",
    "status",
    "subject_area",
    "summary",
    "tags",
    "aliases",
    "applies_when",
    "avoid_when",
    "related",
    "sources",
    "source_confidence",
    "last_reviewed",
]
DEFAULT_REQUIRED_HEADINGS = [
    "Intent",
    "Use when",
    "Avoid when",
    "Context and problem",
    "Forces",
    "Guidance",
    "Implementation moves",
    "Checks",
    "Failure modes",
    "Agent trigger hints",
    "Source notes",
]
LIST_FIELDS = {"tags", "aliases", "applies_when", "avoid_when", "related", "sources"}


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data or {}


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("unterminated YAML frontmatter")
    data = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data, body


def all_pattern_files() -> list[Path]:
    return sorted(p for p in PATTERNS.glob("*/*.md") if p.name != "README.md")


def words(s: str) -> set[str]:
    return set(re.findall(r"[a-z0-9][a-z0-9-]{2,}", s.lower()))


def validate() -> int:
    policy = load_yaml(CONFIG / "repo_policy.yml")
    taxonomy = load_yaml(CONFIG / "taxonomy.yml")
    subjects = load_yaml(CONFIG / "subjects.yml").get("subjects", {})
    required_fm = policy.get("pattern_contract", {}).get("required_frontmatter", DEFAULT_REQUIRED_FM)
    required_headings = policy.get("pattern_contract", {}).get("required_body_headings", DEFAULT_REQUIRED_HEADINGS)
    max_quote_words = int(policy.get("repository_policy", {}).get("max_quote_words_per_pattern", 25))
    reserved_statuses = set(taxonomy.get("reserved_statuses", ["seed", "draft", "reviewed", "deprecated"]))
    tag_families = taxonomy.get("required_tag_families", {})
    source_conf = set(taxonomy.get("source_confidence", {"high": "", "medium": "", "low": ""}).keys())

    errors: list[str] = []
    warnings: list[str] = []
    pattern_ids: dict[str, Path] = {}
    all_ids: set[str] = set()
    files = all_pattern_files()

    if not files:
        errors.append("no pattern files found under patterns/<subject>/")

    parsed: list[tuple[Path, dict[str, Any], str]] = []
    for path in files:
        rel = path.relative_to(ROOT)
        try:
            fm, body = split_frontmatter(path)
            parsed.append((path, fm, body))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{rel}: {exc}")
            continue

        pid = fm.get("id")
        if isinstance(pid, str):
            if pid in pattern_ids:
                errors.append(f"{rel}: duplicate id {pid!r}; already used in {pattern_ids[pid].relative_to(ROOT)}")
            pattern_ids[pid] = path
            all_ids.add(pid)

    for path, fm, body in parsed:
        rel = path.relative_to(ROOT)
        for key in required_fm:
            if key not in fm or fm.get(key) in (None, ""):
                errors.append(f"{rel}: missing required frontmatter key {key!r}")

        for key in LIST_FIELDS:
            if key in fm and not isinstance(fm[key], list):
                errors.append(f"{rel}: {key!r} must be a list")

        pid = fm.get("id")
        if not isinstance(pid, str) or not re.match(r"^[a-z][a-z0-9-]*(\.[a-z0-9-]+)+$", pid):
            errors.append(f"{rel}: id must look like platform.example-pattern")

        status = fm.get("status")
        if status not in reserved_statuses:
            errors.append(f"{rel}: status {status!r} must be one of {sorted(reserved_statuses)}")

        subject = fm.get("subject_area")
        folder = path.parent.name
        if subject != folder:
            errors.append(f"{rel}: subject_area {subject!r} must match folder {folder!r}")
        if subject not in subjects:
            errors.append(f"{rel}: unknown subject_area {subject!r}; add it to config/subjects.yml")

        conf = fm.get("source_confidence")
        if conf not in source_conf:
            errors.append(f"{rel}: source_confidence {conf!r} must be one of {sorted(source_conf)}")

        tags = fm.get("tags") or []
        if not isinstance(tags, list) or len(tags) < 4:
            errors.append(f"{rel}: tags must contain at least four values")
        else:
            tag_set = {str(t) for t in tags}
            missing_families = []
            for family, values in tag_families.items():
                values_set = set(values or [])
                if values_set and not tag_set.intersection(values_set):
                    missing_families.append(family)
            # Scope is useful but not always applicable. Treat it as a warning rather than hard failure.
            hard_missing = [f for f in missing_families if f != "scope"]
            if hard_missing:
                errors.append(f"{rel}: tags missing required taxonomy families: {', '.join(hard_missing)}")
            if "scope" in missing_families:
                warnings.append(f"{rel}: tags have no scope tag such as cloud-agnostic, terraform, kubernetes, database, identity")

        for heading in required_headings:
            pattern = rf"^##\s+{re.escape(heading)}\s*$"
            if not re.search(pattern, body, flags=re.MULTILINE):
                errors.append(f"{rel}: missing body heading ## {heading}")

        related = fm.get("related") or []
        if isinstance(related, list):
            for rid in related:
                if rid not in all_ids:
                    warnings.append(f"{rel}: related id {rid!r} is not present in this repo")
                if rid == pid:
                    errors.append(f"{rel}: pattern cannot relate to itself")

        quote_words = 0
        for line in body.splitlines():
            stripped = line.strip()
            if stripped.startswith(">"):
                quote_words += len(words(stripped))
        if quote_words > max_quote_words:
            errors.append(f"{rel}: block quotes contain {quote_words} words; max is {max_quote_words}")

        lower = body.lower()
        risky_phrases = [
            "in chapter ",
            "this chapter explains",
            "the author says",
            "the book says",
            "below is a summary of",
        ]
        for phrase in risky_phrases:
            if phrase in lower:
                warnings.append(f"{rel}: phrase {phrase!r} may indicate recap-style writing; prefer pattern guidance")

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"\nValidation failed: {len(errors)} error(s), {len(warnings)} warning(s).", file=sys.stderr)
        return 1

    print(f"Validation passed: {len(files)} pattern file(s), {len(warnings)} warning(s).")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate knowledge-base pattern files.")
    parser.parse_args()
    raise SystemExit(validate())


if __name__ == "__main__":
    main()
