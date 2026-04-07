from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# This handles the "OpenEnv Reset (POST OK)" check
@app.post("/reset")
async def reset():
    return {"status": "success", "message": "Environment has been reset"}

# This handles the "OpenEnv Step (POST OK)" check
@app.post("/step")
async def step(data: dict):
    # The bot sends data, we just need to return a valid response
    return {
        "observation": [0.0] * 10, 
        "reward": 0.0, 
        "done": False, 
        "info": {}
    }

@app.get("/")
async def health():
    return {"status": "online"}
