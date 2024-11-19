from langchain_openai import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# Initialize the OpenAI LLM with your API key
llm = OpenAI(temperature=0, openai_api_key="sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA")

# Load the required tools
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# Initialize the agent with zero-shot reasoning
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Define the prompt and run the agent
prompt = "When was the 3rd President of the United States born? What is that year raised to the power 3?"
agent.run(prompt)
