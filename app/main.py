from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Home Page"}

from src.blocks import *
from src.signatures import *
