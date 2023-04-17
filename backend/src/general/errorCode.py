"""
    * draft
"""


from datetime import datetime, timedelta
from typing import Optional, List
from odmantic import AIOEngine, Model, Field, ObjectId, Reference
from fastapi.responses import JSONResponse
from enum import Enum

class ErrorCodeLevel(str, Enum):
    Unknown = "0"
    System = "1"
    Business = "2"
    User = "3"


class ErrorCodeModule(str, Enum):
    Unknown = "00"  
    Auth = "01"
    Role = "02"
    Company = "03"
    Image = "04"
    Inspection = "05"
    _3DTile = "06"
    Drone = "07"
    Bridge = "08"
    County = "09"
    Adm = "10"
    Backtest = "11"

class ErrorCodeException(BaseException):
    
    def __init__(self,error_code: str, error_message:str):
        
        self.error_code = error_code
        self.error_message = error_message
    
    

    
