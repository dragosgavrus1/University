from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

print(f"Number of documents: {len(vectorstore)}")

# Optional: test a query
results = vectorstore.similarity_search("quantum computing", k=3)
for doc in results:
    print(doc.metadata)
    print(doc.page_content[:200], "\n---")