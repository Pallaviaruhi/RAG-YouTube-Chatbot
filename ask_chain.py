from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableMap, RunnablePassthrough, RunnableLambda, RunnableSequence
load_dotenv()
import os
#print("✅ TOKEN:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))



def load_vectordb(persist_directory="db"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectordb


llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation"

)

model=ChatHuggingFace(llm=llm)

rag_prompt = PromptTemplate.from_template("""
Answer the following question based on the context provided. 
If you don't know, say you don't know.

Context:
{context}

Question:
{question}
""")

def build_rag_chain():
    vectordb = load_vectordb()
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    rag_chain=(
        {"context":retriever,"question":RunnablePassthrough()}
        |rag_prompt
        |model
    )

    return rag_chain
