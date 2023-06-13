from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ModelName(str, Enum):
    """독스트링 스타일

    첫줄에 요약된 설명을 작성하고 추가설명은 한줄 띄운 후 기입
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/ping")
def pong():
    return {"message": "Ping Pong!"}


@app.get("/")
def root():
    return {"message": "Hello, World!"}


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
