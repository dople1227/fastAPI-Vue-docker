from fastapi import FastAPI
from .routes.users import user_router
from .routes.events import event_router
import uvicorn
from .database.connection import conn


app = FastAPI()


@app.on_event("startup")
def on_startup():
    conn()


app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
