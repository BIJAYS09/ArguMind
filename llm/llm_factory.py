from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

def get_llm(temperature: float = 0.7):
    """
    Factory function to create and return a Gemini LLM instance.
    All agents must get their LLM from here.
    """
    #api_key = os.getenv("GEMINI_API_KEY")
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

    # return ChatGoogleGenerativeAI(
    #     model="gemini-robotics-er-1.5-preview",
    #     temperature=temperature,
    #     api_key=api_key
    # )
    return ChatGroq(
        model="allam-2-7b",  # or: llama3-8b-8192, mixtral-8x7b-32768, etc.
        temperature=0.2,
    )