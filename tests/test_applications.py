import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from application.main import app  # Импортируйте ваше приложение
from application.schemas import ApplicationCreate, Application
import pytest_asyncio
client = TestClient(app)


@pytest_asyncio.fixture
async def mock_db(mocker):
    # Создаем мок для базы данных
    mock_session = AsyncMock()
    # Мокируем контекстный менеджер для базы данных
    mock_session.__aenter__.return_value = mock_session
    mock_session.__aexit__.return_value = None
    mocker.patch('application.routes.AsyncSessionLocal', return_value=mock_session)
    return mock_session

@pytest.mark.asyncio
async def test_create_application(mocker, mock_db):
    # Данные для теста
    application_data = ApplicationCreate(user_name="test_user", description="Test description")
    
    # Мокируем метод new_application
    mock_new_application = mocker.patch('application.routes.new_application', new_callable=AsyncMock)
    mock_new_application.return_value = Application(id=1, **application_data.dict())  # Возвращаем созданное приложение

    # Выполняем запрос на создание приложения
    response = client.post("/applications", json=application_data.dict())

    # Проверяем ответ
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["user_name"] == application_data.user_name
    assert response_data["description"] == application_data.description
    assert response_data["id"] == 1  # Проверяем, что ID возвращается правильно

    # Проверяем, что new_application был вызван с правильными параметрами
    mock_new_application.assert_called_once_with(mock_db, application_data)

@pytest.mark.asyncio
async def test_read_applications(mocker):
    mocker.patch("application.routes.get_applications", 
                 return_value=[{"user_name": "test_user", 
                                "description": "Test description",
                                "id": 1, 
                                "created_at": "2025-01-18T15:25:47.264241"}])


    # Выполняем запрос на чтение приложений
    response = client.get("/applications?page=1&size=10")


    assert response.status_code == 200
    assert response.json() == [{"user_name": "test_user", 
                                "description": "Test description", 
                                "id": 1, 
                                "created_at": "2025-01-18T15:25:47.264241"}]
