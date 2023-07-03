from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, Any, List
from pydantic import BaseSettings, BaseModel
from ..models.users import User
from ..models.events import Event
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(
            database=client.get_default_database(), document_models=[Event, User]
        )

    class Config:
        env_file = ".env"


class Database:
    def __init__(self, model):
        self.model = model

    # 레코드 생성
    async def save(self, document) -> None:
        await document.create()
        return

    # 단일 레코드 조회
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    # 전체 레코드 조회
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    # 레코드 변경
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    # 레코드 삭제
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
