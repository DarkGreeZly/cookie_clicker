from sqlalchemy import Column, String, Integer

from .database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    hashed_password = Column(String)
    score = Column(Integer, default=0)


Base.metadata.create_all(bind=engine)