from pydantic import BaseModel


class UserBase(BaseModel):
    telegram_id: str

class UserCreate(UserBase):
    score: int

class User(UserBase):
    id: int
    name: str
    telegram_id: str
    score: int

    class Config:
        orm_mode = True