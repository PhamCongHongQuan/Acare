import google.generativeai as genai
import os
from dotenv import load_dotenv

# API key is read from the GOOGLE_API_KEY environment variable or from a local .env file
# (see .env.example). Never commit a real key.
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("Missing GOOGLE_API_KEY. Copy .env.example to .env and set your Gemini API key.")

genai.configure(api_key=GOOGLE_API_KEY)

GEMINI_MODEL = "models/gemini-2.5-flash" 
EMBED_MODEL_NAME  = "sentence-transformers/all-MiniLM-L6-v2"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "data", "docs")
FAISS_DIR = os.path.join(BASE_DIR, "vectordb")

os.makedirs(DOCS_DIR, exist_ok=True)

