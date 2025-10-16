from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)