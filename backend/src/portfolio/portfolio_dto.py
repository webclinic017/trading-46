from datetime import datetime, timedelta
from typing import Optional, List
from fastapi.openapi.models import Example
from odmantic import AIOEngine, Model, Field, ObjectId, EmbeddedModel, Reference
from src.personnelManagement.company.Company_dto import Company


class PortFolio(Model):
    portfolio_id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
    portfolio_name: str = Field(...)
    portfolio_description: Optional[str] = Field(...)
    portfolio_type: Optional[str] = Field(str)
    portfolio_author: str = Field(...)
    portfolio_status: Optional[str] = Field(...)
    portfolio_src: str = Field(...)
    portfolio_created_date: datetime = Field(default_factory=datetime.now)
    portfolio_updated_date: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "backtest_portfolios"

    def __str__(self):
        return f"{self.portfolio_id}"

    def __repr__(self):
        return f"{self.portfolio_id}"

    def __eq__(self, other):
        return self.portfolio_id == other.portfolio_id

    def __hash__(self):
        return hash(self.portfolio_id)

    def __len__(self):
        return len(self.portfolio_id)

    def __getitem__(self, item):
        return self.portfolio_id[item]

    def __setitem__(self, key, value):
        self.portfolio_id[key] = value

    def __delitem__(self, key):
        del self.portfolio_id[key]

    def __iter__(self):
        return iter(self.portfolio_id)

    def __contains__(self, item):
        return item in self.portfolio_id

    def __add__(self, other):
        return self.portfolio_id + other.portfolio_id

    def __sub__(self, other):
        return self.portfolio_id - other.portfolio_id

    def __mul__(self, other):
        return self.portfolio_id * other.portfolio_id