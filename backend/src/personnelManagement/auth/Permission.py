"""
    * draft
"""

from datetime import datetime, timedelta
from typing import Optional, List
from odmantic import AIOEngine, Model, Field, ObjectId, Reference
from enum import Enum

class Permission(int, Enum):


    


    ROOT = -1
    View = 0
    CreateUser = 1
    CreateProject = 2
    
    GetAllUser = 3
    ChangeUserInfo = 4
    DeleteUser = 5
    
    CreateImage = 6
    ReadImage = 7
    DeleteImage = 8
    
    CreateCompany = 9
    UpdateCompany = 10
    DeleteCompany = 11
    
    CreateBridge = 12
    UpdateBridge = 13
    DeleteBridge = 14
    ReadBridge = 15
    
    CreateVirturalInspection = 16
    CreateActualInspection = 17
    

    
