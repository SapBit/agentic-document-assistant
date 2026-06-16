#!/usr/bin/env python3
"""
One-Click Run Script for Agentic AI Document Assistant
For Windows, Mac, and Linux
Just run: python RUN.py
"""

import subprocess
import sys
import os
import time
from pathlib import Path

def print_header(text):
    """Print formatted header."""
    print()
    print("=" * 50)
    print(f"  {text}")
    print("=" * 50)
    print()

def check_python():
    """Check Python version."""
    print("[1/5] Checking Python installation...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        print(f"✓ Python {version.major}.{version.minor} OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} - Need 3.9+")
        return False

def check_ollama():
    """Check if Ollama is running."""
    print("[2/5] Checking Ollama connection...")
    try:
        import urllib.request
        urllib.request.urlopen('http://localhost:11434/api/tags', timeout=2)
        print("✓ Ollama is running")
        return True
    except Exception as e:
        print("✗ Cannot connect to Ollama")
        print()
        print("Please start Ollama:")
        print("  1. Open Command Prompt")
        print("  2. Run: ollama serve")
        print("  3. Keep that window open")
        return False

def setup_venv():
    """Setup virtual environment."""
    print("[3/5] Setting up Python environment...")
    venv_path = Path('venv')
    
    if not venv_path.exists():
        print("  Creating virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=False)
    
    print("✓ Virtual environment ready")
    return True

def install_dependencies():
    """Install required packages."""
    print("[4/5] Checking dependencies...")
    
    try:
        import streamlit
        print("✓ All dependencies installed")
        return True
    except ImportError:
        print("  Installing packages (may take 1-2 minutes)...")
        
        # Determine pip executable
        if sys.platform == 'win32':
            pip_exe = Path('venv') / 'Scripts' / 'pip'
        else:
            pip_exe = Path('venv') / 'bin' / 'pip'
        
        result = subprocess.run(
            [str(pip_exe), 'install', '-q', '-r', 'requirements.txt'],
            capture_output=True
        )
        
        if result.returncode == 0:
            print("✓ Dependencies installed")
            return True
        else:
            print("✗ Failed to install dependencies")
            print("Try manually: pip install -r requirements.txt")
            return False

def start_app():
    """Start the Streamlit application."""
    print_header("Starting Agentic AI Assistant")
    
    print("Browser will open automatically at: http://localhost:8501")
    print()
    print("To stop the application: Press Ctrl+C")
    print()
    
    time.sleep(2)
    
    # Determine python executable in venv
    if sys.platform == 'win32':
        python_exe = Path('venv') / 'Scripts' / 'python'
    else:
        python_exe = Path('venv') / 'bin' / 'python'
    
    try:
        subprocess.run([str(python_exe), '-m', 'streamlit', 'run', 'app.py'])
    except KeyboardInterrupt:
        print("\nApplication stopped.")
    except Exception as e:
        print(f"Error starting application: {e}")
        return False
    
    return True

def main():
    """Main startup flow."""
    print_header("Agentic AI Document Assistant - Startup")
    
    # Check Python
    if not check_python():
        print("\nPlease install Python 3.9+")
        sys.exit(1)
    print()
    
    # Check Ollama
    if not check_ollama():
        print("\nPlease start Ollama before continuing.")
        sys.exit(1)
    print()
    
    # Setup venv
    if not setup_venv():
        print("\nFailed to setup virtual environment")
        sys.exit(1)
    print()
    
    # Install dependencies
    if not install_dependencies():
        print("\nFailed to install dependencies")
        sys.exit(1)
    print()
    
    # Start app
    if not start_app():
        sys.exit(1)

if __name__ == '__main__':
    main()
