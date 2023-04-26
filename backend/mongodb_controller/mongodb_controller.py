#!/usr/bin/python
# -*- coding: UTF-8 -*-
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, ObjectId


class MongoEngine:

    MONGO_USERNAME = 'oscar'
    MONGO_PASSWORD = '12345678'
    MONGO_HOST = 'mongodb'
    MONGO_PORT = 27017
    # MONGO_HOST = 'localhost'
    # MONGO_PORT = 27018


    # MONGO_AUTHSOURCE = 'admin'

    # uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:27017"
    uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authMechanism=DEFAULT"

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

