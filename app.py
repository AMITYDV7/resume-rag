import streamlit as st

from embedding import create_embeddings
from langchain_chroma import Chroma
from llm import ask_llm


st.title("📄 Resume AI Assistant")

# Load embedding model
embedding_model = create_embeddings()

# Load existing vector database
vector_store = Chroma(
    persist_directory="./resume_vectorDb",
    embedding_function=embedding_model
)

# User question
query = st.chat_input("Ask something about my resume...")

if query:

    # Search relevant chunks
    data = vector_store.similarity_search(query)

    # Convert documents → context
    content = "\n\n".join(
        doc.page_content
        for doc in data
    )

    # Send context + question to LLM
    answer = ask_llm(content, query)

    # Show answer
    st.write(answer)