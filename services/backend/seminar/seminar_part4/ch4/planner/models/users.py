from typing import Optional, List
from beanie import Document
from pydantic import BaseModel, EmailStr
from .events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "jhlee@yescnc.co.kr",
                "username": "juno",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
