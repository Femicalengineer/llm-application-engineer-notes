# app2.py
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    thread_id: str = Field(default="default")

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # Placeholder logic for now -- the real agent gets wired in next section.
    return ChatResponse(reply=f"You said: {request.message} (thread={request.thread_id})")