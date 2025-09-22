from mcp.server.fastmcp import FastMCP 
from mcp.server.fastmcp.utilities.types import Image
import pyautogui 
import io


mcp = FastMCP("screenshot")



@mcp.tool() 
def capture_screenshot() -> Image:
    """
    Captures the current screenshot and return the image. Use this tool whenever user requests a screenshot activity.
    """
    buffer = io.BytesIO()
    
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    
    return Image(data=buffer.getvalue(), format='jpeg')


if __name__ == "__main__":
    mcp.run()