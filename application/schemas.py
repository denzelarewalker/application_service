from pydantic import BaseModel, conint
from datetime import datetime
from typing import Optional


class ApplicationCreate(BaseModel):
    user_name: str
    description: str


class Application(ApplicationCreate):
    id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ApplicationQueryParams(BaseModel):
    user_name: Optional[str] = None
    page: conint(ge=1) = 1  # Минимальное значение 1
    size: conint(ge=1, le=100) = 10  # Минимальное значение 1, максимальное 100