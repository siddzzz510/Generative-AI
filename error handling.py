import openai

def get_openai_response(api_key, prompt):
    openai.api_key = api_key
    try:
        # Request response from OpenAI using gpt-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.AuthenticationError:
        raise Exception("Invalid API Key")
    except Exception as e:
        raise Exception(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    api_key = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"
    prompt = "Write a short story about friendship."
    
    try:
        print(get_openai_response(api_key, prompt))
    except Exception as e:
        print(e)
