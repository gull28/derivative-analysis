from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from db.session import Base

class Option(Base):
    def __init__(self):
        print()
