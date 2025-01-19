## Users Applicaions Service (FastAPI)

Используемые технологии:
* FastAPI
* PostgreSQL
* Kafka
* Docker

Для использования API:
* Установите на компьютер Docker-Desktop
* Скачайте архив с приложением и распакуйте его
* Используя командную строку перейдите в корень каталога, например: `cd C:\library_service_FastAPI-main`
* Запустите контейнеры с помощью: `docker compose up -d --build` (запросы адаптированы для использования их в ОС Windows)


[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - FastAPI's documentation

## Use Cases

| Метод  | Описание                                | Пример запроса                                                                                                                  |
|--------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| POST   | Добавление нового запроса                | `curl -X POST "http://127.0.0.1:8000/applications" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"user_name\": \"string\", \"description\": \"string\"}` |
| GET    | Получение списка запросов           | `curl http://127.0.0.1:8000/applications`                                                                                             |
| GET    | Получениесписка запросов с указанием номера страницы и количеством запросов         | `curl http://127.0.0.1:8000/applications?user_name=string&page=3&size=20`                 |


Для тестирования приложения:
* установите менеджер управления проектом poetry `pip install poetry`
* Установите зависимости проекта `poetry install`
* Воспользуйтесь командой `poetry run pytest tests/`