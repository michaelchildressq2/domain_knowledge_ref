#!/usr/bin/env python3
"""Convert a PDF into full text plus one text file per detected chapter."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


STRICT_CHAPTER_PATTERN = re.compile(r"^\s*CHAPTER\s+(\d+|[IVXLCDM]+)\s*$")
INLINE_CHAPTER_PATTERN = re.compile(r"^\s*Chapter\s+(\d+|[IVXLCDM]+)\s*[:.\-]\s+(.+)$")
APPENDIX_PATTERN = re.compile(r"^\s*Appendix\s+([A-Z]|\d+)\s*[:.\-]?\s*(.*)$")
END_MATTER_PATTERN = re.compile(
    r"^\s*(Index|About the Author|About the Authors|Colophon|Glossary|Bibliography|References)\s*$",
    re.I,
)
PROSE_REFERENCE_WORDS = {
    "and",
    "describes",
    "describe",
    "relevant",
    "see",
    "showed",
    "shows",
    "explains",
    "explained",
}
SKIP_TITLE_LINES = {
    "contents",
    "table of contents",
    "part i",
    "part ii",
    "part iii",
    "part iv",
    "part v",
    "part vi",
}


@dataclass
class Page:
    number: int
    text: str
    start_line: int
    end_line: int


@dataclass
class Boundary:
    kind: str
    number: str
    title: str
    page: int
    line: int


def slugify(value: str, fallback: str = "book") -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug[:80] or fallback


def clean_line(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def meaningful_lines(text: str) -> list[str]:
    lines = [clean_line(line) for line in text.splitlines()]
    return [line for line in lines if line and sum(ch.isalpha() for ch in line) >= 2]


def extract_with_pdfium(pdf_path: Path) -> tuple[list[str], str]:
    try:
        import pypdfium2 as pdfium  # type: ignore
    except Exception as exc:
        raise RuntimeError("pypdfium2 is not installed") from exc

    doc = pdfium.PdfDocument(str(pdf_path))
    pages: list[str] = []
    for page in doc:
        textpage = page.get_textpage()
        pages.append(textpage.get_text_range() or "")
    return pages, "pypdfium2"


def extract_with_pdftotext(pdf_path: Path) -> tuple[list[str], str]:
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext is not available")
    proc = subprocess.run(
        ["pdftotext", "-layout", str(pdf_path), "-"],
        check=True,
        text=True,
        capture_output=True,
    )
    return [page for page in proc.stdout.split("\f") if page.strip()], "pdftotext"


def extract_pages(pdf_path: Path) -> tuple[list[Page], list[str], str]:
    try:
        raw_pages, extractor = extract_with_pdfium(pdf_path)
    except Exception:
        raw_pages, extractor = extract_with_pdftotext(pdf_path)

    pages: list[Page] = []
    all_lines: list[str] = []
    for index, text in enumerate(raw_pages, start=1):
        start = len(all_lines)
        lines = text.splitlines()
        all_lines.extend(lines)
        pages.append(Page(index, text, start, len(all_lines)))
        all_lines.append(f"\n--- PDF page {index + 1} ---\n")
    return pages, all_lines, extractor


def detect_title(pages: list[Page], pdf_path: Path) -> str:
    for page in pages[:8]:
        candidates = meaningful_lines(page.text)[:20]
        for index, line in enumerate(candidates):
            if re.match(r"^by\s+[\w .'-]+$", line, re.I) and index > 0:
                return candidates[index - 1][:120]
    for page in pages[:8]:
        candidates = meaningful_lines(page.text)[:20]
        if candidates and candidates[0].lower().startswith("praise for "):
            continue
        for index in range(len(candidates) - 1):
            combined = f"{candidates[index]} {candidates[index + 1]}"
            if re.search(r"\bInfrastructure\s+as\s+Code\b", combined, re.I):
                next_line = candidates[index + 2] if index + 2 < len(candidates) else ""
                if next_line and len(next_line) <= 90 and next_line.lower() != "second edition":
                    return f"Infrastructure as Code: {next_line}"[:120]
                return "Infrastructure as Code"
        for index, line in enumerate(candidates):
            if re.search(r"\bInfrastructure\s+as\s+Code\b", line, re.I):
                next_line = candidates[index + 1] if index + 1 < len(candidates) else ""
                if next_line and len(next_line) <= 90 and not re.search(r"\bby\b", next_line, re.I):
                    return f"{line}: {next_line}"[:120]
                return line
    for page in pages[:5]:
        candidates = [
            line for line in meaningful_lines(page.text)[:10]
            if len(line) <= 90 and line.lower() not in SKIP_TITLE_LINES
        ]
        if candidates:
            return candidates[0]
    return pdf_path.stem


def next_title(lines: list[str], start: int) -> str:
    title_lines: list[str] = []
    continuation_pattern = re.compile(r"(,|:|\b(and|or|of|the|with|for|to|in))$", re.I)
    for offset, line in enumerate(lines[start + 1 : start + 8], start=start + 1):
        value = clean_line(line)
        low = value.lower()
        if not value or low in SKIP_TITLE_LINES or re.match(r"^\d+$", value):
            continue
        if STRICT_CHAPTER_PATTERN.match(value) or INLINE_CHAPTER_PATTERN.match(value) or APPENDIX_PATTERN.match(value):
            continue
        if value.endswith(":"):
            for extra in lines[offset + 1 : offset + 4]:
                continuation = clean_line(extra)
                if continuation and not re.match(r"^\d+$", continuation):
                    return f"{value} {continuation}"[:100]
        if len(value) <= 70 and not re.search(r"[.!?]$", value):
            title_lines.append(value)
            if not continuation_pattern.search(value):
                break
            continue
        if title_lines:
            break
        return value[:100]
    if title_lines:
        return " ".join(title_lines)[:100]
    return ""


def looks_like_prose_reference(title: str) -> bool:
    words = {word.lower().strip(".,:;()") for word in title.split()}
    if words & PROSE_REFERENCE_WORDS:
        return True
    return title.endswith(".") and len(title.split()) > 6


def detect_boundaries(pages: list[Page], all_lines: list[str]) -> list[Boundary]:
    boundaries: list[Boundary] = []
    seen: set[tuple[str, str]] = set()
    late_page_threshold = max(20, int(len(pages) * 0.75))
    for page in pages:
        for line_no in range(page.start_line, page.end_line):
            line = clean_line(all_lines[line_no])
            if len(line) > 120:
                continue
            kind = ""
            number = ""
            title = ""
            strict = STRICT_CHAPTER_PATTERN.match(line)
            inline = INLINE_CHAPTER_PATTERN.match(line)
            appendix = APPENDIX_PATTERN.match(line)
            end_matter = END_MATTER_PATTERN.match(line)
            if strict:
                kind = "chapter"
                number = strict.group(1)
                title = next_title(all_lines, line_no)
            elif inline and not looks_like_prose_reference(inline.group(2)):
                kind = "chapter"
                number = inline.group(1)
                title = clean_line(inline.group(2))
            elif appendix:
                kind = "appendix"
                number = appendix.group(1)
                title = clean_line(appendix.group(2)) or next_title(all_lines, line_no)
            elif end_matter and page.number > 20:
                if end_matter.group(1).lower() in {"references", "bibliography"} and page.number < late_page_threshold:
                    continue
                kind = "end"
                number = ""
                title = clean_line(end_matter.group(1))
            else:
                continue
            key = (kind, title.lower() if kind == "end" else number.lower())
            if key not in seen:
                seen.add(key)
                boundaries.append(Boundary(kind, number, title, page.number, line_no))
    return boundaries


def find_signal_pages(pages: list[Page], word: str, limit: int = 6) -> list[int]:
    pattern = re.compile(rf"\b{re.escape(word)}\b", re.I)
    return [page.number for page in pages if pattern.search(page.text)][:limit]


def front_matter_excerpt(pages: list[Page], word: str, max_chars: int = 2500) -> str:
    for page in pages[:40]:
        if any(clean_line(line).lower() == word.lower() for line in page.text.splitlines()):
            return clean_line(page.text[:max_chars])
    for page in pages[:40]:
        if re.search(rf"\b{re.escape(word)}\b", page.text, re.I):
            return clean_line(page.text[:max_chars])
    return ""


def write_context(
    output_dir: Path,
    pdf_path: Path,
    title: str,
    extractor: str,
    pages: list[Page],
    boundaries: list[Boundary],
) -> None:
    toc_pages = find_signal_pages(pages[:50], "contents")
    preface_pages = find_signal_pages(pages[:80], "preface")
    index_pages = find_signal_pages(pages[-80:], "index")
    lines = [
        f"Title: {title}",
        f"Source: {pdf_path}",
        f"Extractor: {extractor}",
        f"Pages: {len(pages)}",
        f"Detected chapters: {len([b for b in boundaries if b.kind == 'chapter'])}",
        f"TOC signal pages: {toc_pages or 'none'}",
        f"Preface signal pages: {preface_pages or 'none'}",
        f"Index signal pages: {index_pages or 'none'}",
        "",
        "Detected boundaries:",
    ]
    lines.extend(
        f"- p. {b.page}: {b.kind.title()} {b.number} {b.title}".rstrip()
        for b in boundaries
    )
    preface = front_matter_excerpt(pages, "preface")
    if preface:
        lines.extend(["", "Preface excerpt for context:", preface])
    output_dir.joinpath("context.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def clean_previous_outputs(output_dir: Path) -> None:
    for path in output_dir.glob("chapter-*.txt"):
        path.unlink()
    for name in ("full-text.txt", "context.txt"):
        path = output_dir / name
        if path.exists():
            path.unlink()


def write_chapters(output_dir: Path, all_lines: list[str], boundaries: list[Boundary]) -> None:
    file_index = 1
    for index, boundary in enumerate(boundaries):
        if boundary.kind not in {"chapter", "appendix"}:
            continue
        end = boundaries[index + 1].line if index + 1 < len(boundaries) else len(all_lines)
        title = boundary.title or f"{boundary.kind}-{boundary.number}"
        filename = f"{boundary.kind}-{file_index:03d}-{slugify(title, boundary.kind)}.txt"
        body = "\n".join(all_lines[boundary.line:end]).strip() + "\n"
        output_dir.joinpath(filename).write_text(body, encoding="utf-8")
        file_index += 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Input PDF path")
    parser.add_argument("--output-dir", type=Path, help="Output folder")
    args = parser.parse_args(argv)

    pdf_path = args.pdf
    if not pdf_path.exists():
        parser.error(f"PDF not found: {pdf_path}")

    pages, all_lines, extractor = extract_pages(pdf_path)
    if sum(len(page.text.strip()) for page in pages) < 1000:
        raise RuntimeError("Very little text was extracted; this PDF may need OCR.")

    title = detect_title(pages, pdf_path)
    output_dir = args.output_dir or pdf_path.with_name(f"{slugify(pdf_path.stem)}-chapters")
    output_dir.mkdir(parents=True, exist_ok=True)
    clean_previous_outputs(output_dir)
    output_dir.joinpath("full-text.txt").write_text("\n".join(all_lines), encoding="utf-8")

    boundaries = detect_boundaries(pages, all_lines)
    write_context(output_dir, pdf_path, title, extractor, pages, boundaries)
    if boundaries:
        write_chapters(output_dir, all_lines, boundaries)

    print(f"Wrote {output_dir}")
    print(f"Extractor: {extractor}; pages: {len(pages)}; boundaries: {len(boundaries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
