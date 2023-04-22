from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import yfinance as yf
from backtesting.test import SMA, GOOG
import pandas as pd
import datetime
import requests
import json
from talib import abstract
from data import AllStockdata
from src.strategies.strategies_class import SmaCross, KdCross, RSI, MACD, BBANDS, CustomStrategy
import math
import time , random
import multiprocessing
import pprint
from fastapi.params import Depends

from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import MongoEngine
from odmantic import ObjectId

from fastapi import BackgroundTasks
from src.personnelManagement.auth.auth_dto import User

from src.htmlPlottings.htmlPlottings_service import store_htmlPlottings_src

from main import logger
import os

def data_backtesting_with_CSI(stock_symbol, strategy,strategy_name,  plot, start_date="2022-01-01", end_date=None, cash=1000000, commission=0.001425, username=""):
    pd_data = pd.read_csv(
        '../csvdata/{}_change.csv'.format(stock_symbol), index_col=0, parse_dates=True)
        # 'D:/studyplace/python_stock/quantitativetrading/trading/Alldata/{}_change.csv'.format(stock_symbol), index_col=0, parse_dates=True)

    # 將資料轉換成talib可以使用的格式
    pd_data2 = pd_data.rename(
        columns={'High': 'high', 'Low': 'low', 'Close': 'close'})
    # 加入各種指標，包括KD、MACD、RSI、BBANDS
    pd_kd = abstract.STOCH(pd_data2, fastk_period=9, slowk_period=3,
                        slowk_matype=0, slowd_period=3, slowd_matype=0)
    pd_MACD = abstract.MACD(pd_data2, fastperiod=12,
                            slowperiod=26, signalperiod=9)
    pd_RSI = abstract.RSI(pd_data2, 14)
    pd_RSI.name = 'RSI'
    pd_bbands = abstract.BBANDS(
        pd_data2, timeperiod=5, nbdevup=float(2), nbdevdn=float(2), matype=0)
    # 將資料合併至 pd_data_with_kd
    pd_data_with_kd = pd.merge(pd_data, pd_kd, on='Date')
    pd_data_with_kd = pd.merge(pd_data_with_kd, pd_MACD, on='Date')
    pd_data_with_kd = pd.merge(pd_data_with_kd, pd_RSI, on='Date')
    pd_data_with_kd = pd.merge(pd_data_with_kd, pd_bbands, on='Date')

    # 定義要回測的資料範圍，預設為從2022-01-01到今天
    desired_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    if end_date == None:
        end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    else:
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    data = pd_data_with_kd.loc[desired_date:end_date]

    # data = pd.read_csv(
    #     'Alldata/1336_change.csv', index_col=0, parse_dates=True)

    bt = Backtest(data, strategy, commission=commission, cash=cash,
                exclusive_orders=True)
    stats = bt.run()
    if plot:
        os.remove('../htmlplots/{}_{}_{}.html'.format(username,strategy_name,stock_symbol))
        bt.plot(filename='../htmlplots/{}_{}_{}.html'.format(username,strategy_name,stock_symbol),open_browser=False)
    # bt.plot()
    # print((stats))
    # logger.info(stats.to_dict())
    
    return stats.to_dict()


def multipreocess_backtesting( strategy, plot, start_date, end_date, cash, commission):
    stock_list = []
    for i in AllStockdata:
        try:
            # 如果最新一筆的資料股價大於 40元, 則不加入回測清單
            pd_data = pd.read_csv(
                'D:/studyplace/python_stock/quantitativetrading/trading/Alldata/{}_change.csv'.format(i["stock_id"]), index_col=0, parse_dates=True)
            # if pd_data.iloc[-1]['Close'] < 10:
            if i['industry_category'] == '電子工業':
                    print(i["stock_id"], i["stock_name"],
                            '價格', pd_data.iloc[-1]['Close'])
                    stock_list.append(
                        [i["stock_id"], RSI,'RSI', False, '2022-01-01', '2023-03-14', 100000, .000145,'OSCAR'])
        except Exception as e:
            print("error in ", i["stock_id"])
    # cpus = multiprocessing.cpu_count()
    # pool = multiprocessing.Pool(processes=cpus)
    # results = pool.starmap(multipreocess_backtesting, stock_list)
    logger.info(stock_list)
    results = []
    for i in stock_list:
        try:
            data = data_backtesting_with_CSI(
                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            logger.info(str(data['Return [%]']),str(data['Profit Factor']))
            results.append([i[0],data['Return [%]'],data['Profit Factor']])
        except Exception as e:
            print("error in ", i[0])


    # print(results[0][0])
    logger.info(results)
    average_return_list = []
    profit_factor = []
    for i in results:
        if i != None:
            # i[0] 為股票代號, i[1] 為回測結果
            # print(i[0], i[1]['Return [%]'], i[1]['Profit Factor'])
            logger.info(str(i))
            logger.info(str(i[0]), str(i[1]), str(i[2]))
            average_return_list.append(i[1])
            profit_factor.append(i[2])

    profit_factor = [x for x in profit_factor if str(
        x) != 'nan' or math.isnan(x) == False]
    logger.info('total number', str(len(profit_factor)))
    logger.info("average totol return", str(sum(
        average_return_list)/len(average_return_list)))
    logger.info("average profit factor", str(sum(
        profit_factor)/len(profit_factor)))
    return {'average_return': str(sum(average_return_list)/len(average_return_list)), 'average_profit_factor':str(sum(profit_factor)/len(profit_factor)), 'total_number': len(profit_factor)}


def data_backtesting_with_CSI_multiple(stock_list, strategy,strategy_name,  plot, start_date="2022-01-01", end_date=None, cash=1000000, commission=0.001425, username=""):
    start_time = time.time()

    # BackgroundTasks.add_task(
    result =  multipreocess_backtesting(strategy = strategy,  plot=plot, start_date=start_date, end_date=end_date, cash=cash, commission=commission)
    end_time = time.time()
    logger.info('time elapsed', end_time - start_time)
    return result

def live_data_backtesting(self,stock_symbol):
    ''' notice: this function is still under construction
    stock_symbol: 股票代號
    '''
    stock_list_tse = [stock_symbol]
    stock_list_otc = []
    # tse開頭為上市股票。
    # otc開頭為上櫃股票。
    # 如果是興櫃股票則無法取得。
    # 組合API需要的股票清單字串
    stock_list1 = '|'.join('tse_{}.tw'.format(stock)
                        for stock in stock_list_tse)

    # 6字頭的股票參數不一樣
    stock_list2 = '|'.join('otc_{}.tw'.format(stock)
                        for stock in stock_list_otc)
    stock_list = stock_list1 + '|' + stock_list2


    # 　組合完整的URL
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
    # (data['msgArray'][0])
    # 過濾出有用到的欄位
    columns = ['c', 'n', 'z', 'tv', 'v', 'o', 'h', 'l', 'y', 'tlong']
    df = pd.DataFrame(data['msgArray'], columns=columns)
    df.columns = ['股票代號', '公司簡稱', '成交價', '成交量',
                '累積成交量', '開盤價', '最高價', '最低價', '昨收價', '資料更新時間']
    today_str = datetime.datetime.today().strftime('%Y-%m-%d')
    today_datetime = datetime.datetime.strptime(today_str, '%Y-%m-%d')
    pd_data = pd.read_csv(
        'Alldata/{}_change.csv'.format(stock_symbol), index_col=0, parse_dates=True)
    print(datetime.datetime.today().strftime('%Y-%m-%d'))
    open = float(df.at[0, '開盤價'])
    high = float(df.at[0, '最高價'])
    low = float(df.at[0, '最低價'])
    close = float(df.at[0, '成交價'])
    Adj_Close = float(df.at[0, '昨收價'])
    volume = float(df.at[0, '累積成交量'])
    print(df.to_markdown(), 'df')
    # high = df['最高價']
    # low = df['最低價']
    # close = df['成交價']
    # Adj_Close = df['昨收價']
    # volume = df['累積成交量']

    # Open,High,Low,Close,Adj Close,Volume

    desired_date_str = '2021-03-24'
    desired_date = datetime.datetime.strptime(desired_date_str, '%Y-%m-%d')

    pd_data.loc[today_datetime] = [open, high, low, close, Adj_Close, volume]
    print(pd_data, 'pd_data')
    data = pd_data.loc[desired_date:today_str]

    # data = pd.read_csv(
    #     'Alldata/1336_change.csv', index_col=0, parse_dates=True)

    bt = Backtest(data, SmaCross, commission=.000145, cash=100000,
                exclusive_orders=True)
    stats = bt.run()
    # bt.plot()
    print(stats[1])





if __name__ == '__main__':
    # 回測單一股票
    # print(data_backtesting_with_CSI('0050', strategy=RSI, plot=False,
    #       start_date='2021-03-01', cash=100000, commission=.000145))

    # 分產業群回測並計算平均報酬率 可於 data.py 中查看產業群名稱
    # 此未進行多線程加速
    # average_return_list = []
    # profit_factor = []
    # start_time = time.time()
    # for i in AllStockdata:
    #     if i['industry_category'] == '電子工業':
    #         try:
    #             print(i["stock_id"], i["stock_name"])
    #             data = data_backtesting_with_CSI(i["stock_id"], strategy=CustomStrategy, plot=False, start_date='2022-01-01', cash=100000, commission=.000145)
    #             print(data['Profit Factor'])
    #             average_return_list.append(
    #                 data['Return [%]'])
    #             profit_factor.append(
    #                 data['Profit Factor'])
    #         except Exception as e:
    #             print('error in ', i["stock_id"], i["stock_name"])
    #             print(e)
    # profit_factor = [x for x in profit_factor if str(x) != 'nan' or math.isnan(x) == False]
    # print('total number', len(average_return_list))
    # print("average totol return", sum(
    #     average_return_list)/len(average_return_list))
    # print("average profit factor", sum(
    #     profit_factor)/len(profit_factor))
    # end_time = time.time()
    # print('time elapsed', end_time - start_time)

    # 使用 multiprocessing 進行多股票回測
    # 使用該方法速度會提升約五倍, 實測台股約 2400檔股票, 回測時間約為 35秒, 尚未進行優化前約為 157秒
    # 使用 cpu 為 8核心, AMD Ryzen 7 5800H 筆電 cpu
    # 使用多線程數量為 cpu 數量, 可於 cpus 中修改
    # 須注意此方法會提高 cpu 使用率
    # start_time = time.time()
    # stock_list = []
    # for i in AllStockdata:
    #     try:
    #         # 如果最新一筆的資料股價大於 40元, 則不加入回測清單
    #         pd_data = pd.read_csv(
    #             'Alldata/{}_change.csv'.format(i["stock_id"]), index_col=0, parse_dates=True)
    #         if pd_data.iloc[-1]['Close'] < 40:
    #             # if i['industry_category'] == '電子工業':
    #             print(i["stock_id"], i["stock_name"],
    #                   '價格', pd_data.iloc[-1]['Close'])
    #             stock_list.append(
    #                 (i["stock_id"], RSI, False, '2022-01-01', None, 100000, .000145))
    #     except Exception as e:
    #         print('error in ', i["stock_id"], i["stock_name"])
    #         print(e)

    # cpus = multiprocessing.cpu_count()
    # pool = multiprocessing.Pool(processes=cpus)
    # results = pool.starmap(multipreocess_backtesting, stock_list)

    # # print(results[0][0])
    # average_return_list = []
    # profit_factor = []
    # for i in results:
    #     if i != None:
    #         # i[0] 為股票代號, i[1] 為回測結果
    #         # print(i[0], i[1]['Return [%]'], i[1]['Profit Factor'])
    #         average_return_list.append(i[1]['Return [%]'])
    #         profit_factor.append(i[1]['Profit Factor'])

    # profit_factor = [x for x in profit_factor if str(
    #     x) != 'nan' or math.isnan(x) == False]
    # print('total number', len(profit_factor))
    # print("average totol return", sum(
    #     average_return_list)/len(average_return_list))
    # print("average profit factor", sum(
    #     profit_factor)/len(profit_factor))

    # end_time = time.time()
    # print('time elapsed', end_time - start_time)

    # 及時資料進行回測下單 尚未實作完成
    while True:
        try:
            live_data_backtesting('2330')
            time.sleep(random.randint(7, 12))

        except Exception as e:
            print(e)
            time.sleep(random.randint(7, 12))
