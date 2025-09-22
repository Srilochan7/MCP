from mcp.server.fastmcp import FastMCP

mcp = FastMCP("local-notes")

@mcp.tool()
async def add_note_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.
    """
    filename = "notes.txt"
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content + "\n")
        return f"✅ Note added to {filename}"
    except Exception as e:
        return f"❌ Failed to add note: {e}"

@mcp.tool()
async def read_notes() -> str:
    """
    Reads and returns the content of the user's local notes.
    """
    filename = "notes.txt"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            notes = file.read()
        return notes if notes.strip() else "No notes found."
    except FileNotFoundError:
        return "No notes file found yet."
    except Exception as e:
        return f"❌ Failed to read notes: {e}"

mcp.run()
