@echo off
REM One-Click Run Script for Agentic AI Document Assistant
REM For Windows Command Prompt
REM Robust version - won't crash on missing tools

setlocal enabledelayedexpansion

echo.
echo ========================================
echo  Agentic AI Document Assistant
echo  One-Click Startup
echo ========================================
echo.

REM Check if Python is installed
echo [1/3] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo OK - Found: %PYTHON_VERSION%
echo.

REM Note about Ollama
echo [2/3] Ollama Status:
echo.
echo   Make sure Ollama is running in a SEPARATE window:
echo   - Open Command Prompt
echo   - Run: ollama serve
echo   - Keep that window OPEN
echo.
timeout /t 3
echo.

REM Check if virtual environment exists, if not create it
echo [3/3] Setting up Python environment...
if not exist "venv" (
    echo   Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Could not create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo WARNING: venv activation returned error, continuing anyway...
)
echo OK - Virtual environment ready
echo.

REM Check and install dependencies
echo Installing/checking dependencies...
python -m pip show streamlit >nul 2>&1
if errorlevel 1 (
    echo Installing required packages ^(this may take 1-2 minutes^)...
    pip install --quiet -r requirements.txt
    if errorlevel 1 (
        echo.
        echo WARNING: Some packages may not have installed
        echo But we'll try to start the app anyway...
        timeout /t 2
    )
)
echo OK - Dependencies ready
echo.

REM Start the application
echo ========================================
echo Starting Streamlit application...
echo ========================================
echo.
echo If browser doesn't open automatically:
echo   Visit: http://localhost:8501
echo.
echo To stop: Press Ctrl+C in this window
echo.

timeout /t 2

REM Try to start the app
streamlit run app.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to start Streamlit
    echo.
    echo Try these solutions:
    echo   1. Check Ollama is running in separate window
    echo   2. Install dependencies manually: pip install -r requirements.txt
    echo   3. Run in PowerShell instead: python RUN.py
    echo.
    pause
    exit /b 1
)

pause
