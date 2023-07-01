from pymongo import MongoClient
conn =MongoClient()

db = conn["local"]
collection = db["user"]

# Perform the data migration
collection.update_many({}, {"$rename": {"emial": "email"}})