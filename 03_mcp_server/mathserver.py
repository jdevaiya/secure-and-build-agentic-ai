from mcp.server.fastmcp import FastMCP

mcp = FastMCP("math")

@mcp.tool()
def add(a:int,b:int)->int:
    """Add two number"""
    return a+b

@mcp.tool()
def multiple(a:int,b:int)->int:
    """multiply two number"""
    return a*b

# The transport= "stdio" argument tells the server to:

# Use standard input/output (stdin and stdout) to receive and respond to tool function calls


if __name__ == "__main__":
    mcp.run(transport="stdio")