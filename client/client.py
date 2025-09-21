from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import json
import traceback



server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"],
)

async def run():
    try:
        print("Starting client...")
        async with stdio_client(server_params) as (read, write):
            print("Client started.")
            async with ClientSession(read, write) as session:
                print("Session started.")
                
                await session.initialize()
                
                print("listing tools...")
                tools = await session.list_tools()
                print("Tools:", tools)
                
                print("Calling get_weather...")
                weather = await session.call("get_weather", arguments={"location": "New York"})
                print("Weather:", weather)
                
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()
        
        
if __name__ == "__main__":
    asyncio.run(run())