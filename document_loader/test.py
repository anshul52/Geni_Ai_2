from langchain_docling.loader import DoclingLoader
# from langchain_community.document_loaders import TextLoader
FILE_PATH = "document_loader/notes.txt"

loader = DoclingLoader(file_path=FILE_PATH)

# Load all documents
documents = loader.load()

# For large datasets, lazily load documents
# for document in loader.lazy_load():
print("====================================")
print(documents[0].page_content)
print(len(documents))