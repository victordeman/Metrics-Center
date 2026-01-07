from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from .main import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_background_tasks():
    return BackgroundTasks()

from .utils.auth import get_current_user
