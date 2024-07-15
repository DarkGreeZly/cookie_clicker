from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import schema, models, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

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

@app.get("/")
async def root():
    return {"message": "hello Fastapi cookie clicker backend"}


@app.post("/load_score")
async def load_score(telegram_id: str):
    pass

@app.post("/save_score")
async def save_score(data):
    print(data)

@app.post("/create_user", response_model=schema.User)
async def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_telegram_id(db, telegram_id=user.telegram_id)
    if not db_user:
        return crud.create_user(db=db, user=user)