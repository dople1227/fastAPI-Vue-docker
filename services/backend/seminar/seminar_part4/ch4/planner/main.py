from fastapi import FastAPI
from .database.connection import Settings
from .routes.users import user_router
from .routes.events import event_router


app = FastAPI()
settings = Settings()

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()
