from langchain_huggingface import HuggingFaceEmbeddings

embedding =  HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

text = [
    "hey this is all about Gen AI",
    "Agentic AI trending in IT",
    "RAG most demanding"
]

vector = embedding.embed_documents(text)
print(vector)
