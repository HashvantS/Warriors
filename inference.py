from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# This handles the "OpenEnv Reset (POST OK)" check
@app.post("/reset")
async def reset():
    return {"status": "success", "message": "Environment reset"}

# This handles the validation steps
@app.post("/step")
async def step(action: dict):
    return {"observation": {}, "reward": 0.0, "done": False}

@app.get("/")
async def health_check():
    return {"status": "running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
