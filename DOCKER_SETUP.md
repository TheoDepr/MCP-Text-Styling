# Docker MCP Client Connection Guide

## Connection Methods

### 1. Stdio Transport (Recommended for Testing)

**Direct Docker execution:**
```bash
# Build the image first
docker build -t text-styling-mcp .

# Run with stdio transport (interactive)
docker run -i --rm text-styling-mcp
```

**From Python client:**
```python
from mcp.client.fastmcp import FastMCPClient

async with FastMCPClient(
    transport_type="stdio",
    command=["docker", "run", "-i", "--rm", "text-styling-mcp"]
) as client:
    result = await client.call_tool("get_writing_style", style="romantic")
```

### 2. HTTP Transport (For Network Access)

**Start server with HTTP:**
```bash
# Using docker-compose (automatically uses --http flag)
docker-compose up -d

# Or manually with HTTP transport
docker run -p 8000:8000 text-styling-mcp python server.py --http
```

**From Python client:**
```python
async with FastMCPClient(
    transport_type="sse",
    url="http://localhost:8000"
) as client:
    result = await client.call_tool("get_writing_style", style="business")
```

### 3. Claude Desktop Configuration

Add to your Claude Desktop MCP settings:

**For stdio transport:**
```json
{
  "mcpServers": {
    "text-styling": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "text-styling-mcp"]
    }
  }
}
```

**For HTTP transport:**
```json
{
  "mcpServers": {
    "text-styling": {
      "url": "http://localhost:8000"
    }
  }
}
```

## Testing the Connection

Run the example client:
```bash
# Install FastMCP client
pip install mcp[cli]

# Run the test client
python client_example.py
```

## Available Tools

- `get_writing_style(style: str)` - Returns writing style prompts from the styles/ directory

## Troubleshooting

- Ensure Docker image is built: `docker build -t text-styling-mcp .`
- For HTTP transport, verify port 8000 is accessible
- Check container logs: `docker logs text-styling-server`