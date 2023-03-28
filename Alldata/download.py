import time
import backtrader as bt
import yfinance as yf
from data import AllStockdata
import json
import datetime
import pandas as pd
import requests
import sys
import os

tsmc = []
for company in AllStockdata:
    category = [
        "資訊服務業",
        "鋼鐵工業",
        "其他電子類",
        "電子通路業",
        "化學生技醫療",
        "生技醫療業",
        "電機機械",
        "汽車工業",
        "文化創意業",
        "觀光事業",
        "電子零組件業",
        "電子工業",
        "半導體業",
        "光電業",
        "通信網路業",
        "其他電子業",
        "電腦及週邊設備業"
    ]
    if company["industry_category"] in category:
        tsmc.append(company["stock_id"])

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wMy0yOCAxMTo0NDo1MiIsInVzZXJfaWQiOiJvc2NhciIsImlwIjoiMS4xNjEuODUuMjM2In0.0qcTZ2wf8MP8FA_2slZyLSSuOnZN9NhkBejJg2pd7Kc"
url = "https://api.web.finmindtrade.com/v2/user_info"
payload = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wMy0yOCAxMTo0NDo1MiIsInVzZXJfaWQiOiJvc2NhciIsImlwIjoiMS4xNjEuODUuMjM2In0.0qcTZ2wf8MP8FA_2slZyLSSuOnZN9NhkBejJg2pd7Kc"
}
resp = requests.get(url, params=payload)
used_time = resp.json()["user_count"]  # 使用次數
resp.json()["api_request_limit"]  # api 使用上限

print(resp.json()["user_count"],'times')
print(resp.json()["api_request_limit"])
# try:
#     for company in tsmc:
#         url = "https://api.finmindtrade.com/api/v4/data"
#         parameter = {
#             "dataset": "TaiwanStockPrice",
#             "data_id": company,
#             "start_date": "2000-01-01",
#             "end_date": "2023-03-28",
#             "token": token,  # 參考登入，獲取金鑰
#         }
#         resp = requests.get(url, params=parameter)
#         data = resp.json()
#         data = pd.DataFrame(data["data"])
#         data.to_csv('{}_data.csv'.format(company), index=False)
#         print('success in {}'.format(company))
# except:
#     print("error in {}".format(company))
#     pass

def download():
    leftstock = []
    for company in AllStockdata:
        if os.path.isfile('{}_data.csv'.format(company["stock_id"])) is False:
            leftstock.append(company["stock_id"])
    print(len(leftstock))
    # print(leftstock)
    i = 0

    try:
        for company in leftstock:
            if i<(600-int(used_time)):                    
                url = "https://api.finmindtrade.com/api/v4/data"
                parameter = {
                    "dataset": "TaiwanStockPrice",
                    "data_id": company,
                    "start_date": "2000-01-01",
                    "end_date": "2023-03-28",
                    "token": token,  # 參考登入，獲取金鑰
                }
                resp = requests.get(url, params=parameter)
                i += 1
                data = resp.json()
                data = pd.DataFrame(data["data"])
                data.to_csv('{}_data.csv'.format(company), index=False)
                print('success in {}'.format(company))
            else:
                print('already use 600 times')
                break

    except:
        print("error in {}".format(company))
        pass
def deleteNoDataCSV():
    for company in AllStockdata:
        if os.path.isfile('{}_data.csv'.format(company["stock_id"])) is True:
            try:
                pd.read_csv('{}_data.csv'.format(company["stock_id"]))
            except pd.errors.EmptyDataError:
                os.remove('{}_data.csv'.format(company["stock_id"]))
                print('delete {}'.format(company["stock_id"]))
download()
# deleteNoDataCSV()

#cd C:\Users\kaikai\Desktop\work\trading\trading\Alldata
#python download.py