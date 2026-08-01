# app5_test_external.py
import asyncio
from fastmcp import Client

async def main():
    client = Client("https://docs.langchain.com/mcp")
    async with client:
        tools = await client.list_tools()
        print(f"Connected to a real, public MCP server we did not write.")
        print(f"It exposes {len(tools)} tools:")
        for t in tools:
            print(f"  - {t.name}: {t.description[:80] if t.description else ''}")

asyncio.run(main())