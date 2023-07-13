from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.users import user_router
from .routes.events import event_router
from .database.connection import conn, Settings

app = FastAPI()

# CORS미들웨어설정
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headears=["*"],
)


@app.on_event("startup")
def on_startup():
    conn()


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
