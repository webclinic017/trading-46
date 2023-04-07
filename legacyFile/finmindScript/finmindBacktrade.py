import numpy as np
import pandas as pd
from FinMind import strategies
from FinMind.data import DataLoader
from FinMind.strategies.base import Strategy
from ta.momentum import StochasticOscillator

data_loader = DataLoader()
# data_loader.login(user_id, password) # 可選
obj = strategies.BackTest(
    stock_id="0056",
    start_date="2018-01-01",
    end_date="2019-01-01",
    trader_fund=500000.0,
    fee=0.001425,
    data_loader=data_loader,
)
obj.stock_price

class ShortSaleMarginPurchaseRatio(Strategy):
    """
    summary:
        策略概念: 券資比越高代表散戶看空，法人買超股票會上漲，這時候賣可以跟大部分散戶進行相反的操作，反之亦然
        策略規則: 券資比>=30% 且法人買超股票, 賣
                券資比<30% 且法人賣超股票 買
    """

    ShortSaleMarginPurchaseTodayRatioThreshold = 0.3

    def load_taiwan_stock_margin_purchase_short_sale(self):
        self.TaiwanStockMarginPurchaseShortSale = (
            self.data_loader.taiwan_stock_margin_purchase_short_sale(
                stock_id=self.stock_id,
                start_date=self.start_date,
                end_date=self.end_date,
            )
        )
        self.TaiwanStockMarginPurchaseShortSale[
            ["ShortSaleTodayBalance", "MarginPurchaseTodayBalance"]
        ] = self.TaiwanStockMarginPurchaseShortSale[
            ["ShortSaleTodayBalance", "MarginPurchaseTodayBalance"]
        ].astype(
            int
        )
        self.TaiwanStockMarginPurchaseShortSale[
            "ShortSaleMarginPurchaseTodayRatio"
        ] = (
            self.TaiwanStockMarginPurchaseShortSale["ShortSaleTodayBalance"]
            / self.TaiwanStockMarginPurchaseShortSale[
                "MarginPurchaseTodayBalance"
            ]
        )

    def load_institutional_investors_buy_sell(self):
        self.InstitutionalInvestorsBuySell = (
            self.data_loader.taiwan_stock_institutional_investors(
                stock_id=self.stock_id,
                start_date=self.start_date,
                end_date=self.end_date,
            )
        )
        self.InstitutionalInvestorsBuySell[["sell", "buy"]] = (
            self.InstitutionalInvestorsBuySell[["sell", "buy"]]
            .fillna(0)
            .astype(int)
        )
        self.InstitutionalInvestorsBuySell = (
            self.InstitutionalInvestorsBuySell.groupby(
                ["date", "stock_id"], as_index=False
            ).agg({"buy": np.sum, "sell": np.sum})
        )
        self.InstitutionalInvestorsBuySell["diff"] = (
            self.InstitutionalInvestorsBuySell["buy"]
            - self.InstitutionalInvestorsBuySell["sell"]
        )

    def create_trade_sign(self, stock_price: pd.DataFrame) -> pd.DataFrame:
        stock_price = stock_price.sort_values("date")
        self.load_taiwan_stock_margin_purchase_short_sale()
        self.load_institutional_investors_buy_sell()
        stock_price = pd.merge(
            stock_price,
            self.InstitutionalInvestorsBuySell[["stock_id", "date", "diff"]],
            on=["stock_id", "date"],
            how="left",
        ).fillna(0)
        stock_price = pd.merge(
            stock_price,
            self.TaiwanStockMarginPurchaseShortSale[
                ["stock_id", "date", "ShortSaleMarginPurchaseTodayRatio"]
            ],
            on=["stock_id", "date"],
            how="left",
        ).fillna(0)
        stock_price.index = range(len(stock_price))
        stock_price["signal"] = 0
        sell_mask = (
            stock_price["ShortSaleMarginPurchaseTodayRatio"]
            >= self.ShortSaleMarginPurchaseTodayRatioThreshold
        ) & (stock_price["diff"] > 0)
        stock_price.loc[sell_mask, "signal"] = -1
        buy_mask = (
            stock_price["ShortSaleMarginPurchaseTodayRatio"]
            < self.ShortSaleMarginPurchaseTodayRatioThreshold
        ) & (stock_price["diff"] < 0)
        stock_price.loc[buy_mask, "signal"] = 1
        return stock_price
    
obj.add_strategy(ShortSaleMarginPurchaseRatio)
obj.simulate()
obj.final_stats
obj.trade_detail
obj.plot()