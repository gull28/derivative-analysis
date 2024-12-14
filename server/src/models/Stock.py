from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Float
from db.session import Base

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    ticker = Column(String)
    underlyingPrice = Column(Float)
    marketCap = Column(Float)

