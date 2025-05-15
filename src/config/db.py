from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
DB_URI = os.getenv("MONGO_URI")


conn = MongoClient(DB_URI)