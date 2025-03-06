import os
from dotenv import load_dotenv
from src.agents.query_agent import QueryAgent
from src.agents.summarization_agent import SummarizationAgent
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Load environment variables from .env file (if it exists)
load_dotenv()

def main():
    """
    Main function to run the legal chatbot.
    """

    # Initialize OpenAI API key
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OpenAI API key not found.  Set the OPENAI_API_KEY environment variable.")

    # Initialize Agents
    embeddings = OpenAIEmbeddings()  # You can specify openai_api_key=openai_api_key here if needed
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

    query_agent = QueryAgent(vectorstore_path="./chroma_db", embeddings=embeddings)
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
