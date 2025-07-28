from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    sample_text = "This is a sample transcript sentence. " * 50
    chunks = chunk_text(sample_text)
    print(f"Total Chunks: {len(chunks)}")
    print("First chunk:\n", chunks[0])