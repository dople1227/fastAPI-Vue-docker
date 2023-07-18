from fastapi import APIRouter, Path
from .schemas import Todo

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(
        ...,
        title="타이틀 ",
        description="문서화 시 보여 줄 파라미터 설명",
        gt=0,
        le=5,
        example=4,
    )
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}

    return {"message": "Todo with supplied ID doesn`t exist."}
