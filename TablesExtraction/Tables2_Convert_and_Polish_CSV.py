
import openai
import os
import csv
import logging
import time
from openai.error import OpenAIError

# Environment Variables for API Keys
api_key = os.getenv("OPENAI_API_KEY", "your-default-api-key")

# Set up Azure OpenAI API configuration
openai.api_type = "azure"
openai.api_base = "https://your-instance.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = api_key

# Setup for relative paths
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
output_folder = os.path.join(script_dir, "OUTPUT_Tables")  # Relative path


def detect_table_structure(text):
    # Placeholder for your table structure detection logic
    if "Total numbers" in text:
        return "complex"
    return "simple"

def improve_table_formatting(text, table_type):
    additional_instructions = (
        "Ensure each row corresponds to a single line in the output CSV, "
        "with clear, descriptive headers and any subtotals or annotations as separate rows. "
        "Ensure all data is accurately preserved and entries with commas are properly quoted."
    )
    example = "Example:\nHeader1,Header2,Header3\ndata1,data2,data3\nsubtotal1,,subtotal3\nNote: Descriptions or special instructions"
    prompt = (f"Please format the following {'complex' if table_type == 'complex' else 'simple'} table into a structured CSV. "
              f"Follow these instructions:\n{additional_instructions}\n\n{example}\n\nTable Content:\n{text}")

    try:
        response = openai.Completion.create(
            engine="gpt-35-turbo-instruct",
            prompt=prompt,
            max_tokens=4000
        )
        formatted_text = response.choices[0].text.strip()
        return formatted_text.split('\n')
    except OpenAIError as e:
        logging.error(f"API error while formatting table: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while formatting table: {e}")
        return None

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        
        table_type = detect_table_structure(text_content)
        csv_lines = improve_table_formatting(text_content, table_type)
        if csv_lines is None:
            logging.info(f"Skipping file due to errors in table formatting: {file_path}")
            return
        
        csv_filename = os.path.splitext(file_path)[0] + ".csv"
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in csv_lines:
                csv_writer.writerow(line.split(','))
        logging.info(f"Processed and saved: {csv_filename}")
        print(f"Processed and saved: {csv_filename}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {e}")

def main():
    files_processed = 0
    for filename in os.listdir(output_folder):
        if filename.endswith(".txt"):
            process_file(os.path.join(output_folder, filename))
            files_processed += 1
            if files_processed % 10 == 0:
                logging.info("Processed 10 files, pausing for 10 seconds to manage API rate limits.")
                time.sleep(20)

if __name__ == "__main__":
    main()

