from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

DATABASE = "test"
CONNECTION_STRING = "mongodb://localhost:27019/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"

uri = CONNECTION_STRING 
client = AsyncIOMotorClient(uri)
engine = AIOEngine(client=client, database=DATABASE)

   
def getMongoEngine():
    """
    ! Discard
    """
    pass
    

