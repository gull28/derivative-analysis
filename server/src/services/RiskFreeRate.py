
class RiskFreeRate:
    def __init__(self, yahooClient) -> None:
        self.yahooClient = yahooClient
    
    def getShortTerm(self):
        return self.yahooClient.Ticker("^IRX")
    
    def getMidTerm(self):
        return self.yahooClient.Ticker("^FVX")
    
    def getLongTerm(self):
        return self.yahooClient.Ticker("^TNX")