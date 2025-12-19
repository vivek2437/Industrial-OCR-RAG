import os
import faiss
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings

CHUNKS_DIR = r"data\chunks"
INDEX_DIR = r"rag\index"

os.makedirs(INDEX_DIR, exist_ok=True)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

documents = []
for file in os.listdir(CHUNKS_DIR):
    if not file.endswith(".txt"):
        continue

    with open(os.path.join(CHUNKS_DIR, file), "r", encoding="utf-8") as f:
        documents.extend([line.strip() for line in f if line.strip()])

print(f"Embedding {len(documents)} chunks...")

vectors = embeddings.embed_documents(documents)
vectors = np.array(vectors).astype("float32")

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

faiss.write_index(index, os.path.join(INDEX_DIR, "docs.index"))

with open(os.path.join(INDEX_DIR, "docs.txt"), "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc + "\n")

print("FAISS index built successfully.")
