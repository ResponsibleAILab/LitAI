# LitAI
## Enhanced Accessibility and Comprehension of Scientific Literature through AI

**Abstract**—Information processing and retrieval in literature are critical for advancing scientific research and knowledge discovery. The inherent multimodality and diverse formats of literature, including text, tables, figures, and references, present significant challenges. This paper introduces LitAI, a novel approach that employs readily available generative AI tools to enhance multimodal information retrieval from literature documents. By integrating tools such as optical character recognition (OCR) with generative AI services, LitAI facilitates the retrieval of text, tables, figures, and references from PDF documents. We have developed specific prompts that leverage in-context learning and prompt engineering within Generative AI to achieve precise information extraction. Our empirical evaluations, conducted on datasets from the ecological and biological sciences, demonstrate the superiority of our approach over several established baselines including Tesseract-OCR and GPT-4.

# Text Processing
### 1. Instructions for Running PDF Text Processing Pipeline

This section contains Python scripts for processing PDF files, polishing text, and extracting sections using various natural language processing techniques.

#### Prerequisites
- Python 3.12 installed on your system.
- Access to an OpenAI API key for text polishing.

#### Usage
Follow these steps to run the PDF text processing pipeline:

##### Set Up Environment Variables:
Ensure you have an OpenAI API key. Set it as an environment variable named OPENAI_API_KEY.

##### Organize Directories:
Place your PDF files to be processed in the InputPDF directory.

##### Run the Scripts:
- **Step 1:** Convert PDF files to raw text 
  ```bash
  python Text1_PdfInput_to_Text.py

- **Step 2:** Polish the text using OpenAI's GPT-35-turbo-16k model 
  ```bash
  python Text2_Convert_Raw_to_PolishedContent.py

- **Step 3:** Convert PDF files to raw text 
  ```bash
  python Text3_PdfInput_to_Text.py

Check Output:
Processed text files will be saved in the PolishedTextfiles directory.
Extracted section JSON files will be saved in the SectionWiseJson directory.


# Table Processing
### 1. Instructions for Running PDF Table Extraction Pipeline

This section contains Python scripts for extracting tables from PDF files and converting them into structured data formats using various data processing techniques.

#### Prerequisites
- Python 3.12 installed on your system.
- Access to an OpenAI API key for text polishing.

#### Usage
Follow these steps to run the PDF text processing pipeline:

##### Set Up Environment Variables:
Ensure you have an OpenAI API key. Set it as an environment variable named OPENAI_API_KEY.

##### Organize Directories:
Place your PDF files to be processed in the InputPDF directory.

##### Run the Scripts:
- **Step 1:** Extract tables from PDF files 
  ```bash
  python Tables1_Processing_Pdf.py

- **Step 2:** Convert extracted tables to CSV format and polish/format using OpenAI's GPT-35-turbo-instruct model
  ```bash
  python Tables2_Convert_Raw_to_PolishedContent.py

Check Output:
Extracted and formatted table files will be saved in the FormattedTables directory.

# Enhanced Document Processing Pipeline
## This project involves extracting figures, text, and processing images from PDF documents using AI tools.

### Prerequisites
- Python 3.12 installed on your system.
- PyMuPDF, PyPDF2, pytesseract, PIL, and OpenAI Python libraries installed.
- Access to an OpenAI API key for advanced text and image processing.
- Tesseract OCR installed and configured on your system.

### Setup Environment Variables
- Ensure you have an OpenAI API key set as an environment variable named `OPENAI_API_KEY`.
- Configure your Tesseract-OCR path correctly in the scripts if not in the default location.

### Directory Structure
- **InputPDF/**: Place your PDF files to be processed in this directory.
- **output/extracted_images/**: Output directory for extracted images and related data.

### Running the Scripts

- **Step 1:** Extract and Name Figures from PDFs
This script extracts images and their corresponding captions from PDF files, and names the files based on these captions.
```bash
python Images_1_fig_cap_Extraction.py


- **Step 2:**  Extract Text and Find Related Paragraphs

After images are extracted and named, this script reads text from the PDF and uses OpenAI's GPT-35-turbo-instruct model to find paragraphs related to the image captions.
```bash
python Images_2_related_para_extraction.py


- **Step 3:**  Process Images and Update JSON Data

The final script encodes images in base64 and sends them to OpenAI's GPT-4-Vision-Preview model for processing, retrieving descriptive content about the images which it adds to the JSON output.

```bash
python Images_3_Extracting_Image_Content.py

