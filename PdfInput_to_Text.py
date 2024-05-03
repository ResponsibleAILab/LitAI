#!/usr/bin/env python
# coding: utf-8

# In[2]:


import fitz  # PyMuPDF
import os
input_folder = r"C:\Users\medis\OneDrive\Desktop\Validatation\bilology_pdf"
output_folder = r"C:\Users\medis\OneDrive\Desktop\Validatation\biology_text"
def convert_pdf_to_text(pdf_path):
    text = ""
    try:
        pdf_document = fitz.open(pdf_path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
        pdf_document.close()
    except Exception as e:
        print(f"Error converting {pdf_path} to text: {e}")
    return text

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")
        text = convert_pdf_to_text(pdf_path)
        with open(output_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)
        print(f"Converted {pdf_path} to {output_path}")

