from fastapi import APIRouter
from fastapi import FastAPI, APIRouter
import pandas as pd
from db.session import get_db_session
from datetime import datetime
import asyncio
from repo.TickerRepo import TickerRepo
from pydantic import BaseModel
from models.Ticker import Ticker
from fastapi import HTTPException
from services.YahooFinanceClient import YahooFinanceClient
from request.tickers import AddTickerRequest

router = APIRouter(
    prefix="/tickers",
    tags=["tickers"]
)

@router.get("")
def get_tickers():
    with get_db_session() as session:
        repo = TickerRepo(session=session)

        tickers = repo.fetchAllTickers()

        return {"tickers": tickers}



@router.post("")
def post_tickers(request: AddTickerRequest):
    yahooFinance = YahooFinanceClient(request.ticker)

    print("here123")
    yahooFinance.fetch()

    if not yahooFinance.isValid():
        raise HTTPException(status_code=404, detail="Ticker not found")

    print(request.ticker) 
    with get_db_session() as session:
        repo = TickerRepo(session=session)

        try:
            ticker = Ticker()
            ticker.ticker = request.ticker.upper()
            ticker.keepTracking = True
            repo.addTicker(ticker)

            newTickers = repo.fetchAllTickers()

            return {"message": "Good!!", "tickers": newTickers}
        except Exception:
            print("error")
            raise HTTPException(status_code=500, detail="An error occurred")


@router.put("/{ticker_id}/toggle")
def post_tickers(ticker_id: int):
    
    with get_db_session() as session:
        repo = TickerRepo(session=session)

        try:
            toggledTicker = repo.toggleTrack(ticker_id)

            return {"message": "Tracking toggled", "ticker": toggledTicker}
        except Exception:
            print("error")
            raise HTTPException(status_code=500, detail="An error occurred")


@router.delete("/{ticker_id}")
def delete_tickers(ticker_id: int):

    with get_db_session() as session:
        repo = TickerRepo(session=session)

        try:
            repo.deleteTicker(ticker_id)

            tickers = repo.fetchAllTickers()

            return {"message": "Ticker deleted", "tickers": tickers}
        except Exception:
            print("error")
            raise HTTPException(status_code=500, detail="An error occurred")
