import os 
import logfire
from dotenv import load_dotenv
load_dotenv()

def setup_tracing()->None:
    """ 
    Configure Logfire once for the entire app
    Call this exactly once - use st.cache_resource in streamlit
    """
    
    logfire.configure(
        token=os.getenv("LOGFIRE_TOKEN"),
        service_name="multi-agent-sys"
    )
    #start automatic tracing
    logfire.instrument_openai()