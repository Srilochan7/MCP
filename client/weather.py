from mcp.server.fastmcp import FastMCP

mcp = FastMCP('weather')


@mcp.tool()
def get_weather(location: str) -> str:
    """
    Gets the current weather for a given location.

    Args:
        location: location, can be city name, zip code, etc.
    """
    
    return "The weather is hot and sunny"


if __name__ == "__main__":
    mcp.run()