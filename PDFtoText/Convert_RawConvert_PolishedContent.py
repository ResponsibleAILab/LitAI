#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import openai
import logging
import os
import sys

# Environment Variables for API Keys
api_key = os.getenv("OPENAI_API_KEY", "your-default-api-key")

# Set up logging configuration
logging.basicConfig(filename='polishing_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up Azure OpenAI API configuration
openai.api_type = "azure"
openai.api_base = "https://your-instance.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = api_key

def polish_text_with_gpt3(text):
    logging.info("Starting text polishing with GPT-3...")
    text_chunks = [text[i:i + 4096] for i in range(0, len(text), 4096)]
    polished_chunks = []

    for chunk in text_chunks:
        try:
            response = openai.ChatCompletion.create(
                engine="gpt-35-turbo-16k",
                messages=[
                    {"role": "system", "content": "You are a typo correction tool assigned to refine an ecology research paper."},
                    {"role": "user", "content": chunk}
                ]
            )
            polished_text = response['choices'][0]['message']['content']
            polished_chunks.append(polished_text)
        except Exception as e:
            logging.error(f"Failed to polish text chunk: {e}")
            sys.exit(1)

    polished_text = ' '.join(polished_chunks)
    logging.info("Text polishing completed.")
    return polished_text

def process_directory(input_directory, output_directory):
    logging.info("Starting the batch text polishing process...")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, f"Polished_{filename}")
            logging.info(f"Processing file: {filename}")

            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text_content = file.read()

                polished_content = polish_text_with_gpt3(text_content)

                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(polished_content)

                logging.info(f"Processed '{filename}'. Polished content saved to '{output_file_path}'.")
            except Exception as e:
                logging.error(f"An error occurred while processing '{filename}': {e}")

def main():
        
    input_directory = os.path.join(current_dir, "RawTextfromPdf")
    output_directory = os.path.join(current_dir, "PolishedTextfiles")
    
    process_directory(input_directory, output_directory)

if __name__ == "__main__":
    main()

