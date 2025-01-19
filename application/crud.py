from sqlalchemy.future import select
from . import models, schemas
from .kafka_publisher import send_application
from datetime import datetime, timezone


async def new_application(db, application):
    db_application = models.Application(
        user_name=application.user_name,
        description=application.description,
        created_at=datetime.now(timezone.utc),
    )
    db.add(db_application)
    await db.commit()
    await db.refresh(db_application)

    # Публикация в Kafka
    app_data = schemas.Application.from_orm(
        db_application
    )  # Преобразование в Pydantic-схему
    await send_application(app_data)

    return db_application

async def get_applications(db, query_params):
    user_name = query_params.user_name
    page = query_params.page
    size = query_params.size
    query = select(models.Application)
    if user_name:
        query = query.filter(models.Application.user_name == user_name)

    query = query.offset((page - 1) * size).limit(size)
    result = await db.execute(query)

    applications = result.scalars().all()
    return applications