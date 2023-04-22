"""
    * draft
"""
from typing import  List, Optional
from odmantic import  Model, Field
from src.personnelManagement.auth.Permission import Permission

class Role(Model):
    name: str = Field(unique=True , example="guest")
    description:str = Field(default='' , example="guest")
    permissions: List[Permission]
    class Config:
        collection = "Role"

class RolePatchSchema(Model):
    name: Optional[str] = Field(unique=True , example="guest")
    description:Optional[str] = Field(example="guest")
    permissions: Optional[List[Permission]]
    
