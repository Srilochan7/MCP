from mcp.server.fastmcp import FastMCP 


mcp = FastMCP('Prompt')

@mcp.tool
def get_prompt(topic: str) -> str:
    """Get a writing prompt based on the given topic."""
    return f"Write a creative story about {topic}."