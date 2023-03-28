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
def get_symbols():
    '''
    取得股票代號
    '''
    symbol_link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
    symbols = pd.read_csv(symbol_link)
    return symbols

def gen_calendar():
    '''
    產生日期表
    '''
    this_year = datetime.datetime.now()
    years = range(2010, this_year.year + 1)  # Fugle提供的資料從2010年
    begin = [int(str(y) + '0101') for y in years]
    end = [int(str(y) + '1231') for y in years]
    calendar = pd.DataFrame({'begin': begin,
                            'end': end})
    calendar['begin'] = pd.to_datetime(calendar['begin'], format='%Y%m%d')
    calendar['end'] = pd.to_datetime(calendar['end'], format='%Y%m%d')
    calendar[['begin', 'end']] = calendar[['begin', 'end']].astype('str')
    return calendar

def get_hist_data(symbols=[]):
    '''
    透過富果Fugle API抓取歷史資料
    '''
    if len(symbols) == 0:
        symbols = get_symbols()
    calendar = gen_calendar()
    result = pd.DataFrame()
    print('抓取歷史資料中...')
    for i in range(len(symbols)):
        cur_symbol = symbols[i]
        symbol_result = pd.DataFrame()
        print('正在抓取{}的資料...'.format(cur_symbol))
        try:
            for j in range(len(calendar)):
                    cur_begin = calendar.loc[j, 'begin']
                    cur_end = calendar.loc[j, 'end']
                    # 透過富果Fugle API抓取歷史資料
                    data_link = f'https://api.fugle.tw/marketdata/v0.3/candles?symbolId={cur_symbol}&apiToken=demo&from={cur_begin}&to={cur_end}&fields=open,high,low,close,volume,turnover,change'
                    resp = requests.get(url=data_link)
                    # csv = pd.DataFrame(resp.json())
                    data = resp.json()
                    json_string = json.dumps(data, indent=4)
                    print(json_string)
                    break

                    # candles = data['candles']
                    new_result = pd.DataFrame.from_dict(data)
                    symbol_result = pd.concat([symbol_result, new_result])
                    time.sleep(1)
            symbol_result['symbol'] = cur_symbol
            result = pd.concat([result, symbol_result])
            result.to_csv('{}_data.csv'.format(cur_symbol), index=True)
            print('已完成{}的資料抓取'.format(cur_symbol))
        except:
            print('抓取{}的{}資料時發生錯誤'.format(cur_symbol, cur_begin))
            continue
    return result

# 全部股票歷史資料
# data = get_symbols()
# print(data)
# 單一個股歷史資料 - 2330台積電
# yf.download('2303.TW', start="2022-01-01", end="2023-03-24")
# pd.DataFrame(yf.download('2303.TW', start="2022-01-01", end="2023-03-24")).to_csv('2303TW.csv')
# calender = gen_calendar()
# print(calender)
class DonchianChannels(bt.Indicator):
    # 這個物件的別名，所以後面我們可以用DCH/DonchianChannel來呼叫這個指標
    alias = ('DCH', 'DonchianChannel',)
    
    # 三條線分別代表唐奇安通道中的 中軌(上軌加下軌再除以2)、上軌、下軌
    lines = ('dcm', 'dch', 'dcl',)  # dc middle, dc high, dc low
    
    # 軌道的計算方式：用過去20天的資料來計算，所以period是20，lookback的意思是要不要將今天的資料納入計算，由於唐奇安通道是取過去20天的最高或最低，所以一定不能涵蓋今天，不然永遠不會有訊號出現，所以要填-1(從前一天開始算20天)
    params = dict(
        period=20,
        lookback=-1,  # consider current bar or not
    )
    
    # 是否要將Indicators另外畫一張圖，然而通道線通常都是跟股價圖畫在同一張，才能看得出相對關係，所以這裡就填subplot=False
    plotinfo = dict(subplot=False)  # plot along with data
    
    # 繪圖設定，ls是line style，'--'代表虛線
    plotlines = dict(
        dcm=dict(ls='--'),  # dashed line
        dch=dict(_samecolor=True),  # use same color as prev line (dcm)
        dcl=dict(_samecolor=True),  # use same color as prev line (dch)
    )
    
    def __init__(self):
        # hi與lo是指每日股價的最高與最低價格
        hi, lo = self.data.high, self.data.low
        
        # 視需求決定是否要從前一天開始讀資料，上面已經定義lookback存在，所以這邊會直接從前一天的資料開始跑
        if self.p.lookback:  # move backwards as needed
            hi, lo = hi(self.p.lookback), lo(self.p.lookback)
        
        # 定義三條線的計算方式
        self.l.dch = bt.ind.Highest(hi, period=self.p.period)
        self.l.dcl = bt.ind.Lowest(lo, period=self.p.period)
        self.l.dcm = (self.l.dch + self.l.dcl) / 2.0  # avg of the above

class MyStrategy(bt.Strategy):
    def __init__(self):
        # DCH就是上面定義的 DonchianChannels的alias
        self.myind = DonchianChannels()

    def next(self):
        if self.data[0] > self.myind.dch[0]:
            self.buy()
        elif self.data[0] < self.myind.dcl[0]:
            self.sell()



url = "https://api.web.finmindtrade.com/v2/user_info"
payload = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wMy0yOCAxMTo0NDo1MiIsInVzZXJfaWQiOiJvc2NhciIsImlwIjoiMS4xNjEuODUuMjM2In0.0qcTZ2wf8MP8FA_2slZyLSSuOnZN9NhkBejJg2pd7Kc"
}
resp = requests.get(url, params=payload)
resp.json()["user_count"]  # 使用次數
resp.json()["api_request_limit"]  # api 使用上限

print(resp.json()["user_count"] )
print(resp.json()["api_request_limit"] )
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMy0wMy0yOCAxMTo0NDo1MiIsInVzZXJfaWQiOiJvc2NhciIsImlwIjoiMS4xNjEuODUuMjM2In0.0qcTZ2wf8MP8FA_2slZyLSSuOnZN9NhkBejJg2pd7Kc"

tsmc =[]
for company in AllStockdata:
    if company["industry_category"] == "電子工業":
        tsmc.append(company["stock_id"])
    if company["industry_category"] == "半導體業":
        tsmc.append(company["stock_id"])
tsmc.remove("2330")

try:
    for company in tsmc:
        url = "https://api.finmindtrade.com/api/v4/data"
        parameter = {
            "dataset": "TaiwanStockPrice",
            "data_id": company,
            "start_date": "2000-01-01",
            "end_date": "2023-03-28",
            "token": token, # 參考登入，獲取金鑰
        }
        resp = requests.get(url, params=parameter)
        data = resp.json()
        data = pd.DataFrame(data["data"])
        data.to_csv('{}_data.csv'.format(company), index=False)
        print('success in {}'.format(company))
except:
    print("error in {}".format(company))
    pass

# try:
#     for company in tsmc:
#         df_change = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], index=None ) 
#         df = pd.read_csv('{}_data.csv'.format(company), usecols=[5])
#         for index, row in df.iterrows():
#             # print(type(row[0]))
#             data = eval(row[0])
#         # Date,Open,High,Low,Close,Adj Close,Volume
#             df_change = df_change.append({'Date': pd.to_datetime(data['date']), 'Open': data['open'], 'High': data['high'], 'Low': data['low'], 'Close': data['close'], 'Adj Close': data['close'], 'Volume': data['volume']}, ignore_index=True)

#             # data = eval('{}{}{}'.format('"', row[0], '"'))
#             # print(data['date'])

#         df_change_reindex = df_change.set_index('Date')
#         df_change_reindex.to_csv('{}_change.csv'.format(company))
# except:
#     print('error')
#     pass


# df.plot()
# plt.show()
# cerebro = bt.Cerebro()
# cerebro.broker.setcash(1000)
# cerebro.broker.setcommission(commission=0.00145)
# cerebro.addstrategy(MyStrategy)

# data = bt.feeds.PandasData(dataname = df_change_reindex)

# cerebro.adddata(data)
# cerebro.run()
# print('Ending Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot()