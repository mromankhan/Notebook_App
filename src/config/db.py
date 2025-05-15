from pymongo import MongoClient
MONGO_URI = "mongodb+srv://roman:roman_notes@cluster0.sjws2.mongodb.net/notes"

conn = MongoClient(MONGO_URI)