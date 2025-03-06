from langchain.chains import RetrievalQA
from langchain.llms import OpenAI # Or another LLM
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

class QueryAgent:
    def __init__(self, vectorstore_path="./chroma_db", embeddings=None, llm=None):
        """
        Initializes the QueryAgent.

        Args:
            vectorstore_path (str): Path to the ChromaDB vectorstore.
            embeddings (langchain.embeddings.Embeddings): Embedding model to use.
            llm (langchain.llms.base.LLM): Language model to use.
        """

        self.embeddings = embeddings or OpenAIEmbeddings()
        self.db = Chroma(persist_directory=vectorstore_path, embedding_function=self.embeddings)
        self.llm = llm or OpenAI()  # Default to OpenAI if no LLM is provided

    def generate_answer(self, query):
        """
        Generates an answer to a user query using the vectorstore and a language model.

        Args:
            query (str): The user's query.

        Returns:
            str: The generated answer.
        """
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,  # Or another LLM (e.g., GPT-3.5, GPT-4)
            chain_type="stuff",  # "stuff" is simplest, but consider "map_reduce" for large documents
            retriever=self.db.as_retriever(search_kwargs={'k': 3}),
            return_source_documents=False # Adjust based on whether you want to show sources
        )
        result = qa_chain({"query": query})
        return result["result"]
