# LitAI
## Enhanced Accessibility and Comprehension of Scientific Literature through AI

**Abstract**—Information processing and retrieval in literature are critical for advancing scientific research and knowledge discovery. The inherent multimodality and diverse formats of literature, including text, tables, figures, and references, present significant challenges. This paper introduces LitAI, a novel approach that employs readily available generative AI tools to enhance multimodal information retrieval from literature documents. By integrating tools such as optical character recognition (OCR) with generative AI services, LitAI facilitates the retrieval of text, tables, figures, and references from PDF documents. We have developed specific prompts that leverage in-context learning and prompt engineering within Generative AI to achieve precise information extraction. Our empirical evaluations, conducted on datasets from the ecological and biological sciences, demonstrate the superiority of our approach over several established baselines including Tesseract-OCR and GPT-4.

## PDF Document
[View PDF](docs/document.pdf)



# Text Processing
### 1. Instructions for Running PDF Text Processing Pipeline

This section contains Python scripts for processing PDF files, polishing text, and extracting sections using various natural language processing techniques.

###  Prerequisites
- Python 3.12 installed on your system.
- Access to an OpenAI API key for text polishing.

###  Usage
Follow these steps to run the PDF text processing pipeline:

###  Set Up Environment Variables:
Ensure you have an OpenAI API key. Set it as an environment variable named OPENAI_API_KEY.

###  Organize Directories:
Place your PDF files to be processed in the InputPDF directory.

###  Run the Scripts:
- **Step 1:** Convert PDF files to raw text 
  ```bash
  python Text_1_PdfInput_to_Text.py

- **Step 2:** Polish the text using OpenAI's GPT-35-turbo-16k model 
  ```bash
  python Text_2_Convert_Raw_to_PolishedContent.py

- **Step 3:** Convert PDF files to raw text 
  ```bash
  python Text_3_PdfInput_to_Text.py

###  Output:
- Processed text files will be saved in the PolishedTextfiles directory.
- Extracted section JSON files will be saved in the SectionWiseJson directory.


# Table Processing
### 1. Instructions for Running PDF Table Extraction Pipeline

This section contains Python scripts for extracting tables from PDF files and converting them into structured data formats using various data processing techniques.

### Prerequisites
- Python 3.12 installed on your system.
- Access to an OpenAI API key for text polishing.

###  Usage
Follow these steps to run the PDF text processing pipeline:

###  Set Up Environment Variables:
Ensure you have an OpenAI API key. Set it as an environment variable named OPENAI_API_KEY.

###  Organize Directories:
- **InputPDF/**: Place your PDF files to be processed in this directory.

###  Run the Scripts:
- **Step 1:** Extract tables from PDF files 
  ```bash
  python Tables_1_Processing_Pdf.py

- **Step 2:** Convert extracted tables to CSV format and polish/format using OpenAI's GPT-35-turbo-instruct model
  ```bash
  python Tables_2_Convert_Raw_to_PolishedContent.py

###  Output:
- Extracted and formatted table files will be saved in the FormattedTables directory.

# Image Content Extraction
This section involves extracting figures, text, and processing images from PDF documents using AI tools.

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
- **Step 1:** Extract and Name Figures from PDFs, This script extracts images and their corresponding captions from PDF files, and names the files based on these captions
  ```bash
  python Images_1_fig_cap_Extraction.py

- **Step 2:** Extract Text and Find Related Paragraphs, uses OpenAI's GPT-35-turbo-instruct model
  ```bash
  python Images_2_related_para_extraction.py

- **Step 3:** Process Images and retrieving descriptive content about the images OpenAI's GPT-4-Vision-Preview model 
  ```bash
  python Images_3_Extracting_Image_Content.py

### Final Outputs
- Extracted Images: Images extracted from PDFs are saved in the `output/extracted_images/` directory.
- Initial JSON File (`image_details.json`): This file includes basic details such as file names, page numbers, and captions for each extracted image, stored in the `output/extracted_images/` directory.
- Enhanced JSON File (`image_data_with_responses.json`): This updated file contains all the information from the initial JSON plus additional descriptive content about the images provided by AI analysis, located in the same directory.

