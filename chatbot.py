import openai

# Function to interact with the chatbot
def math_tutor_chatbot(api_key, question):
    openai.api_key = api_key
    try:
        # OpenAI API request to answer the question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful maths tutor."},
                {"role": "user", "content": question}
            ],
            max_tokens=100  # Limit the response length
        )
        # Extract and return the answer
        return response['choices'][0]['message']['content'].strip()
    
    except openai.error.AuthenticationError:
        raise Exception("Invalid API Key")
    except Exception as e:
        raise Exception(f"Error: {e}")

# Main function to ask math questions
if __name__ == "__main__":
    api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"
    
    print("Welcome to the Maths Tutor Chatbot!")
    print("Ask any math-related question, or type 'exit' to quit.")
    
    while True:
        # Take user input
        question = input("You: ")
        
        if question.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            # Get the answer from the chatbot
            answer = math_tutor_chatbot(api_key, question)
            print(f"Maths Tutor: {answer}")
        except Exception as e:
            print(f"Error: {e}")
