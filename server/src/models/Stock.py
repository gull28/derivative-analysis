from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from db.session import Base

class Stock(Base):
    def __init__(self):
        print()
