from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain import SerpAPIWrapper, WikipediaAPIWrapper, LLMMathChain
import os

# Manually set your API keys
os.environ["OPENAI_API_KEY"] = "sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA"
serpapi_api_key = "df99b39815ffea49734a4fead352565ff91761e16628a0c82adf293a352dccd2"

# Initialize the ChatOpenAI model
llm = ChatOpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the math tool
llm_mathchain = LLMMathChain.from_llm(llm=llm, verbose=True)

# Initialize the search tool with your SerpAPI API Key
search = SerpAPIWrapper(serpapi_api_key=serpapi_api_key)

# Initialize the Wikipedia tool
wikipedia = WikipediaAPIWrapper()

# Define the tools
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for answering questions about current events"
    ),
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful for looking up facts and statistics"
    ),
    Tool(
        name="Calculator",
        func=llm_mathchain.run,
        description="Useful for calculations"
    ),
]

# Set up the agent with zero-shot reasoning
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True
)

# Define the prompt and run the agent
prompt = """Where is the next summer Olympics to be conducted?
What is the population of that country raised to 0.4 power?"""
response = agent.run(prompt)

# Print the response
print(response)
