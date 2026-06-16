# 🚀 One-Click Startup Guide

Choose the appropriate startup method for your system:

## 🪟 Windows Users

### Option 1: RUN.bat (Easiest!)
Simply **double-click** the `RUN.bat` file in the project folder.

**What it does:**
- ✅ Checks Python installation
- ✅ Verifies Ollama connection
- ✅ Creates virtual environment
- ✅ Installs dependencies
- ✅ Starts the application

**That's it!** No terminal commands needed.

### Option 2: RUN.py
Open Command Prompt in the project folder and run:
```cmd
python RUN.py
```

---

## 🍎 Mac Users

### Option: RUN.py
Open Terminal in the project folder and run:
```bash
python3 RUN.py
```

### Or RUN.sh (Advanced)
Make the script executable first:
```bash
chmod +x RUN.sh
./RUN.sh
```

---

## 🐧 Linux Users

### Option: RUN.py
Open Terminal in the project folder and run:
```bash
python3 RUN.py
```

### Or RUN.sh (Preferred)
Make the script executable:
```bash
chmod +x RUN.sh
./RUN.sh
```

---

## ⚠️ Before Running

### Required: Ollama Must Be Running!

**Windows:**
1. Open a **separate** Command Prompt window
2. Run: `ollama serve`
3. You should see: `Listening on 127.0.0.1:11434`
4. **Leave this window open**
5. Now run RUN.bat or RUN.py in a different window

**Mac/Linux:**
1. Open a **separate** Terminal window
2. Run: `ollama serve`
3. You should see: `Listening on 127.0.0.1:11434`
4. **Leave this window open**
5. Now run RUN.py or RUN.sh in a different terminal

---

## 🔍 What Each Script Does

### RUN.bat (Windows .batch file)
- Designed for users who prefer point-and-click
- Double-click to run
- Automatic setup and startup
- Shows progress in Command Prompt window

### RUN.py (Python script - Cross-platform)
- Works on Windows, Mac, and Linux
- Runs: `python RUN.py`
- Checks all dependencies
- Sets up virtual environment
- Installs packages if needed

### RUN.sh (Bash script - Mac/Linux)
- Optimized for Unix-like systems
- Runs: `./RUN.sh`
- Lightweight and fast
- Requires `chmod +x RUN.sh` first

---

## 📋 Step-by-Step: Windows RUN.bat

1. **Start Ollama in separate window:**
   - Open Command Prompt
   - Type: `ollama serve`
   - Wait for: "Listening on 127.0.0.1:11434"
   - **Don't close this window**

2. **Run the application:**
   - Open File Explorer
   - Navigate to project folder
   - **Double-click** `RUN.bat`
   - A Command Prompt window opens
   - Automated setup begins

3. **Wait for browser:**
   - Script checks everything
   - Virtual environment is set up
   - Dependencies are installed
   - Browser opens to http://localhost:8501

4. **Use the application:**
   - Upload documents
   - Process with agents
   - Download results

5. **Stop when done:**
   - Press `Ctrl+C` in the Command Prompt window
   - Close the window

---

## ✅ Success Indicators

After running the startup script, you should see:

```
[1/4] Checking Python installation...
✓ Python 3.11 OK

[2/4] Checking Ollama connection...
✓ Ollama is running

[3/4] Setting up Python environment...
✓ Virtual environment activated

[4/4] Installing dependencies...
✓ Dependencies ready

==================================================
Starting application...
==================================================

Browser will open at: http://localhost:8501
```

Then your browser automatically opens!

---

## 🐛 Troubleshooting

### Error: "Cannot connect to Ollama"

**Solution:**
- Open a **separate** Command Prompt/Terminal
- Run: `ollama serve`
- Wait for the "Listening" message
- **Keep that window open**
- Return to startup script and try again

### Error: "Python is not installed"

**Solution:**
- Download Python from: https://www.python.org/downloads/
- During installation, **CHECK** "Add Python to PATH"
- Restart your computer
- Try again

### Error: "Failed to install dependencies"

**Solution:**
- Ensure you have internet connection
- Try manually: `pip install -r requirements.txt`
- Check your Python version: `python --version`

### Script hangs or takes too long

**Normal!** First time can be slow because:
- Virtual environment is being created
- Packages are being downloaded
- Depends on your internet speed

Just wait, don't close the window.

---

## 🎯 Recommended Workflow

### Daily Use (Windows)

```
1. Open Command Prompt → ollama serve → WAIT
2. (In different window) Double-click RUN.bat
3. Streamlit opens automatically
4. Use the app
5. Close both windows when done
```

### Quick Reference

| System | Command | Command |
|--------|---------|---------|
| **Windows** | Double-click `RUN.bat` | OR `python RUN.py` |
| **Mac** | `python3 RUN.py` | OR `./RUN.sh` |
| **Linux** | `python3 RUN.py` | OR `./RUN.sh` |

---

## 📱 From VS Code

You can also run from VS Code integrated terminal:

**Windows:**
```powershell
.\RUN.py
```

**Mac/Linux:**
```bash
python3 RUN.py
```

Or open terminal at the project folder and double-click RUN.bat (Windows).

---

## 🎓 Teaching Your Teacher

When presenting:

1. **Show the startup:** Double-click RUN.bat or run python RUN.py
2. **Explain what happens:** Automatic checks and setup
3. **Show the app:** Browser opens, ready to use
4. **Process documents:** Upload, process, download
5. **Show the code:** Explain agents architecture

**Impress them with:** "Zero-configuration startup - everything is automated!"

---

## ⚡ Environment Variables

If you need to customize, edit `.env`:

```
OLLAMA_HOST=http://localhost:11434
DOCUMENT_MODEL=llama3.2:3b
SUMMARY_MODEL=gemma3:4b
INFO_MODEL=deepseek-r1:7b
```

The startup scripts don't require any manual `.env` setup - they use defaults!

---

## 🔐 Security Notes

- Scripts only run locally
- No data sent to cloud
- Safe to examine (both .bat and .py are readable text files)
- Can be modified if needed

---

## 📞 Quick Help

**Something not working?**

1. ✅ Ollama running? (`ollama serve` in separate window)
2. ✅ Python installed? (`python --version`)
3. ✅ In the right folder? (Can see RUN.bat or RUN.py)
4. ✅ Try again with fresh window/terminal

---

**Ready? Pick your startup method and go! 🚀**

- **Windows →** Double-click `RUN.bat`
- **Mac/Linux →** Run `python3 RUN.py`

All automated from there!
