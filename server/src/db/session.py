from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from utils.config import Config
import os


config = Config()

engine = create_engine(config.db.getUrl(), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_database():
    from models.Ticker import Ticker  
    from models.Option import Option
    from models.Stock import Stock
    
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
