from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import yfinance as yf
from backtesting.test import SMA, GOOG
import pandas as pd


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
data = pd.read_csv(
    'Alldata/1336_change.csv', index_col=0, parse_dates=True)

bt = Backtest(data, SmaCross, commission=.000145, cash=100000,
              exclusive_orders=True)
stats = bt.run()
bt.plot()
print(stats)
