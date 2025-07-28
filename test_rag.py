from ask_chain import build_rag_chain

if __name__ == "__main__":
    chain = build_rag_chain()
    query = input("Ask a question about the video: ")
    answer = chain.invoke(query)
    
    print("\n💬 Answer:\n", answer.content)