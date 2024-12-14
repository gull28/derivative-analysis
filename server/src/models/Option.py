from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Float
from db.session import Base

class Option(Base):
    __tablename__ = 'options'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stocks.id'), nullable=False)
    strikePrice = Column(Float)
    expirationDate = Column(Date)
    timeToExpiry = Column(Float)
    iv = Column(Float)
    riskFreeRate = Column(Float)
    type = Column(String)
    optionPrice = Column(Float)
    openInterest = Column(Integer)
    delta = Column(Float)
    gamma = Column(Float)
    positionSize = Column(Float)
