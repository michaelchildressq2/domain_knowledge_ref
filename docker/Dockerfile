FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        curl \
        git \
        jq \
        make \
        nodejs \
        npm \
        ripgrep \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY requirements.txt /tmp/kb-requirements.txt
RUN pip install -r /tmp/kb-requirements.txt

CMD ["bash"]
