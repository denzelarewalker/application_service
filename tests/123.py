import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from application.main import app  # Импортируйте ваше FastAPI приложение
from application.database import AsyncSessionLocal
from application import models, schemas

# Создание тестового клиента
@pytest.fixture(scope="module")
def test_app():
    app.dependency_overrides[AsyncSessionLocal] = AsyncSessionLocal
    with TestClient(app) as client:
        yield client

# Создание тестовой базы данных
@pytest.fixture(scope="module")
async def test_db():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Создание таблиц
            await models.Base.metadata.create_all(bind=session.get_bind())
        yield session
        async with session.begin():
            # Удаление таблиц
            await models.Base.metadata.drop_all(bind=session.get_bind())

# Тест на создание заявки
@pytest.mark.asyncio
async def test_create_application(test_app, test_db):
    application_data = {
        "user_name": "test_user",
        "description": "Test description"
    }
    response = test_app.post("/applications", json=application_data)
    
    assert response.status_code == 200
    assert response.json()["user_name"] == application_data["user_name"]
    assert response.json()["description"] == application_data["description"]

# Тест на чтение заявок
@pytest.mark.asyncio
async def test_read_applications(test_app, test_db):
    # Создаем заявку для теста
    application_data = {
        "user_name": "test_user",
        "description": "Test description"
    }
    test_app.post("/applications", json=application_data)

    response = test_app.get("/applications", params={"user_name": "test_user", "page": 1, "size": 10})
    
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["user_name"] == application_data["user_name"]