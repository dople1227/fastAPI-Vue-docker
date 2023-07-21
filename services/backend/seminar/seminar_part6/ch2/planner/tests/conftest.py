import asyncio
import httpx
import pytest
import sys
from pathlib import Path
from fastapi import Depends
from sqlmodel import select

ROOT_PATH = str(Path(__file__).resolve().parents[2])
sys.path.append(ROOT_PATH)

from planner.main import app
from planner.database import connection
from planner.models.events import Event
from planner.models.users import User
from planner.database.connection import get_session_test


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db(session=Depends(get_session_test)):
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