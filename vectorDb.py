from embedding import create_embeddings
from langchain_chroma import Chroma
from textSplitter import split_documents

chunks = split_documents()
embedding_model = create_embeddings()

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./resume_vectorDb",
)

print("Vector DB created successfully!")

query="what is key skills"
def context_pipeline():
    data = vector_store.similarity_search(query)
    
    print(data)
    
context_pipeline()