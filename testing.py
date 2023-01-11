import requests

r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=G4A2CU9PIX0WRDXH")
print (r.json()[0])