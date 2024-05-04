import os
from PyPDF2 import PdfReader
import re

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Define a regular expression pattern to locate table descriptions like "Table 1"
table_description_pattern = r"Table\s+\d+\..*?(?=(?:Table\s+\d+|$))"

# Function to process PDF files in a folder
def process_pdfs_in_folder(folder_path, output_folder):
    # Create the output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through PDF files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_file = os.path.join(folder_path, filename)
            # Extract text from the PDF file
            pdf_text = extract_text_from_pdf(pdf_file)
            # Find all matches of the table description pattern
            table_descriptions = re.findall(table_description_pattern, pdf_text, re.DOTALL)
            # Modify the loop to include the file name and table number
            for i, table_description in enumerate(table_descriptions, start=1):
                # Construct the text file name with the PDF file name and table number
                text_filename = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_Table_{i}.txt")
                with open(text_filename, 'w', encoding='utf-8') as text_file:
                    text_file.write(table_description.strip())

# Setup for relative paths
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
folder_path = os.path.join(script_dir, "InputPDF")  # Relative path to folder with PDFs
output_folder = os.path.join(folder_path, "OUTPUT_Tables")  # Relative path for output

# Process PDFs in the folder
process_pdfs_in_folder(folder_path, output_folder)
