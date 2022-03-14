import pandas as pd
import requests
from datetime import datetime as dt
api_key = '6156f2d1c12e19.46412053'

def end_of_day_historical_stockdata(ticker, start_date, end_date, period):
    p = period[-2]
    url = f'https://eodhistoricaldata.com/api/eod/{ticker}?api_token={api_key}&from={start_date}&to={end_date}&fmt=json&period={p}'
    raw_df = requests.get(url).json()
    df = pd.DataFrame(raw_df).set_index('date')
    return df
