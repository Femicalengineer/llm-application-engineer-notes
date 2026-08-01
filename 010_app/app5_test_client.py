# test_client.py
import asyncio
from fastmcp import Client

async def main():
    # Points straight at the .py file -- fastmcp handles starting app5_math_server.py
    # as a subprocess and talking to it over stdio, underneath this one line.
    client = Client("app5_math_server.py")
    async with client:
        tools = await client.list_tools()
        print("Available tools:")
        for t in tools:
            print(f"  - {t.name}: {t.description}")

        result = await client.call_tool("add", {"a": 5, "b": 7})
        print("\nadd(5, 7) ->", result.content[0].text)

        result2 = await client.call_tool("multiply", {"a": 6, "b": 7})
        print("multiply(6, 7) ->", result2.content[0].text)

asyncio.run(main())