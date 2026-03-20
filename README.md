# 📄 DocQuery AI — Hybrid RAG Document Assistant

An AI-powered document assistant that allows users to upload PDFs and interact with them using natural language. Supports both **local LLMs (Ollama)** and **cloud LLMs (Groq & Gemini)**.

---

## 🚀 Features

* 📄 Upload multiple PDF documents
* 💬 Chat with documents like ChatGPT
* 🔎 Semantic search using vector embeddings
* ⚡ Fast responses using Groq (cloud LLM)
* 🧠 Intelligent fallback using Google Gemini
* 🖥️ Local AI support using Ollama (offline mode)
* 🔄 Hybrid LLM switching (Local + Cloud)
* 📚 Context-aware answers with source references
* 🎨 Clean UI using Streamlit

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Framework:** LangChain
* **Vector DB:** FAISS
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)

### 🤖 LLM Support

* **Cloud Models:**

  * Groq (LLaMA3 – fast inference)
  * Google Gemini (fallback reasoning)

* **Local Models:**

  * Ollama (e.g., `phi`, `llama3`)

---

## 🏗️ Architecture

```id="arc123"
User Query
   ↓
Embedding (HuggingFace)
   ↓
FAISS Vector Search
   ↓
Relevant Context Retrieval
   ↓
LLM (Groq / Gemini / Ollama)
   ↓
Final Answer
```

---

## 🌐 Live Demo

👉 [DocQuery.AI](https://docquer-ai.streamlit.app/)

---

## 📦 Installation

```bash id="inst01"
git clone https://github.com/YOUR_USERNAME/docquery-ai.git
cd docquery-ai

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔑 Setup

### Option 1: Cloud LLMs (Recommended)

Create `.streamlit/secrets.toml`:

```toml id="sec01"
GROQ_API_KEY = "your_groq_key"
GOOGLE_API_KEY = "your_google_key"
```

---

### Option 2: Local LLM (Offline Mode)

Install Ollama:

👉 https://ollama.com

Run model:

```bash id="ollama01"
ollama run phi
```

---

## ▶️ Run App

```bash id="run01"
streamlit run app.py
```

Open:

```id="url01"
http://localhost:8501
```

---

## 📄 Example Use Cases

* Resume analysis
* Study notes Q&A
* Research paper summarization
* Document search assistant

---

## ⚠️ Limitations

* Local models depend on hardware performance
* Cloud APIs may have rate limits
* Large PDFs increase processing time

---

## 🚀 Future Improvements

* 🔄 Streaming responses
* 🧠 Multi-turn chat memory
* 💾 Persistent vector database
* 🎛 Advanced model selection UI
* 🌐 Multi-user support

---

## 👨‍💻 Author

**Adhithya P V**
📧 [contactwithaditya27@gmail.com](mailto:contactwithaditya27@gmail.com)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
