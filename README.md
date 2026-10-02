# 📄 Resume RAG — AI Resume Assistant

An AI-powered Resume Question Answering system built using **Retrieval-Augmented Generation (RAG)**.

The application uses a resume PDF as its knowledge source. Users can ask questions about the resume through a Streamlit chat interface, and the system retrieves relevant resume sections from ChromaDB before generating an answer using an LLM.

---

## 🚀 Features

- 📄 Resume PDF as the knowledge source
- ✂️ PDF text extraction and document chunking
- 🔢 Google Gemini embeddings
- 🗄️ ChromaDB vector database
- 🔍 Semantic similarity search
- 🤖 Groq LLM for answer generation
- 💬 Interactive Streamlit chat interface
- 🔐 Environment-based API key configuration
- ⚡ Fast retrieval-based question answering

---

<img width="448" height="273" alt="Screenshot 2026-10-02 100333" src="https://github.com/user-attachments/assets/7585bfeb-5dcf-476a-8fc5-fc8a7607bf42" />

## 🏗️ Architecture

```text
                    Resume PDF
                        │
                        ▼
                  PDF Document Loader
                        │
                        ▼
                  Text Splitter
                        │
                        ▼
                Document Chunks
                        │
                        ▼
              Gemini Embeddings
                        │
                        ▼
                  ChromaDB
                 Vector Database
                        │
                        │
              ┌─────────┴─────────┐
              │                   │
         User Question       Similarity Search
              │                   │
              └─────────┬─────────┘
                        ▼
                 Relevant Chunks
                        │
                        ▼
                   Groq LLM
                        │
                        ▼
                  Final Answer
                        │
                        ▼
                Streamlit UI






