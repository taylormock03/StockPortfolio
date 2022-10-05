from flask import Flask, render_template, request, url_for, flash, redirect
from markupsafe import escape

import json

from Lib.portfolio import Portfolio
from Lib.portfolioHandler import *
from Lib.stockDataScraper import *

app = Flask(__name__)
with open('secretKey', 'r') as key:
    app.config["SECRET_KEY"] = key.readline()

# Pages

# Home page
@app.route('/')
def index():
    portfolios = loadAllPortfolios()
    return render_template('index.html', portfolios=portfolios)

# This shows an overview of your portfolio
@app.route('/portfolio/<portfolio>')
def portfolioOverview(portfolio):
    return render_template('portfolio.html', portfolio=loadPortfolio(portfolio+".json"))

# This allows you to create a new portfolio
@app.route('/create/', methods = ('GET', 'POST'))
def create():
    if request.method=="POST":
        name = request.form['name']
        money = request.form['money']

        if not name:
            flash("A Name is Required!")
        elif name in getPortfolioNames():
            flash("A portfolio already has that name!")
        elif not money:
            flash("A starting amount of money is required!")
        elif not money.isnumeric():
            flash('Money must be a number!')
        else:
            a = Portfolio(name, int(money))
            a.savePortfolio()
            return redirect(url_for('index'))

    return render_template('create.html')

# This will delete any portfolio
@app.route('/delete/<portfolio>')
def deletePortfolio(portfolio):
    os.remove('Portfolios/'+portfolio+'.json')
    return redirect(url_for('index'))

# This page will get the code of the stock we are adding
@app.route('/add/<portfolio>', methods = ('GET', 'POST'))
def addStockCode(portfolio):
    portfolio = loadPortfolio(portfolio + ".json")

    if request.method=="POST":
        code = request.form['stock']

        if not code:
            flash("A Stock Name is Required!")
        
        elif not checkCode(code):
            flash("No Stocks were found with that code")
        else:
            return redirect(url_for('addStockQty', portfolio=portfolio.name, code=code))


    return render_template('stockCode.html', portfolio=portfolio)

# If the previous function found a stock with matching code, 
@app.route('/add/<portfolio>/<code>', methods = ('GET', 'POST'))
def addStockQty(portfolio, code):
    portfolio = loadPortfolio(portfolio + ".json")
    price = getPrice(code)
    name = getStockName(code)

    if request.method=="POST":
        
        qty = request.form['qty']

        if not qty:
            flash("Please Specify how many shares you wish to buy")

        elif not qty.isnumeric():
            flash('Quantity must be a full number greater than 0!')
            
        elif (price * int(qty)) > int(portfolio.money):
            flash('You do not have enough money to purchase this stock!')
        
        else:
            qty = int(qty)
            portfolio.addStock(name, code, qty, price)
            return redirect(url_for('portfolioOverview', portfolio=portfolio.name))


    return render_template('stockQty.html', portfolio=portfolio, name = name, price = price)


# running my methods in the Portfolio class
def getStockTotal(stock):

    return stock.getStockTotal()


app.jinja_env.globals.update(getStockTotal=getStockTotal)










if __name__ == "__main__":    
    app.run(port=12345, debug=True)