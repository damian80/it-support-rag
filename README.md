# 🖥️ IT Support RAG Assistant

**Live Demo:** https://it-support-rag-4qzbhregshcakrhvnagqnk.streamlit.app/

RAG-powered IT support assistant. Upload PDF documents and ask questions. Built with Python, OpenAI API, FAISS, and Streamlit.

## What it does

- Provides AI-powered IT support responses via a chat interface
- Remembers conversation context within a session
- Responds as a named IT support technician
- Built with real-world IT support use cases from a school environment

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
