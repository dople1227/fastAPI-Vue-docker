from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo() -> dict:
    todo_list.append()
    return {"msg": "Todo add Successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
