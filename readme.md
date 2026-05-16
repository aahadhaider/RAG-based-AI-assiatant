# 🎓 RAG-Based AI Teaching Assistant

> Turn your lecture videos into an intelligent, queryable knowledge base — powered by Retrieval-Augmented Generation (RAG) and Large Language Models.

---

## 🚀 Overview

This project transforms raw educational video content into a fully functional AI assistant that can answer questions based on your own lecture material. By combining audio transcription, vector embeddings, and LLM-powered response generation, it delivers accurate, context-aware answers grounded in your data — not just generic knowledge.

---

## 🧠 How It Works

```
Videos → Audio (MP3) → Transcripts (JSON) → Embeddings (Joblib) → LLM Response
```

The pipeline extracts knowledge from your videos step by step, stores it as semantic vector embeddings, and retrieves the most relevant context at query time before generating a response.

---

## 🛠️ Setup & Pipeline

### Step 1 — Collect Your Videos

Place all your lecture or educational videos inside the `videos/` folder.

```
project/
└── videos/
    ├── lecture_01.mp4
    ├── lecture_02.mp4
    └── ...
```

---

### Step 2 — Convert Videos to Audio

Run the conversion script to extract audio from each video file and save it as an MP3.

```bash
python video_to_mp3.py
```

> Converts all `.mp4` files in `videos/` → `.mp3` files ready for transcription.

---

### Step 3 — Transcribe Audio to JSON

Transcribe each MP3 file into structured text using the transcription script.

```bash
python mp3_to_json.py
```

> Produces one `.json` transcript file per audio file, capturing the full spoken content.

---

### Step 4 — Generate Vector Embeddings

Preprocess the JSON transcripts into a semantic vector dataframe and persist it as a Joblib pickle for fast reloading.

```bash
python preprocess_json.py
```

> Chunks transcripts, generates embeddings, and saves the result as a `.joblib` file — your searchable knowledge base.

---

### Step 5 — Query the AI Assistant

Load the knowledge base into memory, retrieve relevant chunks based on your query, construct a context-aware prompt, and get a response from the LLM.

```bash
python assistant.py
```

> Ask any question — the assistant retrieves the most relevant lecture content and generates a precise, grounded answer.

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Transcription | Whisper / SpeechRecognition |
| Embeddings | Sentence Transformers / OpenAI Embeddings |
| Vector Store | FAISS / Joblib |
| LLM | OpenAI GPT / Ollama |
| Orchestration | LangChain |
| Language | Python |

---

## 📁 Project Structure

```
rag-teaching-assistant/
├── videos/                  # Raw lecture videos
├── mp3s/                    # Extracted audio files
├── transcripts/             # JSON transcripts
├── video_to_mp3.py          # Step 2: Video → MP3
├── mp3_to_json.py           # Step 3: MP3 → JSON transcript
├── preprocess_json.py       # Step 4: JSON → Embeddings (Joblib)
├── assistant.py             # Step 5: Query the RAG assistant
└── README.md
```

---

## 💡 Use Cases

- 📚 Query your own lecture recordings for exam revision
- 🔍 Instantly find answers within hours of course content
- 🤖 Build a personalised AI tutor for any subject
- 🏫 Help educators create interactive Q&A tools from existing material

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas to improve the pipeline or extend functionality.

---

## 👤 Author

**Mohd Aahad**
linkedin-www.linkedin.com/in/mohd-aahad11

---

> ⭐ If you found this project useful, consider giving it a star — it helps others discover it!
