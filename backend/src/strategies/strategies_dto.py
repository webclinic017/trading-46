from datetime import datetime, timedelta
from typing import Optional, List
from fastapi.openapi.models import Example
from odmantic import AIOEngine, Model, Field, ObjectId, EmbeddedModel, Reference
from src.personnelManagement.company.Company_dto import Company


class Strategy(Model):
    strategy_id: str = Field(...)
    strategy_name: str = Field(...)
    strategy_description: str = Field(...)
    strategy_code: str = Field(...)
    strategy_type: str = Field(...)
    strategy_parameters: str = Field(...)
    strategy_author: str = Field(...)
    strategy_status: str = Field(...)
    strategy_created_date: datetime = Field(default_factory=datetime.now)
    strategy_updated_date: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "backtest_strategies"

    def __str__(self):
        return f"{self.strategy_id}"

    def __repr__(self):
        return f"{self.strategy_id}"

    def __eq__(self, other):
        return self.strategy_id == other.strategy_id

    def __hash__(self):
        return hash(self.strategy_id)

    def __len__(self):
        return len(self.strategy_id)

    def __getitem__(self, item):
        return self.strategy_id[item]

    def __setitem__(self, key, value):
        self.strategy_id[key] = value

    def __delitem__(self, key):
        del self.strategy_id[key]

    def __iter__(self):
        return iter(self.strategy_id)

    def __contains__(self, item):
        return item in self.strategy_id

    def __add__(self, other):
        return self.strategy_id + other.strategy_id

    def __sub__(self, other):
        return self.strategy_id - other.strategy_id

    def __mul__(self, other):
        return self.strategy_id * other.strategy_id

    def __truediv__(self, other):
        return self.strategy_id / other.strategy_id

    def __floordiv__(self, other):
        return self.strategy_id // other.strategy_id

    def __mod__(self, other):
        return self.strategy_id % other.strategy_id

    def __divmod__(self, other):
        return divmod(self.strategy_id, other.strategy_id)

    def __pow__(self, power, modulo=None):
        return pow(self.strategy_id, power, modulo)

    def __lshift__(self, other):
        return self.strategy_id << other.strategy_id

    def __rshift__(self, other):
        return self.strategy_id >> other.strategy_id

    def __and__(self, other):
        return self.strategy_id & other.strategy_id
    
    def __or__(self, other):
        return self.strategy_id | other.strategy_id
    
    def __xor__(self, other):
        return self.strategy_id ^ other.strategy_id
    
    def __radd__(self, other):
        return other.strategy_id + self.strategy_id
    
    def __rsub__(self, other):
        return other.strategy_id - self.strategy_id
    
    def __rmul__(self, other):
        return other.strategy_id * self.strategy_id
    
    def __rtruediv__(self, other):
        return other.strategy_id / self.strategy_id
    
    def __rfloordiv__(self, other):
        return other.strategy_id // self.strategy_id
    