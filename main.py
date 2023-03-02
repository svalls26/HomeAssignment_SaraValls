from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Home Page"}

from endpoints.blocks import *

