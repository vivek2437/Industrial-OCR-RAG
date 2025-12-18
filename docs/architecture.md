# System Architecture

## Design Principles
- Simplicity over completeness
- Modular components
- Emphasis on evaluation and failure analysis

---

## Components

### OCR Module
Responsible for converting scanned images into raw text using Tesseract OCR with basic preprocessing.

### Text Processing
Cleans and chunks OCR output into semantically meaningful segments.

### Vector Store
Uses FAISS to store embeddings for efficient similarity search.

### LLM Interface
Uses retrieved chunks as context to generate answers.

---

## Data Flow
1. Image → OCR
2. OCR text → chunks
3. Chunks → embeddings
4. Embeddings → FAISS
5. Query → retrieval → LLM

---

## Trade-offs
- Faster development using pretrained models
- Lower accuracy on complex layouts
- Manual evaluation instead of automated metrics

---

## Rationale
This architecture mirrors real industrial ML systems where imperfect data and fast iteration matter more than theoretical optimality.
