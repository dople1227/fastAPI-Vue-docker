from fastapi import APIRouter, HTTPException, status, Path
from .schemas import Todo, TodoItem, TodoItems

todo_router = APIRouter()
todo_list = []


@todo_router.get("/todo", response_model=TodoItems)
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


# todo 한개 SELECT
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(
        ...,
        title="Title of Path Parameter",
        description="Description of Path Parameter",
    )
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo supplied ID doesn`t exist",
        headers={"testHeader": "testHeader Message", "secondHeader": "second Msg"},
    )


# todo 한개 UPDATE
@todo_router.put("/todo/{todo_id}", status_code=201)
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="The ID of the todo to be updated"),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo supplied ID doesn`t exist",
        headers={"testHeader": "testHeader Message"},
    )


# todo 한개 DELETE
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(
    todo_id: int = Path(..., title="The ID of the todo to be deleted")
) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo supplied ID doesn`t exist",
        headers={"testHeader": "testHeader Message"},
    )


# 전체 todo DELETE
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Todos deleted successfully"}
