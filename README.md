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

