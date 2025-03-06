# Legal Chatbot

## Overview

This project implements a multi-agent chatbot designed to provide users with accessible and understandable legal information related to Indian law. The chatbot leverages trusted legal sources, simplifies complex concepts, and delivers concise answers to user queries. It is built using Python, Langchain, and OpenAI's language models.

## Architecture

The chatbot uses a pipeline architecture consisting of the following agents:

1.  **User Query:** The user inputs a legal question.
2.  **Query Agent:** This agent receives the user's query, searches the pre-processed legal documents (stored in a vector database using ChromaDB), and retrieves the most relevant sections.
3.  **Summarization Agent:** This agent takes the retrieved text from the Query Agent and generates a simplified and concise summary using OpenAI's GPT models.  It aims to convert legal jargon into plain language.
4.  **Response to User:** The summarized answer is presented to the user.

![Architecture Diagram](docs/architecture.png) 

## Key Features

*   **Multi-Agent Architecture:** Employs a modular design with specialized agents for efficient information retrieval and summarization.
*   **Legal Knowledge Base:**  Utilizes [Guide to Litigation in India](https://www.cyrilshroff.com/wp-content/uploads/2020/09/Guide-to-Litigation-in-India.pdf) and [Legal Compliance & Corporate Laws by ICAI](https://kb.icai.org/pdfs/PDFFile5b28c9ce64e524.54675199.pdf) (replace with actual URLs if available) as trusted data sources.
*   **Simplified Language:** Converts complex legal terms into easy-to-understand explanations.
*   **OpenAI Integration:** Leverages powerful language models for text summarization and question answering.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd legal-chatbot
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    ```

4.  **Activate the virtual environment:**
    *   **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows:**
        ```bash
        venv\Scripts\activate
        ```

5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Set up environment variables:**

    *   You'll need an OpenAI API key.  Get one at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys).
    *   Set the `OPENAI_API_KEY` environment variable:

        *   **Linux/macOS:**
            ```bash
            export OPENAI_API_KEY="your_openai_api_key"
            ```
        *   **Windows:**
            ```bash
            set OPENAI_API_KEY="your_openai_api_key"
            ```

    *   **Alternatively,** you can create a `.env` file in the project root directory with the following content:

        ```
        OPENAI_API_KEY=your_openai_api_key
        ```
        And then load it in `config.py` using `python-dotenv`.

7. **Download Sample Data (if applicable):**
    * If the legal documents are not included directly in the repository (recommended for large files), run the following script to download sample data:
        ```bash
        python src/data/download_data.py
        ```
        *Replace sample data with your data source if you have one.*

## Usage

1.  **Run the chatbot:**
    ```bash
    python src/main.py
    ```

2.  **Interact with the chatbot:**
    *   The chatbot will prompt you to enter your legal query.
    *   Type your question and press Enter.
    *   The chatbot will provide a summarized answer based on the legal documents.
    *   Type `exit` to quit the chatbot.

### Example Queries

*   "What are the steps involved in filing a lawsuit in India?"
*   "Explain the concept of corporate social responsibility in Indian law."
*   "What are the key provisions of the Companies Act, 2013?"
*   "What are the different types of taxes levied in India?"

## Challenges Faced

*   **Data Scarcity:**  Finding comprehensive and readily available legal datasets can be challenging.
*   **Ambiguity in Legal Language:** Legal text often contains complex and ambiguous language, making it difficult for the chatbot to accurately understand the meaning and provide relevant summaries.
*   **Hallucinations:**  Large language models can sometimes generate inaccurate or fabricated information.
*   **Computational Cost:** Summarizing long legal documents can be computationally expensive.

## Possible Improvements

*   **Finetuning the LLM:** Finetuning the LLM on a legal dataset can improve its accuracy and performance in legal tasks.
*   **Advanced Retrieval Strategies:** Implementing hybrid search (keyword and semantic) to improve retrieval.
*   **Knowledge Graph Integration:**  Building a knowledge graph to better represent legal concepts and relationships.
*   **Human-in-the-Loop:** Incorporating human review for high-stakes legal advice.
*   **GUI:** Creating a graphical user interface for a better user experience.

## License

This project is licensed under the [MIT License](LICENSE).
