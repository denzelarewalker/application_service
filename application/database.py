from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)


DATABASE_URL = "postgresql+asyncpg://user:password@db/postgres"


engine = create_async_engine(DATABASE_URL, echo=True, future=True)


AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()