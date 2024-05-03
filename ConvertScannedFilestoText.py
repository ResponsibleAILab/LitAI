#!/usr/bin/env python
# coding: utf-8

# In[21]:


import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

# Path to the PDF file
pdf_path =r"C:\Users\medis\OneDrive\Desktop\Validatation\bilology_pdf\Vascular cells_2023.pdf"
# r"C:\Users\medis\OneDrive\Desktop\Validatation\body_size_pdf_functionalfeeding\Cremona et al 2010.pdf"

# r"C:\Users\medis\OneDrive\Desktop\Validatation\body_size_pdf_trophiclinkage\Winfield_1986.pdf"
# Replace with the path to your PDF file

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize an empty list to store extracted text
extracted_text = []

# Open the PDF file using PyMuPDF
pdf_document = fitz.open(pdf_path)

# Iterate through each page of the PDF
for page_number in range(pdf_document.page_count):
    # Get the current page
    page = pdf_document.load_page(page_number)

    # Convert the page to an image
    page_image = page.get_pixmap()
    image = Image.frombytes("RGB", [page_image.width, page_image.height], page_image.samples)

    # Perform OCR on the image to extract text
    text = pytesseract.image_to_string(image)

    # Check if the extracted text is not empty before adding it
    if text.strip():
        extracted_text.append(text)

# Close the PDF file
pdf_document.close()

# Concatenate all the extracted text
all_extracted_text = '\n'.join(extracted_text)

# Define the output directory
output_directory = r'C:\Users\medis\OneDrive\Desktop\Validatation\scanned'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Extract the input file name without extension
input_file_name = os.path.splitext(os.path.basename(pdf_path))[0]
# Generate the output file name
output_file_name = os.path.join(output_directory, f"SC_{input_file_name}.txt")

# Write the extracted text to the output file
with open(output_file_name, 'w', encoding='utf-8') as file:
    file.write(all_extracted_text)

print(f"Extracted text saved to: {output_file_name}")


# In[11]:


pdf_path =r"C:\Users\medis\OneDrive\Desktop\Validatation\body_size_pdf_functionalfeeding\Cremona et al 2010.pdf"


# In[2]:


import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import os

# Configure path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Define input and output directories
input_directory = r'C:\Users\medis\OneDrive\Desktop\Validatation\Test SC'
output_directory = r'C:\Users\medis\OneDrive\Desktop\Validatation\Test SC'
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


# In[ ]:




