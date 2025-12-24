import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

st.set_page_config(page_title="Python Course Assistant", page_icon="🐍")

@st.cache_resource
def load_data():
    return joblib.load('embeddings.joblib')

df = load_data()

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    return r.json()["embeddings"]

def get_relevant_chunks(query, top_results=5):
    question_embedding = create_embedding([query])[0]
    similarities = cosine_similarity(np.vstack(df['embedding']), [question_embedding]).flatten()
    top_indx = similarities.argsort()[::-1][:top_results]
    return df.iloc[top_indx]

def get_ai_response(query, filtered_df):
    prompt = f'''Python course assistant. Video subtitles:

{filtered_df[["title", "number", "start", "end", "text"]].to_json(orient="records")}

Q: "{query}"

Provide: Answer + video references (number, title, MM:SS timestamp) + recommendation.
Only answer course questions.'''
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="Your API Key",
    )
    
    completion = client.chat.completions.create(
        model="openai/gpt-4o",  # ✅ Changed to gpt-4o
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return completion.choices[0].message.content

# UI
st.title("🐍 Python Course Assistant")
st.write("Ask anything about the Python course!")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "👋 Hi! Ask me about the Python course!"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("🤔 Searching..."):
            try:
                filtered_df = get_relevant_chunks(prompt)
                response = get_ai_response(prompt, filtered_df)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error: {str(e)}")
