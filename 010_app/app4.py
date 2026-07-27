# app_async.py
import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/sync-slow")
def sync_slow():
    # Simulates a slow LLM call using a BLOCKING sleep.
    time.sleep(2)
    return {"done": "sync"}

@app.get("/async-slow")
async def async_slow():
    # Simulates a slow LLM call using a NON-blocking wait.
    await asyncio.sleep(2)
    return {"done": "async"}

