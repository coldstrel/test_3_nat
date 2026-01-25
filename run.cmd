@echo off
setlocal

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
  %PYTHON% -m venv .venv
)

call .venv\Scripts\activate.bat
pip install -r requirements.txt

python src\pipeline.py

echo OK Pipeline executed.
echo Starting Streamlit in background...
start "" /B .venv\Scripts\python.exe -m streamlit run app.py > streamlit.log 2>&1
echo Streamlit log: streamlit.log
echo Open: http://localhost:8501
echo Check: outputs/, reports/, data/processed/
