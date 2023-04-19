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


class KdCross(Strategy):
    def init(self):
        super().init()

    def next(self):
        if crossover(20, self.data.slowk):  # K<20 買進
            self.buy()
        elif crossover(self.data.slowk, 80):  # K>80 平倉
            self.position.close()


class RSI(Strategy):
    def init(self):
        super().init()

    def next(self):
        if crossover(30, self.data.RSI):  # RSI<30 買進
            self.buy()
        elif crossover(self.data.RSI, 70):  # RSI>70 平倉
            self.position.close()

class MACD(Strategy):
    def init(self):
        super().init()

    def next(self):
        if crossover(self.data.macd, self.data.macdsignal):  # macd>macdsignal 買進
            self.buy()
        elif crossover(self.data.macdsignal, self.data.macd):  # macdsignal>macd 平倉
            self.position.close()

class BBANDS(Strategy):
    def init(self):
        super().init()

    def next(self):
        if crossover(self.data.close, self.data.upperband):  # close>upperband 買進
            self.buy()
        elif crossover(self.data.lowerband, self.data.close):  # lowerband>close 平倉
            self.position.close()


eval_class_wiithout_indentation = """
class CustomStrategy(Strategy):
    def init(self):
        super().init()
        price = self.data.Close
        self.price = price
        self.ma5 = self.I(SMA, price, 5)
        self.ma10 = self.I(SMA, price, 10)
        self.ma20 = self.I(SMA, price, 20)
        self.ma25 = self.I(SMA, price, 25)
        self.ma60 = self.I(SMA, price, 60)
        self.ma120 = self.I(SMA, price, 120)
        self.buy_pct = 0.5
        self.sell_pct = 1
    def next(self):
        # 若是持有股票，且收盤價低於 25 日均線，則賣出 100% 的股票
        if crossover(self.ma25, self.price):
            if self.position:
                self.sell(size=self.sell_pct)
        if crossover(self.ma5, self.ma10) or crossover(self.ma10, self.ma20):
            self.buy(size=self.buy_pct)
        if crossover(self.ma20, self.ma10) and crossover(self.ma10, self.ma5):
            if crossover(self.ma5, self.ma25):
                self.sell(size=self.sell_pct)
"""

eval_class = """
class CustomStrategy2(Strategy):
    def init(self):
        super().init()
        price = self.data.Close
        self.price = price
        self.ma5 = self.I(SMA, price, 5)
        self.ma10 = self.I(SMA, price, 10)
        self.ma20 = self.I(SMA, price, 20)
        self.ma25 = self.I(SMA, price, 25)
        self.ma60 = self.I(SMA, price, 60)
        self.ma120 = self.I(SMA, price, 120)
        self.buy_pct = 0.5
        self.sell_pct = 1
    def next(self):
        # 若是持有股票，且收盤價低於 25 日均線，則賣出 100% 的股票
        if crossover(self.ma25, self.price):
            if self.position:
                self.sell(size=self.sell_pct)
        if crossover(self.ma5, self.ma10) or crossover(self.ma10, self.ma20):
            self.buy(size=self.buy_pct)
        if crossover(self.ma20, self.ma10) and crossover(self.ma10, self.ma5):
            if crossover(self.ma5, self.ma25):
                self.sell(size=self.sell_pct)
"""
class CustomStrategy(Strategy):
    def init(self):
        super().init()
        price = self.data.Close
        self.price = price
        self.ma5 = self.I(SMA, price, 5)
        self.ma10 = self.I(SMA, price, 10)
        self.ma20 = self.I(SMA, price, 20)
        self.ma25 = self.I(SMA, price, 25)
        self.ma60 = self.I(SMA, price, 60)
        self.ma120 = self.I(SMA, price, 120)
        self.buy_pct = 0.5
        self.sell_pct = 1
    def next(self):
        # 若是持有股票，且收盤價低於 25 日均線，則賣出 100% 的股票
        if crossover(self.ma25, self.price):
            if self.position:
                self.sell(size=self.sell_pct)
        if crossover(self.ma5, self.ma10) or crossover(self.ma10, self.ma20):
            self.buy(size=self.buy_pct)
        if crossover(self.ma20, self.ma10) and crossover(self.ma10, self.ma5):
            if crossover(self.ma5, self.ma25):
                self.sell(size=self.sell_pct)