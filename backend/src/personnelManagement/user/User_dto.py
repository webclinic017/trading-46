"""
    * draft
"""
from fastapi.datastructures import UploadFile
from datetime import datetime, timedelta
from enum import unique
from typing import Optional, List
from odmantic import AIOEngine, Model, Field, ObjectId, Reference
from pydantic import validator
from src.personnelManagement.company.Company_dto import Company
from src.personnelManagement.role.Role_dto import Role


class UpdateUser(Model):
    company: Optional[ObjectId] = Field(None, example=ObjectId())
    phoneNumber: Optional[str]
    fullName: Optional[str] = Field(example="Eddy Kuo")
    oldPassword: Optional[str] = Field(min_length=6, example="12369874")
    role: Optional[ObjectId] = Field(None, example=ObjectId())
    newPassword: Optional[str] = Field(min_length=6, example="12369874")
    password: Optional[str] = Field(min_length=6, example="12369874")


class User(Model):
    company: Optional[ObjectId] = Field(None, example=ObjectId())
    imageAlbums: Optional[List[ObjectId]] = Field([], example=[])
    inspections: Optional[List[ObjectId]] = Field([], example=[])
    email: str = Field(unique=True, regex="[^@]+@[^@]+\.[^@]+",example="test01@example.com")
    phoneNumber: Optional[str]
    fullName: str = Field(example="Oscar Yuh")
    password: str = Field(min_length=6, example="123456")
    role: Optional[ObjectId] = Field(
        None, example=ObjectId())   # ? should be Optional?
    enable: Optional[bool] = Field(True, example=True)
    lastLogin: Optional[datetime] = Field(
        datetime.now(), example=datetime.now())
    avatarUrl: Optional[str] = Field(
        example="https://avatars.githubusercontent.com/u/11992530?v=4")

    class Config:
        collection = "User"
class UserPatchSchema(Model):
    company: Optional[ObjectId] = Field(None, example=ObjectId())
    inspections: Optional[List[ObjectId]] = Field([], example=[])
    imageAlbums: Optional[List[ObjectId]] = Field([], example=[])
    email: Optional[str] = Field(unique=True, regex="[^@]+@[^@]+\.[^@]+", example="test01@example.com")
    phoneNumber: Optional[str]
    fullName: Optional[str] = Field(example="Oscar Yuh")
    password: Optional[str] = Field(min_length=6, example="12369874")
    oldPassword: Optional[str] = Field(min_length=6, example="12369874")
    role: Optional[ObjectId] = Field(
        None, example=ObjectId())   # ? should be Optional?
    enable: Optional[bool] = Field(True, example=True)
    newPassword: Optional[str] = Field(min_length=6, example="12369874")
    lastLogin: Optional[datetime] = Field(
        datetime.now(), example=datetime.now())
    avatarUrl: Optional[str] = Field(
        example="https://avatars.githubusercontent.com/u/11992530?v=4")
