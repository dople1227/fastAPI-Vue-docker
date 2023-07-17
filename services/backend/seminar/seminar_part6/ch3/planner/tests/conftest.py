import asyncio
import httpx
import pytest
import sys
from pathlib import Path
from sqlmodel import SQLModel, select, Session, or_

ROOT_PATH = str(Path(__file__).resolve().parents[2])
sys.path.append(ROOT_PATH)

from planner.main import app
from planner.models.events import Event
from planner.models.users import User
from planner.database.connection import get_session_test, Settings, conn


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABSE_CONNECTION_STRING = "sqlite:///planner.db"
    engine_url = test_settings.initialize_database()
    SQLModel.metadata.create_all(engine_url)


@pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client
        # 리소스 정리
        session = get_session_test()

        # 사용자 생성 테스트데이터 삭제
        sel_user = select(User).where(User.email == "test@test.com")
        sel_user_results = session.exec(sel_user).fetchall()
        for user in sel_user_results:
            session.delete(user)

        # 이벤트 생성 테스트데이터 삭제
        sel_event = select(Event).where(
            or_(Event.title == "테스트이벤트", Event.title == "업데이트된 테스트이벤트")
        )
        sel_event_results = session.exec(sel_event)
        for event in sel_event_results:
            session.delete(event)

        session.commit()
