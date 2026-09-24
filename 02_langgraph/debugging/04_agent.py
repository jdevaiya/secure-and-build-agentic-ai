from typing_extensions import TypedDict
from typing import Annotated
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langgraph.prebuilt import tools_condition
from IPython.display import display,Image
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEy") #type:ignore
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEy") #type:ignore

os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]="jayendra"
os.environ["LANGSMITH_ENDPOINT"]="https://api.smith.langchain.com"

from langchain.chat_models import init_chat_model
llm = init_chat_model("groq:openai/gpt-oss-120b")

class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]
    
## graph with tool call 
from langchain_core.tools import tool
def make_tool_graph():
    @tool 
    def add(a:float,b:float):
        """Add two number"""
        
        return a+b

    tools = [add]
    llm_with_tool = llm.bind_tools([add])

    def call_llm_model(state:State): #type:ignore
        return {"messages":[llm_with_tool.invoke(state['messages'])]} #type:ignore

    ## StateGraph

    builder = StateGraph(State)
    builder.add_node("tool_calling_llm", call_llm_model)
    builder.add_node("tools",ToolNode(tools))

    #edge
    builder.add_edge(START,"tool_calling_llm")
    builder.add_conditional_edges(
        "tool_calling_llm",
        tools_condition
    )
    builder.add_edge("tools","tool_calling_llm")

    graph = builder.compile()

    return graph

tool_agent = make_tool_graph()