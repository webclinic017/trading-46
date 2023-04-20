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
from src.general.deleteByIdObject import *
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule
from mongodb_controller.mongodb_controller import MongoEngine
from odmantic import ObjectId

from src.personnelManagement.auth.auth_dto import User
from main import logger

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi import HTTPException
from fastapi import  UploadFile, File
from fastapi.params import Form
from fastapi.exceptions import RequestValidationError

from datetime import date
from typing import List
import os

from src.personnelManagement.auth.Permission import Permission
from src.general.errorCode import ErrorCodeLevel, ErrorCodeModule, ErrorCodeException

from src.personnelManagement.auth.auth_service import get_current_active_user,get_current_user
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
async def add_strategy(strategy_id: str, strategy_name: str, strategy_description: str, strategy_code: str, strategy_type: str, strategy_parameters: str, strategy_author: str, strategy_status: str, current_user: User = Depends(get_current_active_user)):
    # if not RoleService.checkPermission(current_user, Permission.Backtest):
    #     raise HTTPException(status_code=403, detail="Permission denied")
    try:
        strategy_author = current_user.email
        strategy = await StrategiesService.add_strategy(strategy_id, strategy_name, strategy_description, strategy_code, strategy_type, strategy_parameters, strategy_author, strategy_status)
        return strategy
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")