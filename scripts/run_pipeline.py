import os
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def run(step_name, command):
    print(f"\n{'='*60}")
    print(f"RUNNING: {step_name}")
    print(f"{'='*60}")
    result = subprocess.run(
        [sys.executable, command],
        cwd=PROJECT_ROOT
    )
    if result.returncode != 0:
        print(f"❌ Failed at step: {step_name}")
        sys.exit(1)
    print(f"✅ Completed: {step_name}")

# --------------------------------------------------
# PIPELINE STEPS
# --------------------------------------------------

if __name__ == "__main__":

    # 1️⃣ Image preprocessing
    run(
        "Image Preprocessing",
        "preprocess.py"
    )

    # 2️⃣ OCR extraction (EasyOCR)
    run(
        "OCR Extraction",
        os.path.join("ocr", "extract_text.py")
    )

    # 3️⃣ Chunk extracted text
    run(
        "Text Chunking",
        os.path.join("rag", "chunk_text.py")
    )

    # 4️⃣ Build FAISS index
    run(
        "Build Vector Index",
        os.path.join("rag", "build_index.py")
    )

    # 5️⃣ Start QA system
    print("\n🚀 Starting QA system...\n")
    subprocess.run(
        [sys.executable, os.path.join("rag", "qa.py")],
        cwd=PROJECT_ROOT
    )
