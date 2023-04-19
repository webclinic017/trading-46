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


# def get_stock_data(buy, sell):
init = "price = self.data.Close \n        self.ma1 = self.I(SMA, price, 10) \n        self.ma2 = self.I(SMA, price, 20)"
next_day = "if crossover(self.ma1, self.ma2): self.buy() \n        elif crossover(self.ma2, self.ma1): self.sell()"
class_strategy = f"""
import backtesting
class SmaCross(backtesting.Strategy):
    def init(self):
        {init}
    def next(self):
        {next_day}
"""
print(class_strategy)
exec(class_strategy)

data = Backtest(GOOG,SmaCross , commission=.002,  ).run()
print(data)
data.plot()

