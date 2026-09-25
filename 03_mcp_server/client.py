from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],## Ensure correct absolute path
                "transport":"stdio"
            },
            "weather":{
                "url":"http://localhost:8000/mcp",# ensure your server is running
                "transport":"streamable-http"
            }
        } # type: ignore
    )
    
    import os 
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY") #type:ignore
    
    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b")
    agent = create_agent(
        model,tools
    )
    
    
    math_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"what's (3+5)*12?"}]}
    )
    
    print("Math response:", math_response['messages'][-1].content)
    
    weather_response = await agent.ainvoke(
            {"messages":[{"role":"user","content":"What is the weather in California?"}]}
    )
        
    print("Weather response:", weather_response['messages'][-1].content)
    
asyncio.run(main())