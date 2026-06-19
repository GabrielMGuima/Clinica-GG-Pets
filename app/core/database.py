import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Lê o host do ambiente, se não achar, usa 'localhost' para rodar fora do Docker
DB_HOST = os.getenv("DB_HOST", "localhost")
DATABASE_URL = f"postgresql://usuario:senha@{DB_HOST}:5432/clinica_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()