from flask import Flask
from stock_pull import stockPull, stock_generator

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>App is live</p>"

@app.route("/grab-data/<tickers>/<startdate>/<enddate>", methods=['GET'])
def grab_data(tickers, startdate, enddate):

    tickers_array = tickers.split(",")

    new_request = stockPull(tickers_array, startdate, enddate)
    
    return new_request.generate_data_set()

def startAPI():
    if __name__ == "__main__":
        app.run()


startAPI()