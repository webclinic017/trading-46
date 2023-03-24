# import yfinance as yf
# import matplotlib.pyplot as plt

# # 獲取 2330 台積電的股價數據
# stock = yf.Ticker("2330.TW")
# df = stock.history(period="max")

# # 繪製歷史線圖
# plt.figure(figsize=(10, 6))
# plt.plot(df["Close"])
# plt.title("2330 台積電歷史股價線圖")
# plt.xlabel("日期")
# plt.ylabel("股價")
# plt.show()

import backtrader as bt
import yfinance as yf
import math
class MyStrategy(bt.Strategy):
    
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        
    def next(self):
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                if self.dataclose[-1] < self.dataclose[-2]:
                    self.buy()
        elif self.dataclose[0] > self.dataclose[-1]:
            if self.dataclose[-1] > self.dataclose[-2]:
                self.sell()
class MovingAverageCrossStrategy(bt.Strategy):
    
    params = (
        ('pfast', 5),
        ('pslow', 20),
    )
    
    def __init__(self):
        self.fastma = bt.indicators.SMA(period=self.params.pfast)
        self.slowma = bt.indicators.SMA(period=self.params.pslow)
        self.crossover = bt.indicators.CrossOver(self.fastma, self.slowma)
    
    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()


class LongTermBearStrategy(bt.Strategy):
    
    params = (
        ('stop_loss', 0.1),
        ('take_profit', 0.2),
    )
    
    def __init__(self):
        self.stop_loss_price = 0
        self.take_profit_price = 0
        self.entry_price = 0
        self.order = None
    
    def next(self):
        if not self.position:
            if self.data.close[0] < self.data.close[-1]:
                self.entry_price = self.data.close[0]
                self.stop_loss_price = self.entry_price * (1 - self.params.stop_loss)
                self.take_profit_price = self.entry_price * (1 + self.params.take_profit)
                self.order = self.buy(price=self.entry_price)
        else:
            if self.data.close[0] < self.stop_loss_price:
                self.sell(price=self.stop_loss_price, exectype=bt.Order.Stop)
            elif self.data.close[0] > self.take_profit_price:
                self.sell(price=self.take_profit_price, exectype=bt.Order.Limit)


class BearMarketStrategy(bt.Strategy):
    
    def __init__(self):
        self.stop_loss_price = 0
        self.take_profit_price = 0
        self.entry_price = 27
        self.order = None
        self.buy_filter_price = 15# 定義買進價格過濾器
       
    
    def next(self):
        if not self.position and self.data.close[0] < self.buy_filter_price:
            self.entry_price = self.data.close[0]
            self.buy_filter_price = self.entry_price * 0.95 # 降低買進價格過濾器
            self.stop_loss_price = self.entry_price * 0.95 # 設置止損價格
            self.take_profit_price = self.entry_price * 1.1 # 設置止盈價格
            self.order = self.buy()
            
        elif self.position:
            if self.data.close[0] > self.take_profit_price or self.data.close[0] < self.stop_loss_price:
                self.sell() # 如果達到止盈或止損價格，就平倉
            elif self.data.close[0] < self.buy_filter_price:
                self.buy_filter_price = self.data.close[0] * 0.90 # 降低買進價格過濾器
cerebro = bt.Cerebro()

# 獲取 2330 台積電的股價數據
# data = bt.feeds.PandasData(dataname=yf.download("3481.TW", start="2022-01-01", end="2023-03-24"))

# cerebro.adddata(data)
# cerebro.addstrategy(BearMarketStrategy)
# cerebro.addsizer(bt.sizers.PercentSizer, percents = 80)

# cerebro.broker.setcash(100.0)
# cerebro.broker.setcommission(commission=0.001)
# cerebro.run()
# print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot()
# 將以下轉換為 array 1402   遠紡       	 1407   華隆       	 1408   中紡       	 1409   新纖       	 1410   南染       
# 1413   宏洲       	 1414   東和       	 1416   廣豐       	 1417   嘉裕       	 1418   東華       
# 1419   新紡       	 1423   利華       	 1432   大魯閣     	 1434   福懋       	 1435   中福       
# 1436   福益       	 1437   勤益       	 1438   裕豐       	 1439   中和       	 1440   南紡       
# 1441   大東       	 1442   名軒       	 1443   立益       	 1444   力麗       	 1445   大宇       
# 1446   宏和       	 1447   力鵬       	 1449   佳和       	 1450   新藝       	 1451   年興       
# 1452   宏益       	 1453   大將       	 1454   台富       	 1455   集盛       	 1456   怡華       
# 1457   宜進       	 1458   嘉畜       	 1459   聯發       	 1460   宏遠       	 1462   東雲       
# 1463   強盛       	 1464   得力       	 1465   偉全       	 1466   聚隆       	 1467   南緯       
# 1468   昶和       	 1469   理隆       	 1470   大統       	 1471   首利       	 1472   三洋纖     
# 1473   台南       	 1474   弘裕       	 1475   本盟       	 1476   儒鴻       	 1477   聚陽

cloth = [
    ['1402.TW' ,'遠紡'],
    ['1407.TW', '華隆'],
    ['1408.TW', '中紡'],
    ['1409.TW', '新纖'],
    ['1410.TW', '南染'],
    ['1413.TW' ,'宏洲'],
    ['1414.TW' ,'東和'],
    ['1416.TW', '廣豐'],
    ['1417.TW', '嘉裕'],
    ['1418.TW', '東華'],
    ['1419.TW', '新紡'],                 
    ['1423.TW' ,'利華'],
    ['1432.TW', '大魯閣'],
    ['1434.TW', '福懋'],
    ['1435.TW', '中福'],
    ['1436.TW', '福益'],
    ['1437.TW' ,'勤益'],
    ['1438.TW', '裕豐'],
    ['1439.TW' ,'中和'],
    ['1440.TW', '南紡'],
]

for company in cloth:
    
    cerebro = bt.Cerebro()

# 獲取 2330 台積電的股價數據
    data = bt.feeds.PandasData(dataname=yf.download(company[0], start="2022-01-01", end="2023-03-24"))
    cerebro.adddata(data)
    cerebro.addstrategy(BearMarketStrategy)
    cerebro.addsizer(bt.sizers.PercentSizer, percents = 80)

    cerebro.broker.setcash(1000.0)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.run()
    print('公司名稱: %s' % company[1])
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())