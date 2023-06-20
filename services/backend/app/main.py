from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db.models import ModelName, User
from .db.session import db_engine, get_db
from .db.crud import get_user

# from .todo import todo_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/dbtest")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        # 데이터베이스 연결 테스트 쿼리 실행
        with db_engine.connect() as conn:
            conn.execute(f"SELECT * FROM zoo")
        return {"message": "Database connection successful"}
    except Exception as e:
        return {"message": f"Database connection error: {str(e)}"}


@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"msg": "root"}


@app.get("/user")
def route_get_user():
    get_user(get_db(), 1)


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# app.include_router(todo_router)
