import requests
import pandas as pd
import time
from signals import calculate_signal

def get_klines(symbol, interval="5m", limit=200, retries=3):
    for i in range(retries):
        try:
            url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
            resp = requests.get(url, timeout=10)
            data = resp.json()
            df = pd.DataFrame(data, columns=[
                "open_time","open","high","low","close","volume",
                "close_time","quote_asset_volume","trades",
                "taker_base","taker_quote","ignore"
            ])
            df[["open","high","low","close","volume"]] = df[["open","high","low","close","volume"]].astype(float)
            return df
        except Exception as e:
            print(symbol, "error:", e)
            time.sleep(5)
    return None

def scan_market(symbols):
    signals = []
    for symbol in symbols:
        df = get_klines(symbol)
        try:
            signal = calculate_signal(symbol, df)
            if signal:
                signals.append(signal)
            else:
                print(symbol, "-> Signal: None")
        except Exception as e:
            print(symbol, "error in calculate_signal:", e)
    return signals
