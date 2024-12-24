from models.Ticker import Ticker


class TickerRepo:
    def __init__(self, session):
        self.session = session

    def fetchAllTickers(self):
        return self.session.query(Ticker).all()
    
    def fetchAllTickersToTrack(self):
        return self.session.query(Ticker).filter(Ticker.keepTracking == True).all()

    def fetchById(self, tickerId):
        return self.session.query(Ticker).filter(Ticker.id == tickerId).first()

    def addTicker(self, ticker):
        self.session.add(ticker)
        self.session.commit()