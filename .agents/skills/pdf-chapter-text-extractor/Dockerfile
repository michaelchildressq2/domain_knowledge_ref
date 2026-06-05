FROM python:3.13-slim

RUN pip install --no-cache-dir pypdfium2

COPY scripts/pdf_to_chapters.py /opt/pdf_to_chapters.py

WORKDIR /work
ENTRYPOINT ["python", "/opt/pdf_to_chapters.py"]
