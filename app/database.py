from config import MONGODB_URI
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGODB_URI)
db = client["SmartManufacturing"]

async def startup_db_client():
    try:
        await client.server_info()
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")

async def shutdown_db_client():
    client.close()