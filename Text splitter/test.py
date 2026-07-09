from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_docling.loader import DoclingLoader


# from langchain_community.document_loaders import TextLoader
FILE_PATH = "Text splitter/notes.md"
loader = DoclingLoader(file_path=FILE_PATH)
# Load all documents
documents = loader.load()

print("====================================")
text_splitter = RecursiveCharacterTextSplitter(
   chunk_size=500,
    # chunk_overlap=100,

    # length_function=len,
    is_separator_regex=False,
    # keep_separator=True
)
print("================000000000000====================")
print(documents)
texts = text_splitter.create_documents(documents)



# For large datasets, lazily load documents
# for document in loader.lazy_load():
print("====================================")
print(texts)
print(len(texts))