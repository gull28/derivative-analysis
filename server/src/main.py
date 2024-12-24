from fastapi import FastAPI
from db.session import Base, engine
from contextlib import asynccontextmanager
from services.YahooFinanceClient import YahooFinanceClient
import pandas as pd
from db.session import get_db_session
import schedule
from cronjobs.GetData import fetchData
import datetime

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
    yield
    print("Shutting down...")

with get_db_session() as session:
    schedule.every(20).seconds.do(lambda: fetchData(ticker="MSFT"))

app = FastAPI(lifespan=lifespan)

yahooFinance = YahooFinanceClient("MSFT")

yahooFinance.fetch()

for optionExpiry in yahooFinance.options.options:
    calls_df = pd.DataFrame(yahooFinance.options.option_chain(optionExpiry).calls)

    required_columns = [
        "contractSymbol", "strike", "impliedVolatility", "openInterest", "lastPrice"
    ]
    if not all(col in calls_df.columns for col in required_columns):
        print(f"Missing required columns in data for expiry {optionExpiry}")
        continue

    for _, row in calls_df.iterrows():
        option = {
            "stock_id": None,
            "strikePrice": row["strike"],
            "expirationDate": datetime.strptime(optionExpiry, "%Y-%m-%d").date(),
            "timeToExpiry": (datetime.strptime(optionExpiry, "%Y-%m-%d") - datetime.now()).days / 365,
            "iv": row["impliedVolatility"],
            "riskFreeRate": None,
            "type": "call",
            "optionPrice": row["lastPrice"],
            "openInterest": row["openInterest"],
            "delta": None,
            "gamma": None,
            "positionSize": None
        }


@app.get("/") 
def read_root(): return {"message": "Hello, World!"}

@app.post("/add-ticker")
def post_ticker(): return {"message": "add ticker!"}




