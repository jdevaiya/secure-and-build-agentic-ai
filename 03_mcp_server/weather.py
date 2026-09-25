from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the wether location"""
    return "it's always raining in california"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")