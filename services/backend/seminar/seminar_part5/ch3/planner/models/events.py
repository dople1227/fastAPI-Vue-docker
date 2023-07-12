from pydantic import BaseModel
from sqlmodel import SQLModel, JSON, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    """Event테이블, SQLModel"""

    id: int = Field(
        title="이벤트ID",
        description="PK,자동증가값,이벤트마다 부여되는 고유식별자",
        default=None,
        primary_key=True,
    )
    title: str = Field(title="이벤트명", description="이벤트의 타이틀")
    image: str = Field(title="이미지경로", description="이벤트 이미지 배너의 링크")
    description: str = Field(title="설명", description="이벤트에 대한 설명")
    tags: List[str] = Field(
        title="이벤트 태그", description="그룹화를 위한 이벤트 태그", sa_column=Column(JSON)
    )
    location: str = Field(title="이벤트위치", description="이벤트 위치")

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "이벤트 타이틀 example",
                "image": "http://이미지경로/image.png example",
                "description": "이벤트에 대한 설명 example",
                "location": "이벤트 위치 example",
                "tags": ["태그 example 1", "태그 example 2", "태그 example 3"],
            }
        }


class EventUpdate(BaseModel):
    """이벤트 업데이트시에 사용하는 요청검증모델"""

    title: Optional[str] = Field(title="이벤트명", description="이벤트명")
    image: Optional[str] = Field(title="이미지경로", description="이벤트 이미지 배너의 링크")
    description: Optional[str] = Field(title="설명", description="이벤트에 대한 설명")
    tags: Optional[List[str]] = Field(title="이벤트 태그", description="그룹화를 위한 이벤트 태그")
    location: Optional[str] = Field(title="이벤트위치", description="이벤트 위치")

    class Config:
        schema_extra = {
            "example": {
                "title": "이벤트 타이틀 example",
                "image": "http://이미지경로/image.png example",
                "description": "이벤트에 대한 설명 example",
                "location": "이벤트 위치 example",
                "tags": ["태그 example 1", "태그 example 2", "태그 example 3"],
            }
        }
