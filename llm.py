import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=st.secrets["GROQ_API_KEY"]
)

def ask_llm(content, query):

    prompt = f"""
You are a helpful assistant which provides the answer based on the Context provided for my Question.
this resume belongs to Amit Yadav 
If you don't know the answer, return "This content is not present in the Resume".
Also explain why you don't know the answer.

Context:
{content}

Question:
{query}
"""

    res = llm.invoke(prompt)

    return res.content