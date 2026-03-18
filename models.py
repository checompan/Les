from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)
    phone = Column(String)

class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    age = Column(Integer)

class Walk(Base):
    __tablename__ = "walks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    location = Column(String)
    max_people = Column(Integer)

class Registration(Base):
    __tablename__ = "registrations"
    id = Column(Integer, primary_key=True)
    walk_id = Column(Integer)
    user_id = Column(Integer)
    participants = Column(String)
    status = Column(String)