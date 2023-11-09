

from polygon import RESTClient
from demo import api_key
import pandas as pd
import requests
import glob

# create a RESTClient to access data from the API
client = RESTClient(api_key=api_key)

def get_aggregates(ticker: str, timespan: str):
    """
    Documentation goes here

    aggs = []
    for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_-"2023-01-01", to="2023-06-13", limit=5000):
        aggs.append(a)
    df = pd.DataFrame(aggs)
    df.to_csv("aggregates.csv")
    """


# get a list of all the stock market ticker
def get_tickers():
    url = "https://api.polygon.io/v3/reference/tickers"
    params = {
        "active" : True,
        "apiKey" : api_key
    }

    try:
        response = requests.get(url, params)
        data = response.json()["results"]
    except:
        ValueError("Error while fetching data from api")
    
    df = pd.DataFrame(data)
    # export as a csv file
    df.to_csv("tickers.csv")

    return df.head()

def get_tickers_symbols():
    df = pd.read_csv("tickers.csv")
    symbols = df.ticker

    return symbols

def get_ticker_details(ticker: str):
    """
    Returns a detailed information about a ticker and the company behind it
    
    ticker : A short sequence of string representing a company in the stock market
    """
print(get_tickers_symbols())


# mental note, these actions seem repititive, possible to create a class to minimize
# the redundant code

