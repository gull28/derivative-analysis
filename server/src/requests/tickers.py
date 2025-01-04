from pydantic import BaseModel

class AddTickerRequest(BaseModel):
    ticker: str

class RemoveTickerRequest(BaseModel):
    id: int