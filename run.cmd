@echo off
setlocal

echo === Bike RAP runner (Windows) ===

REM Prefer python3 if available, fall back to python
where python3 >nul 2>nul
if %ERRORLEVEL%==0 (
  set "PYTHON=python3"
) else (
  set "PYTHON=python"
)

where %PYTHON% >nul 2>nul
if NOT %ERRORLEVEL%==0 (
  echo Error: Python not found. Install Python 3.10+ and retry.
  exit /b 1
)

if not exist ".venv\Scripts\python.exe" (
  echo Creating virtualenv...
  %PYTHON% -m venv .venv
)

call .venv\Scripts\activate.bat
echo Installing dependencies...
pip install -r requirements.txt

echo Running pipeline...
python src\pipeline.py

echo OK Pipeline executed.
echo Check: outputs/, reports/, data/processed/
