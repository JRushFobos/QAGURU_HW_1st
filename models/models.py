from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine("sqlite:///./users.db", echo=True)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    avatar = Column(String)


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    avatar: HttpUrl


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    avatar: HttpUrl


class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar: Optional[str] = None


class PaginatedResponse(BaseModel):
    total: int
    page: int
    size: int
    pages: int
    items: List[UserResponse]