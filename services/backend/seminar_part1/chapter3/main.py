from fastapi import FastAPI
from .todopath import todo_router

app = FastAPI()


@app.get("/")
async def hello() -> dict:
    return {"message": "Hello"}


app.include_router(todo_router)
