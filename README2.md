# Bike-sharing Demand RAP — Peak Hours Analysis

A **Reproducible Analytical Pipeline (RAP)** for analyzing bike-sharing demand patterns with a focus on identifying peak hours across different day types (workdays vs weekends).

## Overview

This pipeline performs end-to-end analysis of the UCI Bike Sharing Dataset:

1. **Data Acquisition**: Downloads the UCI Bike Sharing Dataset (`hour.csv`)
2. **Data Processing**: Cleans and prepares hourly bike-sharing records
3. **Peak Hours Analysis**: Identifies usage patterns for workdays vs weekends
4. **Baseline Modeling**: Trains a fast predictive model for demand forecasting
5. **Output Generation**: Creates tables, visualizations, and analytical reports
6. **Interactive Dashboard**: Provides a Streamlit web interface for exploration

## Features

- **Fully containerized** with Docker for consistent execution across platforms
- **Reproducible** with pinned dependencies and version control
- **Interactive visualization** via Streamlit dashboard
- **Automated pipeline** from raw data to insights
- **Local file persistence** for outputs and reports

## Prerequisites

Before you begin, ensure you have:

- **Docker** installed on your system:
  - **Windows**: Docker Desktop with WSL2 enabled
  - **macOS/Linux**: Docker Engine
- A terminal (PowerShell, CMD, Git Bash, or Unix shell)
- This repository cloned locally

## Quick Start

### 1. Build the Docker Image

Navigate to the project directory and build the image:

```shell
docker build -t bike-rap:latest .
```

This command creates a Docker image named `bike-rap:latest` with all dependencies installed.

### 2. Run the Pipeline

Execute one of the following commands based on your shell:

**Git Bash (Windows):**

```shell
docker run --rm -p 8501:8501 --mount type=bind,source="$(pwd)",target=/app bike-rap:latest
```

**CMD, PowerShell, WSL, Linux, or macOS:**

```shell
docker run --rm -p 8501:8501 -v .:/app bike-rap:latest
```

This command will:
- Run the complete analytical pipeline
- Generate `outputs/`, `reports/`, and `processed_data/` directories
- Launch the Streamlit dashboard
- Expose the application on port 8501

### 3. Access the Dashboard

Open your browser and navigate to:

[http://localhost:8501](http://localhost:8501)

## Reproducibility

- **Python Version**: Pinned to 3.12.7 in `.python-version` (supports Python 3.10-3.13)
- **Dependencies**: Locked versions in `requirements.txt`
- **Containerization**: Docker ensures consistent environment across platforms
- **Version Control**: Git tracking for complete pipeline history

## Development

To run the pipeline locally without Docker:

```shell
# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python run.py

# Launch the dashboard
streamlit run app.py
```

## Output Artifacts

After running the pipeline, you'll find:

- **`outputs/`**: Generated charts and visualizations
- **`reports/`**: Analytical reports and summary statistics
- **`processed_data/`**: Cleaned and transformed datasets
