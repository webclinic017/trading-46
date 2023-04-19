from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from mongodb_controller.mongodb_controller import  CONNECTION_STRING, DATABASE
from multiprocessing import Process
import os
import asyncio
from re import U
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from datetime import datetime
from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, Request,WebSocket
import uvicorn
import os
from dotenv import load_dotenv
from multiprocessing import Pool


from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename='./server.log')
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)
logger.addHandler(fh)

# from src import image_router
from src import user_router
from src import role_router
from src import auth_router
from src import company_router
from src import backtest_router
from src import strategies_router
# from src import image_album_router




from fastapi.middleware.cors import CORSMiddleware
from src.general.errorCode import ErrorCodeException, ErrorCodeLevel, ErrorCodeModule

from fastapi_socketio import SocketManager

from celery.result import AsyncResult
from pymongo import MongoClient
from logging import Logger
import logging

from typing import Optional, List

from odmantic import AIOEngine, Model, Field, ObjectId, EmbeddedModel, Reference
import json, time



load_dotenv()




app = FastAPI()
pool = Pool(processes=4) 
origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:8000",
    "http://localhost:8050",
    "http://localhost:8080",
    "http://localhost:3000",
    'http://localhost:3005',
    'http://localhost:3000/mainpage/AlbumView',
    '[*]',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# middleware = [
#     Middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=['*'],
#         allow_headers=['*']
#     )
# ]

# app = FastAPI(middleware=middleware)



API_VERSION = "/api/v1"
    
@app.exception_handler(HTTPException)
async def ErrorCodeExceptionHandler(request: Request, exception: HTTPException):
    print(exception)
    if type(exception.detail) != type(ErrorCodeException(error_code="", error_message="")):
        return JSONResponse (status_code = exception.status_code, content = {"error_code": ErrorCodeLevel.Unknown + ErrorCodeModule.Unknown + "0001", "error_message": "unknown error"})
    else:
        return JSONResponse (status_code = exception.status_code, content = {"error_code": exception.detail.error_code, "error_message": exception.detail.error_message})

app.include_router(auth_router, prefix=API_VERSION)
app.include_router(user_router, prefix=API_VERSION)
app.include_router(role_router, prefix=API_VERSION)
app.include_router(company_router, prefix=API_VERSION)
app.include_router(backtest_router, prefix=API_VERSION)
app.include_router(strategies_router, prefix=API_VERSION)
# app.include_router(image_router, prefix=API_VERSION)
# app.include_router(image_album_router, prefix=API_VERSION)




@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"message": "Connected!"})
    while True:
        data = await websocket.receive_text()
        await websocket.send_json({"message": data})


@app.get("/", response_class=HTMLResponse)
async def home():
    # return """
    #     <html>
    #         <head>
    #             <title>Vision X Backend APIII Server</title>
    #         </head>
    #         <body>
    #             <div style="width:800px; margin:0 auto;">
    #                 <img width="800px" src="https://static.accupass.com/eventintro/1911041001001992042421.jpg">
    #                 <h1>Welcome to Vision X Backend APIII Server</h1>
    #                 This is a backend API server, please get the API token then use these APIs.</br>
    #                 If you want to get the detail, please reference "http://host-ip:8000/docs".</br>
    #                 Remember to change the host ip address.</br>
    #             </div>
    #         </body>
    #     </html>
    # """
    return  """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat</title>
        </head>
        <body>
            <h1>WebSocket Chat</h1>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" id="messageText" autocomplete="off"/>
                <button>Send</button>
            </form>
            <ul id='messages'>
            </ul>
            <script>
                var ws = new WebSocket("ws://localhost:8000/ws");
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                function sendMessage(event) {
                    var input = document.getElementById("messageText")
                    ws.send(input.value)
                    input.value = ''
                    event.preventDefault()
                }
            </script>
        </body>
    </html>
    """
    
@app.get("/userss")
async def test():
    return """
        <html>
            <head>
                <title>Vision X Backend APIII Server</title>
            </head>
            <body>
                <div style="width:800px; margin:0 auto;">
                    <img width="800px" src="https://static.accupass.com/eventintro/1911041001001992042421.jpg">
                    <h1>Welcome to Vision X Backend APII Server</h1>
                    This is a backend API server, please get the API token then use these APIs.</br>
                    If you want to get the detail, please reference "http://host-ip:8000/docs".</br>
                    Remember to change the host ip address.</br>
                </div>
            </body>
        </html>
    """
# class Test(Model):
#     number: int
#     class Config:
#         collection = "test"
# @app.post('/process')
# async def processcal():
#         result = start_process.delay(13,2)
#         while not result.ready():
#                 print(f'[Waiting] It is {result.ready()} that we have results')
#                 time.sleep(2) # sleep to second
#         print(f'[Done] It is {result.ready()} that we have results')
#         # print(f'[Result] {result.result}')
#         # # test = Test
#         # # test.number = result.get()
#         # # await engine.save(test)
#         return {"task_id": result.id}




# async def create_sample():
#     import pprint
#     # connect to mongodb
#     # from pymongo import MongoClient
#     uri = "mongodb://%s:%s@%s:%s" % ('admin', 'SyVZrFx9vRWvA6HL', 'localhost', '27018')

#     client = AsyncIOMotorClient(uri)
#     engine = AIOEngine(motor_client=client, database="VisionX")

#     company = Company()
#     savedCompany = await engine.save(company)
#     print(savedCompany.dict())

#     adminUser = User(company = company.id)
#     adminUser.password = bcrypt.hashpw(adminUser.password.encode('utf-8'), bcrypt.gensalt())
#     await engine.save(adminUser)

#     player_count = await engine.count(Company)
#     print(player_count)

#     result = await engine.find(Company)
#     print(result)



# if __name__ == "__main__":
#     myproc = Process(target=uvicorn.run, kwargs={'app':'main:app'})
#     myproc.start()
    
    
    
