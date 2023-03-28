import requests
import pandas as pd
import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
import requests
import pandas as pd
import datetime
import json
from Alldata.data import AllStockdata
import yfinance as yf
import matplotlib.pyplot as plt
import backtrader as bt
import time






token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wMy0yOCAxMTo0NDo1MiIsInVzZXJfaWQiOiJvc2NhciIsImlwIjoiMS4xNjEuODUuMjM2In0.0qcTZ2wf8MP8FA_2slZyLSSuOnZN9NhkBejJg2pd7Kc"

# resp2 = requests.get('https://api.finmindtrade.com/api/v4/data', params={
#     "dataset": "TaiwanStockInfo"
#     ,'token': token
# })
# print(resp2.json())
# data = pd.DataFrame(data["data"])
# print(data.head())



# url = "https://api.web.finmindtrade.com/v2/user_info"
# payload = {
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wMy0yOCAxMTo0NDo1MiIsInVzZXJfaWQiOiJvc2NhciIsImlwIjoiMS4xNjEuODUuMjM2In0.0qcTZ2wf8MP8FA_2slZyLSSuOnZN9NhkBejJg2pd7Kc",
#     'dataset': 'TaiwanStockPriceTick'
#     'data_id': 'TWSE_2330_2021-03-26'
# }
# resp = requests.get(url, params=payload)
# resp.json()["user_count"]  # 使用次數
# resp.json()["api_request_limit"]  # api 使用上限

# print(resp.json()["user_count"] )
# print(resp.json()["api_request_limit"] )



df = pd.read_csv('2330_data.csv', index_col=None)
df = df.drop(['Unnamed: 0'], axis=1)
df.to_csv('2330_data2.csv')

# url = "https://api.finmindtrade.com/api/v4/data"
# parameter = {
#     "dataset": "TaiwanStockPrice",
#     "data_id": "2330",
#     "start_date": "2000-01-01",
#     "end_date": "2023-03-28",
#     "token": token, # 參考登入，獲取金鑰
# }
# resp = requests.get(url, params=parameter)
# data = resp.json()
# data = pd.DataFrame(data["data"])
# print(data.head())
# data.to_csv('2330_data.csv')

# tsmc =[]
# for company in AllStockdata:
#     if company["industry_category"] == "電子工業":
#         tsmc.append(company["stock_id"])
# try:
#     for company in tsmc:
#         try:
#             # data = yf.download(company, start="2015-01-01", end="2023-03-28")
#             df = pd.DataFrame(data)
#             df.to_csv('{}_data.csv'.format(company))
#             print('success in {}'.format(company))
#         except:
#             print('error in {}'.format(company))
#             pass
# except:
#     pass