from flask import Flask, make_response
from stock_pull import stockPull
from formulas import JSON_to_EXCEL
import re

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>App is live</p>"

@app.route("/grab-data/<tickers>/<startdate>/<enddate>/<datatype>", methods=['GET'])
def grab_data(tickers, startdate, enddate, datatype):

    tickers_array = re.findall(r'[A-Z]+', tickers)

    new_request = stockPull(tickers_array, startdate, enddate)
    try:
        new_request = new_request.generate_data_set()
    except Exception as e:
        return "ERROR"  

    if datatype == "JSON":
        return new_request
    elif datatype == "CSV":
        xlsm_request = JSON_to_EXCEL(new_request)

        with open('/home/ubuntu/helloworld/data.xlsx', 'rb') as f:
            file_bytes = f.read()

        response = make_response(file_bytes)
        response.headers.set('Content-Type', 'application/vnd.ms-excel.sheet.macroEnabled.12')
        response.headers.set('Content-Disposition', 'attachment', filename='/home/ubuntu/helloworld/data.xlsx')

        return response

@app.route("/grab-master", methods=['GET'])
def grab_master():

    return




def startAPI():
    if __name__ == "__main__":
        app.run()

  

startAPI()