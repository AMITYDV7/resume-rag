from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)


def ask_llm(content, query):

    prompt = f"""
You are a helpful assistant which provide the answer based on the Context provided for my Question
if you don't know the answer just return ' I don't know '
also explain me why you don't know the answer.

Context:
{content}

Question:
{query}
"""

    res = llm.invoke(prompt)

    return res.content