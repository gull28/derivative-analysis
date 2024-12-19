

class OptionParser:
    def __init__(self, option):
        self.option = option
    
    def parse(self):
        raise NotImplementedError

    def getDTExpiration(self):
        raise NotImplementedError
