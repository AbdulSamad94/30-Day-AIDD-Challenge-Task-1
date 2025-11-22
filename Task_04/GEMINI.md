# Role: Senior Python AI Engineer

**Objective:** Build a **PDF Summarizer & Quiz Generator Agent** using Chainlit, OpenAgents SDK, and Context7 MCP server.

## 1. Project Overview

The goal is to develop a **web-based agent** that:

1. Summarizes uploaded PDFs.
2. Generates quizzes (MCQs or mixed-style) from the original PDF text.

- **UI:** Chainlit (Streamlit optional, modern web interface).
- **Model:** Google Gemini via OpenAgents SDK (`gemini-2.5-flash`).
- **PDF Extraction:** `PyPDF` library.
- **Agent Tools:** Provided by Context7 MCP server (OpenAgents SDK, PDF handling, etc.).

---

## 2. Critical Technical Constraints

1. **Zero-Bloat Protocol (CRITICAL):**

   - Only implement required features: PDF summarization and quiz generation.
   - No unnecessary error handling or extra UI elements.
   - Do not invent features not documented in OpenAgents SDK or Context7 MCP.

2. **MCP Server Integration:**

   - Must connect Context7 MCP server to Gemini CLI before agent creation.
   - Use MCP-provided tools for PDF text extraction, summarization, and quiz generation.

3. **SDK Specificity:**

   - Use **OpenAgents SDK** with Gemini model.
   - Must follow MCP server’s documentation for tool integration.

4. **Environment & Keys:**

   - Load API keys from `.env`.
   - Do not hardcode any credentials.

---

## 3. Architecture & File Structure

```text
.
├── .env                  # Environment variables (OPENAI_API_KEY, etc.)
├── agent.py              # Agent setup + tool bindings (summarizer, quiz generator)
├── utils.py              # PDF text extraction & helper functions
├── app.py                # Chainlit UI & event handlers
├── prompts.md            # Optional: store GPT prompts for summarizer/quiz
├── pyproject.toml        # Dependencies & uv configuration
└── README.md             # Usage instructions
```

---

## 4. Implementation Steps

**Follow this exact flow. Do not skip steps.**

### Step 1: Documentation & Tool Analysis

1. Connect Gemini CLI to **Context7 MCP server**.
2. Use MCP tools to fetch documentation for:

   - `OpenAgents SDK`
   - `PDF text extraction`
   - `Quiz generation`

3. Verify syntax for:

   - Tool registration with agent
   - Async function usage
   - Model initialization (`gemini-2.5-flash`)

---

### Step 2: PDF Utilities (`utils.py`)

- **Function:** `extract_text_from_pdf(file_path)`

  - Uses PyPDF to return all text as string.

- **Constraint:** Only basic text extraction. No extra processing.

```python
from pypdf import PdfReader

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
```

---

### Step 3: Agent Configuration (`agent.py`)

- Initialize Gemini client using OpenAgents SDK.
- Load **tools from Context7 MCP**:

  1. `SummarizerTool` → Generates summary from text.
  2. `QuizGeneratorTool` → Generates MCQs or mixed-style quiz from original text.

- System prompt instructions:

```
You are an AI assistant. When a user uploads a PDF:
1. Summarize the PDF first in clear, structured format.
2. Wait for user to request a quiz.
3. Generate a quiz based on the original PDF text.
4. Use Chainlit streaming to send responses.
```

- **Bind tools** exactly as MCP docs prescribe.

---

### Step 4: UI & Event Handlers (`app.py`)

- **`@cl.on_chat_start`**:

  - Send static welcome: _"Hello! I can summarize PDFs and generate quizzes."_

- **`@cl.on_message`**:

  - Detect uploaded PDF: call `extract_text_from_pdf()` → pass text to `SummarizerTool`.
  - Display summary in UI.
  - On "Create Quiz" click: call `QuizGeneratorTool` with original PDF text.
  - Stream output back to Chainlit UI.

---

### Step 5: Prompts & Messaging

**Single prompt example (for agent tool registration / Gemini CLI):**

```
You are a PDF Summarizer & Quiz Generator assistant.
1. Summarize the uploaded PDF in structured format.
2. Generate a quiz on demand from the original PDF text.
3. Provide MCQs with 4 options each, highlight correct answers.
4. Stream outputs using Chainlit.
```

- Store prompt in `prompts.md` (optional for clarity).

---

### Step 6: Environment & Dependencies

- `.env` must include:

```
GEMINI_API_KEY=<your_key_here>
```

- `pyproject.toml` includes:

```
[tool.uv.dependencies]
chainlit = "*"
openai-agents = "*"
pypdf = "*"
```

- Use **uv** for installation. Check existing packages before installing.

---

## 5. Testing Scenarios

1. **Upload PDF:** Agent summarizes text and displays summary.
2. **Create Quiz:** Agent generates 5+ MCQs or mixed-style questions based on original PDF text.
3. **Streaming:** Responses appear progressively in Chainlit UI.
4. **Error Handling:** Minimal. Only ensure agent does not crash on empty PDF.
