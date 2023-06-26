from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {"example": {"id": 1, "item": "Example Todo"}}


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item": "Example TodoItem"}}


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example TodoItems 1"},
                    {"item": "Example TodoItems 2"},
                ]
            }
        }
