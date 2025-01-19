# Users Applicaions FastAPI

Для использования API:
* Установите на компьютер Docker-Desktop
* Скачайте архив с приложением и распакуйте его
* Используя командную строку перейдите в корень каталога, например: `cd C:\library_service_FastAPI-main`
* Запустите контейнеры с помощью: `docker compose up -d --build` (запросы адаптированы для использования их в ОС Windows)

Пример POST запроса:
`curl -X POST "http://127.0.0.1:8000/applications" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"user_name\": \"string\", \"description\": \"string\"}`

Пример GET запроса:
`http://127.0.0.1:8000/applications?page=1&size=10`

Для тестирования приложения:
* установите менеджер управления проектом poetry `pip install poetry`
* Установите зависимости проекта `poetry install`
* Воспользуйтесь командой `poetry run pytest tests/`