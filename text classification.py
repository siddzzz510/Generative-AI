import openai

# Set your OpenAI API key
openai.api_key = 'sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA'

# List of companies
companies = [
    "Microsoft Corporation", "Roche Holding AG", "Apple Inc", "Amazon.com, Inc",
    "Pfizer Inc", "JPMorgan Chase & Co.", "Johnson & Johnson", 
    "Bank of America Corporation", "Industrial and Commercial Bank of China"
]

# Prepare the user prompt
prompt = "Classify the following companies into sectors such as Technology, Pharmaceuticals/Biotechnology, and Financial Services:\n" + "\n".join(companies)

# Call the OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=150
)

# Print the classification result
print(response['choices'][0]['message']['content'])
