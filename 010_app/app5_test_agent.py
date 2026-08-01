# app5_test_agent.py -- needs the servers from Sections 3 and 5 still running
import os
import getpass
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Anthropic API key: ")

async def main():
    client = MultiServerMCPClient({
        "math": {"transport": "stdio", "command": "python3", "args": ["app5_math_server.py"]},
        "weather": {"transport": "http", "url": "http://127.0.0.1:8765/mcp"},
    })
    tools = await client.get_tools()

    agent = create_agent(
        model="claude-haiku-4-5",
        tools=tools,
        system_prompt="You are a helpful assistant with access to math and weather tools.",
    )

    result = await agent.ainvoke({"messages": [
        {"role": "user", "content": "What's 23 times 47, and what's the weather in Chicago?"}
    ]})
    print(result["messages"][-1].content)

asyncio.run(main())