import yfinance as yf
import pandas as pd
import os

def fetch_live_data(ticker_symbol):

    ticker = yf.Ticker(ticker_symbol)  # this will create a ticker object for the given ticker symbol
    if not ticker.info:
        raise ValueError(f"Ticker {ticker_symbol} not found or no data available.")
    
    live_data = ticker.history(period='1d',interval='5m')  # this will fetch the live data for the ticker in 5 minute intervals, meaning it will fetch the data for the last 1 day

    if live_data.empty:
        raise ValueError(f"No data found for ticker: {ticker_symbol}")
    
    live_data.reset_index(inplace=True) # this will convert the index to a column
    live_data['Datetime'] = live_data['Datetime'].dt.strftime('%Y-%m-%d %H:%M:%S') # this will format the date
    
    os.makedirs('./data', exist_ok=True) 
    live_data.to_csv(f'./data/{ticker_symbol}_live_data.csv', index=False) # this will save the data to a csv file
   
    return live_data 