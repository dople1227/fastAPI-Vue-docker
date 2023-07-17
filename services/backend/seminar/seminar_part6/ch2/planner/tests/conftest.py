import asyncio
import httpx
import pytest
from fastapi import Depends
from sqlmodel import select

from ..main import app
from ..database import connection
from ..models.events import Event
from ..models.users import User

from ..database.connection import get_session


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db(session=Depends(get_session)):
    test_settings = connection.Settings()
    test_settings.DATABSE_CONNECTION_STRING = "sqlite:///test.db"
    test_settings.initialize_database()
    connection.conn()

    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # 리소스 정리
        statement = select(Event)
        result = session.exec(statement)
        session.delete(result)

        statement = select(User)
        result = session.exec(statement)
        session.delete(result)

        session.commit()
