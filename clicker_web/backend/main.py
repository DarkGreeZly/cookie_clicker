from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime, timedelta, timezone
from typing import Optional, List, Annotated
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .database import SessionLocal, SECRET_KEY, ALGORITHM
from . import models
from .schema import User, UserCreate, Token, TokenData




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="token")
db_dependency = Annotated[Session, Depends(get_db)] 

def get_current_user(db: db_dependency, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(user_name=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.user_name)
    if user is None:
        raise credentials_exception
    return user

user_dependency = Annotated[dict, Depends(get_current_user)]

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user(db, user_name: str):
    return db.query(models.User).filter(models.User.user_name == user_name).first()

def authenticate_user(db, user_name: str, password: str):
    user = get_user(db, user_name=user_name)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

@app.post("/register", response_model=Token)
async def register(user: UserCreate, db: db_dependency):
    db_user = get_user(db, user.user_name)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    hashed_password = get_password_hash(user.password)
    db_user = User(user_name= user.user_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = create_access_token(data={"sub": db_user.user_name})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/token", response_model=Token)
async def login_for_access_token(db: db_dependency, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.user_name, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token = create_access_token(data={"sub": user.user_name})
    return {"access token": access_token, "token_type": "bearer"}


@app.get("user/me", response_model= UserCreate)
async def read_users_me(current_user: user_dependency):
    return current_user

        