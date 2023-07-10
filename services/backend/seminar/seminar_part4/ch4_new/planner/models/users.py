from pydantic import EmailStr
from sqlmodel import SQLModel, JSON, Field, Column
from typing import Optional, List
from .events import Event


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr
    username: str
    password: str
    events: Optional[List[Event]] = Field(sa_column=Column(JSON))

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "John",
                "password": "pwd123!",
                "events": [],
            }
        }


class UserSignIn(SQLModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Jhon",
            }
        }
