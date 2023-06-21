from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    phoneNumber: str
    is_active: bool = True
    is_superuser: bool = False
