from pymongo import MongoClient
import json

#Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

#Access a database
db = client["mydatabase"]

#Access a collection
collection = db["articles"]

#read form the json file
with open('output.json_post') as file:
    data = json.load(file)

#Insert the links into the collection
for article in data:
    collection.insert_one(article)


