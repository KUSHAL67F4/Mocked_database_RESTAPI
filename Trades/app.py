from fastapi import FastAPI, Query
import uvicorn
from typing import List, Optional
import json
from datetime import datetime
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse


fsapi = FastAPI()

fsapi.mount("/static", StaticFiles(directory="static"), name="static")

#templates = Jinja2Templates(directory="templates")

trades_database = [
    {
        "id": 1,
        "counterparty": "Vishal Sharma",
        "instrumentId": "IKEA",
        "instrumentName": "IKEA",
        "trader": "John Snow",
        "assetClass": "Equity",
        "price": 1000.0,
        "tradeType": "Buy",
        "date": "25-05-2023",
    },
    {
        "id": 2,
        "counterparty": "Mithali Raj",
        "instrumentId": "HP",
        "instrumentName": "HP Inc.",
        "trader": "Bob Smith",
        "assetClass": "Equity",
        "price": 2500.0,
        "tradeType": "Sell",
        "date": "25-06-2023",
    },
    {
        "id": 3,
        "counterparty": "Karthik Rao",
        "instrumentId": "BMW",
        "instrumentName": "BMW",
        "trader": "Alice Smith",
        "assetClass": "Equity",
        "price": 5000.0,
        "tradeType": "Buy",
        "date": "27-05-2023",
    },
    {
        "id": 4,
        "counterparty": "Abel Tesfaya",
        "instrumentId": "HBO",
        "instrumentName": "HBO Inc.",
        "trader": "Mohith Chouhan",
        "assetClass": "Equity",
        "price": 8000.0,
        "tradeType": "Buy",
        "date": "26-05-2023",
    },
    {
        "id": 5,
        "counterparty": "Chris Shane",
        "instrumentId": "SMSG",
        "instrumentName": "SAMSUNG",
        "trader": "Chris pine",
        "assetClass": "Equity",
        "price": 2000.0,
        "tradeType": "Sell",
        "date": "28-05-2023",
    },
    {
        "id": 6,
        "counterparty": "Arjun Kumari",
        "instrumentId": "GGL",
        "instrumentName": "ALPHABET Inc.",
        "trader": "Ben Kingsley",
        "assetClass": "Equity",
        "price": 3500.0,
        "tradeType": "Buy",
        "date": "01-06-2023",
    },
    {
        "id": 7,
        "counterparty": "Rob Kingston",
        "instrumentId": "YMH",
        "instrumentName": "YAMAHA MOTOR Co.",
        "trader": "Mitsushi",
        "assetClass": "Equity",
        "price": 8000.0,
        "tradeType": "Buy",
        "date": "04-06-2023",
    },
    {
        "id": 8,
        "counterparty": "Ramesh Mahraj",
        "instrumentId": "AMZN",
        "instrumentName": "AMAZON Inc.",
        "trader": "Jeff Bezoz",
        "assetClass": "Equity",
        "price": 11000.0,
        "tradeType": "Sell",
        "date": "06-06-2023",
    },
    {
        "id": 9,
        "counterparty": "Enzo Ferrari",
        "instrumentId": "FRRI",
        "instrumentName": "FERRARI S.P.A",
        "trader": "Henry Ford",
        "assetClass": "Equity",
        "price": 7000.0,
        "tradeType": "Sell",
        "date": "28-05-2023",
    },
    {
        "id": 10,
        "counterparty": "Max Verstappen",
        "instrumentId": "REDBLL",
        "instrumentName": "RED BULL",
        "trader": "Lewis Hamilton",
        "assetClass": "Equity",
        "price": 9000.0,
        "tradeType": "Sell",
        "date": "31-05-2023",
    }
]

@fsapi.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=open("static/index.html", "r").read(), status_code=200)



@fsapi.get("/api/trades")
async def get_trades(
    assetClass: Optional[str] = Query(None, description="Filters trades by asset class"),
    endDate: Optional[str] = Query(None, description="Filters trades by end date"),
    maxPrice: Optional[float] = Query(None, description="Filters trades by maximum price"),
    minPrice: Optional[float] = Query(None, description="Filters trades by minimum price"),
    startDate: Optional[str] = Query(None, description="Filters trades by start date"),
    tradeType: Optional[str] = Query(None, description="Filters trades by trade type")
):
    filtered_trades = trades_database

    if assetClass:
        filtered_trades = [trade for trade in filtered_trades if trade.get("assetClass") == assetClass]

    if startDate:
        start_date = datetime.strptime(startDate, "%Y-%m-%d")
        filtered_trades = [trade for trade in filtered_trades if datetime.strptime(trade.get("date"), "%d-%m-%Y") >= start_date]

    if endDate:
        end_date = datetime.strptime(endDate, "%Y-%m-%d")
        filtered_trades = [trade for trade in filtered_trades if datetime.strptime(trade.get("date"), "%d-%m-%Y") <= end_date]

    if maxPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.get("price") <= maxPrice]

    if minPrice:
        filtered_trades = [trade for trade in filtered_trades if trade.get("price") >= minPrice]

    if tradeType:
        filtered_trades = [trade for trade in filtered_trades if trade.get("tradeType") == tradeType]

    return filtered_trades

@fsapi.get("/api/all-trades")
async def get_all_trades():
    return trades_database




@fsapi.get("/trades/{trade_id}", response_model=dict)
async def get_trades_id(trade_id: int):
    for trade in trades_database:
        if trade["id"] == trade_id:
            return trade

    return {"error": "Trade not found"}


if __name__ == "__main__":
    uvicorn.run(fsapi, host="127.0.0.1", port=8000)
