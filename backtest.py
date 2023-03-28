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
from Alldata.data import AllStockdata
import backtrader as bt
import yfinance as yf
import math
import pandas as pd
import time


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
                self.stop_loss_price = self.entry_price * \
                    (1 - self.params.stop_loss)
                self.take_profit_price = self.entry_price * \
                    (1 + self.params.take_profit)
                self.order = self.buy(price=self.entry_price)
        else:
            if self.data.close[0] < self.stop_loss_price:
                self.sell(price=self.stop_loss_price, exectype=bt.Order.Stop)
            elif self.data.close[0] > self.take_profit_price:
                self.sell(price=self.take_profit_price,
                          exectype=bt.Order.Limit)


class BearMarketStrategy(bt.Strategy):

    def __init__(self):
        self.stop_loss_price = 0
        self.take_profit_price = 0
        self.entry_price = 27
        self.order = None
        self.buy_filter_price = 15  # 定義買進價格過濾器

    def next(self):
        if not self.position and self.data.close[0] < self.buy_filter_price:
            self.entry_price = self.data.close[0]
            self.buy_filter_price = self.entry_price * 0.95  # 降低買進價格過濾器
            self.stop_loss_price = self.entry_price * 0.95  # 設置止損價格
            self.take_profit_price = self.entry_price * 1.1  # 設置止盈價格
            self.order = self.buy()

        elif self.position:
            if self.data.close[0] > self.take_profit_price or self.data.close[0] < self.stop_loss_price:
                self.sell()  # 如果達到止盈或止損價格，就平倉
            elif self.data.close[0] < self.buy_filter_price:
                self.buy_filter_price = self.data.close[0] * 0.90  # 降低買進價格過濾器


class RSIStrategy(bt.Strategy):

    params = (('period', 14), ('overbought', 70), ('oversold', 30))

    def __init__(self):
        self.rsi = bt.indicators.RSI(
            self.data.close, period=self.params.period)

    def next(self):
        if not self.position:
            if self.rsi < self.params.oversold:
                self.buy()
        elif self.rsi > self.params.overbought:
            self.close()


class MovingAverageCrossStrategy(bt.Strategy):

    params = (('fast', 10), ('slow', 30))

    def __init__(self):
        self.fastma = bt.indicators.SMA(
            self.data.close, period=self.params.fast)
        self.slowma = bt.indicators.SMA(
            self.data.close, period=self.params.slow)
        self.crossover = bt.indicators.CrossOver(self.fastma, self.slowma)

    def next(self):
        if not self.position:
            if self.crossover > 0:
                self.buy()
        elif self.crossover < 0:
            self.close()


class MAIndicator(bt.Indicator):
    lines = ('ma',)
    params = (('period', 20),)

    def __init__(self):
        self.lines.ma = bt.indicators.MovingAverageSimple(
            self.data, period=self.p.period)


class MaCrossStrategy(bt.Strategy):
    params = (
        ('sma1', 5),
        ('sma2', 10),
        ('sma3', 20),
        ('sma4', 60),
        ('sma5', 120),
        ('sma25', 25),
        ('buy_pct', 0.5), ('sell_pct', 1),
    )
    lines = ('FTcrossover', 'FTWcrossover', 'TTWcrossover')

    def __init__(self):
        self.buy_size = None
        self.sell_size = None
        self.ma1 = bt.indicators.SMA(period=self.params.sma1)
        self.ma2 = bt.indicators.SMA(period=self.params.sma2)
        self.ma3 = bt.indicators.SMA(period=self.params.sma3)
        self.ma4 = bt.indicators.SMA(period=self.params.sma4)
        self.ma5 = bt.indicators.SMA(period=self.params.sma5)
        self.ma25 = bt.indicators.SMA(period=self.params.sma25)

        # FT means five days to Ten days MA cross
        self.FTcrossover = bt.indicators.CrossOver(self.ma1, self.ma2)
        # FTW means five days to Twenty days MA cross
        self.FTWcrossover = bt.indicators.CrossOver(self.ma1, self.ma3)
        # TT means Ten days to Twenty days MA cross
        self.TTWcrossover = bt.indicators.CrossOver(self.ma2, self.ma3)
        # FTWF means five days to twentyfive days MA cross
        self.FTWFcrossover = bt.indicators.CrossOver(self.ma1, self.ma25)
        self.trade_count = 1

    def next(self):
        if self.data.close[0] < self.ma25[0]:
            self.sell_size = self.getposition().size * self.params.sell_pct
        if not self.position:
            if self.FTcrossover > 0:
                self.buy_size = (self.broker.cash *
                                 self.params.buy_pct) / self.datas[0].close[0]
                self.buy(size=self.buy_size)
                # print('buy broker cash: %.2f' % self.broker.cash)
                # print('buy size: %.2f' % self.buy_size)
                # print('第幾次交易', self.trade_count)
                # print('----------------------------------------')
                self.trade_count += 1
        elif self.ma1 < self.ma25:
            self.sell_size = self.getposition().size * self.params.sell_pct
        elif self.FTcrossover < 0 or self.TTWcrossover < 0:

            if self.FTWcrossover < 0:
                self.sell_size = self.getposition().size * self.params.sell_pct
                # print('sell broker cash: %.2f' % self.broker.cash)
                # print('sell size: %.2f' % self.sell_size)
                # print('第幾次交易', self.trade_count)
                # print('----------------------------------------')
                self.sell(size=self.sell_size)
                self.trade_count += 1

        elif self.data.close[0] < self.ma3[0]:
            self.sell_size = self.getposition().size * self.params.sell_pct

    # def notify_order(self, order):
    #     if order.status in [order.Completed]:
    #         if order.isbuy():
    #             self.buy_size = self.broker.cash * self.params.buy_pct / self.datas[0].close[0]
    #         elif order.issell():
    #             self.sell_size = self.getposition().size * self.params.sell_pct


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


cerebro = bt.Cerebro()

# # 獲取 2330 台積電的股價數據
# data = bt.feeds.PandasData(dataname=yf.download('2303.TW', start="2022-01-01", end="2023-03-24"))
# cerebro.adddata(data)
# cerebro.addstrategy(MaCrossStrategy)
# # cerebro.addsizer(bt.sizers.PercentSizer, percents = 80)

# cerebro.broker.setcash(1000.0)
# cerebro.broker.setcommission(commission=0.001)
# cerebro.run()
# cerebro.plot()
# print('公司名稱: %s' % '聯電')
# print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# # 获取苹果公司股票的历史数据
# aapl = yf.Ticker('1440.TW')
# hist = aapl.history(period="max")

# # 计算5天、10天和30天的移动平均线
# ma5 =hist['MA5'] = hist['Close'].rolling(window=5).mean()
# ma10 = hist['MA10'] = hist['Close'].rolling(window=10).mean()
# ma30 = hist['MA30'] = hist['Close'].rolling(window=30).mean()

# # 打印计算结果
# print(hist[['Close', 'MA5', 'MA10', 'MA30']].tail())
# 日期和均線

avg_returen = []
positve_list = []
positve_list_name_and_value = []
negatve_list = []
negatve_list_name_and_value = []
stop = 0

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
        tsmc.append(
            {"stock_id": company["stock_id"], "stock_name": company["stock_name"]})


for index, company in enumerate(tsmc):

    cerebro = bt.Cerebro()

# 獲取 2330 台積電的股價數據
    try:
        # data = bt.feeds.PandasData(dataname=yf.download(company['stock_id']+'.TW', start="2022-01-01", end="2023-03-24"))
        # data = bt.feeds.PandasData(dataname=yf.download(
        #     company['stock_id']+'.TW', start="2022-01-01", end="2023-03-28"))
        pd_data = pd.read_csv(
            'Alldata/{}_change.csv'.format(company["stock_id"]), index_col=0, parse_dates=True)

        data = bt.feeds.PandasData(
            dataname=pd_data.loc['2022-01-01':'2023-03-28'])

        cerebro.adddata(data)
        cerebro.addstrategy(MaCrossStrategy)
        # cerebro.addsizer(bt.sizers.PercentSizer, percents=80)

        cerebro.broker.setcash(1000.0)
        cerebro.broker.setcommission(commission=0.001425)
        cerebro.run()

        print('number %d company' % (index+1))
        print('company name: %s' %
              company["stock_name"], 'id: %s' % company['stock_id']+'.TW')
        print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
        avg_returen.append(cerebro.broker.getvalue())
        if cerebro.broker.getvalue() > 1000:
            positve_list.append(cerebro.broker.getvalue())
            positve_list_name_and_value.append(
                [company['stock_id']+'.TW', company["stock_name"], cerebro.broker.getvalue()])
        else:
            negatve_list.append(cerebro.broker.getvalue())
            negatve_list_name_and_value.append(
                [company['stock_id']+'.TW', company["stock_name"], cerebro.broker.getvalue()])
            cerebro.plot()
        # .subtitle('股票名稱: {}, 股票代號: {}'.format(company["stock_name"], company['stock_id']+'.TW'), fontsize=20)
        print('------------------------------------')
    except:
        print('第 %d 個公司' % (index+1))
        print('公司名稱: {}'.format(company["stock_name"]),
              '股票代碼: %s' % company['stock_id']+'.TW')
        print('沒有資料')
        print('------------------------------------')
        pass

print('平均報酬率: %.2f' % (sum(avg_returen)/len(avg_returen)))
print('交易總數: %d' % len(avg_returen))
print('------------------------------------')
print('正報酬率: %.2f' % (sum(positve_list)/len(positve_list)))
print('正報酬率交易總數: %d' % len(positve_list))
print('------------------------------------')
print('負報酬率: %.2f' % (sum(negatve_list)/len(negatve_list)))
print('負報酬率交易總數: %d' % len(negatve_list))
print('------------------------------------')

# print('正報酬率公司列表與其報酬率由大到小排序')
# positive_sorted_list = sorted(
#     positve_list_name_and_value, key=lambda x: x[2], reverse=True)

# for index, company in enumerate(positive_sorted_list):
#     print('第 %d 個公司 ' % (index+1))
#     print('公司名稱: {}'.format(company[1]),
#           '股票代碼: %s' % company[0])
#     return_rate = (company[2] - 1000) / 1000
#     print('報酬率: %.2f' % return_rate)
#     print('------------------------------------')


# print('負報酬率公司列表與其報酬率由大到小排序')

# negative_sorted_list = sorted(negatve_list_name_and_value, key=lambda x: x[2])
# for index, company in enumerate(negative_sorted_list):
#     print('第 %d 個公司 ' % (index+1))
#     print('公司名稱: {}'.format(company[1]),
#           '股票代碼: %s' % company[0])
#     return_rate = (company[2] - 1000) / 1000
#     print('報酬率: %.2f' % return_rate)
#     print('------------------------------------')
