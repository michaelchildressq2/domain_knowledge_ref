#!/usr/bin/env python3
"""Extract source text into local, gitignored chunks for agent analysis."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_text(text: str, max_chars: int) -> list[str]:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks: list[str] = []
    current: list[str] = []
    size = 0
    for para in paras:
        if current and size + len(para) + 2 > max_chars:
            chunks.append("\n\n".join(current))
            current = []
            size = 0
        current.append(para)
        size += len(para) + 2
    if current:
        chunks.append("\n\n".join(current))
    return chunks


def extract_pdf(path: Path) -> list[tuple[str, str]]:
    try:
        from pypdf import PdfReader
    except ImportError:  # pragma: no cover
        raise SystemExit("PDF extraction requires pypdf. Install with: pip install -r requirements.txt")
    reader = PdfReader(str(path))
    pages = []
    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append((f"page-{idx}", clean_text(text)))
    return pages


def extract_text_file(path: Path) -> list[tuple[str, str]]:
    return [("document", clean_text(path.read_text(encoding="utf-8", errors="ignore")))]


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract source text into gitignored chunks for analysis.")
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--chunk-chars", type=int, default=5000)
    args = parser.parse_args()

    in_path = args.input
    if not in_path.exists():
        raise SystemExit(f"Input file not found: {in_path}")
    out = args.out
    out.mkdir(parents=True, exist_ok=True)

    suffix = in_path.suffix.lower()
    if suffix == ".pdf":
        units = extract_pdf(in_path)
    elif suffix in {".txt", ".md"}:
        units = extract_text_file(in_path)
    else:
        raise SystemExit(f"Unsupported input type {suffix!r}. Convert to PDF, TXT, or MD first.")

    records = []
    chunk_num = 0
    for unit_id, text in units:
        if not text:
            continue
        for chunk in chunk_text(text, args.chunk_chars):
            chunk_num += 1
            record = {
                "source_id": args.source_id,
                "chunk_id": f"{args.source_id}-{chunk_num:04d}",
                "unit": unit_id,
                "text": chunk,
            }
            records.append(record)

    jsonl = out / "chunks.jsonl"
    with jsonl.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    manifest = {
        "source_id": args.source_id,
        "input_name": in_path.name,
        "chunks": len(records),
        "note": "Generated for local analysis. Do not commit extracted source text unless rights review approves it.",
    }
    (out / "extract-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(records)} chunk(s) to {jsonl}")


if __name__ == "__main__":
    main()
