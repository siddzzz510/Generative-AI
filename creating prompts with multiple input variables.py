from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Define the prompt template with the required format
prompt = PromptTemplate(
    template="""
    You are a naming consultant. Respond to the following question:
    {question}. Do not use technical words; give easy-to-understand responses.
    Provide your response in {language}.
    """,
    input_variables=["question", "language"]
)

# Format the prompt with specified variable values
prompt_formatted_str = prompt.format(
    question="Suggest a good name for a company that makes socks?",
    language="English"
)

# Instantiate the OpenAI instance
llm = OpenAI(openai_api_key="sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA", temperature=0.9)  # Replace with your actual API key

# Make a prediction
prediction = llm.predict(prompt_formatted_str)

# Print the prediction
print(prediction)
