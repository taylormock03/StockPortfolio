from flask import Flask, render_template, request, url_for, flash, redirect
from markupsafe import escape

import json

from Lib.portfolio import Portfolio
from Lib.portfolioHandler import *

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
            a = Portfolio(name, money)
            a.savePortfolio()
            return redirect(url_for('index'))

    return render_template('create.html')

# This will delete any portfolio
@app.route('/delete/<portfolio>')
def deletePortfolio(portfolio):
    os.remove('Portfolios/'+portfolio+'.json')
    return redirect(url_for('index'))

@app.route('/add/<portfolio>', methods = ('GET', 'POST'))
def addStock(portfolio):
    portfolio = loadPortfolio(portfolio + ".json")

    if request.method=="POST":
        stock = request.form['stock']
        qty = request.form['qty']

        if not stock:
            flash("A Stock Name is Required!")
        elif not qty:
            flash("Please Specify how many shares you wish to buy")
        elif not qty.isnumeric():
            flash('Quantity must be a number!')
        else:
            portfolio.addStock(stock, int(qty))
            return redirect(url_for('portfolioOverview', portfolio=portfolio.name))


    return render_template('addStock.html', portfolio=portfolio)


# running my methods in the Portfolio class
def getStockTotal(stock):

    return stock.getStockTotal()


app.jinja_env.globals.update(getStockTotal=getStockTotal)










if __name__ == "__main__":    
    app.run(port=12345, debug=True)