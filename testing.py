import requests
try:
    r = requests.get("http://127.0.0.1:5000/grab-data/AAPL/2010-01-10/2015-02-19")
    r.json()
except Exception as e:
    print(e)

print(r.content)