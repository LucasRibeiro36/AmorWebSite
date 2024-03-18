from .baseModel import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    isAdmin = Column(Boolean, default=False)