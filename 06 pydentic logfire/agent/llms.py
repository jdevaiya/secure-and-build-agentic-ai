import os 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

#groq llm 
def groq_llm(temperature: float=0.3) ->ChatOpenAI:
    return ChatOpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"), #type:ignore
        model="qwen/qwen3.8-27b",
        temperature=temperature
    )
    
    
#Gemini llm

def gemini_llm(temperature: float=0.3) ->ChatOpenAI:
    return ChatOpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai",
        api_key=os.getenv("GOOGLE_API_KEY"), #type:ignore
        model="gemini-3.7-flash",
        temperature=temperature
    )