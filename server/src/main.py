from fastapi import FastAPI
from db.session import Base, engine
from contextlib import asynccontextmanager
from services.YahooFinanceClient import YahooFinanceClient
import pandas as pd

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

yahooFinance = YahooFinanceClient("MSFT")

data = yahooFinance.fetch()
print(data.options)
for optionExpiry in data.options:
    for _, row in pd.DataFrame(data.option_chain(optionExpiry).calls).iterrows():
        contractSymbol, strike, bid, ask, change, percentChange, volume, openInterest, iv = row["contractSymbol"], row["strike"], row["bid"], row["ask"], row["change"], row["percentChange"], row["volume"], row["openInterest"],row["impliedVolatility"] 
        print(iv)

@app.get("/") 
def read_root(): return {"message": "Hello, World!"}





