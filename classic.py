import os
from mcp.server.fastmcp import FastMCP

STYLES_DIR = os.path.join(os.path.dirname(__file__), "styles")

# Create the MCP server
mcp = FastMCP("TextStyling")


@mcp.tool()
def get_writing_style(style: str) -> dict:
    """Retrieve the style prompt for a given writing style."""
    style_file = os.path.join(STYLES_DIR, f"{style}.txt")
    if not os.path.isfile(style_file):
        return {"error": f"Style '{style}' not found."}
    with open(style_file, "r", encoding="utf-8") as f:
        prompt = f.read()
    return {"prompt": prompt}


if __name__ == "__main__":
    mcp.run()
