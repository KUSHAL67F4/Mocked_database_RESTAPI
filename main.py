from fastapi import FastAPI, Query
from typing import List, Optional

fsapi = FastAPI()

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
    },
]


@fsapi.get("/trades", response_model=List[dict])
async def get_trades(
    assetClass: Optional[str] = Query(
        None, description="Filters trades by asset class"
    ),
    endDate: Optional[str] = Query(
        None, description="Filters trades by end date"
    ),
    maxPrice: Optional[float] = Query(
        None, description="Filters trades by maximum price"
    ),
    minPrice: Optional[float] = Query(
        None, description="Filters trades by minimum price"
    ),
    startDate: Optional[str] = Query(
        None, description="Filters trades by start date"
    ),
    tradeType: Optional[str] = Query(
        None, description="Filters trades by trade type"
    )
):

    filtered_trades = trades_database
    if assetClass:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("assetClass") == assetClass:  
                filtered_trades.append(trade)

    if startDate:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("date") >= startDate:  
                filtered_trades.append(trade)
                

    if endDate:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("date") <= endDate:  
                filtered_trades.append(trade)
                

    if maxPrice:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("price") <= maxPrice:  
                filtered_trades.append(trade)
                

    if minPrice:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("price") >= minPrice:  
                filtered_trades.append(trade)

    
    '''if tradeDate:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("date") == tradeDate:  
                filtered_trades.append(trade) '''

    if tradeType:
        filtered_trades=[]
        for trade in filtered_trades:  
            if trade.get("tradeType") == tradeType:  
                filtered_trades.append(trade)

    return filtered_trades


@fsapi.get("/trades/{trade_id}", response_model=dict)

async def get_trades_id(trade_id: int):
    trade = None  
    for trade in trades_database:  
        if trade["id"] == trade_id:  
            trade = trade  
            break
        else:
            trade = None  

    if trade:
        return trade
    return {"error": "Trade not found"}
