from langchain_openai import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# Initialize the OpenAI LLM with your API key
llm = OpenAI(temperature=0.8, openai_api_key="sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA")

# Load the required tools (in this case, "human")
tools = load_tools(["human"], llm=llm)

# Initialize the agent with zero-shot reasoning
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Define the prompt and run the agent
agent.run("What is my son's name?")
