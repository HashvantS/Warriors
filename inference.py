from fastapi import FastAPI
app = FastAPI()

@app.post("/reset")
async def reset():
    return {"status": "success"}

@app.post("/step")
async def step(action: dict):
    return {"observation": {}, "reward": 0, "done": False}
