from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"


def venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def ensure_venv() -> None:
    if not VENV_DIR.exists():
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])


def install_requirements() -> None:
    subprocess.check_call([str(venv_python()), "-m", "pip", "install", "-r", "requirements.txt"])


def run_pipeline() -> None:
    subprocess.check_call([str(venv_python()), "src/pipeline.py"])


def run_streamlit(background: bool) -> None:
    cmd = [str(venv_python()), "-m", "streamlit", "run", "app.py"]
    if background:
        log_path = ROOT / "streamlit.log"
        with log_path.open("wb") as log:
            subprocess.Popen(cmd, stdout=log, stderr=subprocess.STDOUT)
        print(f"Streamlit log: {log_path}")
        print("Open: http://localhost:8501")
    else:
        subprocess.check_call(cmd)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run pipeline and/or Streamlit app.")
    parser.add_argument("--pipeline-only", action="store_true", help="Only run the pipeline.")
    parser.add_argument("--streamlit", action="store_true", help="Run Streamlit after pipeline.")
    parser.add_argument("--streamlit-bg", action="store_true", help="Run Streamlit in background.")
    args = parser.parse_args()

    ensure_venv()
    install_requirements()

    if args.pipeline_only or not args.streamlit and not args.streamlit_bg:
        run_pipeline()
    else:
        run_pipeline()
        run_streamlit(background=args.streamlit_bg)


if __name__ == "__main__":
    main()
