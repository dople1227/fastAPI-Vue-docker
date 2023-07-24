from typing import Optional
from sqlmodel import SQLModel, Session, create_engine
from pydantic import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import pdb

DB_ROOT_PATH = str(Path(__file__).resolve().parents[4])
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)


class Settings(BaseSettings):
    """환경변수 관리 클래스"""
    
    DATABASE_CONNECTION_STRING: str = None
    SECRET_KEY: Optional[str] = None

    def initialize_database(self):
        connect_args = {"check_same_thread": False}
        return create_engine(
            self.DATABASE_CONNECTION_STRING, echo=True, connect_args=connect_args
        )

    class Config:
        env_file = ".env"


settings = Settings()
engine_url = settings.initialize_database()


def conn():
    """create_all()실행. DB 및 테이블 스키마 생성"""
    SQLModel.metadata.create_all(engine_url)


def get_session():
    """세션 관리"""
    with Session(engine_url) as session:
        yield session
