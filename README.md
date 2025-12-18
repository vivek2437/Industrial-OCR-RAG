# Industrial OCR + RAG System

## Overview

This project implements an end-to-end OCR and Retrieval-Augmented
Generation (RAG) pipeline for understanding scanned documents. The
system extracts text from scanned images using OCR, indexes the
extracted content using vector embeddings, and answers natural language
questions using a language model.

The goal is to simulate real-world industrial document intelligence,
where data is noisy, unstructured, and imperfect.

------------------------------------------------------------------------

## Problem Statement

Industrial environments rely heavily on scanned documents such as
manuals, SOPs, and reports. These documents are difficult to search and
query due to poor scan quality, inconsistent layouts, and OCR errors.

This project explores: - How OCR performs on noisy scanned data - How
retrieval quality impacts downstream LLM answers - How to evaluate and
document failure modes

------------------------------------------------------------------------

## Dataset

-   **Dataset:** Scanned Images Dataset for OCR (Kaggle)
-   **Type:** Scanned document images
-   **Challenges:** Low resolution, uneven lighting, layout noise

> Dataset files are not committed to the repository.

------------------------------------------------------------------------

## System Architecture

Scanned Images\
↓\
Image Preprocessing\
↓\
OCR (Tesseract)\
↓\
Text Chunking\
↓\
Embeddings (Sentence Transformers)\
↓\
FAISS Vector Store\
↓\
LLM (Question Answering)

------------------------------------------------------------------------

## OCR Pipeline

-   Convert images to grayscale
-   Apply thresholding
-   Extract text using Tesseract OCR
-   Store extracted text per image

------------------------------------------------------------------------

## RAG Pipeline

-   Chunk extracted text into manageable segments
-   Generate embeddings using sentence-transformers
-   Store vectors in FAISS
-   Retrieve top-k chunks for each query
-   Use an LLM to generate answers with retrieved context

------------------------------------------------------------------------

## Evaluation Summary

-   OCR quality evaluated manually on sample images
-   Retrieval accuracy evaluated using test questions
-   Hallucination and latency observed

Detailed results: - evaluation/ocr_evaluation.md -
evaluation/rag_evaluation.md

------------------------------------------------------------------------

## Failure Analysis

Known limitations and failure cases are documented in: -
docs/failure_cases.md

------------------------------------------------------------------------

## Future Improvements

-   Layout-aware OCR models
-   Table structure extraction
-   Better chunking strategies
-   Domain-specific embeddings

------------------------------------------------------------------------

## How to Run

1.  Install dependencies:

        pip install -r requirements.txt

2.  Run OCR:

        python ocr/extract_text.py

3.  Build vector index:

        python rag/build_index.py

4.  Ask questions:

        python rag/qa.py

------------------------------------------------------------------------

## Key Takeaway

The most challenging part of this system was handling noisy OCR outputs
and imperfect retrieval. This project focuses on understanding and
documenting real-world limitations rather than optimizing for ideal
accuracy.