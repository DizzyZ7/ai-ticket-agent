from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    message = Column(Text)
    category = Column(String)
    priority = Column(String)
    reply = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
