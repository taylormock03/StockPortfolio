from datetime import date

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
        self.values[str(date.today())]= valueDict 
        
    
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

    # STUB PROGRAM - GIVE VALUES LATER
    def getStockTotal(self):
        totalQty = 0
        for purchase in self.values:
            print(purchase)
            totalQty += self.values[purchase]['qty']
        price = getPrice(self.code)
        return totalQty * price

    def addPurchase(self, qty, price = 0):
        try:
            self.values[str(date.today())]['qty'] +=qty
            
        except:
            self.values[str(date.today())] = {'qty': qty, 'price': price}
