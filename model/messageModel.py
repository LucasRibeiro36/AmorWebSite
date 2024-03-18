from .baseModel import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from datetime import datetime


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    autor = Column(String(100), nullable=False)
    to = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now())
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    extra = Column(Text, nullable=True)
    category = Column(String(100), nullable=True)
    isSubmited = Column(Boolean, nullable=False, default=False)