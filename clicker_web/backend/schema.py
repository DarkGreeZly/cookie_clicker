from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    user_name: str
    password: str

class UserInDB(UserCreate):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_name: Optional[str] = None