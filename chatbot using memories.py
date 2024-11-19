# Example 1: Memory and Chatbot
from langchain.chat_models import ChatOpenAI
from langchain import ConversationChain

# Pass the API key explicitly
llm = ChatOpenAI(temperature=0.8, openai_api_key="sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA")

# Initialize a conversation chain
conversation = ConversationChain(llm=llm, verbose=True)

# Example conversation
print(conversation.predict(input="Hi!"))
print(conversation.predict(input="Can we talk about the weather?"))
print(conversation.predict(input="It's a beautiful day!"))

# Example 2: Terminal Chatbot
print("\nWelcome to your AI Chatbot!")
for i in range(3):
    human_input = input("You: ")
    ai_response = conversation.predict(input=human_input)
    print(f"AI: {ai_response}")

# Example 3: Store and Retrieve Chat History
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict

# Initialize chat history
initial_dialogue = ChatMessageHistory()
initial_dialogue.add_user_message("Hi! Let's talk about giraffes.")
initial_dialogue.add_ai_message("I am down to talk!")

# Convert messages to dictionary for context
dicts = messages_to_dict(initial_dialogue.messages)
context = messages_from_dict(dicts)

# Initialize the Chat history with context
history = ChatMessageHistory(messages=context)

# Initialize a memory object with the chat history
buffer = ConversationBufferMemory(chat_memory=history)

# Create a conversation chain with memory
conversation_with_memory = ConversationChain(llm=llm, memory=buffer, verbose=True)

# Continue the conversation
print(conversation_with_memory.predict(input="What are giraffes?"))
print(conversation_with_memory.predict(input="Tell me more about their habitats."))
