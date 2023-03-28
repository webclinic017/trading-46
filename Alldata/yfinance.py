import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
import pandas as pd
import datetime
import json
from data import AllStockdata
import yfinance as yf
import matplotlib.pyplot as plt
import backtrader as bt
import time





tsmc =[]
for company in AllStockdata:
    if company["industry_category"] == "電子工業":
        tsmc.append(company["stock_id"])
try:
    for company in tsmc:
        try:
            data = yf.download(company, start="2015-01-01", end="2023-03-28")
            df = pd.DataFrame(data)
            df.to_csv('{}_data.csv'.format(company))
            print('success in {}'.format(company))
        except:
            print('error in {}'.format(company))
            pass
except:
    pass
