from flask import Flask, render_template
from markupsafe import escape

import json

from Lib.portfolio import Portfolio
from Lib.portfolioHandler import loadAllPortfolios, loadPortfolio

app = Flask(__name__)

@app.route('/')
def index():
    portfolios = loadAllPortfolios()
    return render_template('index.html', portfolios=portfolios)

@app.route('/portfolio/<portfolio>')
def portfolioOverview(portfolio):
    return render_template('portfolio.html', portfolio=loadPortfolio(portfolio+".json"))


# running my methods in the Portfolio class
def getStockTotal(portfolio, name):
    return portfolio.getStockTotal(name)
app.jinja_env.globals.update(getStockTotal=getStockTotal)


if __name__ == "__main__":
    
    app.run(port=12345, debug=True)
