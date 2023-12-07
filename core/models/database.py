from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config import MONGO_DB_NAME, MONGO_URL

db_client = AsyncIOMotorClient(MONGO_URL)

async def get_db():
    return db_client[MONGO_DB_NAME]

# mock db
db = {}
db_reports = {}