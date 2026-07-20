from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)
MODEL="llama-3.3-70b-versatile"