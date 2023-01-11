import requests

# time_frame must be 
def stock_generator(ticker, time_start, time_end):

    date_price_dict = {}

    new_request = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=full&apikey=G4A2CU9PIX0WRDXH")
    new_request = new_request.json()
    new_request = new_request["Time Series (Daily)"]
    clean_request = {}

    for date in new_request:
        clean_request[date.replace("-", "")] = new_request[date]
    

    date_check = []

    for date in new_request:
        date_check.append(date.replace("-", ""))
        
    new_date_range = []

    for date in date_check:
        if (int(date) < int(time_end.replace("-", ""))) & (int(date) > int(time_start.replace("-", ""))):
            new_date_range.append(date)

    data_price_dict = {}

    for data in clean_request:

        if data in new_date_range:

            data_price_dict[data] = clean_request[data]["5. adjusted close"]

    final_dict = {}
    final_dict[ticker] = data_price_dict

    return final_dict



class stockPull():

    def __init__(self, ticker_array, time_start, time_end):
        self.ticker_array = ticker_array
        self.time_start = time_start
        self.time_end = time_end
        return None

    def generate_data_set(self):

        self.all_tickers_data = {}

        for ticker in self.ticker_array:
            one_ticker_data = stock_generator(ticker, self.time_start, self.time_end)
            self.all_tickers_data[ticker] = one_ticker_data[ticker]


        return self.all_tickers_data

