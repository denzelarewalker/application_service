from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime, timezone

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
