from pydantic import BaseModel
from typing import Union


class Item(BaseModel):
    item: str
    status: str


class Todo(BaseModel):
    id: Union[int, bool]
    item: str
