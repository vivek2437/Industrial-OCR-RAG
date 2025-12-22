# RAG Evaluation

## Objective
Evaluate how well the retrieval and LLM components answer questions based on OCR-extracted text.

---

## Test Setup
- Created 10 natural language questions
- Retrieved top-3 text chunks per query
- Evaluated answers manually

---

## Metrics (Qualitative)

| Category | Count |
|--------|------|
| Correct | 6 |
| Partially Correct | 3 |
| Incorrect | 1 |

---

## Observations
- Accurate answers when relevant chunks were retrieved
- Hallucinations occurred when retrieval was weak
- Long OCR noise reduced embedding quality

---

## Failure Patterns
- Overly generic answers
- Incorrect assumptions by the LLM
- Missing context due to chunk boundaries

---

## Conclusion
Retrieval quality is the primary bottleneck. Improving chunking and filtering noisy OCR text significantly improves answer quality.
