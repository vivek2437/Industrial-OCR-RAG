import os
from pathlib import Path
import cv2
from tqdm import tqdm

# Paths
INPUT_ROOT = r"C:\Users\ASUS\OneDrive\Desktop\industrial-ocr-rag\data\archive\dataset"
OUTPUT_ROOT = r"C:\Users\ASUS\OneDrive\Desktop\industrial-ocr-rag\data\preprocessed_images"

# Max image width (keeps OCR fast)
MAX_WIDTH = 1600

# Supported image formats
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tiff", ".bmp"}

# Create output directory
os.makedirs(OUTPUT_ROOT, exist_ok=True)

# Image preprocessing function
def preprocess_image(input_path, output_path):
    img = cv2.imread(str(input_path))
    if img is None:
        return False

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize if too large
    height, width = gray.shape
    if width > MAX_WIDTH:
        scale = MAX_WIDTH / width
        new_size = (int(width * scale), int(height * scale))
        gray = cv2.resize(gray, new_size, interpolation=cv2.INTER_AREA)

    # Save preprocessed image
    cv2.imwrite(str(output_path), gray)
    return True

# Process dataset
for folder in tqdm(os.listdir(INPUT_ROOT), desc="Processing folders"):
    input_folder = Path(INPUT_ROOT) / folder
    if not input_folder.is_dir():
        continue

    output_folder = Path(OUTPUT_ROOT) / folder
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        input_file = input_folder / file
        if input_file.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        output_file = output_folder / file
        preprocess_image(input_file, output_file)

print("Preprocessing complete.")
