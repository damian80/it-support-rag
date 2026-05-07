import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🖥️ Harrodian - IT Support Assistant")
st.write("Ask me anything about IT issues")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Describe your IT problem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.write(prompt)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    {"role": "system", "content": "You are Damian, an IT Support Technician at Harrodian School in London. You help staff and students with IT issues. Sign your responses as 'Damian - IT Support'."},
    *st.session_state.messages
]
    )
    
    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    
    with st.chat_message("assistant"):
        st.write(reply)