# 📚 API Reference & Developer Guide

## Module Reference

### 1. Document Agent (`agents/document_agent.py`)

#### `check_and_improve_document(document_text)`

Review and improve a document using Llama 3.2 model.

**Parameters:**
- `document_text` (str): The document to review

**Returns:**
```python
{
    'status': 'success' or 'error',
    'analysis': str,  # Detailed analysis and suggestions
    'model_used': str  # Model name
}
```

**Example:**
```python
from agents.document_agent import check_and_improve_document

doc = "Your text here"
result = check_and_improve_document(doc)

if result['status'] == 'success':
    print(result['analysis'])
```

#### `rewrite_section(section_text, instruction)`

Rewrite a specific section based on instructions.

**Parameters:**
- `section_text` (str): The section to rewrite
- `instruction` (str): Rewriting instruction

**Returns:**
```python
{
    'status': 'success' or 'error',
    'rewritten_text': str
}
```

---

### 2. Summary Agent (`agents/summary_agent.py`)

#### `summarize_document(document_text)`

Create comprehensive summary with executive summary, key points, and takeaways.

**Parameters:**
- `document_text` (str): Document to summarize

**Returns:**
```python
{
    'status': 'success' or 'error',
    'summary': str,  # Full summary
    'model_used': str
}
```

#### `create_bullet_summary(document_text, num_points=5)`

Create bullet-point summary.

**Parameters:**
- `document_text` (str): Document to summarize
- `num_points` (int): Number of bullet points (default: 5)

**Returns:**
```python
{
    'status': 'success' or 'error',
    'bullet_points': str
}
```

#### `extract_key_takeaways(document_text)`

Extract actionable key takeaways.

**Parameters:**
- `document_text` (str): Document to analyze

**Returns:**
```python
{
    'status': 'success' or 'error',
    'takeaways': str
}
```

---

### 3. Information Agent (`agents/info_agent.py`)

#### `extract_information(document_text)`

Extract and organize structured information from document.

**Parameters:**
- `document_text` (str): Document to analyze

**Returns:**
```python
{
    'status': 'success' or 'error',
    'extracted_info': str,  # Organized information
    'model_used': str
}
```

#### `collect_topic_information(topic)`

Research and collect information about a specific topic.

**Parameters:**
- `topic` (str): Topic to research

**Returns:**
```python
{
    'status': 'success' or 'error',
    'research': str,  # Research content
    'topic': str
}
```

#### `extract_entities_and_facts(document_text)`

Extract entities (people, concepts, organizations) and facts.

**Parameters:**
- `document_text` (str): Document to analyze

**Returns:**
```python
{
    'status': 'success' or 'error',
    'entities_and_facts': str
}
```

#### `generate_report(document_text, report_type='comprehensive')`

Generate structured report.

**Parameters:**
- `document_text` (str): Document to process
- `report_type` (str): 'comprehensive', 'executive', or 'action_items'

**Returns:**
```python
{
    'status': 'success' or 'error',
    'report': str,
    'report_type': str
}
```

---

### 4. File Handler (`utils/file_handler.py`)

#### `extract_text_from_pdf(file_path)`

Extract text from PDF file.

**Parameters:**
- `file_path` (str): Path to PDF file

**Returns:**
- `str`: Extracted text

#### `extract_text_from_docx(file_path)`

Extract text from DOCX file.

**Parameters:**
- `file_path` (str): Path to DOCX file

**Returns:**
- `str`: Extracted text

#### `extract_text_from_txt(file_path)`

Extract text from TXT file.

**Parameters:**
- `file_path` (str): Path to TXT file

**Returns:**
- `str`: File content

#### `extract_text_from_file(file_path)`

Auto-detect format and extract text.

**Parameters:**
- `file_path` (str): Path to any supported file

**Returns:**
- `str`: Extracted text

**Supported Formats:**
- .pdf (requires PyPDF2)
- .docx (requires python-docx)
- .txt

#### `save_output(content, filename_prefix, file_format='txt')`

Save processed content to file.

**Parameters:**
- `content` (str): Content to save
- `filename_prefix` (str): Filename prefix
- `file_format` (str): 'txt' or 'docx'

**Returns:**
- `str`: Path to saved file

**Example:**
```python
from utils.file_handler import save_output

result = "Summary text..."
path = save_output(result, 'my_summary')
# Saved to: outputs/my_summary_20250616_143022.txt
```

---

## Prompt Templates (`utils/prompts.py`)

### DOCUMENT_CHECK_PROMPT

Template for document review tasks. Used by Document Agent.

**Format:**
```
You are a professional document editor and writing expert.
Review the following document for:
1. Grammar and spelling errors
2. Clarity and readability
3. Professional tone
4. Structure and organization

Provide:
- A list of issues found
- Corrections and suggestions
- An improved version of the document
```

### SUMMARY_PROMPT

Template for summarization tasks. Used by Summary Agent.

**Includes:**
1. Executive Summary (2-3 sentences)
2. Key Points (5-7 bullet points)
3. Important Takeaways (3-4 points)

### INFO_COLLECTION_PROMPT

Template for information extraction. Used by Info Agent.

**Extracts:**
1. Main Topics/Entities
2. Key Facts
3. Action Items
4. Categories
5. Important Numbers/Data

### TOPIC_RESEARCH_PROMPT

Template for topic research.

**Includes:**
1. Definition and Overview
2. Key Concepts
3. Applications
4. Current Trends
5. Challenges and Limitations
6. Resources for Further Learning

---

## Using the Agents Programmatically

### Basic Usage Example

```python
from agents.document_agent import check_and_improve_document
from agents.summary_agent import summarize_document
from agents.info_agent import extract_information
from utils.file_handler import extract_text_from_file, save_output

# Load document
text = extract_text_from_file('my_document.pdf')

# Process with agents
doc_result = check_and_improve_document(text)
sum_result = summarize_document(text)
info_result = extract_information(text)

# Save results
if doc_result['status'] == 'success':
    save_output(doc_result['analysis'], 'document_analysis')

if sum_result['status'] == 'success':
    save_output(sum_result['summary'], 'summary')

if info_result['status'] == 'success':
    save_output(info_result['extracted_info'], 'extracted_info')
```

### Creating an Agent Pipeline

```python
def process_document_pipeline(file_path):
    """Process document through all agents."""
    
    # Extract text
    text = extract_text_from_file(file_path)
    if "Error" in text:
        return {"error": text}
    
    results = {}
    
    # Agent 1: Document Review
    print("Running Document Agent...")
    results['document_review'] = check_and_improve_document(text)
    
    # Agent 2: Summarization
    print("Running Summary Agent...")
    results['summary'] = summarize_document(text)
    
    # Agent 3: Information Extraction
    print("Running Information Agent...")
    results['information'] = extract_information(text)
    
    # Save all results
    for key, result in results.items():
        if result['status'] == 'success':
            save_output(
                result.get('analysis') or 
                result.get('summary') or 
                result.get('extracted_info'),
                f'result_{key}'
            )
    
    return results

# Usage
results = process_document_pipeline('my_document.pdf')
```

---

## Environment Variables

Configuration in `.env`:

```
# Ollama API Host
OLLAMA_HOST=http://localhost:11434

# Model Names - Edit these to use different models
DOCUMENT_MODEL=llama3.2:3b
SUMMARY_MODEL=gemma3:4b
INFO_MODEL=deepseek-r1:7b
```

### Access Environment Variables in Code

```python
import os
from dotenv import load_dotenv

load_dotenv()

model_name = os.getenv('DOCUMENT_MODEL', 'llama3.2:3b')
ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
```

---

## Error Handling

All agent functions return status-aware results:

```python
result = summarize_document(text)

if result['status'] == 'success':
    print(result['summary'])
else:
    print(f"Error: {result['error_message']}")
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Connection refused" | Ollama not running | Run `ollama serve` |
| "Model not found" | Model not downloaded | Run `ollama pull model_name` |
| "Timeout" | Model taking too long | Reduce text length |
| "Error extracting PDF" | Invalid PDF file | Try different PDF or TXT format |

---

## Customization Examples

### Add a New Agent Type

1. Create `agents/custom_agent.py`:

```python
import ollama
import os

def custom_task(document_text):
    """Custom agent function."""
    model_name = os.getenv('CUSTOM_MODEL', 'llama3.2:3b')
    
    prompt = f"""Your custom prompt here:

{document_text}"""
    
    response = ollama.chat(
        model=model_name,
        messages=[{'role': 'user', 'content': prompt}],
        stream=False
    )
    
    return {
        'status': 'success',
        'result': response['message']['content']
    }
```

2. Add to `.env`:

```
CUSTOM_MODEL=llama3.2:3b
```

3. Use in app:

```python
from agents.custom_agent import custom_task

result = custom_task(document_text)
```

### Modify Prompts

Edit `utils/prompts.py`:

```python
CUSTOM_PROMPT = """Your modified prompt here:
- Instruction 1
- Instruction 2
- Instruction 3

{text}"""
```

---

## Advanced: Direct Ollama API Usage

For more control, use Ollama API directly:

```python
import ollama

response = ollama.chat(
    model='llama3.2:3b',
    messages=[
        {'role': 'user', 'content': 'Your prompt here'}
    ],
    stream=False  # Set True to stream responses
)

print(response['message']['content'])
```

### Streaming Responses

```python
for chunk in ollama.generate(
    model='llama3.2:3b',
    prompt='Your prompt',
    stream=True
):
    print(chunk['response'], end='', flush=True)
```

---

## Performance Tips

1. **Reduce Text Length** - Smaller inputs = faster responses
2. **Use Appropriate Models** - Smaller models are faster
3. **Warm Up Models** - First call loads model (slower)
4. **Close Other Apps** - More RAM for models
5. **Use Quick Options** - "Bullet Points" vs "Full Summary"

---

## Testing Your Agents

### Manual Test Script

```python
from agents.document_agent import check_and_improve_document
from agents.summary_agent import summarize_document
from agents.info_agent import extract_information

test_text = """
Artificial Intelligence is transforming industries.
It helps with healthcare, education, and business.
However, ethical concerns remain important.
"""

print("Testing Document Agent...")
result1 = check_and_improve_document(test_text)
print(f"Status: {result1['status']}")
print(f"Result: {result1['analysis'][:100]}...")

print("\nTesting Summary Agent...")
result2 = summarize_document(test_text)
print(f"Status: {result2['status']}")
print(f"Result: {result2['summary'][:100]}...")

print("\nTesting Info Agent...")
result3 = extract_information(test_text)
print(f"Status: {result3['status']}")
print(f"Result: {result3['extracted_info'][:100]}...")
```

---

## Questions?

Refer to:
- README.md - Project overview
- QUICK_START_WINDOWS_VSCODE.md - Setup guide
- Inline comments in code files
- App.py - UI implementation

**Happy coding! 🚀**
