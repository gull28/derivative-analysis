from sqlalchemy import Column, Integer, String, Boolean
from db.session import Base

class Ticker(Base):
    __tablename__ = 'tickers'

    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    keepTracking = Column(Boolean)