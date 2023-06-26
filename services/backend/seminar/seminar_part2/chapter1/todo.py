from fastapi import APIRouter, Path
from .schemas import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []


@todo_router.get("/todo", response_model=TodoItems)
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}
