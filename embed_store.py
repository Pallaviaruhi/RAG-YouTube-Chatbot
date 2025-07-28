from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import os

def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def store_embeddings(chunks, persist_directory="db"):
    embeddings = get_embedding_model()
    vectordb = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    vectordb.persist()
    print(f"✅ Stored {len(chunks)} chunks in ChromaDB.")
    return vectordb




