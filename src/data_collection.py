import requests
import csv
import pandas as pd
from datetime import datetime
import os

PROJECT_PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PROJECT_PATH, "data", "ETH_data.csv")

def market_fetcher(coin_id, days=30):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }
    response = requests.get(url, params=params)
    return response.json()

def csv_saver(data, filename="market_data.csv"):
    rows = []
    for i in range(len(data.get("prices", []))):
        timestamp = datetime.utcfromtimestamp(data["prices"][i][0] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        price = data["prices"][i][1]
        volume = data["total_volumes"][i][1] if "total_volumes" in data else None
        rows.append([timestamp, price, volume])
    
    df = pd.DataFrame(rows, columns=["timestamp", "price", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.set_index("timestamp", inplace=True)
    df["returns"] = df["price"].pct_change()
    df["volatility"] = df["returns"].rolling(window=10).std()
    df["moving_avg_10"] = df["price"].rolling(window=10).mean()
    df["moving_avg_50"] = df["price"].rolling(window=50).mean()
    df.dropna(inplace=True)
    df.to_csv(filename)
    print(f"Market data with features saved to {filename}")

eth_data = market_fetcher("ethereum")
csv_saver(eth_data, DATA_PATH)
