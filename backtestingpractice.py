from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import yfinance as yf
from backtesting.test import SMA, GOOG
import pandas as pd
import datetime
import requests, json


import talib
from talib import abstract

class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


# data = bt.feeds.PandasData(dataname=yf.download('2303.TW', start="2022-01-01", end="2023-03-24"))
# bt = Backtest(yf.download('2303.TW', start="2022-01-01", end="2023-03-24"), SmaCross, commission=.002,
#               exclusive_orders=True)
# data = pd.read_csv('2330_data.csv',index_col=1, parse_dates=True)
def live_data_backtesting():
    stock_list_tse = ['0050']
    stock_list_otc = []
    # tse開頭為上市股票。
    # otc開頭為上櫃股票。
    # 如果是興櫃股票則無法取得。
    # 組合API需要的股票清單字串
    stock_list1 = '|'.join('tse_{}.tw'.format(stock) for stock in stock_list_tse) 

    # 6字頭的股票參數不一樣
    stock_list2 = '|'.join('otc_{}.tw'.format(stock) for stock in stock_list_otc) 
    stock_list = stock_list1 + '|' + stock_list2
    print(stock_list)

    #　組合完整的URL
    query_url = f'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_list}'

    # 呼叫股票資訊API
    response = requests.get(query_url)

    # 判斷該API呼叫是否成功
    if response.status_code != 200:
        raise Exception('取得股票資訊失敗.')
    else:
        pass
        # print(response.text)

    # 將回傳的JSON格式資料轉成Python的dictionary
    data = json.loads(response.text)

    # 過濾出有用到的欄位
    columns = ['c','n','z','tv','v','o','h','l','y', 'tlong']
    df = pd.DataFrame(data['msgArray'], columns=columns)
    df.columns = ['股票代號','公司簡稱','成交價','成交量','累積成交量','開盤價','最高價','最低價','昨收價', '資料更新時間']
    today_str = datetime.datetime.today().strftime('%Y-%m-%d')
    today_datetime = datetime.datetime.strptime(today_str, '%Y-%m-%d')
    pd_data = pd.read_csv(
        'Alldata/{}_change.csv'.format('0050'), index_col=0,parse_dates=True)
    print(datetime.datetime.today().strftime('%Y-%m-%d'))
    open = float(df.at[0,'開盤價'])
    high = float(df.at[0,'最高價'])
    low = float(df.at[0,'最低價'])
    close = float(df.at[0,'成交價'])
    Adj_Close = float(df.at[0,'昨收價'])
    volume = float(df.at[0,'累積成交量'])

    # high = df['最高價']
    # low = df['最低價']
    # close = df['成交價']
    # Adj_Close = df['昨收價']
    # volume = df['累積成交量']

    # Open,High,Low,Close,Adj Close,Volume

    desired_date_str = '2021-03-24'
    desired_date = datetime.datetime.strptime(desired_date_str, '%Y-%m-%d')

    pd_data.loc[today_datetime] = [open, high, low, close,Adj_Close ,volume]
    print(pd_data, 'pd_data')
    data = pd_data.loc[desired_date:today_str]

    # data = pd.read_csv(
    #     'Alldata/1336_change.csv', index_col=0, parse_dates=True)

    bt = Backtest(data, SmaCross, commission=.000145, cash=100000,
                exclusive_orders=True)
    stats = bt.run()
    bt.plot()
    print(stats)


def backtesting():
    data = pd.read_csv(
        'Alldata/6747_change.csv', index_col=0, parse_dates=True)
    bt = Backtest(data, SmaCross, commission=.000145, cash=100000,
                exclusive_orders=True)
    stats = bt.run()
    bt.plot()
    print(stats)

if __name__ == '__main__':
    backtesting()
    
