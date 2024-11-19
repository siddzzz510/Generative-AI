import openai

openai.api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Generate 3 recipes for baking a cake with instructions"
        }
    ],
    max_tokens=300,
)

print(response['choices'][0]['message']['content'])
