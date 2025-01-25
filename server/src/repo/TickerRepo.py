from models.Ticker import Ticker


class TickerRepo:
    def __init__(self, session):
        self.session = session

    def fetchAllTickers(self):
        return self.session.query(Ticker).order_by(Ticker.ticker).all()
    
    def fetchAllTickersToTrack(self):
        return self.session.query(Ticker).filter(Ticker.keepTracking == True).all()

    def fetchById(self, tickerId):
        return self.session.query(Ticker).filter(Ticker.id == tickerId).first()

    def addTicker(self, ticker):
        self.session.add(ticker)
        self.session.commit()

    def toggleTrack(self, tickerId):
        ticker = self.fetchById(tickerId)
        
        if ticker is None:
            raise ValueError(f"Ticker with id {tickerId} not found")
        
        ticker.keepTracking = not ticker.keepTracking
        
        self.session.commit()
        
        return ticker