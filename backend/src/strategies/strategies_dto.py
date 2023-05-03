from datetime import datetime, timedelta
from typing import Optional, List
from fastapi.openapi.models import Example
from odmantic import AIOEngine, Model, Field, ObjectId, EmbeddedModel, Reference
from src.personnelManagement.company.Company_dto import Company


class Signal(EmbeddedModel):
    id: str = Field(...)
    category: str = Field(...)
    type: str = Field(...)
    indicator_1: str = Field(...)
    compare_operator: str = Field(...)
    indicator_2: str = Field(...)
    buyOrSell: str = Field(...)
    amount: float = Field(...)
    unit: str = Field(...)


class StrategyCode(EmbeddedModel):
    init_indicators: List[Optional[str]] = Field(...)
    stop_loss: float = Field(...)
    take_profit: float = Field(...)
    buy_first: bool = Field(...)
    buy_signal:List[Signal] = Field(...)
    sell_signal: List[Signal] = Field(...)

class Strategy(Model):
    strategy_id: str
    strategy_name: str = Field("strategy_name")
    strategy_description: str = Field("strategy_description")
    strategy_code: StrategyCode = Field(StrategyCode(
        init_indicators=["KD", "MACD", "RSI",'SMA5'],
        stop_loss=10.0,
        take_profit=20.0,
        buy_first=True,
        buy_signal=[
            {
                "id": "id",
                "category": "category",
                "type": "type",
                "indicator_1": "indicator_1",
                "compare_operator": "compare_operator",
                "indicator_2": "indicator_2",
                "buyOrSell": "buyOrSell",
                "amount": 10.0,
                "unit": "unit"
            }
        ],
        sell_signal=[
            {
                "id": "id",
                "category": "category",
                "type": "type",
                "indicator_1": "indicator_1",
                "compare_operator": "compare_operator",
                "indicator_2": "indicator_2",
                "buyOrSell": "buyOrSell",
                "amount": 10.0,
                "unit": "unit"
            }
        ]
    ), embedded=True)
    strategy_type: str = Field("strategy_type")
    strategy_parameters: str = Field( "strategy_parameters")
    strategy_author: str = Field("strategy_author")
    strategy_status: str = Field("strategy_status")
    strategy_created_date: datetime = Field(default_factory=datetime.now)
    strategy_updated_date: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "backtest_strategies"

    