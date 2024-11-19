from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9, openai_api_key="sk-h6S4gfVJsZlsiuqFnQhdCsuOgrjhWm4zyASMOjbgBZT3BlbkFJoo79Qgl6SU60vlG3Ks3ljDYmsFoGCoKbbeijYBqqQA")
prompt = "Suggest a good name for a company that produces socks"
print(llm(prompt))
llm_deterministic = OpenAI(temperature=0)
responses = llm.generate([prompt]*5)
for name in responses.generations:
    print(name[0].text)