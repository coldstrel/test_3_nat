# Reproducible base (pick one):
# - python:3.10-slim  (matches your 3.10 baseline)
# - python:3.12-slim  (faster / newer, usually fine if deps support it)
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel \
 && python -m pip install -r /app/requirements.txt

COPY . /app

ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_PORT=8501

EXPOSE 8501

CMD ["bash", "-lc", "set -euo pipefail; \
  if [ -n \"${BIKE_LEVEL:-}\" ]; then levels=\"$BIKE_LEVEL\"; else levels=\"hour day\"; fi; \
  for lvl in $levels; do \
    echo \"--- Running pipeline for level: $lvl ---\"; \
    BIKE_LEVEL=\"$lvl\" python src/pipeline.py; \
  done; \
  echo \"--- Launching Streamlit app ---\"; \
  exec streamlit run app.py --server.address=0.0.0.0 --server.port=8501"]
