import json

class Portfolio:
    name = ""
    money = 0
    stocks = {}

    def __init__(self, name, money) -> None:
        self.name = name
        self.money = money
        self.stocks = {}
        return


    # Grab an existing portfolio from the portfolios folder
    def loadPortfolio(self,name):
        try:
            with open("Portfolios/" + name + ".json", 'r') as x:
                dict = json.load(x)

                self.name = dict["name"]
                self.money = dict['money']
                self.stocks = dict['stocks']
            return True
        except:
            return False

    # Save an existing portfolio to the portfolios folder
    def savePortfolio(self):
        try:
            with open("Portfolios/" + self.name + ".json", 'w') as x:
                dict = {}
                dict['name'] = self.name
                dict['money'] = self.money
                dict['stocks'] = self.stocks
                json.dump(dict, x)
                
            return True
        except:
            return False