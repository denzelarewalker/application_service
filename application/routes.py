from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from application import schemas
from .database import AsyncSessionLocal
from .crud import get_applications, new_application

router = APIRouter()


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()  # Здесь нужно использовать await


@router.post("/applications", response_model=schemas.Application)
async def create_application(
    application: schemas.ApplicationCreate, db: Session = Depends(get_db)
):
    result = await new_application(db, application)
    return result

@router.get("/applications", response_model=List[schemas.Application])
async def read_applications(
    query_params: schemas.ApplicationQueryParams = Depends(),
    db: Session = Depends(get_db),
):
    result = await get_applications(db, query_params)
    return result