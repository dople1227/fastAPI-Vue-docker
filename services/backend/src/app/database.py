from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:jhlee1324@localhost:3306/soron"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
engine = None
SessionLocal = None


async def init_db(app: FastAPI):
    global engine, SessionLocal

    engine = await create_engine(
        user="root",
        password="jhlee1324",
        host="localhost",
        port=3306,
        db="soron",
        autocommit=False,
        maxsize=20,
    )
    SessionLocal = sessionmaker(engine, expire_on_commit=False)

    async def close_db(app: FastAPI):
        await engine.wait_closed()

    app.add_event_handler("startup", init_db)
    app.add_event_handler("shutdown", close_db)