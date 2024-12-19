import yfinance as yf

class YahooFinanceClient:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.data = None
        
    
    def fetch(self):
        self.data = yf.Ticker(self.ticker)
        return self.data

        
    def get_option_chain(self, expiry_date: str):
        if not self.data:
            raise ValueError("Data has not been fetched. Call `fetch` first.")
        return self.data.option_chain(expiry_date)


    def print(self):
        print(self.data.options)

