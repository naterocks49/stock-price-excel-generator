import pandas as pd
import json
import openpyxl
import re
import requests

def grab_date_master_df():
    new_request = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=COKE&outputsize=full&apikey=32FQZDW0NBL5E5XO")
    new_request = new_request.json()
    new_request = new_request["Time Series (Daily)"]

    master_list = []

    i = 0
    for time in new_request:
        master_list.append(time)
    master_list.reverse()

    for i, date in enumerate(master_list):
        master_list[i] = re.sub("[^0-9]", "", date)

    master_date_df = pd.DataFrame({'date': master_list})



    return master_date_df

def JSON_to_EXCEL(json_data):

    master_date_df = grab_date_master_df()

    df = pd.DataFrame(json_data)
    

    df.reset_index(inplace=True)
    df.rename(columns={'index':'date'}, inplace=True)

    df = pd.merge(master_date_df, df, on="date", how="outer")
    return df.to_excel('data.xlsx', engine='openpyxl', index=False)

def clean_t_arr(ticker_string):

    return re.findall(r'[A-Za-z]+', ticker_string)