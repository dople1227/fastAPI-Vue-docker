from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.get("/ping2")
def pong2():
    return {"ping2": "pong2!"}