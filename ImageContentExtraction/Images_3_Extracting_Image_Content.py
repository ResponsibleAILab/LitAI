import os
import json
import base64
import openai
import time


# Environment Variables for API Keys
api_key = os.getenv("OPENAI_API_KEY", "your-default-api-key")

# Set up Azure OpenAI API configuration
openai.api_type = "azure"
openai.api_base = "https://your-instance.openai.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = api_key
# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to process images and update JSON data
def process_images_from_json(json_path, output_json_path):
    # Load JSON data
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Iterate through each entry in the JSON data
    for item in data:
        image_file_name = item['image_file_name']
        related_paragraph = item['related_paragraph']
        image_path = os.path.join(folder_path, image_file_name)

        if os.path.exists(image_path):
            base64_image = encode_image(image_path)
            attempts = 0
            while attempts < 5:  # Retry up to 5 times
                try:
                    response = openai.ChatCompletion.create(
                        engine="gpt-4 vision-preview",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": f"What's in this image? and some more context of the image is {related_paragraph}"},
                                    {
                                        "type": "image_url",
                                        "image_url": {
                                            "url": f"data:image/jpeg;base64,{base64_image}",
                                        },
                                    },
                                ],
                            }
                        ],
                        max_tokens=300,
                    )
                    # Store response in the JSON data
                    item['image_content'] = response.choices[0].message.content
                    print(f"Response for {image_file_name}: {response.choices[0].message.content}")
                    break  # Exit the retry loop on success
                except openai.error.RateLimitError:
                    attempts += 1
                    wait_time = 30  # seconds
                    print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break

    # Save the updated JSON data to a new file
    with open(output_json_path, 'w') as f:
        json.dump(data, f, indent=4)

# Paths for the JSON input and output
json_path = "output/extracted_images/image_details.json"
output_json_path = "output/image_data_with_responses.json"
folder_path = "output/extracted_images"
process_images_from_json(json_path, output_json_path)