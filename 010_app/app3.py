# app_agent.py
import os
import getpass
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

if not os.environ.get("ANTHROPIC_API_KEY"):
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Anthropic API key: ")

app = FastAPI()

# Built ONCE, at import time -- this line runs when `fastapi run` starts the
# server, not on every request. Reproduced from 008's guardrails section.
agent = create_agent(
    model="claude-haiku-4-5",
    tools=[],
    system_prompt="You are a customer service assistant.",
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        PIIMiddleware("credit_card", strategy="mask", apply_to_input=True),
    ],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = agent.invoke({"messages": [{"role": "user", "content": request.message}]})
    return ChatResponse(reply=result["messages"][-1].content)