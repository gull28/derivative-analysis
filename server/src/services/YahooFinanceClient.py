import yfinance as yf

class YahooFinanceClient:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.options = None
        self.stock = None
    
    def fetch(self):
        self.options = yf.Ticker(self.ticker)
        self.stock = yf.Ticker(self.ticker)

    def isValid(self) -> bool:
        try:
            print(self.stock.info)
            info = self.stock.info
            return 'currentPrice' in info and info['currentPrice'] is not None
        except Exception as e:
            print(f"Error fetching ticker info: {e}")
            return False