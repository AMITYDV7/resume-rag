import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def create_embeddings():

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        google_api_key=st.secrets["GOOGLE_API_KEY"]
    )

    return embeddings