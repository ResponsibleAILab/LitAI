# LitAI
Enhanced Accessibility and Comprehension of Scientific Literature through AI 

Abstract—Information processing and retrieval in literature
are critical for advancing scientific research and knowledge
discovery. The inherent multimodality and diverse formats of
literature, including text, tables, figures, and references, present
significant challenges. This paper introduces LitAI, a novel
approach that employs readily available generative AI tools to
enhance multimodal information retrieval from literature documents. By integrating tools such as optical character recognition
(OCR) with generative AI services, LitAI facilitates the retrieval
of text, tables, figures, and references from PDF documents. We
have developed specific prompts that leverage in-context learning
and prompt engineering within Generative AI to achieve precise
information extraction. Our empirical evaluations, conducted on
datasets from the ecological and biological sciences, demonstrate
the superiority of our approach over several established baselines
including Tesseract-OCR and GPT-4.


## Instructions for Running PDF Text Processing Pipeline

This section contains Python scripts for processing PDF files, polishing text, and extracting sections using various natural language processing techniques.
Prerequisites
    Python 3.x installed on your system.
    Access to an OpenAI API key for text polishing.

Usage
Follow these steps to run the PDF text processing pipeline:

Set Up Environment Variables:
Ensure you have an OpenAI API key. Set it as an environment variable named OPENAI_API_KEY.
Organize Directories:
Place your PDF files to be processed in the InputPDF directory.
Run the Scripts:
Step 1: Convert PDF files to raw text 
        `python PdfInput_to_Text.py`
Step 2: Polish the text using OpenAI's GPT-3 model:
        `python Convert_RawConvert_PolishedContent.py`
Step 3: Extract sections from polished text and save them as JSON files:
        `python Generating_SectionWise_Json.py`

Check Output:
Processed text files will be saved in the PolishedTextfiles directory.
Extracted section JSON files will be saved in the SectionWiseJson directory.




