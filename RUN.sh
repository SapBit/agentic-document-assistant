#!/bin/bash
# One-Click Run Script for Agentic AI Document Assistant
# For Mac and Linux
# Just run: bash RUN.sh

echo ""
echo "=================================================="
echo "  Agentic AI Document Assistant"
echo "  One-Click Startup"
echo "=================================================="
echo ""

# Check Python
echo "[1/4] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 is not installed"
    echo "Please install Python 3.9+ from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $PYTHON_VERSION"
echo ""

# Check Ollama
echo "[2/4] Checking Ollama connection..."
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "✗ Cannot connect to Ollama"
    echo ""
    echo "Please start Ollama:"
    echo "  1. Open Terminal"
    echo "  2. Run: ollama serve"
    echo "  3. Keep that window open"
    exit 1
fi
echo "✓ Ollama is running"
echo ""

# Setup venv
echo "[3/4] Setting up Python environment..."
if [ ! -d "venv" ]; then
    echo "  Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
echo "✓ Virtual environment activated"
echo ""

# Install dependencies
echo "[4/4] Installing dependencies..."
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "  Installing packages (may take 1-2 minutes)..."
    pip install -q -r requirements.txt
fi
echo "✓ Dependencies ready"
echo ""

# Start app
echo "=================================================="
echo "Starting application..."
echo "=================================================="
echo ""
echo "Browser will open at: http://localhost:8501"
echo "Press Ctrl+C to stop"
echo ""

sleep 2
streamlit run app.py
