import time

import streamlit as st

from embedding import create_embeddings
from langchain_chroma import Chroma
from llm import ask_llm


# ---------- UI styling only (no logic changes) ----------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

/* Animated gradient background */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a2a6c);
    background-size: 400% 400%;
    animation: gradientShift 18s ease infinite;
    color: #f1f1f1;
}
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

#MainMenu, footer, header { visibility: hidden; }

/* Title: gradient shimmer */
h1 {
    text-align: center;
    font-weight: 700 !important;
    background: linear-gradient(90deg, #00c6ff, #a18cd1, #fbc2eb, #00c6ff);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmer 6s linear infinite, fadeInDown 0.9s ease both;
}
@keyframes shimmer { to { background-position: 300% center; } }
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Chat bubbles */
[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 18px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    animation: fadeInUp 0.5s ease both;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
[data-testid="stChatMessage"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(0, 198, 255, 0.18);
}

/* Chat input glow */
[data-testid="stChatInput"] {
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.08);
    transition: box-shadow 0.3s ease, border 0.3s ease;
}
[data-testid="stChatInput"]:focus-within {
    border: 1px solid #00c6ff;
    box-shadow: 0 0 18px rgba(0, 198, 255, 0.5);
}
</style>
""",
    unsafe_allow_html=True,
)


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

    # Show the question in a chat bubble
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(query)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("🔍 Searching resume and thinking..."):

            # Search relevant chunks
            data = vector_store.similarity_search(query)

            # Convert documents → context
            content = "\n\n".join(
                doc.page_content
                for doc in data
            )

            # Send context + question to LLM
            answer = ask_llm(content, query)

        # Show answer with typewriter animation
        box = st.empty()
        typed = ""
        for word in str(answer).split(" "):
            typed += word + " "
            box.markdown(typed + "▌")
            time.sleep(0.02)
        box.markdown(typed)