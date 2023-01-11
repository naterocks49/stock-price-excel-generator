from flask import Flask
from stock_pull import stockPull, stock_generator

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>App is live</p>"

@app.route("/grab-data/<tickers>/<startdate>/<enddate>", methods=['GET'])
def grab_data(tickers, startdate, enddate):

    return stock_generator(tickers,startdate,enddate)

def startAPI():
    if __name__ == "__main__":
        app.run()


startAPI()