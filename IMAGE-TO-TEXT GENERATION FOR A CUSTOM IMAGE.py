import base64
import openai
import numpy as np
API_KEY = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"
openai.api_key=API_KEY

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/Users/siddhartha510/Desktop/12345.jpeg"

# Getting the base64 string
base64_image = encode_image(image_path)

response = openai.ChatCompletion.create(
  model="gpt-4o",
    messages=[
      {
          "role": "user",
          "content": [
              {"type": "text", "text": "What’s in this image?"},
              {
                  "type": "image_url",
                  "image_url": { 
                      "url":f"data:image/jpeg;base64, {base64_image}"
                     
                  }

              },
          ],
      }
  ],
 
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
print(response.choices[0].message.content)