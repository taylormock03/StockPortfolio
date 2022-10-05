import numpy as np
import pandas as pd

import yfinance as yf

# Checks if the code is real
def checkCode(code):
    data = yf.download(tickers=code, period='5m', interval='5m')

    return len(data)>0

# This will calculate the price to buy or sell a stock
def getPrice(code):
    data = yf.download(tickers=code, period='5m', interval='15m')
    return round(data["Open"][0],2)

def getStockName(code):
    stock = yf.Ticker(code)

    return stock.info['longName'] 

