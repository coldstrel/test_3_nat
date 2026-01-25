# Bike-sharing demand RAP (Python) — Hour-level (Peak Hours)

This repo is a small **Reproducible Analytical Pipeline (RAP)** that:
1) downloads the **UCI Bike Sharing Dataset** (`hour.csv` by default),
2) cleans/prepares the data,
3) analyzes **peak hours** (workingday vs weekend),
4) trains a fast baseline model,
5) writes **outputs** (tables + figures + a short report).

## Reproducibility
- **Python Version**: Specified in `.python-version` (pinned to 3.12.7). Supports Python 3.10 to 3.13.
- **Dependencies**: Locked in `requirements.lock` for exact environments.
- **Makefile**: Provides a standard interface for reproducibility on Unix systems.

## Quick Start (Unix/macOS/WSL)
If you have `make` installed:
```bash
make
```
This will install dependencies and run the pipeline. You can also use `make test` or `make clean`.

## One-command run (All Platforms)
If you don't have `make` or are on Windows:
```bash
python run.py
```
This script automatically:
1. Detects and uses a compatible Python version (avoids 3.14 alpha).
2. Creates a local virtual environment (`.venv` or `.venv-win`).
3. Installs dependencies from `requirements.lock`.
4. Runs the analysis pipeline.
5. Launches the **Streamlit dashboard** to visualize the results.

## Outputs (generated)
- `outputs/metrics.txt` (RMSE / R²)
- `outputs/summary.csv` (simple group summary)
- `outputs/peak_hours.csv` (top peak hours: workingday vs weekend)
- `outputs/fig_timeseries.png` (rentals over time)
- `outputs/fig_temp_vs_cnt.png` (temperature vs demand)
- `outputs/fig_avg_by_hour.png` (average rentals by hour)
- `reports/REPORT.md` (short human-readable report)
- **Streamlit Dashboard**: A browser-based interactive view of all above.

## Notes
- Default is **hour-level** (`hour.csv`). If you want day-level instead:
  ```bash
  BIKE_LEVEL=day python run.py
  ```
- Downloaded data is stored in `data/raw/` (not committed).
