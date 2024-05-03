
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

# Configure path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Define relative input and output directories
base_directory = os.path.dirname(__file__)  # Gets the directory where this script is located
input_directory = os.path.join(base_directory, 'Test SC')
output_directory = os.path.join(base_directory, 'Validatation', 'Test SC')

# Function to process each PDF file
def process_pdf(pdf_file):
    try:
        pdf_path = os.path.join(input_directory, pdf_file)
        extracted_text = []

        # Open the PDF file using PyMuPDF
        pdf_document = fitz.open(pdf_path)
        
        # Iterate through each page of the PDF
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            page_image = page.get_pixmap()
            image = Image.frombytes("RGB", [page_image.width, page_image.height], page_image.samples)
            text = pytesseract.image_to_string(image)
            
            if text.strip():
                extracted_text.append(text)

        pdf_document.close()

        # Concatenate all the extracted text
        all_extracted_text = '\n'.join(extracted_text)

        # Prepare output file path
        input_file_name = os.path.splitext(pdf_file)[0]
        output_file_name = os.path.join(output_directory, f"SC_{input_file_name}.txt")

        # Write the extracted text to the output file
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(all_extracted_text)

        return f"Processed {pdf_file}"
    except Exception as e:
        return f"Failed to process {pdf_file}: {str(e)}"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all PDF files in the input directory
pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]

# Process each PDF file
for pdf_file in pdf_files:
    result = process_pdf(pdf_file)
    print(result)




