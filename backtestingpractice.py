from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import yfinance as yf
from backtesting.test import SMA, GOOG


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
bt = Backtest(yf.download('2303.TW', start="2022-01-01", end="2023-03-24"), SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()