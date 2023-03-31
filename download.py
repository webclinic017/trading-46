from data import AllStockdata
import datetime
import pandas as pd
import requests
import sys
import os

def change_OTC_date():
    # with open('everydaychange/otc/SQUOTE_EW_1120330.csv', 'rb') as f:
    #     result = chardet.detect(f.read())
    # print(result)
    # ,encoding=result['encoding']
    otc_link = 'https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&se=EW&o=data'
    df2 = pd.read_csv(otc_link, index_col=None)
    # df2 = pd.read_csv('everydaychange/otc/SQUOTE_EW_1120330.csv', index_col=None)
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
                error_list.append([df2.iloc[company, 1], df2.iloc[company, 2]])
                pass            
        except:
            print('error in {}'.format(df2.iloc[company,1]),'證券名稱 : ' , df2.iloc[company,2])
            print('error msg : ',sys.exc_info()[0])
            pass
    print('suceed_list : ',suceed_list)
    print('len of suceed_list : ',len(suceed_list))
    print('error_list : ',error_list)
    print('len of error_list : ',len(error_list))        
    
def change_listed_date():
    listed_link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    df = pd.read_csv(listed_link, index_col=None)
    # df = pd.read_csv('everydaychange/listed/STOCK_DAY_ALL_20230330.csv', index_col=None)
    print(df.shape[0])
    df2=df.dropna(subset=['成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價','漲跌價差'])
    print(df2.shape[0])
    today_str = datetime.datetime.today().strftime('%Y-%m-%d')
    today_datetime = datetime.datetime.strptime(today_str, '%Y-%m-%d')

    error_list = []
    suceed_list = []
    for company in range(0,df2.shape[0]):
        try:
            df_change = pd.read_csv(
                'Alldata/{}_change.csv'.format(df2.iloc[company,0]), index_col=0,parse_dates=True)
            # 證券代號,證券名稱,成交股數,成交金額,開盤價,最高價,最低價,收盤價,漲跌價差,成交筆數
            # print('證券代號 : ',df2.iloc[company,0],'證券名稱 : ' , df2.iloc[company,1])
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
            suceed_list.append([df2.iloc[company, 0], df2.iloc[company, 1]])
        except:
            print('error in {}'.format(df2.iloc[company,0]),'證券名稱 : ' , df2.iloc[company,1])
            error_list.append([df2.iloc[company,0],df2.iloc[company,1]])
            pass
    print('suceed_list : ',suceed_list)
    print('len of suceed_list : ',len(suceed_list))
    print('error_list : ',error_list)
    print('len of error_list : ',len(error_list))      

        
    print(df)

def checkonestock(token, stock_id):
    url = "https://api.finmindtrade.com/api/v4/data"
    parameter = {
        "dataset": "TaiwanStockPrice",
        "data_id": stock_id,
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

def download(token):
    url = "https://api.web.finmindtrade.com/v2/user_info"
    payload = {
        "token": token,  # 參考登入，獲取金鑰
    }
    resp = requests.get(url, params=payload)
    used_time = resp.json()["user_count"]  # 使用次數
    resp.json()["api_request_limit"]  # api 使用上限

    print(resp.json()["user_count"],'已使用次數', resp.json()["api_request_limit"],'使用上限', resp.json()["api_request_limit"]-resp.json()["user_count"],'剩餘次數')
    leftstock = []
    for company in AllStockdata:
        if os.path.isfile('Alldata/{}_data.csv'.format(company["stock_id"])) is False:
            leftstock.append(company["stock_id"])
    print('尚未下載的股票數量 : ',len(leftstock),'個')
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
                data.to_csv('Alldata/{}_data.csv'.format(company), index=False)
                print('success in {}'.format(company))
            else:
                print('already use 600 times')
                break

    except:
        print("error in {}".format(company))
        pass
def deleteNoDataCSV():
    for company in AllStockdata:
        if os.path.isfile('Alldata/{}_data.csv'.format(company["stock_id"])) is True:
            try:
                pd.read_csv('Alldata/{}_data.csv'.format(company["stock_id"]))
            except pd.errors.EmptyDataError:
                os.remove('Alldata/{}_data.csv'.format(company["stock_id"]))
                print('delete {}'.format(company["stock_id"]))


if __name__ == '__main__':
    # 上櫃公司股票當日個股結算下載 'https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&se=EW&o=data'
    # 上事公司股票當日個股結算下載 = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    # 每日進行資料更新的兩個函式, 會更新上市與上櫃的資料, 名稱在 AllStockdata, 會以 _change.csv 結尾
    # OTC 為上櫃, Listed 為上市
    change_OTC_date()
    change_listed_date()

    token = "註冊 finmind 帳號後於個人資料頁面取得"
    # 從 finmind 下載資料 一個小時只能下載 200 次, 若有 token 可以下載 600 次, 將 token 填入即可, 會自動判斷在 AllStockdata 中的股票是否已經下載過, 若沒有則會自動下載
    # download(token)

    # 刪除沒有資料的 csv 檔案, 會在 Alldata 資料夾中刪除沒有資料的 csv 檔案
    # deleteNoDataCSV()

    # 透過 finmind 檢查一個股票的資料, 並在終端機中顯示出來, 會在終端機中顯示出該股票的資料
    # checkonestock(token, '2330')
