from services.YahooFinanceClient import YahooFinanceClient


def fetchData(ticker: str):
    print("fetching data")
    data = YahooFinanceClient(ticker).fetch()
    
    