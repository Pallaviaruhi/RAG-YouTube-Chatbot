from ingest import fetch_transcript
from text_splitter import chunk_text

def run(video_url):
    print("[1] Fetching transcript...")
    transcript = fetch_transcript(video_url)
    
    if not transcript:
        print("❌ Failed to fetch transcript.")
        return

    print("[2] Splitting transcript into chunks...")
    chunks = chunk_text(transcript)
    
    print(f"✅ Total chunks: {len(chunks)}")
    print("🔍 First chunk preview:\n")
    print(chunks[0][:500])
    from embed_store import store_embeddings

    
    print(f"✅ Total chunks: {len(chunks)}")

    print("[3] Storing chunks in ChromaDB...")
    store_embeddings(chunks)

if __name__ == "__main__":
    video_url = input("Paste YouTube video URL: ")
    run(video_url)
