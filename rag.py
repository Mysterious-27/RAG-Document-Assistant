from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
# from langchain_community.llms import OpenAI
from langchain_community.llms import Ollama
# Load PDF
loader = PyPDFLoader("documents/sample.pdf")
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Store in vector DB
vectorstore = FAISS.from_documents(texts, embeddings)

# Ask question
query = input("Ask a question: ")

docs = vectorstore.similarity_search(query)

# # For OpenAI API

# llm = OpenAI()

# context = " ".join([doc.page_content for doc in docs])

# prompt = f"""
# Answer the question based on the context below.

# Context:
# {context}

# Question:
# {query}
# """

# response = llm(prompt)

# print("\nAI Answer:\n", response)

# Ollama API
llm = Ollama(model="llama3")

context = " ".join([doc.page_content for doc in docs])

prompt = f"""
Answer the question based on the context below.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)

print("\nAI Answer:\n", response)