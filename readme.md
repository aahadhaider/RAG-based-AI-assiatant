🤖 RAG-Based AI Assistant

A Retrieval-Augmented Generation (RAG) based AI Assistant that combines the power of semantic search and large language models to provide accurate, context-aware responses from custom data.

📌 Project Overview

This project implements a RAG (Retrieval-Augmented Generation) pipeline where:

Relevant information is retrieved from a custom dataset
The retrieved context is passed to a language model
The model generates accurate and context-based answers

This approach reduces hallucination and improves response reliability.

🚀 Features
🔍 Semantic Search using embeddings
📂 Custom JSON-based knowledge base
⚡ Fast similarity search using cosine similarity
🧠 Context-aware response generation
💾 Embeddings stored using joblib
🔗 Integration with local embedding API (e.g., BGE model)


🛠️ Tech Stack
Python
NumPy
Pandas
Scikit-learn (cosine similarity)
Joblib
Requests
Embedding Model (BGE-M3 or similar)
LLM API (OpenAI / Local LLM)

📁 Project Structure
RAG-AI-Assistant/
│
├── jsons/                # Knowledge base (input data)
├── embeddings.joblib     # Stored embeddings
├── main.py               # Main query script
├── create_embeddings.py  # Script to generate embeddings
├── config.py             # API keys and configs
└── README.md


⚙️ How It Works
Data Loading
JSON files are loaded from the jsons/ folder
Embedding Creation
Text chunks are converted into vector embeddings using an embedding model
Storage
Embeddings are stored locally using joblib
Query Processing
User input is converted into embedding
Similarity Search
Cosine similarity is used to find the most relevant chunks
Response Generation
Retrieved context is passed to the LLM for final answer generation
