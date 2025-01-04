from models.Stock import Stock

class StockRepo:
    def __init__(self, session):
        self.session = session

    def fetchAllTickers(self):
        return self.session.query(Stock).all()

    def fetchById(self, stockId):
        return self.session.query(Stock).filter(Stock.id == stockId).first()

    def addStock(self, stock):
        self.session.add(stock)
        self.session.commit()