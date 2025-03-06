import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in .env file or environment variables.")

CHROMA_DB_PATH = "./chroma_db"  # Or a different path
