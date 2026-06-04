# Intake

Place local source documents under `intake/raw/` only when you have the right to use them for analysis. This directory is gitignored except for `.gitkeep`.

Recommended flow:

1. Add or update the source record in `sources/manifest.yml`.
2. Put the local source file in `intake/raw/`.
3. Run `scripts/extract_source_text.py` to create local chunks under `work/extracts/<source-id>/`.
4. Use a Ralph loop or agent session to synthesize patterns from the local chunks.
5. Commit only original pattern files, source metadata, config, scripts, and indexes.
