from typing import Optional
from sqlmodel import SQLModel, Session, create_engine
from pydantic import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    database_connection_string, echo=True, connect_args=connect_args
)


class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None

    class Config:
        env_file = ".env"


def conn():
    SQLModel.metadata.create_all(engine_url)


def get_session():
    with Session(engine_url) as session:
        yield session
