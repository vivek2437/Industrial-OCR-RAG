# OCR Evaluation

## Objective
Evaluate the quality of OCR output on scanned document images and identify common error patterns.

---

## Methodology
- Randomly selected 10 images from the dataset
- Manually compared OCR output with the original image
- Focused on readability and information loss

---

## Observations

### Strengths
- Printed text is mostly readable
- Headings and simple sentences extracted correctly
- High contrast images perform well

### Common Errors
- Characters misrecognized (O vs 0, I vs 1)
- Broken words due to noise
- Poor handling of tables and columns
- Text order issues in multi-column layouts

---

## Example Error Types

| Issue | Description |
|-----|-------------|
| Missing text | Faint characters not detected |
| Noise | Background artifacts treated as text |
| Layout loss | Table rows merged into paragraphs |

---

## Conclusion
OCR accuracy is highly dependent on scan quality. Preprocessing helps, but layout understanding remains a major limitation.