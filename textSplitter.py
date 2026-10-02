from loader import load_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents():

    docs = load_pdf()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(docs)
    print(f'Number of documents: {len(docs)}\nNumber of chunks: {len(chunks)}\nLength of first chunk: {len(chunks[0].page_content)}\nLength of second chunk: {len(chunks[1].page_content)}')

    return chunks