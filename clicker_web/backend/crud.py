from sqlalchemy.orm import Session

from .models import User
from . import schema


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_telegram_id(db: Session, telegram_id: int):
    return db.query(User).filter(User.telegram_id == telegram_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schema.UserCreate):
    db_user = User(name=user.name, telegram_id=user.telegram_id, score=user.score)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user