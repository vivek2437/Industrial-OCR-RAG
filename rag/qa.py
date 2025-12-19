import faiss
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

INDEX_DIR = r"rag\index"

embeddings = OllamaEmbeddings(model="nomic-embed-text")
llm = Ollama(model="llama3")

index = faiss.read_index(f"{INDEX_DIR}/docs.index")

with open(f"{INDEX_DIR}/docs.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f]

def ask(query, top_k=5):
    query_vector = embeddings.embed_query(query)
    query_vector = np.array([query_vector]).astype("float32")

    _, indices = index.search(query_vector, top_k)
    context = "\n".join([documents[i] for i in indices[0]])

    prompt = f"""
You are an AI assistant for industrial documents.
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer:
"""

    return llm(prompt)

while True:
    q = input("Ask a question (or type 'exit'): ")
    if q.lower() == "exit":
        break
    print(ask(q))
