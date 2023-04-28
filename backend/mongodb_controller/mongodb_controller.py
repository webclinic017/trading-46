#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, ObjectId
import os
from main import logger
class MongoEngine:





    # MONGO_AUTHSOURCE = 'admin'

    # uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:27017"
    uri = os.getenv('MONGO_URI')

    client = AsyncIOMotorClient(uri)
    engine = AIOEngine(client=client, database="backtest")

    _instance = None

    def __init__(self):
        if MongoEngine._instance is not None:
            raise Exception('only one instance can exist')
        else:
            self._id = id(self)
            MongoEngine._instance = self

    def get_id(self):
        return self._id

    @staticmethod
    def getEngine():
        if MongoEngine._instance is None:
            MongoEngine()
        return MongoEngine._instance.engine

