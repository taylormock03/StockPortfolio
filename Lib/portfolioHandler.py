import os

from Lib.portfolio import Portfolio

def loadAllPortfolios():
    portfolios = []
    for x in os.listdir('Portfolios/'):
        portfolios.append(loadPortfolio(x))

    return portfolios

def loadPortfolio(x):
    a = Portfolio("",0)
    a.loadPortfolio(x)
    return a
    