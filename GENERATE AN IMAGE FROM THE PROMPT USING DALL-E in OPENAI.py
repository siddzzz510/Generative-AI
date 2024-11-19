import openai
openai.api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"

response = openai.Image.create(
    prompt="water color image of Zurich with color reflections in water",
    size="1024x1024"
)
print(response['data'][0]['url'])