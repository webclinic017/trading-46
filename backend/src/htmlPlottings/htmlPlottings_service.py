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
from src.strategies.strategies_class import SmaCross, KdCross, RSI, MACD, BBANDS, CustomStrategy
import math
import time , random
import multiprocessing
import pprint
from fastapi.params import Depends

from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import engine
from odmantic import ObjectId

from fastapi import BackgroundTasks
from src.personnelManagement.auth.auth_dto import User
from src.htmlPlottings.htmlPlottings_dto import HtmlPlottings
from main import logger
import os
import time, datetime
# html_plotting_id: str = Field(...)
# html_plotting_name: str = Field(...)
# html_plotting_description: str = Field(...)
# html_plotting_type: str = Field(...)
# html_plotting_author: str = Field(...)
# html_plotting_status: str = Field(...)
# html_plotting_src: str = Field(...)
# html_plotting_created_date: datetime = Field(default_factory=datetime.now)
# html_plotting_updated_date: datetime = Field(default_factory=datetime.now)
async def store_htmlPlottings_src(html_plotting_strategy:str,html_plotting_name: str, html_plotting_author: str, html_plotting_src: str, html_plotting_description: str = str(datetime.datetime.now), html_plotting_status: str ='active', html_plotting_type: str = 'html', html_plotting_created_date = datetime.datetime.now, html_plotting_updated_date = datetime.datetime.now):
    htmlPlottings = HtmlPlottings(
        html_plotting_strategy=html_plotting_strategy,
        html_plotting_name = html_plotting_name,
        html_plotting_description = html_plotting_description,
        html_plotting_type = html_plotting_type,
        html_plotting_author = html_plotting_author,
        html_plotting_status = html_plotting_status,
        html_plotting_src = html_plotting_src,
        # html_plotting_created_date = html_plotting_created_date,
        # html_plotting_updated_date = html_plotting_updated_date
    )
    await engine.save(htmlPlottings)
    return {"message": "Add htmlPlottings successfully"}

async def check_htmlPlottings_name_exist(html_plotting_name: str):
    logger.info("check_htmlPlottings_name_exist", html_plotting_name)
    htmlPlottings = await engine.find_one(HtmlPlottings, HtmlPlottings.html_plotting_name == html_plotting_name)
    return htmlPlottings