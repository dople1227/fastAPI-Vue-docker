from fastapi import FastAPI
from .routes.users import user_router
from .routes.events import event_router

app = FastAPI()

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
