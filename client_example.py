#!/usr/bin/env python3
"""
Example MCP client to connect to the TextStyling server.
Shows different transport methods for connecting to the containerized server.
"""

import asyncio
from mcp.client.fastmcp import FastMCPClient

async def test_stdio_client():
    """Test client using stdio transport (direct Docker execution)"""
    print("Testing stdio transport...")
    
    # For stdio transport with Docker
    async with FastMCPClient(
        transport_type="stdio",
        command=["docker", "run", "-i", "--rm", "text-styling-mcp"]
    ) as client:
        # List available tools
        print("Available tools:", [tool.name for tool in client.tools])
        
        # Call the get_writing_style tool
        result = await client.call_tool("get_writing_style", style="romantic")
        print("Romantic style result:", result)

async def test_http_client():
    """Test client using HTTP transport (docker-compose with --http)"""
    print("Testing HTTP transport...")
    
    # For HTTP transport (requires server running with --http flag)
    async with FastMCPClient(
        transport_type="sse",
        url="http://localhost:8000"
    ) as client:
        # List available tools
        print("Available tools:", [tool.name for tool in client.tools])
        
        # Call the get_writing_style tool
        result = await client.call_tool("get_writing_style", style="business")
        print("Business style result:", result)

async def main():
    """Main function to test different transport methods"""
    print("MCP Client Examples for TextStyling Server")
    print("=" * 50)
    
    try:
        # Test stdio transport
        await test_stdio_client()
        print()
        
        # Test HTTP transport (uncomment if server is running with --http)
        # await test_http_client()
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the Docker image is built: docker build -t text-styling-mcp .")

if __name__ == "__main__":
    asyncio.run(main())