from yahoo_fin import stock_info as si
import time
from datetime import datetime
from datetime import timedelta
import talib as ta
import pandas as pd

now = datetime.now()
stock_data = []
stock_ta = []

args = ["sma", "ema"]

while(True):
    if (now + timedelta(seconds=2)) <= datetime.now():
        now = datetime.now()
        data = round(si.get_live_price("aapl"), 2)
        stock_data.append(data)
        length = len(stock_data)
        if length>5:
            price = {'price': stock_data}
            df = pd.DataFrame(data=price)
            if "sma" in args:
                df["sma"] = ta.SMA(df["price"], timeperiod=5)
            if "ema" in args:
                df["ema"] = ta.EMA(df["price"], timeperiod=5)
            print(data, round(df.iloc[-1,1:], 2))
        else:
            print(data)
        