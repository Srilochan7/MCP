# from mcp.server.fastmcp import FastMCP 




# mcp = FastMCP("Local Notes")

# @mcp.tool()
# async def add_note_to_file(content: str) -> str:
#     """
#     Appends the given content to users local notes

#     Args:
#         content : the text to append
#     """
    
#     filename = "notes.txt"
    
#     try:
#         with open(filename, "a") as file:
#             file.write(content + "\n")
#         return f"Note added to {filename}"
    
#     except Exception as e:
#         return f"Failed to add note: {str(e)}"
    

# @mcp.tool()
# async def read_notes() -> str:
#     """
#     Reads and returns the content of users local notes

#     """
#     filename = "notes.txt"

#     try:
#         with open(filename, "r") as file:
#             notes = file.read()
#         return notes if notes else "No notes found."
#     except Exception as e:
#         return f"Failed to read notes: {str(e)}"
    
    
    
# mcp.run()
