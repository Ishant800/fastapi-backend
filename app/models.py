from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,autoincrement=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    age = Column(Integer)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer,primary_key=True,autoincrement=True,unique=True,nullable=False)
    bookname = Column(String(100),nullable=False)
    title =  Column(String(100))
    author = Column(String(100),nullable=False)
    isbn = Column(Integer,nullable=False)