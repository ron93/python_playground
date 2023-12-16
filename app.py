# /app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/apiv2/info")
async  def hellov2():
    return {"message": "Hello, World from V2"}