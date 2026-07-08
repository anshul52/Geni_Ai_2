from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_docling.loader import DoclingLoader
from langchain_core.prompts import ChatPromptTemplate


load_dotenv(override=True)
llm = ChatOpenAI(model="gpt-4.1-mini")

# docs loader
# FILE_PATH = "document_loader/notes.txt"
FILE_PATH = "https://mossmize.com/"
loader = DoclingLoader(file_path=FILE_PATH)
loaded_documents = loader.load()

# prompt template for the LLM
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that give details about the documents provided."),
    ("human", "{data}")
])

# format the prompt with the loaded document data
formatted_prompt = prompt_template.format_messages(data=loaded_documents[0].page_content)

response = llm.invoke(formatted_prompt)
print("====================================")
print(response.content)
