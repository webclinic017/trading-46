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
from typing import List

from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import engine
from odmantic import ObjectId

from src.personnelManagement.auth.auth_dto import User
from main import logger

from fastapi import APIRouter
from fastapi import Depends

from fastapi import  UploadFile, File
from fastapi.params import Form
from fastapi.exceptions import RequestValidationError

from datetime import date
from typing import List
import os

from src.personnelManagement.auth.Permission import Permission
from src.general.errorCode import ErrorCodeLevel, ErrorCodeModule, ErrorCodeException

from src.personnelManagement.auth.auth_service import get_current_active_user 
from src.personnelManagement.role.role_service import RoleService
from src.personnelManagement.user.User_dto import User

from src.strategies.strategies_service import StrategiesService

from src.backtest.backtest_service import data_backtesting_with_CSI, data_backtesting_with_CSI_multiple
from odmantic import ObjectId 




backtest_router = APIRouter(
    prefix="/backtest",
    tags=["backtest"],
    responses={404: {"description": "Not found"}},
)

@backtest_router.post("/single_backtesting/{stock_symbol}/{strategy_id}")
async def backtesting(stock_symbol: str, strategy_id:str,plot:bool,start_date:str,end_date:str,cash: float, commission:float ,current_user: User = Depends(get_current_active_user)):
    # if not RoleService.checkPermission(current_user, Permission.Backtest):
    #     raise HTTPException(status_code=403, detail="Permission denied")
    try:
        stock_symbol = stock_symbol 
        try:
            logger.info("strategy_id: " + strategy_id)
            strategy = await StrategiesService.findStrategyById(id=ObjectId(strategy_id))
        except:
            raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)
        if strategy.strategy_name == 'SmaCross':
            process_strategy = SmaCross
        return data_backtesting_with_CSI(stock_symbol = stock_symbol, strategy = process_strategy,strategy_name = strategy.strategy_name,plot=plot,start_date=start_date,end_date=end_date,cash=cash, commission=commission, username=current_user.email)
    except Exception as e:
        logger.error(e)
        raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)
    

@backtest_router.post("/multiple_backtesting/{strategy_id}")
async def backtesting(stock_list:List,strategy_id:str,plot:bool,start_date:str,end_date:str,cash: float, commission:float ,current_user: User = Depends(get_current_active_user)):
    # if not RoleService.checkPermission(current_user, Permission.Backtest):
    #     raise HTTPException(status_code=403, detail="Permission denied")
    try:
        try:
            logger.info("strategy_id: " + strategy_id)
            strategy = await StrategiesService.findStrategyById(id=ObjectId(strategy_id))
        except:
            raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)
        if strategy.strategy_name == 'SmaCross':
            process_strategy = SmaCross
        
        return data_backtesting_with_CSI_multiple(stock_list = stock_list,strategy = process_strategy,strategy_name = strategy.strategy_name,plot=plot,start_date=start_date,end_date=end_date,cash=cash, commission=commission, username=current_user.email)
    except Exception as e:
        logger.error(e)
        raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)
