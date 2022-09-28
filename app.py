from flask import Flask, render_template
from Lib.portfolio import Portfolio
import json

app = Flask(__name__)

@app.route('/test')
def index():
    a = Portfolio("test", 123)
    portfolios = [a]
    return render_template('index.html', portfolios=portfolios)

if __name__ == "__main__":
    
    app.run(port=12345, debug=True)
