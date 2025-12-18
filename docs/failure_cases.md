# Failure Cases and Limitations

## OCR Failures
- Low contrast scans lead to missing words
- Tables lose structure completely
- Multi-column layouts mix sentence order

---

## Retrieval Failures
- Noisy OCR text reduces embedding quality
- Important context split across chunks
- Irrelevant chunks sometimes ranked higher

---

## LLM Failures
- Hallucination when context is weak
- Overconfident answers to ambiguous queries
- Sensitive to prompt structure

---

## Lessons Learned
- OCR quality determines downstream success
- Retrieval is more important than the LLM choice
- Failure analysis is essential for real-world ML systems

---

## Future Work
- Layout-aware OCR models
- Better noise filtering
- Domain-specific prompt tuning