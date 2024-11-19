import openai
import numpy as np
API_KEY = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"
openai.api_key=API_KEY
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
                      "url": "https://images.unsplash.com/photo-1597431783670-205a592f954e?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=800&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTcwMzE3ODc4Ng&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1900"
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