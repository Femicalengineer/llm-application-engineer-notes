# test_adapters.py -- math_server.py (stdio) and weather_server.py (http, already
# running from Section 5) both contribute tools to ONE unified list.
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
        "math": {
            "transport": "stdio",
            "command": "python3",
            "args": ["app5_math_server.py"],
        },
        "weather": {
            "transport": "http",
            "url": "http://127.0.0.1:8765/mcp",
        },
    })
    tools = await client.get_tools()
    print(f"Loaded {len(tools)} tools from 2 MCP servers:")
    for t in tools:
        print(f"  - {t.name}: {t.description}")
        print(f"    type: {type(t).__name__}")

asyncio.run(main())