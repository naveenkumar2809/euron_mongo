from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient  
from bson import ObjectId
import os
from dotenv import load_dotenv  

load_dotenv()

MOONGO_URI = os.getenv("MONGO_URI") 

class Employee(BaseModel):
    id: int
    name: str
    department: str
    course: str

app = FastAPI()
client = MongoClient("mongodb+srv://nvnkumar:naveen12345@euron.usryjgk.mongodb.net/?appName=euron")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MongoDB"}

def get_mongo_client():
    return client

client = AsyncIOMotorClient(MOONGO_URI)
db = client["euron"]
euron_collection = db["euron_collection"]

@app.post("/employees/insert")
async def euron_data_insert_helper(emp: Employee):
    result = await euron_collection.insert_one(emp.dict())
    return str(result.inserted_id)

@app.get("/employees/getdata")
async def get_euron_data():
    items = []
    cursor = euron_collection.find({})
    async for document in cursor:
        document['_id'] = str(document['_id'])  
        items.append(document)
    return items