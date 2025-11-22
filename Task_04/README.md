# PDF Summarizer & Quiz Generator Agent

## Overview

A Chainlit app that lets users upload PDFs, generates a summary, and creates quizzes from the original PDF text.

## Features

- **PDF Summarization:** Extracts text using PyPDF and creates a clean summary.
- **Quiz Generator:** Produces MCQs or mixed-style quizzes from the original PDF.
- **UI:** Streamlit or Chainlit interface.
- **Tools:** OpenAgents SDK via Context7 MCP server.

## MCP Servers

- Bridge between AI model/CLI and tools.
- Provide access to files, APIs, local functions, external systems.
- Make AI modular, maintainable, and easy to extend.

## Why Context7 MCP

- Complete MCP server with up-to-date documentation.
- Ensures Gemini CLI builds agents without errors.
- Supports Python, OpenAgents SDK, Supabase, FastAPI, and more.

## Setup

1. Connect **Context7 MCP server** to Gemini CLI (see [Guide](https://www.notion.so/Personalization-Chatbot-with-Chainlit-2b2644e5197680728913dc57ee7df803)).
2. Install dependencies from `pyproject.toml` or `.env`.
3. Run `app.py` with Chainlit.

## Usage

1. Upload a PDF file.
2. View the generated summary.
3. Click **Create Quiz** to get MCQs or mixed quizzes.

## Tech Stack

- Python, OpenAgents SDK, Chainlit, PyPDF, Streamlit
- Context7 MCP server for tool access
- Gemini model (`gemini-2.5-flash`)

## Testing

- Upload different PDFs to ensure proper summarization.
- Generate quizzes and verify answers.
- Confirm streaming responses appear in UI correctly.

## Important Links

- [Context7 Website](https://context7.com)
- [MCP Server Setup Guide](https://www.notion.so/Personalization-Chatbot-with-Chainlit-2b2644e5197680728913dc57ee7df803)
