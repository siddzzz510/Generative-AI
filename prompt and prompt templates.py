# Import necessary libraries
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Create the prompt template
prompt_template: str = """
You are a vehicle mechanic, give responses to the following 
question: {question}. Do not use technical words; give easy-to-understand responses.
"""

# Initialize the prompt template
prompt = PromptTemplate.from_template(template=prompt_template)

# Format the prompt to add variable values
prompt_formatted_str = prompt.format(
    question="Why won't a vehicle start on ignition?"
)

# Instantiate the OpenAI instance with the API key if required
llm = OpenAI(openai_api_key="sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA", temperature=0.9)

# Make a prediction
prediction = llm(prompt_formatted_str)

# Print the prediction
print(prediction)
