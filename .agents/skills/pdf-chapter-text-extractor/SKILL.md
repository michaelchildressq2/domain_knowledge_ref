---
name: pdf-chapter-text-extractor
description: Convert PDF books, reports, manuals, or long documents into local plain-text files split by chapter. Use when asked to extract PDF text, create per-chapter text files, use a parse.py-like PDF parser, or prepare chapter text for later analysis.
---

# PDF Chapter Text Extractor

Use this skill to turn one input PDF into a local folder of plain-text chapter files.

## Workflow

1. Locate the PDF and choose the output directory.
   - Default output folder: `./work/book-<cleaned-title>/chapter-out/` from the repository root.
   - Folder names and file names should be filesystem-safe slugs based on the book and chapter titles.
   - Keep raw PDF text output under `./work`; do not write chapter text to tracked folders.

2. Run the bundled parser in Docker first.

Build the image when needed:

```bash
docker build -t pdf-chapter-text-extractor .agents/skills/pdf-chapter-text-extractor
```

Run the parser from the repository or working directory that contains the PDF:

```bash
docker run --rm -v "$PWD:/work" pdf-chapter-text-extractor path/to/book.pdf
```

Optional explicit output:

```bash
docker run --rm -v "$PWD:/work" pdf-chapter-text-extractor path/to/book.pdf --output-dir work/book-cleaned-title/chapter-out
```

If Docker is unavailable, use host Python as a fallback. The host environment needs `pypdfium2` installed, or `pdftotext` available on `PATH`.

```bash
python3 .agents/skills/pdf-chapter-text-extractor/scripts/pdf_to_chapters.py path/to/book.pdf
```

Optional explicit output:

```bash
python3 .agents/skills/pdf-chapter-text-extractor/scripts/pdf_to_chapters.py path/to/book.pdf --output-dir work/book-cleaned-title/chapter-out
```

3. Inspect `context.txt`.
   - Use detected title, preface, table-of-contents, outline, and index signals to understand the book structure.
   - Treat inferred chapter boundaries as evidence to review, not guaranteed truth.

4. Inspect generated chapter files.
   - Expected files include `full-text.txt`, `context.txt`, and `chapter-001-<slug>.txt`.
   - If chapter splitting looks wrong, refine the script or manually adjust boundaries from the evidence in `context.txt`.

## Quality Rules

- Prefer the script over rewriting ad hoc parsing code.
- Keep raw extracted text local. Do not commit, publish, or reuse full copyrighted chapter text unless the user explicitly approves.
- For scanned/image-only PDFs, stop if extraction produces little text and tell the user OCR is needed.
- If no reliable chapters are found, preserve `full-text.txt`, report the limitation, and use `context.txt` for next-step diagnosis.

## Resource

- `scripts/pdf_to_chapters.py`: uses `pypdfium2` like `parse.py`, extracts full text, derives context from front matter/index signals, and writes one text file per detected chapter.
