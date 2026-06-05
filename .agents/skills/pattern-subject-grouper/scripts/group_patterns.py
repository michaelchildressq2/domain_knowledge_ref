#!/usr/bin/env python3
"""Group pattern markdown files into subject-area indexes."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SUBJECTS: dict[str, dict[str, list[str]]] = {
    "system-qualities": {
        "title": ["System Qualities"],
        "keywords": [
            "reliability", "scalability", "maintainability", "operability",
            "correctness", "availability", "latency", "performance", "quality",
            "service-level", "slo", "high-availability",
        ],
    },
    "change-and-delivery": {
        "title": ["Change And Delivery"],
        "keywords": [
            "safe-change", "delivery", "pipeline", "testing", "validation",
            "rollback", "roll-forward", "compatibility", "migration", "deploy",
            "release", "progressive", "feedback", "schema-evolution",
        ],
    },
    "modular-boundaries": {
        "title": ["Modular Boundaries"],
        "keywords": [
            "module", "component", "boundary", "stack", "repository", "repo",
            "service-stack", "coupling", "cohesion", "reusable", "monolithic",
            "abstraction", "facade", "spaghetti", "cluster", "kubernetes",
        ],
    },
    "configuration-and-contracts": {
        "title": ["Configuration And Contracts"],
        "keywords": [
            "configuration", "parameter", "schema", "contract", "registry",
            "message", "api", "query", "compatibility", "externalized",
            "version", "interface",
        ],
    },
    "data-modeling-and-storage": {
        "title": ["Data Modeling And Storage"],
        "keywords": [
            "data-model", "data-modeling", "database", "document", "graph",
            "relational", "query", "index", "storage", "warehouse", "analytics",
            "column", "b-tree", "lsm", "persistence",
        ],
    },
    "replication-consistency-and-coordination": {
        "title": ["Replication Consistency And Coordination"],
        "keywords": [
            "replication", "consistency", "transaction", "isolation", "consensus",
            "leader", "coordination", "lock", "fencing", "conflict", "linearizability",
            "eventual-consistency", "distributed",
        ],
    },
    "partitioning-scaling-and-performance": {
        "title": ["Partitioning Scaling And Performance"],
        "keywords": [
            "partition", "shard", "hot-spot", "hot-key", "rebalance", "scaling",
            "scalability", "capacity", "load", "throughput", "latency", "performance",
        ],
    },
    "pipelines-streams-and-derived-data": {
        "title": ["Pipelines Streams And Derived Data"],
        "keywords": [
            "batch", "stream", "event", "event-log", "derived", "materialized",
            "dataflow", "pipeline", "replay", "backpressure", "idempotent",
            "consumer", "producer", "data-quality",
        ],
    },
    "operations-recovery-and-governance": {
        "title": ["Operations Recovery And Governance"],
        "keywords": [
            "runtime", "operations", "observability", "incident", "recovery",
            "disaster", "backup", "continuity", "governance", "compliance",
            "policy", "metrics", "drift", "platform", "platform-engineering",
            "cluster", "cluster-management", "kubernetes",
        ],
    },
    "security-and-secrets": {
        "title": ["Security And Secrets"],
        "keywords": [
            "security", "secrets", "secret", "identity", "least-privilege",
            "authorization", "policy", "isolation", "tenant", "sensitive",
        ],
    },
}


@dataclass
class Pattern:
    path: Path
    id: str
    title: str
    type: str
    summary: str
    tags: list[str]
    aliases: list[str]
    sources: list[str]


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter")
    return text[4:end], text[end + 5 :]


def parse_frontmatter(frontmatter: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current: str | None = None
    for raw in frontmatter.splitlines():
        stripped = raw.strip()
        if not stripped:
            continue
        if re.match(r"^[A-Za-z0-9_]+:\s*", stripped):
            key, value = stripped.split(":", 1)
            current = key.strip()
            value = value.strip()
            data[current] = [] if not value else value.strip('"').strip("'")
            continue
        if stripped.startswith("- ") and current:
            if not isinstance(data.get(current), list):
                data[current] = []
            data[current].append(stripped[2:].strip().strip('"').strip("'"))
    return data


def load_pattern(path: Path) -> Pattern:
    frontmatter, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    data = parse_frontmatter(frontmatter)
    return Pattern(
        path=path,
        id=str(data.get("id", path.stem)),
        title=str(data.get("title", path.stem)),
        type=str(data.get("type", "")),
        summary=str(data.get("summary", "")),
        tags=[str(item) for item in data.get("tags", [])],
        aliases=[str(item) for item in data.get("aliases", [])],
        sources=[str(item) for item in data.get("sources", [])],
    )


def normalized_words(pattern: Pattern) -> set[str]:
    text = " ".join([
        pattern.id,
        pattern.title,
        pattern.type,
        pattern.summary,
        " ".join(pattern.tags),
        " ".join(pattern.aliases),
    ]).lower()
    words = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text))
    for tag in pattern.tags:
        words.update(part for part in tag.lower().split("-") if part)
    return words


def classify(pattern: Pattern) -> list[str]:
    words = normalized_words(pattern)
    text = " ".join(words)
    matches: list[str] = []
    for slug, spec in SUBJECTS.items():
        score = 0
        for keyword in spec["keywords"]:
            key = keyword.lower()
            if key in words or key in text:
                score += 1
        if score:
            matches.append(slug)
    return matches or ["unclassified"]


def iter_patterns(input_dirs: list[Path]) -> list[Pattern]:
    patterns: list[Pattern] = []
    for input_dir in input_dirs:
        if not input_dir.is_dir():
            raise ValueError(f"not a directory: {input_dir}")
        for path in sorted(input_dir.glob("*.md")):
            if path.name.lower() in {"readme.md", "index.md"}:
                continue
            patterns.append(load_pattern(path))
    return patterns


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)


def write_group(output_dir: Path, slug: str, patterns: list[Pattern]) -> None:
    title = "Unclassified" if slug == "unclassified" else SUBJECTS[slug]["title"][0]
    lines = [
        f"# {title}",
        "",
        f"Pattern count: {len(patterns)}",
        "",
    ]
    for pattern in sorted(patterns, key=lambda item: (item.title.lower(), item.id)):
        tags = ", ".join(f"`{tag}`" for tag in pattern.tags)
        lines.extend([
            f"## {pattern.title}",
            "",
            f"- `id`: `{pattern.id}`",
            f"- `type`: `{pattern.type}`",
            f"- `source`: `{rel(pattern.path)}`",
            f"- `tags`: {tags}",
            f"- `summary`: {pattern.summary}",
            "",
        ])
    output_dir.joinpath(f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def write_outputs(output_dir: Path, groups: dict[str, list[Pattern]]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for old in output_dir.glob("*.md"):
        old.unlink()
    for old in output_dir.glob("*.json"):
        old.unlink()

    ordered = sorted(groups.items(), key=lambda item: (item[0] == "unclassified", item[0]))
    for slug, patterns in ordered:
        write_group(output_dir, slug, patterns)

    readme = [
        "# Pattern Subject Groups",
        "",
        "Generated subject-area grouping for pattern markdown files.",
        "",
        "## Groups",
        "",
    ]
    for slug, patterns in ordered:
        title = "Unclassified" if slug == "unclassified" else SUBJECTS[slug]["title"][0]
        readme.append(f"- [{title}]({slug}.md): {len(patterns)} pattern(s)")
    output_dir.joinpath("README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")

    manifest = {
        "groups": {
            slug: [
                {
                    "id": pattern.id,
                    "title": pattern.title,
                    "type": pattern.type,
                    "path": rel(pattern.path),
                    "tags": pattern.tags,
                    "summary": pattern.summary,
                }
                for pattern in sorted(patterns, key=lambda item: item.id)
            ]
            for slug, patterns in ordered
        }
    }
    output_dir.joinpath("manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dirs", nargs="+", type=Path, help="folders containing pattern .md files")
    parser.add_argument("--output", type=Path, default=Path("subject-groups"), help="output folder")
    args = parser.parse_args()

    patterns = iter_patterns(args.input_dirs)
    if not patterns:
        parser.error("no pattern markdown files found")

    groups: dict[str, list[Pattern]] = {}
    for pattern in patterns:
        for slug in classify(pattern):
            groups.setdefault(slug, []).append(pattern)

    write_outputs(args.output, groups)
    print(f"Wrote {args.output}")
    print(f"Patterns: {len(patterns)}")
    for slug in sorted(groups):
        print(f"{slug}: {len(groups[slug])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
