# IT Support RAG Assistant

A Retrieval-Augmented Generation (RAG) system that allows IT support teams to upload internal documentation (policies, guides, runbooks) and query it using natural language. Built with Streamlit, OpenAI, and FAISS.

🔗 **Live Demo:** [it-support-rag-4qzbhregshcakrhvnagqnk.streamlit.app](https://it-support-rag-4qzbhregshcakrhvnagqnk.streamlit.app)

---

## Features

- **PDF Upload** — Upload IT policies, user guides, or troubleshooting manuals
- **Semantic Search** — Ask questions in natural language and get answers grounded in your documentation
- **Fast Retrieval** — FAISS vector indexing for sub-second query response
- **Context-Aware Responses** — GPT-4o-mini generates answers using only the uploaded document content
- **Clean UI** — Simple Streamlit interface designed for IT professionals

---

## How It Works

1. **Upload** — The user uploads a PDF document such as an IT policy, guide, or troubleshooting manual
2. **Extract** — The application extracts text from the PDF using `pypdf`
3. **Chunk** — The extracted text is split into smaller chunks to improve retrieval accuracy
4. **Embed** — Each chunk is converted into a vector embedding using OpenAI's `text-embedding-3-small` model
5. **Index** — The embeddings are stored in a FAISS vector index for fast similarity search
6. **Query** — When the user asks a question, the query is also converted into an embedding
7. **Retrieve** — FAISS returns the most relevant chunks from the document
8. **Generate** — The retrieved context and user question are passed to `gpt-4o-mini`
9. **Answer** — The assistant generates a response grounded in the uploaded document content

---

## Tech Stack

- **Python** — Core application logic
- **Streamlit** — Web UI framework
- **OpenAI API** — Embeddings (`text-embedding-3-small`) and LLM (`gpt-4o-mini`)
- **FAISS** — Vector similarity search
- **pypdf** — PDF text extraction
- **python-dotenv** — Environment variable management

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/damian80/it-support-rag.git
   cd it-support-rag
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your OpenAI API key:

4. Run the app:
```bash
streamlit run app.py
```

---

## Use Cases

- **IT Support Teams** — Answer user questions using internal documentation
- **Onboarding** — Help new team members find answers in company policies
- **Compliance** — Query security policies and SOC2/ISO27001 documentation
- **Knowledge Management** — Turn static PDFs into searchable knowledge bases

---

## Future Improvements

- Multi-document support (upload multiple PDFs, query across all)
- Persistent storage (save indexes for reuse)
- Source citation (show which page/section the answer came from)
- Authentication and user management
- Support for Word docs, Google Docs, and web scraping

---

## License

MIT

---


## Author

Damian Ciasnocha — IT Technician | Python | AI Tools  
[LinkedIn](https://linkedin.com/in/damianciasnocha) | [GitHub](https://github.com/damian80)
