# 🚀 QUICK START GUIDE - Windows & VS Code

## 5-Minute Setup

### ✅ Prerequisites (Must Have)

1. **Ollama Running** - Open Command Prompt and verify:
   ```
   ollama list
   ```
   You should see all three models:
   - gemma3:4b
   - llama3.2:3b
   - deepseek-r1:7b

2. **Python Installed** - Open Command Prompt and verify:
   ```
   python --version
   ```
   (Should be 3.9 or higher)

3. **VS Code Installed** - Download from https://code.visualstudio.com/

### 🎯 Step-by-Step Setup

#### Step 1: Open Project in VS Code

1. Open VS Code
2. Click **File → Open Folder**
3. Navigate to: `C:\Users\User\Downloads\OLLAMA\agentic-document-assistant`
4. Click **Select Folder**

#### Step 2: Open Terminal in VS Code

1. Press `Ctrl + ~` (backtick) to open the integrated terminal
2. You should see terminal at the bottom
3. Verify you're in the project folder (path should end with `agentic-document-assistant`)

#### Step 3: Create Virtual Environment (Optional)

In the VS Code terminal, run:

```powershell
python -m venv venv
```

Then activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If you get a PowerShell execution error, try:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then retry the activation command above.

**You should see `(venv)` prefix in your terminal** - This means the virtual environment is active.

#### Step 4: Install Dependencies

In the terminal, run:

```powershell
pip install -r requirements.txt
```

Wait for all packages to install (may take 2-3 minutes).

#### Step 5: Verify Ollama Models

In the terminal, run:

```powershell
ollama list
```

**Required output:**
```
NAME                ID              SIZE      MODIFIED
gemma3:4b           ...
llama3.2:3b         ...
deepseek-r1:7b      ...
```

If any model is missing, download it:

```powershell
ollama pull gemma3:4b
ollama pull llama3.2:3b
ollama pull deepseek-r1:7b
```

#### Step 6: Run the Application

In the terminal, run:

```powershell
streamlit run app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
```

A browser window will automatically open, or you can visit `http://localhost:8501`

---

## ✅ Success Indicators

After running `streamlit run app.py`, you should see:

- ✅ Streamlit web interface loads
- ✅ Title: "🤖 Agentic AI Document Processing Assistant"
- ✅ Sidebar with model information
- ✅ File upload area saying "Upload your document"

---

## 🧪 Test the Application

### Test Document Available!

A sample document is included: `sample_document.txt` (AI-related content)

1. In the Streamlit app, click "Upload your document" in the sidebar
2. Select `sample_document.txt`
3. Click "Document Preview" to see extracted text
4. Try one of the agent tabs:
   - **📝 Document Review Tab** - Click "Check & Improve Document"
   - **📋 Summarization Tab** - Click "Full Summary"
   - **🔍 Information Extraction Tab** - Click "Extract Entities & Facts"

Wait a few seconds (models are running locally) and see results!

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ollama'"

**Solution:** Ensure you:
1. Activated virtual environment (you see `(venv)` in terminal)
2. Ran `pip install -r requirements.txt` (check no errors)
3. Try: `pip install ollama==0.1.25`

### Issue: "Connection refused" or "Cannot connect to Ollama"

**Solution:**
1. Open a NEW Command Prompt window
2. Run: `ollama serve`
3. Wait for "Listening on 127.0.0.1:11434"
4. Don't close this window
5. Return to VS Code and try again

### Issue: Streamlit won't load in browser

**Solution:**
1. Close the terminal (Ctrl+C)
2. Wait 5 seconds
3. Run `streamlit run app.py` again
4. Check for any error messages in terminal

### Issue: "Model not found" when trying to process

**Solution:**
1. Check models are downloaded: `ollama list`
2. If missing, download them:
   ```powershell
   ollama pull gemma3:4b
   ollama pull llama3.2:3b
   ollama pull deepseek-r1:7b
   ```

### Issue: Very slow responses (>30 seconds)

**Normal behavior!** Because:
- Models run on your local machine
- First use is slower (model loads into memory)
- Depends on your CPU/RAM
- DeepSeek (7b) is the largest model

**Speed tips:**
- Close other applications
- Use "Quick Summary" instead of "Full Summary"
- Try with shorter documents
- Wait for model to warm up (first request is slowest)

---

## 📂 File Structure After Setup

```
C:\Users\User\Downloads\OLLAMA\agentic-document-assistant\
│
├── app.py                           ← Main application
├── requirements.txt                 ← Dependencies
├── .env                            ← Config (created after setup)
├── sample_document.txt             ← Test document
├── README.md                        ← Full documentation
├── QUICK_START_WINDOWS_VSCODE.md   ← This file
│
├── agents/
│   ├── __init__.py
│   ├── document_agent.py           ← Llama agent
│   ├── summary_agent.py            ← Gemma agent
│   └── info_agent.py               ← DeepSeek agent
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py             ← File processing
│   └── prompts.py                  ← AI prompts
│
├── uploads/                        ← Your uploaded files
└── outputs/                        ← Downloaded results
```

---

## ⚡ Common Commands

Run these in VS Code terminal:

| Command | What it does |
|---------|------------|
| `python --version` | Check Python version |
| `ollama list` | List downloaded models |
| `pip list` | Show installed packages |
| `streamlit run app.py` | Start the application |
| `Ctrl+C` | Stop the application |

---

## 📝 Using the Application

### Basic Workflow

1. **Upload** → Sidebar: Click upload, select a file
2. **Process** → Choose a tab (Document/Summary/Extract)
3. **View** → Results appear on screen
4. **Download** → Go to Download tab, click buttons

### Features by Tab

#### 📝 Document Review
- Check grammar and clarity
- Get improvement suggestions
- Professional tone analysis

#### 📋 Summarization
- Full comprehensive summary
- Bullet point version
- Quick 50-word summary

#### 🔍 Information Extraction
- Extract entities and facts
- Generate comprehensive report
- Research any additional topic

#### 💾 Download
- Save all results as .txt files
- Files also saved to `outputs/` folder
- With timestamps for organization

---

## 🎓 Understanding What's Happening

### The Agent System

When you process a document:

1. **You upload file** → app.py
2. **You choose task** → Which tab/button
3. **Agent decides** → "This is a summary task → use Gemma"
4. **Agent calls Ollama** → Ollama API processes locally
5. **Result returns** → Display on screen

### Models Used

| Model | Purpose | Size |
|-------|---------|------|
| Llama 3.2 3b | Document review & writing | 3 billion parameters |
| Gemma 3 4b | Summarization | 4 billion parameters |
| DeepSeek R1 7b | Information extraction | 7 billion parameters |

**All run locally on your machine!**

---

## 🆘 Need Help?

### Check Error Message Location

Errors appear in two places:

1. **Streamlit App** (in browser) - Shows in red
2. **VS Code Terminal** - Full error details

**Always check the terminal first** for technical details.

### Quick Diagnostics

Run in VS Code terminal:

```powershell
# Check Python
python --version

# Check Ollama
ollama list

# Check Ollama connection
curl http://localhost:11434/api/tags
```

### If Still Stuck

1. Check .env file exists (copy from .env.example if needed)
2. Ensure Ollama is running (separate command prompt window)
3. Restart VS Code
4. Try different document (maybe uploaded file has issues)
5. Check README.md for detailed troubleshooting

---

## 🎉 You're Ready!

You now have:
✅ Agentic AI working locally
✅ Three specialized agents
✅ Beautiful web interface
✅ File upload/download capability
✅ Complete documentation

**Next:** Upload the sample document and test each agent tab!

---

## 💡 Tips for Your Teacher

Show them:
1. Upload a PDF/DOCX/TXT
2. Run each agent
3. Compare outputs from different models
4. Download results
5. Explain how agent chooses the model

**Impress them with:** The fact that everything runs locally - no cloud needed!

---

**Happy Processing! 🚀**
