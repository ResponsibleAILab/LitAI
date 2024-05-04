import openai
import re
import json
import os
import sys

# Environment Variables for API Keys
api_key = os.getenv("OPENAI_API_KEY", "your-default-api-key")

# Set up OpenAI API configuration
openai.api_key = api_key

def extract_sections(file_content):
    section_keywords = ["abstract", "introduction", "materials and methods", "results", "discussion", "conclusion", "acknowledgements", "references"]
    section_start_indices = [(m.start(), m.group().lower()) for m in re.finditer('|'.join(section_keywords), file_content.lower())]
    section_start_indices.sort()

    sections = {}
    for i in range(len(section_start_indices)):
        start_index, section_name = section_start_indices[i]
        section_content = ""
        if i < len(section_start_indices) - 1:
            end_index = section_start_indices[i + 1][0]
            section_content = file_content[start_index:end_index].strip()
        else:
            section_content = file_content[start_index:].strip()
        sections[section_name] = section_content

    return sections

if __name__ == "__main__":
       
    input_directory = os.path.join(current_dir, "Polished")
    output_directory = os.path.join(current_dir, "SectionWiseJson")

    for filename in os.listdir(input_dir_path):
        if filename.endswith(".txt"):  # Check if the file is a text file
            file_path = os.path.join(input_dir_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            sections = extract_sections(file_content)
            file_name = os.path.splitext(filename)[0]
            output_file_path = os.path.join(input_dir_path, f"{file_name}_sections.json")

            with open(output_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(sections, json_file, ensure_ascii=False, indent=4)

            print(f"Extracted sections saved to {output_file_path}")

