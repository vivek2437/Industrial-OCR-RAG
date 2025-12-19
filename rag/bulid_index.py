import os
from pathlib import Path

INPUT_DIR = r"data\extracted_text"
OUTPUT_DIR = r"data\chunks"

CHUNK_SIZE = 500
OVERLAP = 100

os.makedirs(OUTPUT_DIR, exist_ok=True)

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

for file in os.listdir(INPUT_DIR):
    if not file.endswith(".txt"):
        continue

    with open(Path(INPUT_DIR) / file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)

    out_file = Path(OUTPUT_DIR) / f"{file.replace('.txt', '')}_chunks.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk.replace("\n", " ") + "\n")

print("Text chunking complete.")
