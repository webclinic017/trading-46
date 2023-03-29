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
#上櫃: 'http://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_download.php?l=zh-tw&se=EW'

def get_symbols():
    '''
    取得股票代號
    '''

    symbol_link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    symbols = pd.read_csv(symbol_link)
    return symbols
def change_OTC_date():
    df2 = pd.read_csv('everydaychange/otc/SQUOTE_EW_1120329.csv', index_col=None)
    print(df2.shape[0])
    #收盤,漲跌,開盤,最高,最低,成交股數,成交金額,成交筆數,最後買價,最後賣價,發行股數,次日漲停價,次日跌停價
    # df2=df.dropna(subset=['成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價','漲跌價差'])
    # df2 = df.dropna(subset=['收盤', '漲跌', '開盤', '最高', '最低', '成交股數', '成交金額', '成交筆數', '最後買價', '最後賣價', '發行股數', '次日漲停價', '次日跌停價'])
    # print(df2.shape[0])
    today_str = datetime.datetime.today().strftime('%Y-%m-%d')
    today_datetime = datetime.datetime.strptime(today_str, '%Y-%m-%d')

    error_list = []
    suceed_list = []
    for company in range(0,df2.shape[0]):
        try:
            if df2.iloc[company, 10] != int(0):
                df_change = pd.read_csv(
                'Alldata/{}_change.csv'.format(df2.iloc[company,1]), index_col=0,parse_dates=True)
                #資料日期,代號,名稱,收盤,漲跌,開盤,最高,最低,成交股數,成交金額,成交筆數,最後買價,最後賣價,發行股數,次日漲停價,次日跌停價
                # print('證券代號 : ',str(df2.iloc[company,1]),'證券名稱 : ' , df2.iloc[company,2])
                df_change_id = df2.iloc[company,1]
                df_change_name = df2.iloc[company,2]
                df_change_name_volume = df2.iloc[company,8]
                df_change_name_amount = df2.iloc[company,9]
                df_change_name_open = df2.iloc[company,5]
                df_change_name_high = df2.iloc[company,6]
                df_change_name_low = df2.iloc[company,7]
                df_change_name_close = df2.iloc[company,3]
                df_change_name_change = df2.iloc[company,4]
                df_change_name_transaction = df2.iloc[company,10]
                # print('df_change_id : ',df_change_id, 'df_change_name : ',df_change_name, 'df_change_name_volume : ',df_change_name_volume, 'df_change_name_amount : ',df_change_name_amount, 'df_change_name_open : ',df_change_name_open, 'df_change_name_high : ',df_change_name_high, 'df_change_name_low : ',df_change_name_low, 'df_change_name_close : ',df_change_name_close, 'df_change_name_change : ',df_change_name_change, 'df_change_name_transaction : ',df_change_name_transaction)
                df_change.loc[today_datetime] = [df_change_name_open, df_change_name_high, df_change_name_low, df_change_name_close, df_change_name_close, df_change_name_volume]
                df_change.to_csv('Alldata/{}_change.csv'.format(df2.iloc[company,1]))
                suceed_list.append([df2.iloc[company, 1], df2.iloc[company, 2]])

            else:
                print(df2.iloc[company, 10], 'is 0')
                error_list.append([df2.iloc[company, 1], df2.iloc[company, 2]])
            
        except:
            print('error in {}'.format(df2.iloc[company,1]),'證券名稱 : ' , df2.iloc[company,2])
            print('error msg : ',sys.exc_info()[0])
            pass
    print('suceed_list : ',suceed_list)
    print('len of suceed_list : ',len(suceed_list))
    print('error_list : ',error_list)
    print('len of error_list : ',len(error_list))
# change_OTC_date()
        
    
def change_listed_date():
    df = pd.read_csv('STOCK_DAY_ALL_20230329.csv', index_col=None)
    print(df.shape[0])
    df2=df.dropna(subset=['成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價','漲跌價差'])
    print(df2.shape[0])
    today_str = datetime.datetime.today().strftime('%Y-%m-%d')
    today_datetime = datetime.datetime.strptime(today_str, '%Y-%m-%d')

    error_list = []
    for company in range(0,df2.shape[0]):
        try:
            df_change = pd.read_csv(
                'Alldata/{}_change.csv'.format(df2.iloc[company,0]), index_col=0,parse_dates=True)
            # 證券代號,證券名稱,成交股數,成交金額,開盤價,最高價,最低價,收盤價,漲跌價差,成交筆數
            print('證券代號 : ',df2.iloc[company,0],'證券名稱 : ' , df2.iloc[company,1])
            df_change_id = df2.iloc[company,0]
            df_change_name = df2.iloc[company,1]
            df_change_name_volume = df2.iloc[company,2]
            df_change_name_amount = df2.iloc[company,3]
            df_change_name_open = df2.iloc[company,4]
            df_change_name_high = df2.iloc[company,5]
            df_change_name_low = df2.iloc[company,6]
            df_change_name_close = df2.iloc[company,7]
            df_change_name_change = df2.iloc[company,8]
            df_change_name_transaction = df2.iloc[company,9]
            df_change.loc[today_datetime] = [df_change_name_open, df_change_name_high, df_change_name_low, df_change_name_close, df_change_name_close, df_change_name_volume]
            df_change.to_csv('Alldata/{}_change.csv'.format(df2.iloc[company,0]))
        except:
            print('error in {}'.format(df2.iloc[company,0]),'證券名稱 : ' , df2.iloc[company,1])
            error_list.append([df2.iloc[company,0],df2.iloc[company,1]])
            pass
    print('error_list : ',error_list)

        
    print(df)
def checkonestock():
    url = "https://api.finmindtrade.com/api/v4/data"
    parameter = {
        "dataset": "TaiwanStockPrice",
        "data_id": '6474',
        "start_date": "2023-01-01",
        "end_date": "2023-03-29",
        "token": token,  # 參考登入，獲取金鑰
    }
    resp = requests.get(url, params=parameter)
    data = resp.json()
    data = pd.DataFrame(data["data"])
    print(data)
# checkonestock()
# df = df.drop(['Unnamed: 0'], axis=1)
# df.to_csv('2330_data2.csv')

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
# deleteNoDataCSV()

#cd C:\Users\kaikai\Desktop\work\trading\trading\Alldata
#python download.py