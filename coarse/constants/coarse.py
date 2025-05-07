import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

S2_API_KEY = os.getenv("S2_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0
)