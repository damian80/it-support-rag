import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy as np
import faiss
import pypdf

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🖥️ IT Support RAG Assistant")
st.write("Upload an IT document and ask questions about it")

def extract_text_from_pdf(file):
    reader = pypdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def build_index(chunks):
    embeddings = [get_embedding(chunk) for chunk in chunks]
    embeddings_array = np.array(embeddings).astype('float32')
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings_array)
    return index, embeddings

def search_similar(query, index, chunks, k=3):
    query_embedding = np.array([get_embedding(query)]).astype('float32')
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]

with st.sidebar:
    st.header("📄 Upload Document")
    uploaded_file = st.file_uploader("Upload IT policy or guide (PDF)", type="pdf")
    if uploaded_file:
        if "doc_index" not in st.session_state:
            with st.spinner("Processing document..."):
                text = extract_text_from_pdf(uploaded_file)
                chunks = chunk_text(text)
                index, embeddings = build_index(chunks)
                st.session_state.doc_index = index
                st.session_state.chunks = chunks
                st.success(f"✅ Document loaded: {len(chunks)} sections")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask about your IT document..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    if "doc_index" in st.session_state:
        relevant_chunks = search_similar(prompt, st.session_state.doc_index, st.session_state.chunks)
        context = "\n\n".join(relevant_chunks)
        system_prompt = f"""You are an IT Support Assistant. Answer questions based on the following document content:

{context}

If the answer is not in the document, say so clearly."""
    else:
        system_prompt = "You are an IT Support Assistant. Help users with IT issues clearly and efficiently."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]
    )
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
