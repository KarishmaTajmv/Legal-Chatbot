# src/main.py
import os
from src.agents.query_agent import QueryAgent
from src.agents.summarization_agent import SummarizationAgent
from src.config import OPENAI_API_KEY
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader #Or other loaders

def load_documents_from_directory(directory):
    """Loads all PDF documents from a directory."""
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):  # Adjust for other file types
            filepath = os.path.join(directory, filename)
            loader = PyPDFLoader(filepath) #or TextLoader, etc
            documents.extend(loader.load())
    return documents

def main():
    # Initialize Agents
    embeddings = OpenAIEmbeddings()
    # Load legal documents
    data_directory = "src/data"
    documents = load_documents_from_directory(data_directory)

    # Create ChromaDB from documents (or load if it exists)
    if os.path.exists("./chroma_db"):
        db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    else:
       from langchain.text_splitter import RecursiveCharacterTextSplitter
       text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
       chunks = text_splitter.split_documents(documents)
       db = Chroma.from_documents(chunks, embeddings, persist_directory="./chroma_db")

    query_agent = QueryAgent(db)
    summarization_agent = SummarizationAgent()

    print("Legal Chatbot Ready! Ask your questions:")

    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            break

        answer = query_agent.generate_answer(user_query)
        print("Bot:", answer)

if __name__ == "__main__":
    main()
