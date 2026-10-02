from typing_extensions import TypedDict, List

class AgentState(TypedDict):
    question:str
    intent:str # this is used for which node execute first  decisions 
    specialist_output:str
    search_results:str
    final_answer:str
    model_used:str
    session_id:str
    node_path:List[str] # track which nodes executed