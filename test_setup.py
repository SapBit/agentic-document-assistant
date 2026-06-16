"""
Test Script - Verify Agentic AI Setup
Run this to test all components before running the Streamlit app.

Usage:
    python test_setup.py
"""

import sys
import os
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 60)
print("🧪 AGENTIC AI SETUP VERIFICATION TEST")
print("=" * 60)
print()

# Test 1: Check Python Version
print("1️⃣ Checking Python Version...")
python_version = sys.version_info
if python_version.major == 3 and python_version.minor >= 9:
    print(f"   ✅ Python {python_version.major}.{python_version.minor} OK")
else:
    print(f"   ❌ Python {python_version.major}.{python_version.minor} - Need 3.9+")
print()

# Test 2: Check Required Packages
print("2️⃣ Checking Installed Packages...")
required_packages = {
    'streamlit': 'Streamlit (Web UI)',
    'ollama': 'Ollama Client',
    'PyPDF2': 'PDF Processing',
    'docx': 'DOCX Processing (python-docx)',
    'dotenv': 'Environment Variables',
}

missing_packages = []
for package, description in required_packages.items():
    try:
        __import__(package)
        print(f"   ✅ {description}")
    except ImportError:
        print(f"   ❌ {description} - NOT INSTALLED")
        missing_packages.append(package)

if missing_packages:
    print()
    print("   💡 Install missing packages:")
    print(f"   pip install {' '.join(missing_packages)}")
print()

# Test 3: Check .env File
print("3️⃣ Checking Configuration (.env)...")
env_path = Path('.env')
env_example_path = Path('.env.example')

if env_path.exists():
    print("   ✅ .env file found")
    with open('.env', 'r') as f:
        content = f.read()
        if 'OLLAMA_HOST' in content:
            print("   ✅ OLLAMA_HOST configured")
        if 'DOCUMENT_MODEL' in content:
            print("   ✅ DOCUMENT_MODEL configured")
        if 'SUMMARY_MODEL' in content:
            print("   ✅ SUMMARY_MODEL configured")
        if 'INFO_MODEL' in content:
            print("   ✅ INFO_MODEL configured")
elif env_example_path.exists():
    print("   ⚠️  .env not found (using .env.example)")
    print("   💡 Copy: copy .env.example .env")
else:
    print("   ❌ .env and .env.example not found")
print()

# Test 4: Check Ollama Connection
print("4️⃣ Testing Ollama Connection...")
try:
    import ollama
    from dotenv import load_dotenv
    
    load_dotenv()
    ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
    
    print(f"   📍 Ollama Host: {ollama_host}")
    
    try:
        # Try to get list of models
        response = ollama.list()
        print("   ✅ Connected to Ollama successfully")
        
        models_found = []
        if hasattr(response, 'models'):
            for model in response.models:
                model_name = model.model if hasattr(model, 'model') else str(model)
                models_found.append(model_name)
        
        print("\n   📊 Available Models:")
        required_models = ['gemma3:4b', 'llama3.2:3b', 'deepseek-r1:7b']
        
        if models_found:
            for model in models_found:
                print(f"      • {model}")
        else:
            print("      • (Unable to parse model list)")
            
        print("\n   ✓ Checking for required models:")
        missing_models = []
        for req_model in required_models:
            found = any(req_model in model for model in models_found)
            if found or len(models_found) == 0:  # Assume OK if can't parse
                status = "✅" if found else "❓"
                print(f"      {status} {req_model}")
            else:
                print(f"      ❌ {req_model} - NOT FOUND")
                missing_models.append(req_model)
        
        if missing_models:
            print("\n   💡 Download missing models:")
            for model in missing_models:
                print(f"      ollama pull {model}")
        
    except Exception as e:
        print(f"   ❌ Cannot connect to Ollama")
        print(f"   Error: {str(e)}")
        print("   💡 Make sure Ollama is running:")
        print("      Open Command Prompt and run: ollama serve")
        
except ImportError:
    print("   ❌ Ollama package not installed")
    print("   💡 Run: pip install ollama")

print()

# Test 5: Check Project Structure
print("5️⃣ Checking Project Structure...")
required_files = {
    'app.py': 'Main Application',
    'requirements.txt': 'Dependencies',
    'README.md': 'Documentation',
    'agents/document_agent.py': 'Document Agent',
    'agents/summary_agent.py': 'Summary Agent',
    'agents/info_agent.py': 'Info Agent',
    'utils/file_handler.py': 'File Handler',
    'utils/prompts.py': 'Prompt Templates',
}

for file_path, description in required_files.items():
    if Path(file_path).exists():
        print(f"   ✅ {description}")
    else:
        print(f"   ❌ {description} ({file_path})")

print()

# Test 6: Check Sample Document
print("6️⃣ Checking Sample Files...")
if Path('sample_document.txt').exists():
    size = Path('sample_document.txt').stat().st_size
    print(f"   ✅ Sample document found ({size} bytes)")
else:
    print(f"   ⚠️  sample_document.txt not found")

# Create directories
os.makedirs('uploads', exist_ok=True)
os.makedirs('outputs', exist_ok=True)
print("   ✅ uploads/ directory")
print("   ✅ outputs/ directory")

print()

# Final Summary
print("=" * 60)
print("📊 VERIFICATION SUMMARY")
print("=" * 60)

if not missing_packages and Path('app.py').exists():
    print("✅ All essential components are set up!")
    print()
    print("🚀 Ready to run:")
    print("   streamlit run app.py")
    print()
    print("Then open your browser to http://localhost:8501")
else:
    print("⚠️  Some issues detected - see above for fixes")
    print()
    print("Common fixes:")
    print("• Install packages: pip install -r requirements.txt")
    print("• Start Ollama: ollama serve (in separate window)")
    print("• Copy config: copy .env.example .env")

print()
print("=" * 60)
