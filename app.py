from flask import Flask, make_response
from stock_pull import stockPull, stock_generator
from formulas import JSON_to_EXCEL
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>App is live</p>"

@app.route("/grab-data/<tickers>/<startdate>/<enddate>/<datatype>", methods=['GET'])
def grab_data(tickers, startdate, enddate, datatype):

    tickers_array = tickers.split(",")

    new_request = stockPull(tickers_array, startdate, enddate)
    new_request = new_request.generate_data_set()

    if datatype == "JSON":
        return new_request
    elif datatype == "CSV":
        xlsm_request = JSON_to_EXCEL(new_request)

        with open('data.xlsx', 'rb') as f:
            file_bytes = f.read()

        response = make_response(file_bytes)
        response.headers.set('Content-Type', 'application/vnd.ms-excel.sheet.macroEnabled.12')
        response.headers.set('Content-Disposition', 'attachment', filename='data.xlsx')

        return response
        



def startAPI():
    if __name__ == "__main__":
        app.run()


startAPI()