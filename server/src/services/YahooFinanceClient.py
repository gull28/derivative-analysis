import yfinance as yf

class YahooFinanceClient:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.options = None
        self.stock = None
    
    def fetch(self):
        self.options = yf.Ticker(self.ticker)
        self.stock = yf.Ticker(self.ticker)
