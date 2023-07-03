from pydantic import BaseModel, EmailStr
from typing import Optional, List
from .events import Event


class User(BaseModel):
    email: EmailStr
    username: str
    password: str
    events: Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "John",
                "password": "pwd123!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Jhon",
                "events": [],
            }
        }
