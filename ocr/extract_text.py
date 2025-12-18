import os
from pathlib import Path
import cv2
from tqdm import tqdm
import easyocr

# Paths
dataset_root = r"C:\Users\ASUS\OneDrive\Desktop\industrial-ocr-rag\data\archive\dataset"
output_root = r"C:\Users\ASUS\OneDrive\Desktop\industrial-ocr-rag\data\extracted_text"

# Create output folder if it doesn't exist
os.makedirs(output_root, exist_ok=True)

# Supported image formats
image_extensions = [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]

# -----------------------------
# Initialize EasyOCR reader
# -----------------------------
reader = easyocr.Reader(['en'], gpu=True)

# OCR function
def ocr_image(image_path):
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Warning: Could not read {image_path}")
        return ""

    # Convert to grayscale (improves accuracy)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # EasyOCR returns list of (bbox, text, confidence)
    results = reader.readtext(gray)

    # Combine detected text lines
    extracted_text = "\n".join([res[1] for res in results])

    return extracted_text

# Loop through folders and images
for folder in tqdm(os.listdir(dataset_root), desc="Processing folders"):
    folder_path = Path(dataset_root) / folder
    if not folder_path.is_dir():
        continue

    for file in os.listdir(folder_path):
        file_path = folder_path / file
        if file_path.suffix.lower() not in image_extensions:
            continue

        # Run OCR
        text = ocr_image(file_path)

        # Save text
        output_filename = f"{folder}_{file_path.stem}.txt"
        output_file_path = Path(output_root) / output_filename

        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(text)

print("OCR extraction complete!")
