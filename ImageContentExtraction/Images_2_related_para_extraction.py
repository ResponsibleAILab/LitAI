import json
import os
import PyPDF2
import openai

# Environment Variables for API Keys
api_key = os.getenv("OPENAI_API_KEY", "your-default-api-key")

# Set up Azure OpenAI API configuration
openai.api_type = "azure"
openai.api_base = "https://your-instance.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = api_key

# Function to extract text from a PDF page
def extract_text_from_pdf(pdf_path, page_number):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        if page_number < 1 or page_number > len(reader.pages):
            return "Invalid page number"
        page_text = reader.pages[page_number - 1].extract_text()
    return page_text

# Function to find a related paragraph with OpenAI
def find_related_paragraph_with_openai(page_text, caption):
    prompt = f"Find the paragraph containing the following figure caption and more details: {caption}\n\n{page_text}"
    max_context_length = 4096  # Adjust based on the model's max token limit
    prompt = prompt[:max_context_length]
    response = openai.Completion.create(
        engine="gpt-35-turbo-instruct ",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Relative path to the JSON file (hard-coded)
json_file_path = "output/extracted_images/image_details.json"

# Resolve the full path based on the current working directory
full_json_path = os.path.join(os.getcwd(), json_file_path)

# Read the JSON file
with open(full_json_path, 'r') as file:
    data = json.load(file)

# Directory where PDF files are stored
pdf_directory = "./inputPDF"  

# Process each entry in the JSON data
for entry in data:
    file_name = entry["file_name"]
    page_number = entry["page_number"]
    caption = entry["caption"]
    image_file_name = entry["image_file_name"]

    # Construct the PDF file path
    pdf_file_path = os.path.join(pdf_directory, file_name)

    # Extract text from the specified page of the PDF file
    page_text = extract_text_from_pdf(pdf_file_path, page_number)

    # Find related paragraph containing the figure caption using OpenAI
    related_paragraph = find_related_paragraph_with_openai(page_text, caption)
    
    # Print the results
    print(f"Image: {image_file_name}")
    print("Related Paragraph:")
    print(related_paragraph)
    
    # Add the related paragraph to the JSON entry
    entry['related_paragraph'] = related_paragraph

# Write the updated JSON data back to the file
with open(full_json_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Updated JSON file saved successfully.")