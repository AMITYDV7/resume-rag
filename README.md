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
