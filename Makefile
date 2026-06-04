PYTHON ?= $(shell if [ -x domain/bin/python ]; then echo domain/bin/python; else echo python3; fi)

.PHONY: validate index suggest-tags write-tags extract-help

validate:
	$(PYTHON) scripts/validate_patterns.py

index:
	$(PYTHON) scripts/build_index.py

suggest-tags:
	$(PYTHON) scripts/enrich_related_tags.py --suggest

write-tags:
	$(PYTHON) scripts/enrich_related_tags.py --write

extract-help:
	$(PYTHON) scripts/extract_source_text.py --help
