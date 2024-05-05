import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
# Assuming the Tesseract executable is in a folder named "Tesseract-OCR" within the current directory
tesseract_path = os.path.join(current_dir, "Tesseract-OCR", "tesseract.exe")

def sanitize_filename(text):
    """Sanitize the text string to be safe for filenames."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '_')
    return text.strip()

def extract_and_name_figures(input_dir, output_dir):
    image_details = []
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        doc = fitz.open(pdf_path)
        print(f"Processing {pdf_path}...")

        for page_number in range(doc.page_count):
            page = doc[page_number]
            image_list = page.get_images(full=True)
            
            # Extract page as an image for higher quality OCR
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Scale to improve OCR
            page_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # Use pytesseract to extract text and bounding boxes
            data = pytesseract.image_to_data(page_image, output_type=pytesseract.Output.DICT)

            # Process each image
            for img in image_list:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                img_rect = fitz.Rect(img[1:5])

                closest_caption = None
                min_distance = float('inf')

                for i, text in enumerate(data['text']):
                    if "Figure" in text or "Fig" in text:
                        caption_range = range(max(0, i-10), min(len(data['text']), i+10))
                        caption = ' '.join(data['text'][j] for j in caption_range)
                        cx, cy = data['left'][i], data['top'][i]
                        # Calculate distance based on proximity above or below image
                        if cy > img_rect.y1:  # Below image
                            distance = cy - img_rect.y1
                        else:  # Above image
                            distance = img_rect.y0 - (cy + data['height'][i])

                        if distance < min_distance:
                            min_distance = distance
                            closest_caption = caption

                if closest_caption:
                    sanitized_caption = sanitize_filename(closest_caption)
                    image_name = f"{page_number+1}_{sanitized_caption}.{image_ext}"
                else:
                    image_name = f"unnamed_image_page{page_number+1}_img{xref}.{image_ext}"

                image_path = os.path.join(output_dir, image_name)
                with open(image_path, "wb") as img_file:
                    img_file.write(image_bytes)

                # Store details for JSON
                image_details.append({
                    "file_name": pdf_file,
                    "page_number": page_number + 1,
                    "caption": closest_caption or "No caption",
                    "image_file_name": image_name
                })

                print(f"Saved image to {image_path}")

    # Write to JSON file
    json_path = os.path.join(output_dir, "image_details.json")
    with open(json_path, 'w') as f:
        json.dump(image_details, f, indent=4)

    print(f"Image details saved to {json_path}")

# Example usage with relative paths
input_dir = "./InputPDF"  # Adjust this path as needed based on your project structure
output_dir = "./output/extracted_images"  # Adjust this path as needed
extract_and_name_figures(input_dir, output_dir)