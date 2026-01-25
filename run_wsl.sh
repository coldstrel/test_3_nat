#!/usr/bin/env bash
set -euo pipefail

# Normalize line endings for WSL if files were edited on Windows.
fix_crlf() {
  local file="$1"
  if [ -f "$file" ]; then
    sed -i 's/\r$//' "$file"
  fi
}

fix_crlf "./run.sh"
fix_crlf "./run_streamlit.sh"

chmod +x ./run.sh
exec ./run.sh
