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
from src.strategies.strategies_class import SmaCross, KdCross, RSI, MACD, BBANDS, CustomStrategy,eval_class, eval_class_wiithout_indentation
import math
import time , random
import multiprocessing
import pprint
from typing import List

from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import MongoEngine
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

from src.htmlPlottings.htmlPlottings_service import store_htmlPlottings_src
from odmantic import ObjectId 

from odmantic import Model



backtest_router = APIRouter(
    prefix="/backtest",
    tags=["backtest"],
    responses={404: {"description": "Not found"}},
)
class single_backtesting_with_custom_strategy(Model):
    stock_symbol: str
    strategy_id:str
    plot:bool
    start_date:str
    end_date:str
    cash: float
    commission:float

@backtest_router.post("/single_backtesting_with_custom_strategy")
async def backtesting(single_backtesting_with_custom_strategy:single_backtesting_with_custom_strategy,current_user: User = Depends(get_current_active_user)
):
    # if not RoleService.checkPermission(current_user, Permission.Backtest):
    #     raise HTTPException(status_code=403, detail="Permission denied")
    single_backtesting_with_custom_strategy = single_backtesting_with_custom_strategy.dict()
    stock_symbol = single_backtesting_with_custom_strategy['stock_symbol']
    strategy_id = single_backtesting_with_custom_strategy['strategy_id']
    plot = single_backtesting_with_custom_strategy['plot']
    start_date = single_backtesting_with_custom_strategy['start_date']
    end_date = single_backtesting_with_custom_strategy['end_date']
    cash = single_backtesting_with_custom_strategy['cash']
    commission = single_backtesting_with_custom_strategy['commission']

    logger.info(single_backtesting_with_custom_strategy)
    try:
        try:
            logger.info("strategy_id: " + strategy_id)
            strategy = await StrategiesService.findStrategyById(id=ObjectId(strategy_id))
        except:
            logger.error("strategy_id: " + single_backtesting_with_custom_strategy.strategy_id)
            raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)


        data = data_backtesting_with_CSI(stock_symbol = stock_symbol, strategy =strategy,strategy_name = strategy.strategy_name,plot=plot,start_date=start_date,end_date=end_date,cash=cash, commission=commission, username=current_user.email)
        def handle_circular_and_convert_timestamps(obj):
            if isinstance(obj, pd.Timedelta):
                return str(obj) 
            if isinstance(obj, pd.Timestamp):
                return obj.strftime('%Y-%m-%d %H:%M:%S')  # Customize the format as needed
            raise TypeError(f'Object of type {type(obj)} is not JSON serializable')
        del data['_strategy'], data['_equity_curve'],data['_trades']
        json_str = json.dumps(data, default=handle_circular_and_convert_timestamps)
        await store_htmlPlottings_src(html_plotting_strategy = strategy.strategy_name,html_plotting_name= '{}_{}_{}'.format(current_user.email,strategy.strategy_name,stock_symbol), html_plotting_author =current_user.email, html_plotting_src='./htmlplots/{}_{}_{}.html'.format(current_user.email,strategy.strategy_name,stock_symbol))

        return {'date': json_str}
    except Exception as e:
        logger.error(e)
        raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)

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
            logger.error("strategy_id: " + strategy_id)
            raise ErrorCodeException(ErrorCodeLevel.User, ErrorCodeModule.Backtest)
        if strategy.strategy_name == 'SmaCross':
            process_strategy = SmaCross
        #這裡加上使用者自訂策略， 為使用輸入的程式碼，並且轉換成class
        process_strategy = exec(eval_class)
        data = data_backtesting_with_CSI(stock_symbol = stock_symbol, strategy = process_strategy,strategy_name = strategy.strategy_name,plot=plot,start_date=start_date,end_date=end_date,cash=cash, commission=commission, username=current_user.email)
        def handle_circular_and_convert_timestamps(obj):
            if isinstance(obj, pd.Timedelta):
                return str(obj) 
            if isinstance(obj, pd.Timestamp):
                return obj.strftime('%Y-%m-%d %H:%M:%S')  # Customize the format as needed
            raise TypeError(f'Object of type {type(obj)} is not JSON serializable')
        del data['_strategy'], data['_equity_curve'],data['_trades']
        json_str = json.dumps(data, default=handle_circular_and_convert_timestamps)
        await store_htmlPlottings_src(html_plotting_strategy = strategy.strategy_name,html_plotting_name= '{}_{}_{}'.format(current_user.email,strategy.strategy_name,stock_symbol), html_plotting_author =current_user.email, html_plotting_src='./htmlplots/{}_{}_{}.html'.format(current_user.email,strategy.strategy_name,stock_symbol))

        return {'date': json_str}
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
