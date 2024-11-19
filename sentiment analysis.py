import openai

# Set the API key correctly
openai.api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"

# Create the chat completion
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": """
                Classify it as either positive, negative, or neutral:
                1. Just got my hands on the new XPhone - absolutely loving the camera and battery life! #TechLove
                2. Disappointed with the XPhone. It's pricey and not much different from the last model. Expected more. #TechTalk
                3. XPhone's latest update is a game-changer for mobile gaming. The graphics are just incredible! #100
                4. Can't believe I waited this long for the XPhone... it's underwhelming and overpriced. Back to my old phone, I guess.
                5. The XPhone has exceeded my expectations. Fast, sleek, and the new AI features are a standout! #Innovation
            """
        }
    ],
    max_tokens=300,
)

# Print the response
print(response['choices'][0]['message']['content'])
