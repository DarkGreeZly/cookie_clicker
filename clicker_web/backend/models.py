from sqlalchemy import Column, String, Integer, Boolean

from config import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    score = Column(Integer, default=0)
    disabled = Column(Boolean, default=True)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.hashed_password, "score": self.score, "disabled": self.disabled}

Base.metadata.create_all(bind=engine)
