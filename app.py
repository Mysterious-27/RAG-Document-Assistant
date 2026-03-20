import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.llms import Ollama
import tempfile
# from langchain_openai import ChatOpenAI
import os


st.set_page_config(page_title="DocQuer.AI", layout="wide")

st.title("📄 DocQuer.AI")
st.markdown("Chat with your PDFs instantly ⚡")

# Upload section (ALWAYS visible)
uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show message if no file
if not uploaded_files:
    st.warning("📄 Please upload at least one PDF to start")
else:
    st.success("Documents uploaded! Processing...")

    all_docs = []

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            loader = PyPDFLoader(tmp_file.name)
            docs = loader.load()
            all_docs.extend(docs)

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(all_docs)

    @st.cache_resource
    def create_vectorstore(_texts):
        embeddings = HuggingFaceEmbeddings()
        return FAISS.from_documents(_texts, embeddings)

    vectorstore = create_vectorstore(texts)

    st.success("✅ Ready! Ask your question below 👇")

    # Chat input
    query = st.chat_input("Ask something...")

    if query:
        st.session_state.messages.append(("user", query))

        docs = vectorstore.similarity_search(query, k=4)
        context = " ".join([doc.page_content for doc in docs])
## Ollama
        # llm = Ollama(model="llama3")
## OpenAI
        # os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

        # llm = ChatOpenAI(model="gpt-3.5-turbo")
## Groq
    #     llm = ChatGroq(
    # groq_api_key="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",
    # model_name="llama3-8b-8192"   # ⚡ correct + fast
# )
## Gemini
        llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key="AIzaSyAxrS6g9u1fOBk7gDfktIvN0DEr5cL-XXk"
    )
        
        prompt = f"""
        You are an AI assistant.
        Use the context below to answer the question. If the answer is partially available, try to summarise.

        Context:
        {context}

        Question:
        {query}
        
        Answer clearly:
        """
        response = llm.invoke(prompt)       
        st.session_state.messages.append(("assistant", response.content))
# Display chat history
for role, message in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)
