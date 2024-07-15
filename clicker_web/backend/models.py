from sqlalchemy import Column, String, Integer

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    telegram_id = Column(String)
    score = Column(Integer, default=0)