from datetime import datetime
import backtrader as bt
import yfinance as yf
import time

# 定義一個Indicator物件
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




# cerebro = bt.Cerebro()
# cerebro.addstrategy(MyStrategy)
# cerebro.broker.setcash(1000)
# cerebro.broker.setcommission(commission=0.001)

# data = bt.feeds.PandasData(dataname=yf.download("3481.TW", start="2020-01-01", end="2023-03-24"))

# cerebro.adddata(data)
# print('Starting Value: %.2f' % cerebro.broker.getvalue())
# cerebro.run()
# print('Ending Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot()

average = []

for company in tech:
    try:
        cerebro = bt.Cerebro()
        cerebro.broker.setcash(1000)
        cerebro.broker.setcommission(commission=0.001)
        cerebro.addstrategy(MyStrategy)

        data = bt.feeds.PandasData(dataname=yf.download(company[0], start="2022-01-01", end="2023-03-24"))
        print('公司名稱:',company[1])
        cerebro.adddata(data)
        cerebro.run()
        print('Ending Value: %.2f' % cerebro.broker.getvalue())
        average.append(cerebro.broker.getvalue())
        time.sleep(2)
    except:
        pass
print('平均值:',sum(average)/len(average))
    