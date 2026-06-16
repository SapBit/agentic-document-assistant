# 🤖 Agentic AI Document Processing Assistant

**Phase 1: API Integration & Agent Introduction**

A beginner-friendly Streamlit application that demonstrates agentic AI by processing documents using multiple AI models through Ollama. The agent automatically selects the appropriate model for each task.

## 📋 Project Overview

This application showcases the concept of **Agentic AI** where an intelligent agent decides which tool (AI model) to use based on the task, rather than just taking user input and providing output.

### What is Agentic AI?

```
Traditional AI:  User → AI → Answer
Agentic AI:      User → Agent → Chooses Tool/Model → Result
```

**This application demonstrates:**
- User uploads a document
- Agent identifies the task (review, summarize, or extract info)
- Agent selects the appropriate Ollama model
- Processing occurs and results are returned

## 🎯 Features

✅ **Document Upload**: Support for PDF, DOCX, and TXT files
✅ **Document Review Agent** (Llama 3.2): Grammar check, clarity improvement, professional tone
✅ **Summarization Agent** (Gemma 3): Executive summaries, bullet points, key takeaways
✅ **Information Extraction Agent** (DeepSeek): Entity extraction, fact organization, report generation
✅ **Multiple Processing Options**: Different analysis types and quick summaries
✅ **Download Results**: Save all outputs as text files
✅ **Clean UI**: Intuitive interface with tabs and expandable sections

## 🛠️ Technology Stack

- **Frontend**: Streamlit (web interface)
- **Backend**: Python
- **AI Models**: Ollama (local LLM server)
- **Libraries**:
  - `ollama` - Ollama API client
  - `streamlit` - Web UI framework
  - `PyPDF2` - PDF text extraction
  - `python-docx` - DOCX text extraction
  - `python-dotenv` - Environment variable management

## 📦 Project Structure

```
agentic-document-assistant/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
│
├── agents/                  # AI Agent modules
│   ├── document_agent.py    # Document review & writing (Llama)
│   ├── summary_agent.py     # Summarization (Gemma)
│   └── info_agent.py        # Information extraction (DeepSeek)
│
├── utils/                   # Utility modules
│   ├── file_handler.py      # File upload/extraction functions
│   └── prompts.py           # Prompt templates for AI models
│
├── uploads/                 # Uploaded documents (created automatically)
└── outputs/                 # Generated results (created automatically)
```

## 🚀 Quick Start

### Prerequisites

✓ Python 3.9+ installed
✓ VS Code installed
✓ **Ollama installed and running**
✓ Required models downloaded:
  - `gemma3:4b` (Summarization)
  - `llama3.2:3b` (Document checking)
  - `deepseek-r1:7b` (Information collection)

### Step 1: Verify Ollama is Running

Open Command Prompt and check:
```bash
ollama list
```

You should see:
```
NAME                ID              SIZE      MODIFIED
gemma3:4b          ...
llama3.2:3b        ...
deepseek-r1:7b     ...
```

If not available, download them:
```bash
ollama pull gemma3:4b
ollama pull llama3.2:3b
ollama pull deepseek-r1:7b
```

### Step 2: Clone/Copy Project Files

Copy the `agentic-document-assistant` folder to your preferred location.

### Step 3: Open in VS Code

```bash
cd agentic-document-assistant
code .
```

### Step 4: Create Virtual Environment (Optional but Recommended)

In VS Code terminal:

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Set Environment Variables

Copy `.env.example` to `.env`:

**Windows (PowerShell):**
```bash
Copy-Item ".env.example" ".env"
```

**Windows (Command Prompt):**
```bash
copy .env.example .env
```

**Mac/Linux:**
```bash
cp .env.example .env
```

Edit `.env` if needed (default values should work):
```
OLLAMA_HOST=http://localhost:11434
DOCUMENT_MODEL=llama3.2:3b
SUMMARY_MODEL=gemma3:4b
INFO_MODEL=deepseek-r1:7b
```

### Step 7: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### 1. Upload a Document

- Click "Upload your document" in the sidebar
- Select a PDF, DOCX, or TXT file
- The application will extract text automatically

### 2. Use the Agents

**Document Review Tab** (📝):
- Click "Check & Improve Document" to analyze grammar, clarity, and tone
- Get suggestions for improvement

**Summarization Tab** (📋):
- "Full Summary": Complete executive summary with key points
- "Bullet Points": 5 key bullet points
- "Quick Summary": 50-word quick summary

**Information Extraction Tab** (🔍):
- "Extract Entities & Facts": Important entities and key facts
- "Generate Report": Comprehensive analysis report
- "Research Topic": Research additional topics

### 3. Download Results

Go to the **Download Results** tab and click download buttons for:
- Document Analysis
- Summaries
- Extracted Information
- Generated Reports

All files are saved to the `outputs/` folder as well.

## 🧠 How Agentic AI Works Here

### User Request Flow

```
User Upload → app.py reads file → agent decides task
                                         ↓
                          Which model to use?
                              /    |    \
                        Llama   Gemma  DeepSeek
                       (review) (sum) (extract)
                              ↓    ↓    ↓
                        Process via Ollama API
                              ↓
                         Return Results
```

### Agent Selection Logic

The app uses **task-based routing**:

| Task | Agent | Model | Function |
|------|-------|-------|----------|
| Document Review | Document Agent | Llama 3.2 | check_and_improve_document() |
| Summarization | Summary Agent | Gemma 3 | summarize_document() |
| Information Extraction | Info Agent | DeepSeek | extract_information() |

### Example: Document Review Agent

```python
def check_and_improve_document(document_text):
    # Agent decides: This is a document review task
    # Agent selects: Llama 3.2 model
    response = ollama.chat(
        model='llama3.2:3b',  # Agent's choice!
        messages=[...]
    )
    return response
```

## 🔌 API Integration Details

### Ollama API Connection

The application connects to Ollama's API locally:

```
Python (app.py) → Ollama API (http://localhost:11434) → Local Models
```

**Ollama API Endpoints:**
- Chat: `POST /api/chat`
- Generate: `POST /api/generate`
- List Models: `GET /api/tags`

### Connection Verification

If you get connection errors:

1. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

2. Check Ollama is accessible:
   ```bash
   curl http://localhost:11434/api/tags
   ```

3. Verify model is downloaded:
   ```bash
   ollama list
   ```

## 📝 Understanding the Prompt System

### How Prompts Work

Each agent uses **prompt templates** to instruct the AI model:

**Document Agent Prompt Example:**
```
You are a professional document editor...
Review the following document for:
1. Grammar and spelling errors
2. Clarity and readability
3. Professional tone
4. Structure and organization

Provide:
- A list of issues found
- Corrections and suggestions
- An improved version...
```

**Modify Prompts** in `utils/prompts.py` to change AI behavior.

## 🐛 Troubleshooting

### Issue: "Connection refused" error

**Solution:**
- Ensure Ollama is running: `ollama serve`
- Check `OLLAMA_HOST` in `.env` is correct
- Verify Ollama is accessible: `curl http://localhost:11434/api/tags`

### Issue: "Model not found" error

**Solution:**
- Download the model: `ollama pull llama3.2:3b`
- Verify with: `ollama list`
- Check model name in `.env`

### Issue: Streamlit app won't load

**Solution:**
- Install dependencies: `pip install -r requirements.txt`
- Try: `pip install streamlit --upgrade`
- Check Python version: `python --version` (3.9+ required)

### Issue: PDF extraction fails

**Solution:**
- Ensure file is valid: Try opening in PDF reader
- Try a different PDF format
- Use TXT or DOCX as alternatives

### Issue: Slow responses

**Solution:**
- Reduce document length
- Use "Quick Summary" option instead of full
- Check system resources (RAM, CPU)
- Models run locally so performance depends on your hardware

## 📚 Example Workflow

### Scenario: Analyze a Research Paper

1. **Upload** the PDF research paper
2. **Document Review** → Check academic writing quality
3. **Summarization** → Generate executive summary
4. **Information Extraction** → Extract key findings and entities
5. **Download** all results
6. **Research** related topics for context

## 🎓 Phase 1 vs Future Phases

### Phase 1 (Current)
✅ API integration with Ollama
✅ Basic agent demonstration
✅ Simple UI with Streamlit
✅ File upload/download
✅ Three specialized agents

### Phase 2 Possibilities (Not Implemented)
- Natural language task understanding
- Chained agent workflows
- Multi-document processing
- Vector similarity search (RAG)
- Advanced prompt engineering
- Context memory between sessions

## 💾 File Format Details

### Supported Formats

| Format | Extension | Library | Status |
|--------|-----------|---------|--------|
| Text | .txt | Built-in | ✅ Working |
| PDF | .pdf | PyPDF2 | ✅ Working |
| Word | .docx | python-docx | ✅ Working |

### Output Format

All outputs are saved as `.txt` files with timestamps:
```
outputs/document_analysis_20250616_143022.txt
outputs/summary_20250616_143045.txt
outputs/extracted_info_20250616_143108.txt
```

## 🔒 Security Notes

- No data is sent to external servers (everything runs locally)
- Models run on your machine via Ollama
- API keys are stored in `.env` (not committed to git)
- Uploaded files are stored in `uploads/` folder

## 📞 Support & Common Questions

### Q: Do I need internet connection?
**A:** No! Everything runs locally on your machine once models are downloaded.

### Q: Can I use this with different models?
**A:** Yes! Download other Ollama models and update `.env`:
```
DOCUMENT_MODEL=mistral:7b  # Instead of llama3.2:3b
```

### Q: How large can documents be?
**A:** Depends on your RAM. Context window varies by model. For best results, keep under 10,000 words.

### Q: Can I add more agents?
**A:** Yes! Create a new file in `agents/` folder following the same pattern.

## 📊 Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                   Streamlit UI (app.py)                 │
│  [Upload] [Tabs: Review | Summary | Extract | Download] │
└────────────────┬────────────────────────────────────────┘
                 │
        ┌────────┴────────┬──────────────┐
        ▼                 ▼              ▼
   ┌─────────────┐ ┌────────────┐ ┌──────────────┐
   │  Document   │ │ Summarizer │ │   Info       │
   │   Agent     │ │   Agent    │ │   Agent      │
   │ (llama)     │ │ (gemma)    │ │ (deepseek)   │
   └──────┬──────┘ └─────┬──────┘ └──────┬───────┘
          │               │               │
          └───────────────┼───────────────┘
                          │
              ┌───────────▼───────────┐
              │   Ollama Local API    │
              │ (http://localhost:    │
              │   11434)              │
              └───────────┬───────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
     ┌─────────┐    ┌─────────┐    ┌──────────┐
     │ Gemma   │    │ Llama   │    │ DeepSeek │
     │ 3 4b    │    │ 3.2 3b  │    │ R1 7b    │
     └─────────┘    └─────────┘    └──────────┘
```

## 📄 Requirements Details

- **streamlit** 1.28.1 - Web UI framework
- **ollama** 0.1.25 - Ollama API client
- **PyPDF2** 3.0.1 - PDF text extraction
- **python-docx** 0.8.11 - DOCX file handling
- **python-dotenv** 1.0.0 - Environment configuration
- **requests** 2.31.0 - HTTP library (if needed)

## 🎯 Next Steps for Your Teacher Presentation

### What to Demonstrate

1. **Show the UI** - Clean, organized interface
2. **Upload Document** - Use a sample document
3. **Run Document Agent** - Show grammar/clarity analysis
4. **Run Summary Agent** - Generate summary
5. **Run Info Agent** - Extract information
6. **Download Results** - Show saved outputs
7. **Explain Architecture** - Show agentic decision-making

### Key Points to Explain

- **Agentic AI** - Agent chooses which model to use
- **API Integration** - Python connects to Ollama
- **Local Models** - No cloud needed, runs on your computer
- **Multiple Agents** - Different models for different tasks
- **Task Routing** - Agent decision logic

## 📝 License

This project is for educational purposes.

## 🚀 Getting Help

If you encounter issues:

1. Check that Ollama is running
2. Verify all models are downloaded
3. Check `.env` file configuration
4. Review error messages in Streamlit console
5. Check Python version compatibility

---

**Happy Processing! 🎉**

Start by uploading a document and watching the agents work!
"# agentic-document-assistant" 
"# agentic-document-assistant" 
