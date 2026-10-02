from embedding import create_embeddings
from langchain_chroma import Chroma
from llm import ask_llm

embedding_model = create_embeddings()

vector_store = Chroma(
    persist_directory="./resume_vectorDb",
    embedding_function=embedding_model,
)

query = "what is my cgpa in b.tech?"

data = vector_store.similarity_search(query)

content = ""

for doc in data:
    content += doc.page_content + "\n"

answer = ask_llm(content, query)

print(answer)