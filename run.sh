#!/usr/bin/env bash
set -euo pipefail

# Pick python interpreter: prefer python3, fallback to python
PYTHON_BIN=""
for candidate in python3 python; do
  if command -v "$candidate" >/dev/null 2>&1; then
    PYTHON_BIN="$candidate"
    break
  fi
done

if [ -z "$PYTHON_BIN" ]; then
  echo "Error: No Python found. Install python3 (recommended)." >&2
  exit 1
fi

if [ ! -d ".venv" ]; then
  "$PYTHON_BIN" -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt

python src/pipeline.py

echo "OK ✅ Pipeline executed."
echo "Check: outputs/, reports/, data/processed/"