#customize strategies for backtesting
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
from src.strategies.strategies_dto import Strategy
import math
import time , random
import multiprocessing
import pprint
from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import MongoEngine
from odmantic import ObjectId

from fastapi import Depends, HTTPException
from src.personnelManagement.auth.auth_controller import get_current_user,get_current_active_user
from src.personnelManagement.auth.auth_dto import User
from src.personnelManagement.role.role_service import RoleService
from src.personnelManagement.user.user_service import UserService
from main import logger
import os



class StrategiesService():
    async def add_strategy(strategy):
        await MongoEngine.getEngine().save(strategy)
        return {"message": "Add strategy successfully"}
    async def findStrategyById(id: ObjectId):
        logger.info("findStrategyById", id)
        strategy = await MongoEngine.getEngine().find_one(Strategy, Strategy.id == ObjectId(id))
        return strategy
    async def findStrategyByAuthor(author: str):
        logger.info("findStrategyByAuthor", author)
        strategy = await MongoEngine.getEngine().find(Strategy, Strategy.strategy_author == author)
        return strategy
    async def get_all_strategies():
        strategy = await MongoEngine.getEngine().find(Strategy)
        return strategy

    async def update_strategy(strategy: Strategy):
        await MongoEngine.getEngine().save(strategy)
        return {"message": "Update strategy successfully"}