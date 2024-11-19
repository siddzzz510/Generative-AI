import openai

# Set your OpenAI API key
openai.api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"

instruction = """Explain what this Python code does in one sentence:
number = int(input("Enter a number:"))
primeFlag = True
for i in range(2, number):
    if number % i == 0:
        primeFlag = False
        break
if primeFlag == True:
    print(number, " is prime.")
else:
    print(number, " is not prime.")
"""

# Make the API request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": instruction  # Use instruction directly as a string
        }
    ],
    max_tokens=300,
)

# Print the response
print(response['choices'][0]['message']['content'])
