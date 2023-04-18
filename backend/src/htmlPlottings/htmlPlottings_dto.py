from datetime import datetime, timedelta
from typing import Optional, List
from fastapi.openapi.models import Example
from odmantic import AIOEngine, Model, Field, ObjectId, EmbeddedModel, Reference
from src.personnelManagement.company.Company_dto import Company

class HtmlPlottings(Model):
    html_plotting_strategy: str = Field(...)
    html_plotting_name: str = Field(...)
    html_plotting_description: Optional[str] = Field(...)
    html_plotting_type: Optional[str] = Field(str)
    html_plotting_author: str = Field(...)
    html_plotting_status: Optional[str] = Field(...)
    html_plotting_src: str = Field(...)
    html_plotting_created_date: datetime = Field(default_factory=datetime.now)
    html_plotting_updated_date: datetime = Field(default_factory=datetime.now)

    class Config:
        collection = "backtest_html_plottings"

    def __str__(self):
        return f"{self.html_plotting_id}"

    def __repr__(self):
        return f"{self.html_plotting_id}"

    def __eq__(self, other):
        return self.html_plotting_id == other.html_plotting_id

    def __hash__(self):
        return hash(self.html_plotting_id)

    def __len__(self):
        return len(self.html_plotting_id)

    def __getitem__(self, item):
        return self.html_plotting_id[item]

    def __setitem__(self, key, value):
        self.html_plotting_id[key] = value

    def __delitem__(self, key):
        del self.html_plotting_id[key]

    def __iter__(self):
        return iter(self.html_plotting_id)

    def __contains__(self, item):
        return item in self.html_plotting_id

    def __add__(self, other):
        return self.html_plotting_id + other.html_plotting_id

    def __sub__(self, other):
        return self.html_plotting_id - other.html_plotting_id

    def __mul__(self, other):
        return self.html_plotting_id * other.html_plotting_id