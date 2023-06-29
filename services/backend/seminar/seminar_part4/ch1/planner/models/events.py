from typing import Optional, List
from sqlmodel import SQLModel, JSON, Field, Column


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    location: str
    tags: List[str] = Field(sa_column=Column(JSON))

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
