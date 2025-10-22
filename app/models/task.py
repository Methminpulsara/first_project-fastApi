from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base


class Tsst(Base):
    __table__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    completed = Column(Boolean, default=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
