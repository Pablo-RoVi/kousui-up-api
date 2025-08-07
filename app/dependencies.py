from typing import Generator
from app.db.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]