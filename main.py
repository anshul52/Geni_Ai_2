from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini")

response = llm.invoke("Hello! Tell me about LangChain.")

print(response.content)