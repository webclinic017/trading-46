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
from mongodb_controller.mongodb_controller import MongoEngine
from odmantic import ObjectId
from src.portfolio.portfolio_dto import PortFolio

from fastapi import BackgroundTasks
from src.personnelManagement.auth.auth_dto import User
from src.htmlPlottings.htmlPlottings_dto import HtmlPlottings
from main import logger
import os
import time, datetime


async def create_porfolio(user: User, portfolio_name: str, portfolio_description: str = str(datetime.datetime.now), portfolio_type: str ='active', portfolio_status: str = 'html', portfolio_created_date = datetime.datetime.now, portfolio_updated_date = datetime.datetime.now):
    portfolio = PortFolio(
        portfolio_name = portfolio_name,
        portfolio_description = portfolio_description,
        portfolio_type = portfolio_type,
        portfolio_status = portfolio_status,
        portfolio_created_date = portfolio_created_date,
        portfolio_updated_date = portfolio_updated_date
    )
    await MongoEngine.getEngine().save(portfolio)
    return {"message": "Add portfolio successfully"}


async def check_portfolio_name_exist(portfolio_name: str):
    logger.info("check_portfolio_name_exist", portfolio_name)
    portfolio = await MongoEngine.getEngine().find_one(PortFolio, PortFolio.portfolio_name == portfolio_name)
    return portfolio

async def get_portfolio_by_id(portfolio_id: str):
    portfolio = await MongoEngine.getEngine().find_one(PortFolio, PortFolio.id == portfolio_id)
    return portfolio

async def get_portfolio_by_name(portfolio_name: str):
    portfolio = await MongoEngine.getEngine().find_one(PortFolio, PortFolio.portfolio_name == portfolio_name)
    return portfolio

async def get_all_portfolio():
    portfolio = await MongoEngine.getEngine().find(PortFolio)
    return portfolio

async def delete_portfolio_by_id(portfolio_id: str):
    portfolio = await MongoEngine.getEngine().find_one(PortFolio, PortFolio.id == portfolio_id)
    await MongoEngine.getEngine().delete(portfolio)
    return {"message": "Delete portfolio successfully"}

async def update_portfolio_by_id(portfolio_id: str, portfolio_name: str, portfolio_description: str, portfolio_type: str, portfolio_status: str, portfolio_created_date, portfolio_updated_date):
    portfolio = await MongoEngine.getEngine().find_one(PortFolio, PortFolio.id == portfolio_id)
    portfolio.portfolio_name = portfolio_name
    portfolio.portfolio_description = portfolio_description
    portfolio.portfolio_type = portfolio_type
    portfolio.portfolio_status = portfolio_status
    portfolio.portfolio_created_date = portfolio_created_date
    portfolio.portfolio_updated_date = portfolio_updated_date
    await MongoEngine.getEngine().save(portfolio)
    return {"message": "Update portfolio successfully"}
