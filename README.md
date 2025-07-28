# RAG-YouTube-Chatbot
## Overview

**YouTube RAG Chatbot** is an AI-powered chatbot that leverages a Retrieval-Augmented Generation (RAG) pipeline to answer questions based on the transcripts of any YouTube video. By combining transcript retrieval, vector database indexing, and powerful language models, this tool provides accurate, context-aware answers sourced directly from the video content.

---

## Features

- **Automatic transcript retrieval** from YouTube videos (with supported captions)
- **Transcript chunking** with overlapping splits for enhanced context retention
- **Efficient storage** of transcript chunks in a Chroma vector database
- **Semantic search:** User questions are embedded and compared for contextual similarity
- **LLM-powered responses:** Uses DeepSeek-R1-0528 or any Hugging Face-compatible model for final answer synthesis
- **Supports multiple videos** and local database persistence
- **Easy to extend** and build upon for custom use cases

---

## Tech Stack

- Python 3.10+
- [LangChain](https://python.langchain.com/) (core, community, HuggingFace integrations)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [ChromaDB](https://www.trychroma.com/)
- [YoutubeTranscriptApi](https://pypi.org/project/youtube-transcript-api/)
- python-dotenv

---

## Getting Started

### 1. Clone the repository

```
git clone https://github.com/Pallaviaruhi/RAG-YouTube-Chatbot
cd Youtube--RAG-Chatbot
```

### 2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up your Hugging Face API key

Create a `.env` file inside the `app/` directory:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## Usage

### Step 1: Ingest a YouTube Transcript

```
python app/run_ingest_and_split.py
```
- When prompted, paste a YouTube video URL (with captions available).
- The transcript will be downloaded, chunked, and stored in your local ChromaDB instance.

### Step 2: Ask Questions About the Video

```
python app/test_rag.py
```
- Enter your question, and get fact-based answers drawn from the video transcript context.

---

## Notes

- Ensure the YouTube video you use has subtitles/captions enabled.
- Vector data is persisted locally in the `db/` folder by ChromaDB.
- Supports ingestion and question-answering for multiple videos.


---
