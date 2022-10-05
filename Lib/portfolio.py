import json

from Lib.stock import Stock

class Portfolio:
    name = ""
    money = 0
    stocks = []

    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money
        self.stocks = []
        return


    # Grab an existing portfolio from the portfolios folder
    def loadPortfolio(self,name):

        with open("Portfolios/" + name, 'r') as x:
            dict = json.load(x)
            self.name = dict["name"]
            self.money = dict['money']
            self.stocks = self.loadStocks(dict['stocks'])



    def loadStocks(self,dictList):
        stocks = []
        for stockData in dictList:
            a = Stock("","",0,0)
            a.load(stockData)
            stocks.append(a)
        return stocks

    # Save an existing portfolio to the portfolios folder
    def savePortfolio(self):
        try:
            with open("Portfolios/" + self.name + ".json", 'w') as x:
                dict = {}
                dict['name'] = self.name
                dict['money'] = self.money
                dict['stocks'] = self.saveStocks()
                json.dump(dict, x)
                
            return True
        except:
            return False

    def saveStocks(self):
        stockList= []
        for stock in self.stocks:
            stockList.append(stock.save())

        return stockList

    def addStock(self, stockName, stockCode, qty, price):
        # remove the cost of the stock from money
        self.money -= price*qty

        # check if a stock already exists in portfolio
        for stock in self.stocks:
            if stock.fullName == stockName:
                stock.addPurchase(qty)
                self.savePortfolio()
                return
        # if it doesn't add it here
        print('empty')
        self.stocks.append(Stock(stockCode, stockName, qty, price))
        self.savePortfolio()

