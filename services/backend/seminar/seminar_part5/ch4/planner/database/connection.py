from typing import Optional
from sqlmodel import SQLModel, Session, create_engine
from pydantic import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)


class Settings(BaseSettings):
    """환경변수 관리 클래스"""

    DATABSE_CONNECTION_STRING: str = None
    SECRET_KEY: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    settings.DATABSE_CONNECTION_STRING, echo=True, connect_args=connect_args
)


def conn():
    """create_all()실행. DB 및 테이블 스키마 생성"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """세션 관리"""
    with Session(engine_url) as session:
        yield session
