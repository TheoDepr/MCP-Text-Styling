# Text Styling MCP Server
# Provides tools for retrieving writing style prompts from text files

import os
from mcp.server.fastmcp import FastMCP

# Directory containing style prompt files
STYLES_DIR = os.path.join(os.path.dirname(__file__), "styles")

# Create the MCP server instance
mcp = FastMCP("TextStyling")


@mcp.tool()
def get_writing_style(style: str) -> dict:
    """Retrieve the style prompt for a given writing style.
    
    Args:
        style: The name of the writing style (e.g., 'formal', 'casual')
    
    Returns:
        Dictionary containing either the style prompt or an error message
    """
    # Construct the path to the style file
    style_file = os.path.join(STYLES_DIR, f"{style}.txt")
    
    # Check if the style file exists
    if not os.path.isfile(style_file):
        return {"error": f"Style '{style}' not found."}
    
    # Read and return the style prompt
    with open(style_file, "r", encoding="utf-8") as f:
        prompt = f.read()
    return {"prompt": prompt}


# Run the server when executed directly
if __name__ == "__main__":
    # Support both stdio (default) and HTTP transports
    import sys
    if "--http" in sys.argv:
        # Run HTTP server on port 8000
        mcp.run(transport="sse", host="0.0.0.0", port=8000)
    else:
        # Default stdio transport
        mcp.run()
