# TextStyling MCP Server

This is an MCP (Model Context Protocol) server called TextStyling. It exposes a tool that, when given a style name (e.g., 'rt40'), loads a prompt that explains the style and returns it. This can be used to instruct a model to write in a certain style.

## Project Structure

- `server.py`: Main entrypoint for the MCP server.
- `styles/`: Directory containing prompt files for each style (e.g., `rt40.txt`).
- `pyproject.toml`: Project metadata and dependencies.

## Usage

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the server:
   ```sh
   python server.py
   ```

## Adding Styles

Add a new `.txt` file in the `styles/` directory with the name of the style (e.g., `rt40.txt`). The file should contain the prompt that explains the style.

## Dependencies
- mcp (Model Context Protocol Python SDK)

## References
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file)
