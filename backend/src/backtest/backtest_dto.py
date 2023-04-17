from datetime import datetime, timedelta
from typing import Optional, List
from fastapi.openapi.models import Example
from odmantic import AIOEngine, Model, Field, ObjectId, EmbeddedModel, Reference
from src.personnelManagement.company.Company_dto import Company

class Description(EmbeddedModel):
    stock_symbol: str = Field(...)
    stock_name: str = Field(...)
    start_date: str = Field(...)
    end_date: str = Field(...)
    strategy_name: str = Field(...)
    commission: float = Field(...)
    cash: float = Field(...)

class SingleBacktest(Model):
    backtest_id: str = Field(...)
    backtest_name: str = Field(...)
    backtest_description: str = Field(...)
    backtest_code: str = Field(...)
    backtest_type: str = Field(...)
    backtest_parameters: str = Field(...)
    backtest_author: str = Field(...)
    backtest_status: str = Field(...)
    backtest_created_date: datetime = Field(default_factory=datetime.now)
    backtest_updated_date: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "backtest_single"
        allow_population_by_field_name = True
        use_enum_values = True

    def __str__(self):
        return f"{self.backtest_id}"

    def __repr__(self):
        return f"{self.backtest_id}"

    def __eq__(self, other):
        return self.backtest_id == other.backtest_id

    def __hash__(self):
        return hash(self.backtest_id)

    def __len__(self):
        return len(self.backtest_id)

    def __getitem__(self, item):
        return self.backtest_id[item]

    def __setitem__(self, key, value):
        self.backtest_id[key] = value

    def __delitem__(self, key):
        del self.backtest_id[key]

    def __iter__(self):
        return iter(self.backtest_id)

    def __contains__(self, item):
        return item in self.backtest_id

    def __add__(self, other):
        return self.backtest_id + other.backtest_id

    def __sub__(self, other):
        return self.backtest_id - other.backtest_id
