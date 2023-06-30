from sqlmodel import SQLModel, JSON, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book",
                "image": "http://limktomyimage.com/image.png",
                "description": "this is description",
                "location": "Google Meet",
                "tags": ["python", "fastapi", "book", "launch"],
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "this is description",
                "tags": ["python", "fastapi", "book", "lunch"],
                "location": "Google Meet",
            }
        }
