from pydantic import EmailStr, BaseModel
from sqlmodel import SQLModel, JSON, Field, Column
from typing import Optional, List
from .events import Event


class User(SQLModel, table=True):
    """User테이블모델, SQLModel"""

    id: int = Field(
        title="사용자ID",
        description="사용자마다 부여되는 고유식별자, PK, 자동증가값",
        default=None,
        primary_key=True,
    )
    email: EmailStr = Field(title="이메일주소", description="이메일주소, EmailStr타입")
    password: str = Field(title="패스워드", description="암호, bcrypt로 해싱")
    events: Optional[List[Event]] = Field(
        sa_column=Column(JSON), title="이벤트", description="사용자별로 생성되는 이벤트 리스트"
    )

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "pwd123!",
            }
        }


class TokenResponse(BaseModel):
    """인증 성공 시 토큰발행에 사용되는 응답모델"""

    access_token: str = Field(title="토큰", description="인증 성공 시 클라이언트에 부여하는 JWT 액세스 토큰")
    token_type: str = Field(title="토큰타입", description="토큰의 유형, Bearer")


# 사용 안함
# class UserSignIn(SQLModel):
#     email: EmailStr
#     password: str

#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "fastapi@packt.com",
#                 "password": "Jhon",
#             }
#         }
