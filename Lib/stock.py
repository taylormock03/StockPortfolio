from datetime import date, datetime

from Lib.stockDataScraper import getPrice


class Stock:
    code = ""
    fullName = ""

    values = {}

    def __init__(self, code, fullName, qty, price) -> None:
        self.code = code
        self.fullName = fullName

        self.values = {}
        valueDict = {}
        valueDict['qty'] = qty
        valueDict['price'] = price
        self.values[str(datetime.now())]= valueDict 
        
    
    def save(self):
        stockDict = {}
        stockDict['code'] = self.code
        stockDict['fullName'] = self.fullName
        stockDict["values"] = self.values
        return stockDict

    def load(self,dict):
        self.code = dict['code']
        self.fullName = dict['fullName']
        self.values = dict['values']

    def getStockTotal(self):
        totalQty = 0
        for purchase in self.values:
            print(purchase)
            totalQty += self.values[purchase]['qty']
        price = getPrice(self.code)
        return totalQty * price

    def addPurchase(self, qty, price):
        # If a purchase was already performed at the same time (very unlikely)
        try:
            self.values[str(datetime.now())]['qty'] +=qty
        # Adding a new log to the stock history
        except:
            self.values[str(datetime.now())] = {'qty': qty, 'price': price}

    def addSale(self, qty, price):
        # If a purchase was already performed at the same time (very unlikely)
        try:
            self.values[str(datetime.now())]['qty'] -=qty
        # Adding a new log to the stock history
        except:
            self.values[str(datetime.now())] = {'qty': -(qty), 'price': -(price)}

    def getStockQty(self):
        totalQty = 0
        for purchase in self.values:
            print(purchase)
            totalQty += self.values[purchase]['qty']
        return totalQty

