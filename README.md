# 🤖 AI Document Assistant (RAG System)

A ChatGPT-like AI application that allows users to upload PDFs and ask questions based on their content using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* 📄 Upload multiple PDF documents
* 💬 Chat with documents like ChatGPT
* 🔎 Semantic search using vector embeddings
* 🤖 Local AI (Ollama + LLM) — no API required
* ⚡ Fast retrieval with FAISS
* 🎨 Clean and interactive UI using Streamlit

---

## 🧠 Tech Stack

* Python
* Streamlit
* LangChain
* FAISS (Vector Database)
* HuggingFace Embeddings
* Ollama (Local LLM)

---

## 🏗️ Architecture

User Query → Embedding → Vector Search → Relevant Chunks → LLM → Answer

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/AI-Document-Assistant.git
cd AI-Document-Assistant

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
ollama run phi
streamlit run app.py
```

Then open:

```
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

* Local LLM performance depends on system hardware
* Large PDFs may increase processing time

---

## 🚀 Future Improvements

* 🌐 Deploy online (Streamlit Cloud)
* 🎤 Voice input support
* 🧠 Chat memory
* 📊 Analytics dashboard

---

## 👨‍💻 Author

**Mysterious-27**
contactwithaditya27@gmail.com

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
