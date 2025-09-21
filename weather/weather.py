from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    Args:
        location: location, can be city,country or state.
        
    """
    return "The weather is hot and dry"



if __name__ == "__main__":
    mcp.run()