from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from fastapi import Depends
from sqlalchemy.orm import Session

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./compliancehub.db"  # Use um banco SQLite para desenvolvimento

    class Config:
        env_file = ".env"

settings = Settings()

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()