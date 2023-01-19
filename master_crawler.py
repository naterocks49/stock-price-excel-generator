import requests
import json
import time

def grab_4_tickers():

    with open('ticker_end.json', 'r') as f:
        ticker_end = json.load(f)["ticker_end"]

    with open('ticker_lists.json', 'r') as f:
        file = json.load(f)
    main_list = file["main"]

    ticker_start_index = main_list.index(ticker_end) + 1
    i = ticker_start_index
    four_ticker_list = []
    while i < (ticker_start_index + 4):
        four_ticker_list.append(main_list[i])
        i+=1
    
    print(four_ticker_list)
        
    final_dict = {}
    

    for ticker in four_ticker_list:
        try:
            new_request = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize=full&apikey=32FQZDW0NBL5E5XO")
            new_request = new_request.json()
            new_request = new_request["Time Series (Daily)"]
        except:
            print(f'ERROR AT {ticker}')
            continue
        clean_request = {}

        for date in new_request:
            clean_request[date.replace("-", "")] = new_request[date]

        data_price_dict = {}

        for data in clean_request:

            data_price_dict[data] = clean_request[data]["5. adjusted close"]

        
        final_dict[ticker] = data_price_dict

    new_ticker_end = four_ticker_list[-1]
    dict_dump = {}
    dict_dump["ticker_end"] = new_ticker_end

    with open('ticker_end.json', 'w') as f:
        json.dump(dict_dump, f, indent=4)

        
    return final_dict





class crawlerInstance():

    def __init__(self):

        return None

    def run_crawler(self):
        count = 0

        while count < 100:

            temp = grab_4_tickers()

            with open("master_dict_main.json", "r") as f:
                master_dict = json.load(f)
            
            for ticker in temp:
                master_dict[ticker] = temp[ticker]
            
            with open("master_dict_main.json", "w") as f:
                master_dict = json.dump(master_dict, f, indent=4)

            count += 1
            time.sleep(58)
        
        return
