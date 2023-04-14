#%%
import pyfolio as pf
import pandas as pd
import yfinance as yf
import datetime
import os

data = yf.download('2330.TW', start="2015-01-01", end="2023-03-28")
df = pd.DataFrame(data)
pf.create_returns_tear_sheet(df['Close'].pct_change().dropna())

#%%
