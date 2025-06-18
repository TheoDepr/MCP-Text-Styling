# TextStyling MCP Server

This project is an MCP (Model Context Protocol) server called **TextStyling**, built using [FastMCP](https://gofastmcp.com/)—the fast, Pythonic way to build MCP servers and clients. The server exposes a tool that, when given a style name (e.g., 'romantic'), loads a prompt that explains the style and returns it. This can be used to instruct a model to write in a certain style.

## What is FastMCP?

[FastMCP](https://gofastmcp.com/) is a high-level framework for building MCP servers and clients in Python. It handles all the protocol details and server management, so you can focus on building tools, resources, and prompts for LLMs. FastMCP is the standard framework for working with the Model Context Protocol.

## Project Structure

- `server.py`: Main entrypoint for the MCP server.
- `styles/`: Directory containing prompt files for each style (e.g., `romantic.txt`, `business.txt`).
- `pyproject.toml`: Project metadata and dependencies.

## Usage

1. **Install dependencies** (Python 3.12+ required):

   ```sh
   pip install -r pyproject.toml
   # or, if using uv (recommended):
   uv pip install -r pyproject.toml
   ```

   Alternatively, you can install dependencies manually:

   ```sh
   pip install mcp[cli]>=1.9.4
   ```

2. **Install the server:**

   ```sh
   uv run mcp install server.py
   ```

   This will install the server in Claude's MCP server directory. There you can copy the config settings.

## Adding Styles

Add a new `.txt` file in the `styles/` directory with the name of the style (e.g., `romantic.txt`). The file should contain the prompt that explains the style. Example styles included:

- `romantic.txt`
- `business.txt`
- `scientific.txt`
- `humorous.txt`
- `poetic.txt`
- `journalistic.txt`
- `technical.txt`
- `persuasive.txt`
- `creative.txt`
- `casual.txt`
- `academic.txt`
- `fancy.txt`
- `mysterious.txt`

## Dependencies

- [mcp (Model Context Protocol Python SDK)](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file)
- [fastmcp](https://gofastmcp.com/) (if using FastMCP 2.x)

## References

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file)
- [FastMCP Documentation](https://gofastmcp.com/)
