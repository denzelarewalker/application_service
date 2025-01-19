from fastapi import FastAPI
from .routes import router
from .database import engine, Base


app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        # Используем MetaData для создания всех таблиц
        await conn.run_sync(Base.metadata.create_all)
    pass  # Здесь можно добавить код инициализации, если потребуется


@app.on_event("shutdown")
async def shutdown_event():
    pass  # Здесь можно добавить код завершения работы, если потребуется
