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
import time
import random
import multiprocessing
import pprint
from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import MongoEngine
from odmantic import ObjectId

from src.personnelManagement.auth.auth_dto import User
from main import logger

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi import HTTPException
from fastapi import UploadFile, File
from fastapi.params import Form
from fastapi.exceptions import RequestValidationError

from datetime import date
from typing import List
import os

from src.personnelManagement.auth.Permission import Permission
from src.general.errorCode import ErrorCodeLevel, ErrorCodeModule, ErrorCodeException

from src.personnelManagement.auth.auth_service import get_current_active_user, get_current_user
from src.personnelManagement.role.role_service import RoleService
from src.personnelManagement.user.User_dto import User

from odmantic import ObjectId
from src.strategies.strategies_dto import Strategy
from src.strategies.strategies_service import StrategiesService

strategies_router = APIRouter(
    prefix="/strategies",
    tags=["strategies"],
    responses={404: {"description": "Not found"}},
)


@strategies_router.post("/add_strategy")
async def add_strategy(strategy: Strategy, current_user: User = Depends(get_current_active_user)):
    # if not RoleService.checkPermission(current_user, Permission.Backtest):
    #     raise HTTPException(status_code=403, detail="Permission denied")
    try:
        strategy_author = current_user.email
        strategy.strategy_author = strategy_author
        logger.info(strategy)
        strategy = await StrategiesService.add_strategy(strategy)
        return strategy
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")

@strategies_router.post("/update_strategy")
async def update_strategy(strategy: Strategy, current_user: User = Depends(get_current_active_user)):
    try:
        strategy_author = current_user.email
        strategy.strategy_author = strategy_author
        logger.info(strategy)
        strategy = await StrategiesService.update_strategy(strategy)
        return strategy
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")


@strategies_router.get("/get_strategy")
async def get_strategy(strategy_id: str, current_user: User = Depends(get_current_active_user)):
    try:
        strategy = await StrategiesService.findStrategyById(strategy_id)
        return strategy
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")


@strategies_router.get("/get_all_strategies")
async def get_all_strategies(current_user: User = Depends(get_current_active_user)):
    try:
        strategies = await StrategiesService.get_all_strategies()
        return strategies
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")


@strategies_router.get("/get_strategies_by_author")
async def get_strategy_by_author(current_user: User = Depends(get_current_active_user)):
    try:
        strategies = await StrategiesService.findStrategyByAuthor(current_user.email)
        return strategies
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")

@strategies_router.post("/update_strategy_by_id")
async def update_strategy_by_id(strategy:Strategy,current_user: User = Depends(get_current_active_user)):
    # if StrategiesService.findStrategyById(strategy.id) is None:
    #     raise HTTPException(status_code=404, detail="Strategy not found")
    try:
        # strategy.strategy_id = ObjectId(strategy.id)
        strategy = await StrategiesService.update_strategy(strategy)
        return strategy
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")
    
# @strategies_router.delete("/delete_strategy")
# async def delete_strategy(strategy_id: str, current_user: User = Depends(get_current_active_user)):
#     if not
