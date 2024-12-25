from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.session import Base, engine
from services.YahooFinanceClient import YahooFinanceClient
import pandas as pd
from db.session import get_db_session
from datetime import datetime
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")

    task = asyncio.create_task(schedule_fetch_data())
    
    yield

    task.cancel()
    print("Shutting down...")


app = FastAPI(lifespan=lifespan)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


yahooFinance = YahooFinanceClient("MSFT")


async def fetch_data():
    print("here")
    with get_db_session() as session:
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
                print(option)
   


async def schedule_fetch_data():
    while True:
        await fetch_data()
        await asyncio.sleep(120)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/add-ticker")
def post_ticker():
    return {"message": "add ticker!"}
