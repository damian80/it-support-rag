# 🖥️ IT Support RAG Assistant

**Live Demo:** https://it-support-rag-4qzbhregshcakrhvnagqnk.streamlit.app/

RAG-powered IT support assistant. Upload PDF documents and ask questions. Built with Python, OpenAI API, FAISS, and Streamlit.

## What it does

- Provides AI-powered IT support responses via a chat interface
- Remembers conversation context within a session
- Responds as a named IT support technician
- Built with real-world IT support use cases from a school environment

## How It Works

1. **Upload** — User uploads a PDF document (IT policy, guide, or manual)
2. **Extract** — Text is extracted from the PDF using pypdf
3. **Chunk** — Text is split into 500-word sections
4. **Embed** — Each section is converted to a vector using OpenAI's text-embedding-3-small model
5. **Index** — Vectors are stored in a FAISS index for fast similarity search
6. **Query** — User asks a question; the question is also embedded
7. **Retrieve** — FAISS finds the 3 most relevant sections
8. **Generate** — Relevant sections + question are sent to GPT-4o-mini
9. **Answer** — Response is grounded in the document content

## Tech Stack

- Python
- Streamlit — web UI
- OpenAI API — language model
- python-dotenv — secure API key management

## How to run locally

1. Clone the repository
```bash
git clone https://github.com/damian80/it-support-rag.git
cd it-support-rag
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install streamlit openai python-dotenv
```

4. Create `.env` file with your OpenAI API key
5. Run the app
```bash
python3 -m streamlit run app.py
```

## Author

Damian Ciasnocha — IT Technician | Python | AI Tools  
[LinkedIn](https://linkedin.com/in/damianciasnocha) | [GitHub](https://github.com/damian80)
